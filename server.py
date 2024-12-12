from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

with open("facts.json") as f:
    json_data = json.load(f)

prev = []

def generate_random_index (array_list):
    while True:
        new_Index = random.randint(0, (len(array_list) -1))
        if new_Index not in prev:
            break
    
    prev.append(new_Index)
    if len(prev) > 3:
        prev.pop(0)

    return new_Index

@app.route("/", methods=["GET"])
def get_all():
    return jsonify(json_data), 200

@app.route("/random-fact", methods=["GET"])
def get_random_fact ():
    random_index = generate_random_index(json_data)
    random_fact = json_data[random_index]
    return jsonify(random_fact), 200

if __name__ == "__main__":
    app.run(port=6000, debug=True)