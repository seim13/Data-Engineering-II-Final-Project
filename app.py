import numpy as np
from flask import Flask, request, jsonify, render_template
from keras.models import model_from_json
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/predict',methods=['POST'])
def predict():

    String_features = [str(x) for x in request.form.values()]
    final_features = list(String_features)

    tokenizer = Tokenizer(split=' ')
    tokenizer.fit_on_texts(final_features)
    X_test = tokenizer.texts_to_sequences(final_features)
    X_test_pad = pad_sequences(X_test)

    prediction = loaded_model.predict_classes(X_test_pad, verbose=0)

    for result in prediction:
        if result == 0:
            output = 'negatif'
        if result == 1:
            output = 'positif'
    
    return render_template('test.html', prediction_text='Your text is {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)

    tokenizer = Tokenizer(split=' ')
    tokenizer.fit_on_texts(list(data.values()))
    X_test = tokenizer.texts_to_sequences(list(data.values()))
    X_test_pad = pad_sequences(X_test)
    
    prediction = loaded_model.predict_classes(X_test_pad)

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)