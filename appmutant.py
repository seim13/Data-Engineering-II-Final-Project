import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from keras.models import model_from_json
from gensim.models import Word2Vec
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial
from collections import Counter
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Gauge, Summary, Histogram
from flask_prometheus_metrics import register_metrics

def register_blueprints(app):
    """
    Register blueprints to the app
    """
    app.register_blueprint(app)
app = Flask(__name__)
METRICS = PrometheusMetrics(app)
METRICS_INFO = ('twitter_app', 'The application is a Twitter search application, where the user inputs a search string, and the application returns the top 20 tweets which are similar to the search string')
register_blueprints(app)
register_metrics(app, app_version=config["version"], app_config=config["config"])
model = Word2Vec.load('model.bin')
print("Loaded model from disk")
#load df
df = pd.read_csv('clean_tweet.csv')

index2word_set = set(model.wv.index2word)

@app.route('/')
def home():
    return render_template('test.html')


@app.route('/predict',methods=['POST'])

def predict():
    index2word_set = set(model.wv.index2word)

    def avg_feature_vector(sentence, model, num_features, index2word_set):
        words = sentence.split()
        feature_vec = np.zeros((num_features, ), dtype='float32')
        n_words = 0
        for word in words:
            if word in index2word_set:
                n_words += 1
                feature_vec = np.add(feature_vec, model[word])
        if (n_words > 0):
            feature_vec = np.divide(feature_vec, n_words)
        return feature_vec

    
    if request.method == 'POST':
        message = request.form['message']
        data = str(message)
        print('computin in action')

        score={}
        for i in df['tweet']:
            sentence2=i
            s2_afv = avg_feature_vector(sentence2, model=model, num_features=300, index2word_set=index2word_set)
            s1_afv = avg_feature_vector(data , model=model, num_features=300, index2word_set=index2word_set)
            sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
            score[sentence2]=sim

        my_prediction= dict(Counter(score).most_common(20))
            
        return render_template('test.html', prediction_text='Top 20 of tweets : {}\n --  '.format(my_prediction))

#@app.route('/metrics')
"""@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def echo_status(status):
    return 'Status: %s' % status, status
 """


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)