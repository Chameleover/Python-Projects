import requests

url = 'https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active'

req = requests.get(url)

filename = 'friday_vehicle.xlsx'

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192): # If file is too big write it in chunks
        if chunk:
            f.write(chunk)