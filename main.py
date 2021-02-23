import json
from websocket import create_connection
from pylive import live_plotter
import numpy as np




uri = "wss://ws.bitstamp.net"
ws = create_connection(uri)

data = {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_etheur"
        }
    }
data_json = json.dumps(data)

ws.send(data_json)
size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = np.random.randn(len(x_vec))
line1 = []
while True:
    try:
        result = ws.recv()
        obj = json.loads(result)
        if bool(obj['data']) :
            price = obj['data']['price']
            y_vec[-1] = price
            line1 = live_plotter(x_vec,y_vec,line1)
            y_vec = np.append(y_vec[1:],0.0)
            print(obj)
    except Exception as e:
        print(e)
        break
