from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    message = request.form.get('Body')
    sender = request.form.get('From')

    # Lógica do bot aqui
    response_message = f"Você disse: {message}"

    send_message(sender, response_message)
    return "OK", 200


def send_message(to, body):
    url = "https://api.twilio.com/2010-04-01/Accounts/YOUR_ACCOUNT_SID/Messages.json"
    auth = ("YOUR_ACCOUNT_SID", "YOUR_AUTH_TOKEN")
    data = {
        "From": "whatsapp:+14155238886",  # Número do sandbox do Twilio
        "To": to,
        "Body": body
    }
    requests.post(url, data=data, auth=auth)


if __name__ == '__main__':
    app.run(debug=True)

from twilio.rest import Client

account_sid = 'ACe609dde303bd28c477429d167b04fd23'
auth_token = '2354833061cedae87aa808740f9a4e25'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+557582529797'
)

print(message.sid)
