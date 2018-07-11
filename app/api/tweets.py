# app/api/tweets.py
from flask import Blueprint, jsonify, request
from app.db import tweet_repository

api = Blueprint('tweets', __name__)


@api.route('/tweets/<int:id>')
def show(id):
    tweet = tweet_repository.get(id)
    return jsonify({
        "id": tweet.id,
        "text": tweet.text,
        "created_at": tweet.created_at
    })


@api.route('/tweets/<int:id>')
def update(id):
    pass


@api.route('/tweets')
def post(message):
    request_json = request.get_json()['message']
    pass


@api.route('/tweets/<int:id>')
def delete(id):
    pass

