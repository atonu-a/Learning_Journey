class Computer:
    def __init__(self, cpu, ram, ssd) -> None:
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        
    def __str__(self) :
        return f"Computer built successfully!"


class Builder:
    def __init__(self) :
        self.cpu = None
        self.ram = None
        self.ssd = None
        
    
    def set_cpu(self, cpu):
        self.cpu = cpu
        print(f"{self.cpu} cpu set")
        return self
    def set_ram(self, ram):
        self.ram = ram
        print(f"{self.ram} GB ram set")
        return self
    def set_ssd(self, ssd):
        self.ssd = ssd
        print(f"{self.ssd} GB ssd set")
        return self
    def build(self):
        return Computer(self.cpu, self.ram, self.ssd)
    
    
build = Builder()
pc = build.set_cpu("Core I5").set_ram("16").set_ssd("512").build()
print(pc)