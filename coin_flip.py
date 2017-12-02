import requests


endpoint = "https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8"

r = requests.get(endpoint)
payload = r.json()
q_value = payload['data'][0]
if q_value > 127:
    print("YES")
else:
    print("NO")