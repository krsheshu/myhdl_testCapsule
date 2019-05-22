from myhdl import Signal, intbv,always, block

class AvalonMM_Pars():
    """ Avalon Memory Mapped IF Parameter class """ 
    def __init__(self, DATAWIDTH=8, ADDRESSWIDTH=3):
        """ Initialize  """
        self.DATAWIDTH      = DATAWIDTH
        self.ADDRESSWIDTH   = ADDRESSWIDTH 

class AvalonMM():
    """ Avalon Memory Mapped IF class """ 
    def __init__(self, pars):
        """ Initialize  """
        if not 32== pars.DATAWIDTH:
            raise ValueError("Avalon Memory-Map bus DATAWIDTH must be 32")
        if not 1 <= pars.ADDRESSWIDTH <= 32:
            raise ValueError("Avalon Memory-Map bus ADDRESSWIDTH between 1-32")
        self.address_i = Signal(intbv(0)[pars.ADDRESSWIDTH:])
        self.write_i = Signal(bool(0))
        self.writedata_i = Signal(intbv(0)[pars.DATAWIDTH:])
        self.read_i = Signal(bool(0))
        self.readdata_o = Signal(intbv(0)[pars.DATAWIDTH:])

