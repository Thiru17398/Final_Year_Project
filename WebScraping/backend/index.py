from flask import Flask, request, jsonify
from BusManager import BusManager
from MetroManager import MetroManager

app = Flask(__name__)
busManager = BusManager()

metroManager = MetroManager()


# @app.route('/busInfo',methods = ['POST'])
# def getBuses():
#     data = request.json
#     response = busManager.getBuses(data['origin'] , data['destination'])
#     if(len(response.keys()) == 0):
#         return "No Buses Found"
#     return jsonify(response)


# @app.route('/')
# def home():
#     return 'Transit Simplified'


# if __name__ == '__main__':
    # app.run(debug=True)

# print(metroManager.getMetroRoute(input('Enter Source : ').strip().lower() , input('Enter Destination : ').strip().lower()))

# busManager = BusManager()

# print(busManager.getBusFare(
# 'Thiruvotriyur',
# 'M.g.r.koyambedu'
# ))

print(metroManager.getMetroFare("egmore","guindy"))