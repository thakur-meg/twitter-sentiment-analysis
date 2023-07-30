from flask import Flask, render_template, request
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from sklearn import svm
import numpy as np

model = pickle.load(open('twitter_sentiment.pkl', 'rb'))
vectorizer = CountVectorizer(binary=True, stop_words='english')
svm = svm.SVC(kernel = 'linear', probability=True)

app = Flask (__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def home():
    
   data1 = request.form['tweet']
   arr = np.array([data1])

   tweet = vectorizer.fit_transform(arr)
   prob = svm.fit(tweet, data1).predict_proba(tweet)

   pred = model.predict(tweet)
   if(pred==0) :
       return render_template('main.html',pred="Your tweet is less likely to be flagged.") 
   
   elif (pred==1) :
       return render_template('main.html',pred="You tweet is highly probable to be flagged.") 



if __name__ == "__main__":
    app.run(debug=True)