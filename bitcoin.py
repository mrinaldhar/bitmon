import requests
import json
from datetime import datetime
import threading

ifp = open('bitcoin.log', 'r')
vals = ifp.read()
vals = vals.split("\n")
for x in xrange(len(vals)):
	vals[x] = vals[x].split(',')
ifp.close()
if len(vals) > 0 and len(vals[-1]) < 2:
	del vals[-1]
def f():
	ofp = open('bitcoin.log', 'a')
	resp = requests.get('https://www.zebapi.com/api/v1/market/ticker/btc/inr')
	data = json.loads(resp.text)
	ofp.write(str(datetime.now()) + "," + str(data["buy"]) + "," + str(data["sell"]) + "\n")
	print str(datetime.now()) + ", " + str(data["buy"]) + ", " + str(data["sell"]),
	if len(vals)>0:
		buydiff = float(vals[-1][1]) - data["buy"]
	else:
		buydiff = 0
	if buydiff < 0:
		print ", Increased: "+str(buydiff)
	elif buydiff > 0:
		print ", Decreased: "+str(buydiff)
	vals.append([str(datetime.now()), data["buy"], data["sell"]])
	
	ofp.close()
	threading.Timer(60, f).start()

f()
