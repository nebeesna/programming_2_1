import requests


class Client:
    def __init__(self):
        self.management_node_address = input('Enter management node address: ')
        self.count = 0

    def add_node(self, address: str):
        r = requests.post('http://' + self.management_node_address + '/add_node', data=address)
        if r.status_code != 200:
            return 'ERROR SENDING REQUEST TO MANAGEMENT NODE'
        return r.text

    def remove_node(self, address: str):
        r = requests.post('http://' + self.management_node_address + '/remove_node', data=address)
        if r.status_code != 200:
            return 'ERROR SENDING REQUEST TO MANAGEMENT NODE'
        return r.text

    def push_message(self, msg: str):
        r = requests.post('http://' + self.management_node_address + '/push_message', data=msg)
        if r.status_code != 200:
            return 'ERROR SENDING REQUEST TO MANAGEMENT NODE'
        self.count += 1
        return r.text

    def get_message(self):
        r = requests.get('http://' + self.management_node_address + '/get_message')
        if r.status_code != 200:
            return 'ERROR SENDING REQUEST TO MANAGEMENT NODE'
        return r.text

    def get_status(self):
        r = requests.get('http://' + self.management_node_address + '/get_status')
        if r.status_code != 200:
            return 'ERROR SENDING REQUEST TO MANAGEMENT NODE'
        return r.text

    def get_count(self):
        return self.count

    def reset_count(self):
        self.count = 0
