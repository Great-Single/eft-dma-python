import memprocfs
import threading


class Memory:
    def __init__(self):
        self.tarkov_process = False
        self.vmm = self.initialize_dma()

    def initialize_dma(self):
        self.vmm = memprocfs.Vmm(["-device", "fpga"])
        print("self.vmm")

    def check_for_process(self):
        if self.tarkov_process:
            return self.tarkov_process
        if not self.vmm:
            print("would check for process, but no dma connection initialized")
            return False
        print("checking for tarkov process")
        threading.Timer(1.0, self.check_for_process).start()
        tarkov_process = self.vmm.process("EscapeFromTarkov.exe")
        if tarkov_process:
            print("found tarkov process")
            self.tarkov_process = tarkov_process
        return False
