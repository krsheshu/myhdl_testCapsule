from myhdl import always, always_comb, Signal, intbv, concat, instances
from avalon_interfaces import AvalonST_SRC
import logging


class StreamingSrcBfm():
    """ Streaming Src BFM Class """

    def __init__(self, validPattern=0xf0f0, dataFIFO=None, av_src_pars=None):
        """  Generics """
        self.validPattern = validPattern
        self.PATTERNBITS = 16

        if (dataFIFO == None):
            raise ValueError(
                "Pattern list for {} not passed !".format(__class__))
        else:
            self.dataFIFO = datFIFO

        """ Interfaces  """
        if (av_src_pars == None):
            raise ValueError(
                "Avalon Streaming Src Interface Pars for {} not passed !".format(__class__))
        else:
            self.av_src = AvalonST_SRC(av_src_pars)

    @block
    def top(reset, clk, av_src):
        """ Top Block """

        circular_patternQueue = Signal(
            intbv(self.validPattern)[self.PATTERNBITS:])

        @always(clk.posedge, reset.posedge)
        def vldPattern_shifter():
            """ Circular Queue for valid pattern """
            if enShift == 1:
                circular_patternQueue.next[self.PATTERNBITS:] = concat(
                    circular_patternQueue[self.PATTERNBITS-1:], circular_patternQueue[self.PATTERNBITS-1])

        enShift = Signal(bool(0))

        @always_comb
        def enShift_proc():
            """ Shift the Queue when data is transfered or when the shift pattern is zero """
            if reset == 1:
                enShift.next = 0
            elif (av_src.ready_i == 1 and av_src.valid_o == 1) or (circular_patternQueue[self.PATTERNBITS] == 0):
                enShift.next = 1
            else:
                enShift.next = 0

        @always_comb
        def genValid_proc():
            """ Generating av_src valid_o patternQueue MSB """
            if reset == 1:
                av_src.valid_o.next = 0
            elif circular_patternQueue[self.PATTERNBITS-1] == 1 and src_bfm_i.valid_i == 1:
                av_src.valid_o.next = 1
            else:
                av_src.valid_o.next = 0

        srcBfm_nbTransfers = 0

        @always(clk.posedge)
        def print_bfm_op():
            # Printing the src bfm data
            if av_src.valid_o == 1 and av_src.ready_i == 1:
                srcBfm_nbTransfers += 1
                # print str(num_counter.nb) + ". SrcBfm: transmitted data:", av_src.data_o

        @  always_comb
        def beh_data_o():
            if reset == 1:
                av_src.data_o.next = 0
                av_src.startofpacket_o.next = 0
                av_src.endofpacket_o.next = 0
            elif av_src.valid_o == 1:
                av_src.data_o.next = src_bfm_i.data_i
                av_src.startofpacket_o.next = src_bfm_i.startofpacket_i
                av_src.endofpacket_o.next = src_bfm_i.endofpacket_i
            else:
                av_src.data_o.next = 0
                av_src.startofpacket_o.next = 0
                av_src.endofpacket_o.next = 0

        return instances()
