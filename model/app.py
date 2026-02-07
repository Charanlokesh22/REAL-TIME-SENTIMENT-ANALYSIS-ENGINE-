from flask import Flask, request, jsonify
from model.sentiment_model import predict_sentiment
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["sentiment_db"]
collection = db["results"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]

    result = predict_sentiment(text)
    collection.insert_one({"text": text, "result": result})

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
