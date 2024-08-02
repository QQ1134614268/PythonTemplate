test()

function test() {
    // 测试lambda
    testBianli(["a", "b"])

    const arr = [{"sql": "ff"}, {"sql": "ff"}, {"sql": "ff"}];
    // 测试lambda
    console.log(filterRepeat(arr));
    console.log(Array.from(new Set(arr)));

    testSetTimeout()
    testInterval()

    const obj1 = {a: 1};
    const obj2 = {a: 1};
    const obj3 = obj1;

    console.log(Object.is(obj1, obj2)); // false
    console.log(Object.is(obj1, obj3)); // true
    console.log(obj1 === obj2); // false
    console.log(obj1 === obj3); // true

    console.log(equals(obj1, obj2)); // true
}

function equals(obj1, obj2) {
    const obj1Keys = Object.keys(obj1);
    const obj2Keys = Object.keys(obj2);

    if (obj1Keys.length !== obj2Keys.length) {
        return false;
    }

    for (let key of obj1Keys) {
        if (obj1[key] === obj2[key]) {
            return false;
        }
    }

    return true;
}

function filterRepeat(arr) {
    // 数组去重 -- 对象数组去重

    // 1.利用Array.from(new Set(arr))去重：
    // 2.利用includes去重
    // 3.利用map去重
    // 4.利用indexOf去重
    // 5.利用单层for循环去重
    // 6.利用双层for循环去重
    // 7.利用递归去重
    // 8.利用Array.filter和map对象数组去重 （性能较高）
    // 9.利用Array.filter和Array.includes 对象数组去重

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

// testJs 测试js
function testBianli(arr) {
    // 测试 遍历js

    // 1. for遍历
    // 2. for in
    // 3. for of
    // 4. foreach
    arr.forEach((item, index, arr) => {
        console.log(item, index)
    })
    // 5. map
    arr.map((item, index, arr) => {
        console.log(item, index)
    })
    // 6. filter
    arr.filter((item, index, arr) => {
        console.log(item, index)
    })
    // 7. some
    arr.some((item, index, arr) => {
        console.log(item, index)
    })
    // 8. every
    arr.every((item, index, arr) => {
        console.log(item, index)
    })

    // 9. reduce
    arr.reduce((total, item, index, arr) => {
        console.log(total, item, index)
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