# from filestack import Client

def upload_to_internet(file: str, api_key= "AdG9aDa0nS0mZnP8S3sFwz"):
    client = Client(apikey= api_key)

    new_file_link = client.upload(filepath= file)
    return new_file_link.url