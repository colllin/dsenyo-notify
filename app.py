import os
from flask import Flask, request

app = Flask(__name__)
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY',False)

@app.route('/')
def hello():
    return 'Notification app for Dsenyo.com'

@app.route('/customer/new', methods=['POST'])
def customer_new():
    app.logger.debug(request) 