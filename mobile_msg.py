from twilio.rest import Client

# For a free trial account, we cannot send sms to others than our verified personal number

def forward(confidence: float):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "AC97833ff926384270d9f7c381274bd07b"
    auth_token = "32a30affde46e6f6818c3fc8846da3a2"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
             messaging_service_sid='MGe1ea35a9abec06c945027febb46bdc3e',
             body=f'Elephant found with {round(confidence, 2) * 100}%',
             to=f'+918610846845' # must be in str not int
         )

    print(message.sid)

if __name__ == "__main__": # else runs on every imports
    forward(0.3)
