from twilio.rest import Client
from file_sharer import upload_to_internet

def send_whatsapp_message(confidence: float, label: str, image_file: str):
    account_sid = 'AC97833ff926384270d9f7c381274bd07b'
    auth_token = '32a30affde46e6f6818c3fc8846da3a2'
    client = Client(account_sid, auth_token)

    url = upload_to_internet(file= image_file)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        # media url must be a source from http (internet)
        media_url= [url],
        body=f'found with confidence {round(confidence, 2) * 100}%',
        to='whatsapp:+918610846845' # for a free trial only verified number works
    )

    print(message.sid)