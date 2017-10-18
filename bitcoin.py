import requests
import json
from datetime import datetime
import threading

ifp = open('bitcoin.log', 'r')
vals = ifp.read()
vals = prev.split("\n")
ifp.close()

def f():
	ofp = open('bitcoin.log', 'a')
	resp = requests.get('https://www.zebapi.com/api/v1/market/ticker/btc/inr')
	data = json.loads(resp.text)
	ofp.write(str(datetime.now()) + "," + str(data["buy"]) + "," + str(data["sell"]))
	print str(datetime.now()) + "," + str(data["buy"]) + "," + str(data["sell"])
	vals.append(str(datetime.now()), data["buy"], data["sell"])
	ofp.close()
	threading.Timer(60, f).start()

f()