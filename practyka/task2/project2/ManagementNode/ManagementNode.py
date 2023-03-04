import requests


class ManagementNode:
    def __init__(self, management_node_address: str):
        self.address = management_node_address
        self.node_list = {}

    def get_status(self):
        if len(self.node_list) == 0:
            return 'There is no any node'
        answer = ''
        for node in self.node_list:
            answer += node + ' '
            r = requests.get('http://' + node + '/node/get_status')
            if r.status_code != 200:
                return 'ERROR SENDING REQUEST TO NODE'
            answer += r.text + '\n'
        return answer

    def add_node(self, address: str):
        for node in self.node_list:
            if node == address:
                return 'This node already exist'
        r = requests.get('http://' + address + '/node/get_status')
        if r.status_code != 200:
            return 'ERROR SENDING REQUEST TO NODE'
        self.node_list[address] = int(r.text)
        return 'OK'

    def remove_node(self, address: str):
        for node in self.node_list:
            if node == address:
                del self.node_list[address]
                return 'OK'
        return 'This node does not exist'

    def push_message(self, msg: str):
        if len(self.node_list) == 0:
            return 'There is no any node'
        node_to_use = ''
        loading = -1
        for node in self.node_list.keys():
            if loading == -1 or self.node_list[node] < loading:
                loading = self.node_list[node]
                node_to_use = node
        print(node_to_use)
        r = requests.post('http://' + node_to_use + '/node/push_message', data=msg)
        if r.status_code != 200:
            return 'ERROR SENDING REQUEST TO NODE'
        self.node_list[node_to_use] += 1
        return r.text

    def get_message(self):
        if len(self.node_list) == 0:
            return 'There is no any node'
        node_to_use = ''
        loading = -1
        for node in self.node_list.keys():
            if self.node_list[node] > loading:
                node_to_use = node
                loading = self.node_list[node]
        r = requests.get('http://' + node_to_use + '/node/get_message')
        if r.status_code != 200:
            return 'ERROR SENDING REQUEST TO NODE'
        self.node_list[node_to_use] -= 1
        return r.text

