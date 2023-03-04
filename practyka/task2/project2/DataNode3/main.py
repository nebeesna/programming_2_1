from DataNode import DataNode
from flask import Flask, request

node = DataNode('localhost:5004')
app = Flask('DataNode')


@app.route('/node/get_status', methods=['GET'])
def get_status():
    return node.get_status()


@app.route('/node/push_message', methods=['POST'])
def push_message():
    msg = request.data.decode()
    return node.push_message(msg)


@app.route('/node/get_message', methods=['GET'])
def get_message():
    return node.get_message()


app.run(host='localhost', port=5004)

