import threading
from os import path

import memprocfs


class Memory:
    def __init__(self):
        self.tarkov_process = False
        self.mmap_exists = self.check_for_mmap()
        self.vmm = self.initialize_dma()

    def initialize_dma(self):
        if self.mmap_exists:
            self.vmm = memprocfs.Vmm(["-device", "fpga", "-mmap", "mmap.txt"])
        else:
            self.vmm = memprocfs.Vmm(["-device", "fpga"])
        if self.vmm:
            print("initialized DMA access")
        if not self.vmm:
            if not self.mmap_exists:
                print("Failed to initialize DMA without mmap - generating mmap")
                self.generate_mmap()
                if self.mmap_exists:
                    self.vmm = memprocfs.Vmm(["-device", "fpga", "-mmap", "mmap.txt"])
                else:
                    print("Could not generate mmap.")
            else:
                print("Failed to connect to DMA device despite existing mamp.txt")

    def check_for_mmap(self):
        if path.exists("mmap.txt"):
            print("found existing mmap.txt")
            return True
        return False

    def generate_mmap(self):
        print("todo: generate a mmap automatically for user")

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
