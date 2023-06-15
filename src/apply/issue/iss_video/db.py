from dataclasses import dataclass


@dataclass()
class CameraChannel:
    username: str
    password: str

    ip: str
    port: str
    channel: int
    desc: str

    @property
    def net(self):
        return f"rtsp://{self.username}:{self.password}@{self.ip}:{self.port}//Streaming/Channels/2"

    @property
    def url(self):
        return f"rtsp://{self.username}:{self.password}@{self.ip}:{self.port}/Streaming/Channels/{self.channel}"

    @property
    def onvif(self):
        return f"rtsp://{self.username}:{self.password}@{self.ip}:{self.port}/cam/realmonitor?channel={self.channel}&subtype=0&unicast=true&proto=Onvif"

    @property
    def channel_1(self):
        return f"rtsp://{self.username}:{self.password}@{self.ip}:{self.port}/Streaming/Channels/{self.channel}"


hik_ = CameraChannel("admin2", "Nshf@188688", "44.39.107.85", "554", 0, desc="云天-小沙山")
