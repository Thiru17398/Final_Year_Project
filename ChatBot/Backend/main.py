import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import urllib3
from nltk.stem import PorterStemmer
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout , Input
import pickle
from tensorflow.keras.models import load_model
from Handlers.Handler import Handler
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import asyncio
import websockets
import os

app = Flask(__name__)

CORS(app)

def extract_source_dest(query):
    pattern = r"from (.*?) to (.*)|between (.*?) and (.*)|between (.*?) to (.*)|to {.*?} from (.*)"
    match = re.search(pattern, query, re.IGNORECASE)

    if match:
        source = match.group(1) or match.group(3) or match.group(5) or match.group(8)
        destination = match.group(2) or match.group(4) or match.group(6) or match.group(7)
        return source.strip(), destination.strip()
    return None, None

def bag_of_words(sentence, words):
    bag = np.zeros(len(words))
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    for sw in sentence_words:
    	for i,word in enumerate(words):
        	if word==sw:
                  bag[i] +=1
    return np.array(bag)

data = {}

with open('./Data/data.json' , 'r') as f:
    data = json.load(f)

words = []
docs_questions = []
docs_intents = []
labels = []


for intent in data["intents"]:
     for question in intent["questions"]:
        tokens = nltk.word_tokenize(question)
        words.extend(tokens)
        docs_questions.append(tokens)
        docs_intents.append(intent['tag'])
          
        if intent["tag"] not in labels:
        	labels.append(intent["tag"])


words = [stemmer.stem(token.lower()) for token in words if token != ['>', '<', '\\', ':', '-', ',', '#','[' , ']', '/', '//', '_', '(', ')']]
words = sorted(list(set(words)))
labels = sorted(labels)


training_data = []

output_empty = [0] * len(labels)


print(docs_intents)
for ind , ques in enumerate(docs_questions):
    bag = []
    stemmed_words = [stemmer.stem(w.lower()) for w in ques if w.isalnum()]

    for w in words:
          bag.append(1 if w in stemmed_words else 0)

    output_row = output_empty[:]
    output_row[labels.index(docs_intents[ind])] = 1
    training_data.append([bag , output_row])


random.shuffle(training_data)

X_train = np.array([item[0] for item in training_data])
y_train = np.array([item[1] for item in training_data])


# tf.compat.v1.reset_default_graph()

# net = tflearn.input_data(shape=[None, len(training_data[0])])

# net_h1 = tflearn.fully_connected(net, 8)
# net_h2 = tflearn.fully_connected(net, 8)

# net = tflearn.fully_connected(net, len(output_row[0], activation="softmax"))
# net = tflearn.regression(net)

# model = tflearn.DNN(net)



model = Sequential([
    Dense(128, input_shape=(len(X_train[0]),), activation="relu"),
    Dropout(0.5),
    Dense(64, activation="relu"),
    Dropout(0.5),
    Dense(len(y_train[0]), activation="softmax")  # Output layer
])

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=200, batch_size=8, verbose=1)


model.save("chatbot_model.h5")
print("Model trained and saved!")

handler = Handler()







def predict_intent(text):
    source , destination = extract_source_dest(text)
    K.clear_session()
    model = load_model("chatbot_model.h5")
    text =  text.replace(source, "{source}").replace(destination, "{destination}")
    bow = bag_of_words(text, words)
    res = model.predict(np.array([bow]))[0]
    max_index = np.argmax(res)
    
    if res[max_index] > 0.7:  # Confidence threshold
        return labels[max_index]
    else:
        return "unknown"


async def chatbot_response(text):
    predictedIntent = predict_intent(text).lower()
    source , destination = extract_source_dest(text)
    if(predictedIntent == 'bus_route_planning'):
        return handler.getBuses(source,destination,random.choice(data['intents'][0]["responses"]))
    if(predictedIntent == 'metro_train_fare'):
        return handler.getMetroFare(source , destination , random.choice(data['intents'][7]["responses"]))
    if(predictedIntent == 'metro_train_route_planning'):
         return handler.getMetroRoutePlanning(source , destination , data['intents'][5]["responses"])
    if(predictedIntent == 'bus_fare'):
        return handler.getBusFare(source, destination, data['intents'][3]["responses"])
    if(predictedIntent == "suburban_train_route_planning"):
        return await handler.getLocalTrainBetweenStations(source, destination, data['intents'][9]["responses"][0])
         
    return "Sorry, I didn't understand that."

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "quit":
#         break
#     response = chatbot_response(user_input)
#     print("Bot:", response)

async def echo(websocket):
    print('Web Socket connected')
    async for message in websocket:
        response = await chatbot_response(message)
        await websocket.send(response)
    
async def main():
    async with websockets.serve(
        echo , 
        "localhost",
        int(os.environ.get('PORT', 8090))
    ):
        await asyncio.Future()



if __name__ == '__main__':
    asyncio.run(main())
