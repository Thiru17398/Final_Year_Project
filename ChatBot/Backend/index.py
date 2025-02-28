from Handlers.Handler import Handler


# from flask import Flask, request, jsonify
# from transformers import pipeline

# app = Flask(__name__)

# chatbot_pipeline = pipeline("question-answering")

# data_source = {
#     "route_updates": "The next bus to Downtown leaves at 10:15 AM from Stop A.",
#     "cost_info": "The average cost for the bus is 25rs.",
#     "transit_switch": "You need to switch to Train B at Central Station.",
#     "travel_time": "The estimated travel time is 45 minutes."
# }

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get('query')
    
#     context = "\n".join([f"{key}: {value}" for key, value in data_source.items()])
    
#     response = chatbot_pipeline({
#         "question": user_input,
#         "context": context
#     })
    
#     return jsonify({"response": response['answer']})

# @app.route('/')
# def index():
#     return "Chatbot Module is Running!"

# if __name__ == '__main__':
#     app.run(debug=True)

handler = Handler()

print(handler.getBusFare('ennore','redhills',"The ticket cost from {source} to {destination} differs based on the type of Bus Service: \n{fare_list}"))