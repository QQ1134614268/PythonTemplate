function post(url, data) {
    return axios.post(url, {data: data});
}

function get(url, params) {
    return axios.get(url, {params: params});
}

let host = 'http://44.39.19.14:17080';
// let host = 'http://44.39.17.34:17080';

let urlList = [
    {
        label: '海韵园44.39.107.80 子码流',
        value: `/api/play/start/44030500101325107080/44030500101325407080`
    },
    {
        label: '海韵园44.39.107.80 主码流',
        value: `/api/play/start/44030500101325107080/44030500101325407080?streamLevel=0`
    },
    {
        label: '海韵园44.39.107.80 历史视频',
        value: `/api/playback/start/44030500101325107080/44030500101325407080`
    },
]

async function gbQuery() {
    let now = new Date();
    let year = now.getFullYear()
    let month = ('0' + (now.getMonth() + 1)).slice(-2)
    let dd = ('0' + now.getDate()).slice(-2)
    let hh = ('0' + now.getHours()).slice(-2)
    let mm = ('0' + now.getMinutes()).slice(-2)
    // return get(`${host}/api/gb_record/query/44030500101325107087/44030500101325407087?startTime=2024-01-15+18:00:00&endTime=${year}-${month}-${dd}+${hh}:${mm}:00`)
    return get(`${host}/api/gb_record/query/44030500101325107087/44030500101325407087?startTime=${year}-${month}-${dd}+09:40:00&endTime=${year}-${month}-${dd}+${hh}:${mm}:00`)
}

async function getGbUrl(url) {
    if (url.includes("playback") && !url.includes("startTime")) {
        let now = new Date();
        let today = `${now.getFullYear()}-${('0' + (now.getMonth() + 1)).slice(-2)}-${('0' + now.getDate()).slice(-2)}`
        url = `${url}?startTime=${today}+07:00:00&endTime=${today}+10:00:00`
    }
    let res = await get(`${host}${url}`)
    let arr = url.split(/[/?]/)
    res.data.deviceId = arr[4]
    res.data.deviceId = arr[5]
    return res
}

function gbStop(deviceId, channelId, streamId) {
    return get(`${host}/api/playback/stop/${deviceId}/${channelId}/${streamId}`)
}

function gbPause(streamId) {
    return get(`${host}/api/playback/pause/${streamId}`)
}

function gbResume(streamId) {
    return get(`${host}/api/playback/resume/${streamId}`)
}

function gbSeek(streamId, seekTime) {
    return get(`${host}/api/playback/seek/${streamId}/${seekTime}`)
}

function gbSpeed(streamId, speed) {
    return get(`${host}/api/playback/speed/${streamId}/${speed}`)
}

function gbExist(streamId) {
    return get(`${host}/api/playback/exist/${streamId}`)
}
