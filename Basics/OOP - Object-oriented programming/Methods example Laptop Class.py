#Focus on methods:

class Laptop:
    def __init__ (self, cpu, ram = 4096, gpu = "AMD", price = 2000):
        self.SetCPU(cpu)
        self.gpu = gpu
        self.price = price
        self.setRam(ram)
        self.PrintData()

    def SetCPU (self, cpu):
        if cpu.lower() == "amd" or cpu.lower() == "intel" or cpu.lower() == "arm":   #cpu.lower() - covers for both capital letters and lowercase
            self.cpu = cpu
        else:
            self.cpu = "other"

    def PrintData (self):
        print(self.cpu, self.ram, self.gpu, self.price)

    def setRam (self, ram): 
        if type(ram) == int and ram >= 2048:
            self.ram = ram
        else:
            self.ram = 2048

LaptopSerna = Laptop ("AMD") # AMD 4096 AMD 2000
LaptopDoffo = Laptop ("Xera", 1024) # other 2048 AMD 2000
LaptopGenko = Laptop ("IntEL" , 8192, "Intel", 3800) # IntEL 8192 Intel 3800



