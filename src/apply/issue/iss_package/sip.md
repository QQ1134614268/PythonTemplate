sip 状态码 
    100 Trying
    200 ok
    486 Busy Here 被叫忙
    500 服务器内部错误
    6xx 全局失败

sip 请求类型:
    INVITE: 媒体协商
    REGISTER
    BYE
    ACK
    CANCEL
    OPTIONS: 获取能力集, 支持的方法

    PEFER
    SUBSCRIBE
    NOTIFY
    PUBLISH
    MESSAGE
    UPDATE
    INFO

sip 请求头
    Call-ID 全局唯一, 呼叫期间一直使用
    CSeq: 每一个新请求,递增
    TO
    FROM:
    Via:
    Contact:
    Max-Forwards:

SDP:
    sip 头域中 Content-Type 可以定义为 sdp 类型

ps:
    pass
h264: