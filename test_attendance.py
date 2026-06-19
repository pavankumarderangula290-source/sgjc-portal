import urllib.request
import urllib.error
import json
import datetime

def post_json(url, data):
    req = urllib.request.Request(url, method='POST')
    req.add_header('Content-Type', 'application/json')
    jsondata = json.dumps(data).encode('utf-8')
    try:
        with urllib.request.urlopen(req, data=jsondata) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        return json.loads(e.read().decode())

def delete_req(url):
    req = urllib.request.Request(url, method='DELETE')
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

student_data = {
    "name": "Test Student",
    "class": "1st Year",
    "branch": "MPC",
    "section": "A",
    "passcode": "0000"
}

res = post_json("http://localhost:3000/api/students", student_data)
student_id = res['id']
print("Created student:", student_id)

url = "http://localhost:3000/api/attendance"

att_data = {
    "date": "2026-06-19",
    "session": "Daily",
    "markedBy": "STFTEST",
    "records": [{"studentId": student_id, "status": "present"}]
}

res1 = post_json(url, att_data)
print("First submission:", res1)

att_data["records"][0]["status"] = "absent"
res2 = post_json(url, att_data)
print("Second submission (1st edit):", res2)

att_data["records"][0]["status"] = "present"
res3 = post_json(url, att_data)
print("Third submission (locked attempt):", res3)

delete_req(f"http://localhost:3000/api/students/{student_id}")
print("Cleaned up student.")
