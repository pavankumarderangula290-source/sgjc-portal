import urllib.request
import urllib.error
import json

url_students = "http://localhost:3000/api/students"
url_fees = "http://localhost:3000/api/admin/fees"

def post_json(url, data):
    req = urllib.request.Request(url, method='POST')
    req.add_header('Content-Type', 'application/json')
    jsondata = json.dumps(data).encode('utf-8')
    try:
        with urllib.request.urlopen(req, data=jsondata) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        return json.loads(e.read().decode())

def get_json(url):
    req = urllib.request.Request(url, method='GET')
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        return json.loads(e.read().decode())

# 1. Create a dummy student
student_res = post_json(url_students, {
    "name": "Fee Test Student",
    "class": "11th Grade",
    "section": "A",
    "dob": "2010-01-01",
    "parentName": "Fee Parent",
    "phone": "9999999999",
    "address": "Fee Address"
})
print("Create student:", student_res)
if student_res.get('success'):
    student_id = student_res['id']
    
    # 2. Assign a fee
    fee_res = post_json(url_fees, {
        "studentId": student_id,
        "amount": 5000,
        "dueDate": "2026-12-31",
        "remarks": "Test fee"
    })
    print("Assign fee:", fee_res)
    
    # 3. Check fees list
    fees_list = get_json(url_fees)
    print("All Fees:", fees_list)
