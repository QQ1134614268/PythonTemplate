function isObjectEqual(obj1, obj2) {
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

    // 1.利用Array.from(new Set(arr))去重：
    // 2.利用includes去重
    // 3.利用map去重
    // 4.利用indexOf去重
    // 5. 利用单层for循环去重
    // 6.利用双层for循环去重
    // 7.利用递归去重
    // 8.利用Array.filter和map对象数组去重 （性能较高）
    // 9.利用Array.filter和Array.includes 对象数组去重

    let newArr = []
    for (let a of arr) {
        let flag = false
        for (let b of newArr) {
            if (isObjectEqual(a, b)) {
                flag = true
            }
        }
        if (flag === false) {
            newArr.push(a)
        }
    }
    return newArr;
}

const obj1 = {a: 1};
const obj2 = {a: 1};
const obj3 = obj1;

console.log(Object.is(obj1, obj2)); // false
console.log(Object.is(obj1, obj3)); // true
console.log(obj1 === obj2); // false
console.log(obj1 === obj3); // true

const arr = [{"sql": "fffffffddffff"}, {"sql": "fffffffddffff"}, {"sql": "fffffffddffff"}, {"sql": "fffffffddffff"}, {"sql": "fffffffddffff"}, {"sql": "fffffffddffff"}, {"sql": "fffffffddffff"}, {"sql": "fffffffddffff"}, {"sql": "fffffffddffff"}, {"sql": "fffffffddffff"}];

console.log(Array.from(new Set(arr)));
console.log(filterRepeat(arr));
