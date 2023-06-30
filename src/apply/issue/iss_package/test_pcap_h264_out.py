from scapy.all import *


class ProcessReader:
    def __init__(self, file):
        self.pcapngFile = file
        self.pkt = None
        self.rtpDict = {}

    def yieldReader(self):
        with PcapReader(self.pcapngFile) as reader:
            yield from reader

    @property
    def hasRawLayer(self) -> bool:
        return self.pkt.haslayer(Raw)

    @property
    def __raw(self):
        if self.hasRawLayer:
            return self.pkt[Raw]
        else:
            raise IndexError("Raw Data not found in packet")

    @property
    def isRTP(self) -> bool:
        # 标准化的RTP Payload Type值由RFC 3551定义
        # https://www.iana.org/assignments/rtp-parameters/rtp-parameters.xhtml
        if self.hasRawLayer:
            rawData = self.pkt[Raw]
            payload_type = rawData.load[1] & 0x7F
            return payload_type == 96
        return False

    @property
    def __ssrc(self):
        ssrc = int.from_bytes(self.__raw.load[8:12], byteorder='big')
        ssrc = hex(ssrc)
        return ssrc

    def getAllRTPSteam(self):
        for pkt in self.yieldReader():
            self.pkt = pkt
            if self.isRTP:
                ssrcNumber = self.__ssrc
                payload = self.__raw.load[12:]
                if ssrcNumber not in self.rtpDict:
                    self.rtpDict[ssrcNumber] = payload
                else:
                    self.rtpDict[ssrcNumber] += payload
        return self

    def run(self):
        self.getAllRTPSteam()
        for ssrc, payloads in self.rtpDict.items():
            wrpcap(f'{ssrc}.raw', payloads)


if __name__ == '__main__':
    filepath = './test_out_export_h264.pcapng'
    process = ProcessReader(filepath)
    process.run()
