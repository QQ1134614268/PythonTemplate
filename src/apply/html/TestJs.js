test()

function test() {
    // 测试lambda
    testBianli(["aa", 'bb'])

    console.log('自定义去重', filterRepeat([{"a": "1"}, {"a": "1"}, {"a": "2"}]));

    const obj1 = {a: 1};
    const obj2 = {a: 1};
    console.log('对象相等: ', Object.is(obj1, obj2), obj1 === obj2);
    console.log('自定义equals: ', equals(obj1, obj2));

    testSetTimeout()

    testInterval()
}

function equals(obj1, obj2) {
    // 考虑null, keys方法不存在场景
    const obj1Keys = Object.keys(obj1);
    const obj2Keys = Object.keys(obj2);

    if (obj1Keys.length !== obj2Keys.length) {
        return false;
    }

    for (let key of obj1Keys) {
        if (obj1[key] !== obj2[key]) {
            return false;
        }
    }

    return true;
}

function filterRepeat(arr) {
    // 数组去重 -- 对象数组去重
    let newArr = []
    for (let a of arr) {
        let flag = false
        for (let b of newArr) {
            if (equals(a, b)) {
                flag = true
            }
        }
        if (flag === false) {
            newArr.push(a)
        }
    }
    return newArr;
}

// testJs 遍历数据
function testBianli(arr) {
    // 测试 遍历数据 Lambda mapReduce

    // 1. for遍历
    for (let i = 0; i < arr.length; i++) {
        console.log('for-i: ', arr[i])
    }
    // 2. for in
    for (const i in arr) {
        console.log('for-in: ', arr[i])
    }
    // 3. for of
    for (const item of arr) {
        console.log('for-of: ', item)
    }
    // 4. foreach
    arr.forEach((item, index, arr) => {
        console.log('forEach: ', item, index)
    })
    // 5. map
    arr.map((item, index, arr) => {
        console.log('map: ', item, index)
    })
    // 6. filter
    arr.filter((item, index, arr) => {
        console.log('filter: ', item, index)
    })
    // 7. some
    arr.some((item, index, arr) => {
        console.log('some: ', item, index)
    })
    // 8. every
    arr.every((item, index, arr) => {
        console.log('every: ', item, index)
    })
    // 9. reduce
    arr.reduce((total, item, index, arr) => {
        console.log('reduce: ', total, item, index)
    })
}

function testSetTimeout() {
    // 测试定时
    setTimeout((arg1, arg2) => {
        console.log(arg1, arg2)
    }, 5000, "tom", "cat")
}

function testInterval() {
    // 测试循环
    let interval = setInterval((arg1, arg2, endTime) => {
        if (new Date().getTime() > endTime) {
            console.log('end')
            clearInterval(interval)
        }
        console.log(arg1, arg2, new Date())
    }, 1000, "tom", "cat", new Date().getTime() + 5000)
}

class User {
    static tableName = "user_t"

    constructor(name, age) {
        this.name = name
        this.age = age
    }

    getName() {
        return this.name
    }

    static of(name, age) {
        return new User(name, age)
    }
}