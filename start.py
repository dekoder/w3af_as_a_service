import requests
import json

data = {'scan_profile': file('./simple.pw3af').read(),
        'target_urls': ['http://127.0.0.1:8023/']}

if __name__ == "__main__":
    response = requests.post('http://127.0.0.1:5000/scans/',
                         data=json.dumps(data),
                         headers={'content-type': 'application/json'})


