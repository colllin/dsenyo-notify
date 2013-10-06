import os
from flask import Flask, request
import sendgrid 

app = Flask(__name__)
SENDGRID_USERNAME = os.getenv('SENDGRID_USERNAME',False)
SENDGRID_PASSWORD = os.getenv('SENDGRID_PASSWORD',False)


@app.route('/')
def hello():
	return 'Notification app for Dsenyo.com'

@app.route('/customer/new', methods=['POST'])
def customer_new():
	customer = request.json
	s = sendgrid.Sendgrid(SENDGRID_USERNAME, SENDGRID_PASSWORD, secure=True)
	subject = "[Dsenyo Notifications] New Wholesale Customer: {} {}".format(customer.first_name, customer.last_name)

	body = """A new customer account was created on the wholesale store.

Name: {} {}
Email: {}
Notes: {}
	""".format(customer.first_name, customer.last_name, customer.email, customer.note)
	# make a message object
	message = sendgrid.Message("notifications@dsenyo.com", subject, body, None )
	# add a recipient
	message.add_to("ashley@dsenyo.com", "Ashley Rein")
	message.add_to("marissa@dsenyo.com", "Marissa Saints")
	# use the Web API to send your message
	s.smtp.send(message)	
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)