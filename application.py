from flask import Flask, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

@application.route("/")
def index():
    news = request.args.get('news')
    if news is None:
        return "Welcome to News Checker! Please enter a query parameter 'news' to check whether it is fake or not!"
    return (str(load_model(news)), 200)

def load_model(news):
    # model loading
    loaded_model = None
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)

    vectorizer = None
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)

    # model making prediction - output will be 'FAKE' if fake, else 'REAL'
    prediction = loaded_model.predict(vectorizer.transform([news]))[0]
    if(prediction == 'FAKE'):
        return 0
    return 1

if __name__ == "__main__":
    application.run(port=5000, debug=True)