import os, json

from flask import Flask, jsonify

class People:
	def __init__(self, name, age):
		self.name = name
		self.age = age

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/entities')
def get_entities():
	peoples = [People('Joey', 20), People('Derek', 24)]
	mappedPeoples = [i for i in map(lambda x: x.__dict__, peoples)]

	return jsonify(mappedPeoples)

if __name__ == '__main__':
    app.run(debug = True)