import os
import requests
from pinatapy import PinataPy
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

# Connect to the IPFS cloud service
pinata_api_key=str(os.environ.get('PinataAPIKey'))
pinata_secret_api_key=str(os.environ.get('PinataAPISecret'))
pinata = PinataPy(pinata_api_key,pinata_secret_api_key)

# Upload the file
result = pinata.pin_file_to_ipfs("markdown.md")

# Should return the CID (unique identifier) of the file
print(result)

# Anything waiting to be done?
print(pinata.pin_jobs())

# List of items we have pinned so far
print(pinata.pin_list())

# Total data in use
print(pinata.user_pinned_data_total())

# Get our pinned item
#gateway="https://gateway.pinata.cloud/ipfs/"
gateway="https://ipfs.io/ipfs/"
print(requests.get(url=gateway+result['IpfsHash']).text)
print(gateway+result['IpfsHash'])
