from Memory import memory


class OperationsManager:
    def __init__(self):
        self.memory = self.memory_init()

    def memory_init(self):
        print("<(o.o<) welcome")
        print("initializing memory access over DMA")
        memory = memory.Memory()
        print("memory", memory)
        self.memory = memory
