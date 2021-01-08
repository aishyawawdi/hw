import requests,time,threading
from flask import Flask
app = Flask(__name__)


@app.route('/')
def bitcoin():
    #threading.Timer(5.0,bitcoin).start
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    value = r.json()['bpi']['USD']['rate']

    return '''<h1>bitcoin price</h1>
    <p>the price is:{} USD. </p>'''.format(value)

#@app.route('/avg')
#def avg_bitcoin():
#    #threading.Timer(70,bitcoin).start
#    mylist=[]
#    duration=600
#    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#    value = r.json()['bpi']['USD']['rate']
#
#    start_time=time.time() #time in sec
#    while time.time()<start_time+duration:
#        r2 = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#        value2 = r2.json()['bpi']['USD']['rate']
#        mylist.append(value2)
#    
#    new_avg=sum(mylist)/len(mylist)
#    return '''<h1>Bitcoin Average Price</h1>
#    <p>The average price is:{} USD. </p>'''.format(new_avg)




if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000)



