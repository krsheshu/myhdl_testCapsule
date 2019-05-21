from myhdl import Signal, intbv,always, block

class AvalonMM():
    """ class to access Altera's avalon memory-mapped interface """
    def __init__(self, data_width=8, address_width=4):
        """ configure the memory-mapped interface with corresponding address and datawidth"""
        if not 32== data_width:
            raise ValueError("avalon memory-map bus data_width must be 32")
        if not 1 <= address_width  <= 32:
            raise ValueError("avalon memory-map bus address_width between 1-32")
        ## address bus
        self.address_i = Signal(intbv(0)[address_width:])
        ## write data bus
        self.writedata_i = Signal(intbv(0)[data_width:])
        ## write enable signal
        self.write_i = Signal(bool(0))
        ## read enable signal
        self.read_i = Signal(bool(0))
        ## read data bus
        self.readdata_o = Signal(intbv(0)[data_width:])


class AvalonST_SNK():
    """ class to access Altera's streaming sink interface """
    def __init__(self, data_width=8, error_width=3, empty_width=3, channel_width=4):
        """ configure the streaming sink interface with corresponding datawidth and streaming related signal  """
        ## ready output signal
        self.ready_o = Signal(bool(0))
        ## start of packet input signal
        self.startofpacket_i = Signal(bool(0))
        ## end of packet input signal
        self.endofpacket_i = Signal(bool(0))
        ## valid input signal
        self.valid_i = Signal(bool(0))
        ## error input signal, currently not used
        self.error_i = Signal(intbv(0)[error_width:])
        ## empty input signal, currently not used
        self.empty_i = Signal(intbv(0)[empty_width:])
        ## channel input signal, currently not used
        self.channel_i = Signal(intbv(0)[channel_width:])
        ## data bus input signal
        self.data_i = Signal(intbv(0)[data_width:])

class AvalonST_SRC():
    """ class to access Altera's streaming source interface """
    def __init__(self, data_width=8, error_width=3, empty_width=3, channel_width=4):
        """ configure the streaming source interface with corresponding datawidth and streaming related signal  """
        ## ready input signal
        self.ready_i = Signal(bool(0))
        ## start of packet output signal
        self.startofpacket_o = Signal(bool(0))
         ## end of packet output signal
        self.endofpacket_o = Signal(bool(0))
         ## valid  output signal
        self.valid_o = Signal(bool(0))
         ## error output signal, currently not used
        self.error_o = Signal(intbv(0)[error_width:])
         ## empty output signal, currently not used
        self.empty_o = Signal(intbv(0)[empty_width:])
         ## channel output signal, currently not used
        self.channel_o = Signal(intbv(0)[channel_width:])
         ## data bus input signal
        self.data_o = Signal(intbv(0)[data_width:])

