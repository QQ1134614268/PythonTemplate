class Db {
    // todo 类似 redis 或 mysql存储 orm
    // row
    // table, id , other

    static db = "Db";
    static  data = {}; // 数组

    static set(data, key) {
        if (!key) {
            key = Math.random().toString()
        }
        data[key] = data
        Db.syncSet()
    }

    static get(key) {
        return data[key]
    }

    static syncSet() {
        localStorage.setItem(Db.db, JSON.stringify(data))
    }

    static syncGet() {
        return JSON.parse(localStorage.getItem(Db.db))
    }

    task() {
        Db.syncSet()
    }
}


class Stream {

}