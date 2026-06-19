import urllib.request
import urllib.error
import json
import os

url_creds = "http://localhost:3000/api/admin/credentials"
url_backup = "http://localhost:3000/api/admin/backup"

def put_json(url, data):
    req = urllib.request.Request(url, method='PUT')
    req.add_header('Content-Type', 'application/json')
    jsondata = json.dumps(data).encode('utf-8')
    try:
        with urllib.request.urlopen(req, data=jsondata) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        return json.loads(e.read().decode())

def get_file(url):
    req = urllib.request.Request(url, method='GET')
    try:
        with urllib.request.urlopen(req) as response:
            return response.read()
    except urllib.error.HTTPError as e:
        return str(e)

# Test credentials
res1 = put_json(url_creds, {"username": "newadmin", "password": "newpassword123"})
print("Credentials update response:", res1)

# Put it back
res2 = put_json(url_creds, {"username": "admin", "password": "admin123"})
print("Credentials restore response:", res2)

# Test backup download
backup_data = get_file(url_backup)
if isinstance(backup_data, bytes):
    print("Backup download successful, size:", len(backup_data), "bytes")
else:
    print("Backup download failed:", backup_data)
