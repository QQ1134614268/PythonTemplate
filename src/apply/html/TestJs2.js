// 测试定时
setTimeout((arg1, arg2) => {
    console.log(arg1, arg2)
}, 5000, "tom", "cat")

// 测试循环
let interval = setInterval((arg1, arg2, endTime) => {
    if (new Date().getTime() > endTime) {
        console.log('end')
        clearInterval(interval)
    }
    console.log(arg1, arg2, new Date())
}, 1000, "tom", "cat", new Date().getTime() + 5000)
