import urllib.request, json
# Test create-order
req = urllib.request.Request('http://127.0.0.1:3000/api/fees/create-order', data=json.dumps({'feeId': 'TEST_FEE_1'}).encode(), headers={'Content-Type': 'application/json'})
res = urllib.request.urlopen(req)
order_data = json.loads(res.read().decode())
print("Order Data:", order_data)

# Test verify-payment
if order_data.get('dummy'):
    req2 = urllib.request.Request('http://127.0.0.1:3000/api/fees/verify-payment', data=json.dumps({
        'feeId': 'TEST_FEE_1',
        'razorpay_payment_id': 'pay_dummy_123',
        'razorpay_order_id': order_data['order_id'],
        'razorpay_signature': 'dummy'
    }).encode(), headers={'Content-Type': 'application/json'})
    res2 = urllib.request.urlopen(req2)
    verify_data = json.loads(res2.read().decode())
    print("Verify Data:", verify_data)
