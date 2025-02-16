from flask import Flask, request, jsonify
from BusManager import BusManager


app = Flask(__name__)
busManager = BusManager()


@app.route('/busInfo',methods = ['POST'])
def getBuses():
    data = request.json
    response = busManager.getBuses(data['origin'] , data['destination'])
    if(len(response.keys()) == 0):
        return "No Buses Found"
    return jsonify(response)


@app.route('/')
def home():
    return 'Transit Simplified'


if __name__ == '__main__':
    app.run(debug=True)