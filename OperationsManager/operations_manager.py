from Memory.memory import Memory


class OperationsManager:
    def __init__(self):
        self.memory = self.memory_init()

    def memory_init(self):
        print("<(o.o<) welcome")
        print("initializing memory access over DMA")
        self.memory = Memory()
