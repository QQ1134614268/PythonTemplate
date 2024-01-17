//  参考       https://blog.csdn.net/shangmingtao/article/details/74463500
const axios = require("axios")
const qs = require("qs")

function test1() {
    let url = `http://127.0.0.1:8080/api/v1/hcmanagement/test0` // get 原始类型 大小写有些影响, 参数多少无影响(多,忽略,少 null)
    let res = axios.get(url, {
        params: {
            name: "tom", // password:[1,2,3],  // Integer[] password  数组参数 接收不到
            password: 1,
        }
    })
    console.log(res)
}

function test2() {
    let url = `http://127.0.0.1:8080/api/v1/hcmanagement/test1`  // get 类 ,,,  直接映射,,若 包装 映射失败  (中英文 无影响)  //类中,原始类型有同名参数
    let res = axios.get(url, {
        params: {
            name: "你", password: "123", k: "来了"
        }
    })
    console.log(res)
}

function test3() {
    let url = `http://127.0.0.1:8080/api/v1/hcmanagement/test2`  // post 基础类型 url参数 大小写敏感,,,()  //  set 方法名,如果 set方法大小写有误,不能映射字段
    axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    let data = qs.stringify({
        name: "tom", passWoRd: "123"
    });
    let res = axios.post(url, data)
    console.log(res)
}

function test4() {
    let url = `http://127.0.0.1:8080/api/v1/hcmanagement/test3`
    let data = {
        name: "11",
        vos: [{name: 1, password: 123}, {name: 1, password: 123}],
        vo: {"name": 1, password: 123},
        ids: ["1", "2"]
    }
    axios.defaults.headers.post['Content-Type'] = 'application/json';
    let res = axios.post(url, data)
    console.log(res)
}
