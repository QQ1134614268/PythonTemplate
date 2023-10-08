function post(url, data) {
    return new axios({
        method: 'POST', url: url, // params: data,
        data: data
    })
}

function get(url, data) {
    return new axios({
        method: 'GET', url: url, params: data
    })
}

function getDevice(params) {
    // ?search=&page=1&count=15
    return get(`http://44.39.19.14:10070/api/device/query/devices`, params)
}

function getChannel(deviceId, params) {
    // ?page=1&count=15&query=&online=&channelType=
    return get(`http://44.39.19.14:10070/api/device/query/devices/${deviceId}/channels`, params)
}

function get452BanDao() {
    // 测试卡顿 视频预警, simd wcs
    // return get(`http://44.39.19.14:10070/api/playback/start/44030500101325097172/44030500101325497172?startTime=2023-09-13+17:20:38&endTime=2023-09-13+17:20:59`)

    // 测试拖拽,倍速播放, 半岛城邦 4小时
    return get(`http://44.39.19.14:10070/api/playback/start/44030500101325149136/44030500101325449136?startTime=2023-09-04+00:00:00&endTime=2023-09-04+10:00:00`)
    // return get(`http://44.39.19.14:10070/api/playback/start/44030500101325107080/44030500101325407080?startTime=2023-09-13+23:59:59&endTime=2023-09-14+10:10:10`)
    // return get(`http://44.39.19.14:10070/api/playback/start/44030500101325166153/44030500101325466153?startTime=2023-09-13+23:59:59&endTime=2023-09-14+04:28:26`)
    // return get(`http://44.39.19.14:10070/api/playback/start/44030500101325166166/44030500101325466166?startTime=2023-09-13+23:59:59&endTime=2023-09-14+11:22:17`)

    // 测试流结束事件  10秒
    // return get(`http://44.39.19.14:10070/api/playback/start/44030500101325149136/44030500101325449136?startTime=2023-09-04+06:00:00&endTime=2023-09-04+06:00:10`)
}

function gbQuery(deviceId, channelId, params) {
    return get(`https://44.39.19.14:10070/api/gb_record/query/${deviceId}/${channelId}`, params)
}

function gbStart() {
    return get(`http://44.39.19.14:10070/api/playback/start/44030500101325149136/44030500101325449136?startTime=2023-09-04+00:00:00&endTime=2023-09-04+10:30:37`)
}

function gbStop(deviceId, channelId, streamId) {
    return get(`http://44.39.19.14:10070/api/playback/${deviceId}/${channelId}/${streamId}`)
}

function gbPause(streamId) {
    return get(`http://44.39.19.14:10070/api/playback/pause/${streamId}`)
}

function gbResume(streamId) {
    return get(`http://44.39.19.14:10070/api/playback/resume/${streamId}`)
}

function gbSeek(streamId, seekTime) {
    return get(`http://44.39.19.14:10070/api/playback/seek/${streamId}/${seekTime}`)
}

function gbSpeed(streamId, speed) {
    return get(`http://44.39.19.14:10070/api/playback/speed/${streamId}/${speed}`)
}

function gbExist(streamId) {
    return get(`http://44.39.19.14:10070/api/playback/exist/${streamId}`)
}
