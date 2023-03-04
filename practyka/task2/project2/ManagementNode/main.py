from flask import Flask, request
from ManagementNode import ManagementNode

management = ManagementNode('localhost:5001')
app = Flask('ManagementNode')


@app.route('/get_status', methods=['GET'])
def get_status():
    return management.get_status()


@app.route('/add_node', methods=['POST'])
def add_node():
    node_address = request.data.decode()
    return management.add_node(node_address)


@app.route('/remove_node', methods=['POST'])
def remove_node():
    node_address = request.data.decode()
    return management.remove_node(node_address)


@app.route('/push_message', methods=['POST'])
def push_message():
    msg = request.data.decode()
    return management.push_message(msg)


@app.route('/get_message', methods=['GET'])
def get_message():
    return management.get_message()


app.run(host='localhost', port=5001)
