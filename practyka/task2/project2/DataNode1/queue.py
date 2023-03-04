class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, msg: str):
        self.queue.append(msg)
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.queue.pop(0)
            self.size -= 1

    def top(self):
        if self.size != 0:
            return self.queue[0]

    def get_size(self):
        return self.size
