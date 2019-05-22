from myhdl import Signal, intbv 

class AvalonST_Pars():
    """ Avalon Streaming IF Parameter class """ 
    def __init__(self, DATAWIDTH=8, ERRORWIDTH=3, EMPTYWIDTH=3, CHANNELWIDTH=4):
        """ Initialize  """
        self.DATAWIDTH      = DATAWIDTH
        self.ERRORWIDTH     = ERRORWIDTH
        self.EMPTYWIDTH     = EMPTYWIDTH
        self.CHANNELWIDTH   = CHANNELWIDTH

class AvalonST_SNK():
    """ Avalon streaming sink interface """
    def __init__(self, pars):
        """ Initialize  """
        self.ready_o = Signal(bool(0))
        self.startofpacket_i = Signal(bool(0))
        self.endofpacket_i = Signal(bool(0))
        self.valid_i = Signal(bool(0))
        self.error_i = Signal(intbv(0)[pars.ERRORWIDTH:])
        self.empty_i = Signal(intbv(0)[pars.EMPTYWIDTH:])
        self.channel_i = Signal(intbv(0)[pars.CHANNELWIDTH:])
        self.data_i = Signal(intbv(0)[pars.DATAWIDTH:])


class AvalonST_SRC():
    """ Avalon streaming source interface """
    def __init__(self, pars):
        """ Initialize  """
        self.ready_i = Signal(bool(0))
        self.startofpacket_o = Signal(bool(0))
        self.endofpacket_o = Signal(bool(0))
        self.valid_o = Signal(bool(0))
        self.error_o = Signal(intbv(0)[pars.ERRORWIDTH:])
        self.empty_o = Signal(intbv(0)[pars.EMPTYWIDTH:])
        self.channel_o = Signal(intbv(0)[pars.CHANNELWIDTH:])
        self.data_o = Signal(intbv(0)[pars.DATAWIDTH:])

