import urllib.request, json, hmac, hashlib, sqlite3, os

conn = sqlite3.connect('database.sqlite')
conn.execute("INSERT OR IGNORE INTO students (id, name, class, section, branch) VALUES ('TEST_STU', 'Test Student', '11', 'A', 'Science')")
conn.execute("INSERT OR REPLACE INTO fees (id, studentId, amount, dueDate, status) VALUES ('TEST_FEE_1', 'TEST_STU', 500.0, '2026-12-31', 'pending')")
conn.commit()
conn.close()

req = urllib.request.Request('http://127.0.0.1:3000/api/fees/create-order', data=json.dumps({"feeId": "TEST_FEE_1"}).encode(), headers={'Content-Type': 'application/json'})
response = urllib.request.urlopen(req)
order_data = json.loads(response.read().decode())
print("Order Data:", order_data)

order_id = order_data['order_id']
payment_id = "pay_dummy" + os.urandom(4).hex()
secret = "asVUne1ArCvPxbf4GYJe7xFO"
msg = order_id + "|" + payment_id
signature = hmac.new(secret.encode(), msg.encode(), hashlib.sha256).hexdigest()

verify_req = urllib.request.Request('http://127.0.0.1:3000/api/fees/verify-payment', data=json.dumps({"feeId": "TEST_FEE_1", "razorpay_payment_id": payment_id, "razorpay_order_id": order_id, "razorpay_signature": signature}).encode(), headers={'Content-Type': 'application/json'})
verify_res = urllib.request.urlopen(verify_req)
print("Verify Data:", json.loads(verify_res.read().decode()))
