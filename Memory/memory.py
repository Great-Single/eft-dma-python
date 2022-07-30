from os import path

import memprocfs

from Utils.timer import RepeatedTimer


class Memory:
    def __init__(self):
        self.tarkov_process = False
        self.mmap_exists = self.check_for_mmap()
        self.initialize_dma()
        self.process_check_timer = RepeatedTimer(1, self.check_for_process)

    def initialize_dma(self):
        print("initializing memory access over DMA")
        if self.mmap_exists:
            self.vmm = memprocfs.Vmm(["-device", "fpga", "-mmap", "mmap.txt"])
        else:
            self.vmm = memprocfs.Vmm(["-device", "fpga"])
        print(dir(self.vmm))
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
        tarkov_process = None
        if self.tarkov_process:
            return
        if not self.vmm:
            print(dir(self.vmm))
            print("would check for process, but no dma connection initialized")
            return
        print("checking for tarkov process")
        try:
            tarkov_process = self.vmm.process("EscapeFromTarkov.exe")
        except RuntimeError:
            print("Tarkov not running")
        if tarkov_process:
            print("found tarkov process")
            self.tarkov_process = tarkov_process
            self.process_check_timer.stop()
        return
