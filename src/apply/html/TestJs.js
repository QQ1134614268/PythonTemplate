// testJs 测试js
function bianli() {
    // 测试 遍历js

    let arr = ["a", "b"]
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

bianli()