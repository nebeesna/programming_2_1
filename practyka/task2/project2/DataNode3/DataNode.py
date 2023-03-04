from queue import Queue
import os.path


class DataNode:
    def __init__(self, data_node_address: str):
        self.address = data_node_address
        self.queue = Queue()

        if os.path.isfile(self.address.split(':')[1] + '.txt'):
            file = open(self.address.split(':')[1] + '.txt', 'r')
            for line in file:
                if line.strip() == '':
                    break
                self.queue.push(line.strip())
            file.close()

    def get_message(self):
        if self.queue.get_size() != 0:
            msg = self.queue.top()
            self.queue.pop()
            read_file = open(self.address.split(':')[1] + '.txt', 'r')
            data = read_file.readlines()
            read_file.close()
            write_file = open(self.address.split(':')[1] + '.txt', 'w')
            for i in range(1, len(data)):
                write_file.write(data[i])
            write_file.close()
            return msg
        else:
            return "There is no any message"

    def push_message(self, msg: str):
        self.queue.push(msg)
        if self.queue.get_size() == 1:
            file = open(self.address.split(':')[1] + '.txt', 'w')
            file.write(msg+'\n')
            file.close()
        else:
            file = open(self.address.split(':')[1] + '.txt', 'a')
            file.write(msg+'\n')
            file.close()
        return 'OK'

    def get_status(self):
        return str(self.queue.get_size())
