!function (e, t) {
    "object" == typeof exports && "undefined" != typeof module ? t(require("path"), require("fs"), require("crypto")) : "function" == typeof define && define.amd ? define(["path", "fs", "crypto"], t) : t((e = "undefined" != typeof globalThis ? globalThis : e || self).path, e.fs, e.crypto$1)
}(this, function (e, g, y) {
    "use strict";

    function b(e) {
        return e && "object" == typeof e && "default" in e ? e : {default: e}
    }

    var Bt = b(e), At = b(g), Tt = b(y);

    function v(e, t) {
        return e(t = {exports: {}}, t.exports), t.exports
    }

    var w = v(function (z) {
        var _;
        (_ = void 0 !== (_ = void 0 !== _ ? _ : {}) ? _ : {}).locateFile = function (e) {
            return "decoder-pro-simd.wasm" == e && "undefined" != typeof JESSIBUCA_PRO_SIMD_WASM_URL && "" != JESSIBUCA_PRO_SIMD_WASM_URL ? JESSIBUCA_PRO_SIMD_WASM_URL : e
        };
        var t, m, R, M, N, O, s, G = Object.assign({}, _), H = "./this.program", V = "object" == typeof window,
            h = "function" == typeof importScripts,
            $ = "object" == typeof process && "object" == typeof process.versions && "string" == typeof process.versions.node,
            e = "", j = ($ ? (e = h ? Bt.default.dirname(e) + "/" : __dirname + "/", O = () => {
                N || (M = At.default, N = Bt.default)
            }, t = function (e, t) {
                return O(), e = N.normalize(e), M.readFileSync(e, t ? void 0 : "utf8")
            }, R = e => {
                e = t(e, !0);
                return e = e.buffer ? e : new Uint8Array(e)
            }, m = (e, r, i) => {
                O(), e = N.normalize(e), M.readFile(e, function (e, t) {
                    e ? i(e) : r(t.buffer)
                })
            }, 1 < process.argv.length && (H = process.argv[1].replace(/\\/g, "/")), process.argv.slice(2), z.exports = _, process.on("uncaughtException", function (e) {
                if (!(e instanceof function (e) {
                    this.name = "ExitStatus", this.message = "Program terminated with exit(" + e + ")", this.status = e
                })) throw e
            }), process.on("unhandledRejection", function (e) {
                throw e
            }), _.inspect = function () {
                return "[Emscripten Module object]"
            }) : (V || h) && (h ? e = self.location.href : "undefined" != typeof document && document.currentScript && (e = document.currentScript.src), e = 0 !== e.indexOf("blob:") ? e.substr(0, e.replace(/[?#].*/, "").lastIndexOf("/") + 1) : "", t = e => {
                var t = new XMLHttpRequest;
                return t.open("GET", e, !1), t.send(null), t.responseText
            }, h && (R = e => {
                var t = new XMLHttpRequest;
                return t.open("GET", e, !1), t.responseType = "arraybuffer", t.send(null), new Uint8Array(t.response)
            }), m = (e, t, r) => {
                var i = new XMLHttpRequest;
                i.open("GET", e, !0), i.responseType = "arraybuffer", i.onload = () => {
                    200 == i.status || 0 == i.status && i.response ? t(i.response) : r()
                }, i.onerror = r, i.send(null)
            }), _.print || console.log.bind(console)), o = _.printErr || console.warn.bind(console),
            W = (Object.assign(_, G), _.arguments && _.arguments, _.thisProgram && (H = _.thisProgram), _.quit && _.quit, _.wasmBinary && (s = _.wasmBinary), _.noExitRuntime, "object" != typeof WebAssembly && b("no native wasm support detected"), !1);

        function Y(e, t) {
            e || b(t)
        }

        var q, f, u, l, K, d, p, X, Z, J, Q = "undefined" != typeof TextDecoder ? new TextDecoder("utf8") : void 0;

        function a(e, t, r) {
            for (var i = t + r, n = t; e[n] && !(i <= n);) ++n;
            if (16 < n - t && e.buffer && Q) return Q.decode(e.subarray(t, n));
            for (var s = ""; t < n;) {
                var a, o, l = e[t++];
                128 & l ? (a = 63 & e[t++], 192 != (224 & l) ? (o = 63 & e[t++], (l = 224 == (240 & l) ? (15 & l) << 12 | a << 6 | o : (7 & l) << 18 | a << 12 | o << 6 | 63 & e[t++]) < 65536 ? s += String.fromCharCode(l) : (o = l - 65536, s += String.fromCharCode(55296 | o >> 10, 56320 | 1023 & o))) : s += String.fromCharCode((31 & l) << 6 | a)) : s += String.fromCharCode(l)
            }
            return s
        }

        function ee(e, t) {
            return e ? a(u, e, t) : ""
        }

        function te(e, t, r, i) {
            if (!(0 < i)) return 0;
            for (var n = r, s = r + i - 1, a = 0; a < e.length; ++a) {
                var o = e.charCodeAt(a);
                if ((o = 55296 <= o && o <= 57343 ? 65536 + ((1023 & o) << 10) | 1023 & e.charCodeAt(++a) : o) <= 127) {
                    if (s <= r) break;
                    t[r++] = o
                } else if (o <= 2047) {
                    if (s <= r + 1) break;
                    t[r++] = 192 | o >> 6, t[r++] = 128 | 63 & o
                } else if (o <= 65535) {
                    if (s <= r + 2) break;
                    t[r++] = 224 | o >> 12, t[r++] = 128 | o >> 6 & 63, t[r++] = 128 | 63 & o
                } else {
                    if (s <= r + 3) break;
                    t[r++] = 240 | o >> 18, t[r++] = 128 | o >> 12 & 63, t[r++] = 128 | o >> 6 & 63, t[r++] = 128 | 63 & o
                }
            }
            return t[r] = 0, r - n
        }

        function re(e) {
            for (var t = 0, r = 0; r < e.length; ++r) {
                var i = e.charCodeAt(r);
                i <= 127 ? t++ : i <= 2047 ? t += 2 : 55296 <= i && i <= 57343 ? (t += 4, ++r) : t += 3
            }
            return t
        }

        _.INITIAL_MEMORY;
        var c, g, y, ie = [], ne = [], se = [], r = 0, ae = null;

        function oe() {
            r++, _.monitorRunDependencies && _.monitorRunDependencies(r)
        }

        function le() {
            var e;
            r--, _.monitorRunDependencies && _.monitorRunDependencies(r), 0 == r && ae && (e = ae, ae = null, e())
        }

        function b(e) {
            throw _.onAbort && _.onAbort(e), o(e = "Aborted(" + e + ")"), W = !0, e += ". Build with -sASSERTIONS for more info.", new WebAssembly.RuntimeError(e)
        }

        function de(e) {
            return e.startsWith("data:application/octet-stream;base64,")
        }

        function he(e) {
            return e.startsWith("file://")
        }

        function fe(e) {
            try {
                if (e == c && s) return new Uint8Array(s);
                if (R) return R(e);
                throw"both async and sync fetching of the wasm failed"
            } catch (e) {
                b(e)
            }
        }

        function ue(e) {
            for (; 0 < e.length;) e.shift()(_)
        }

        function pe(e) {
            this.excPtr = e, this.ptr = e - 24, this.set_type = function (e) {
                p[this.ptr + 4 >> 2] = e
            }, this.get_type = function () {
                return p[this.ptr + 4 >> 2]
            }, this.set_destructor = function (e) {
                p[this.ptr + 8 >> 2] = e
            }, this.get_destructor = function () {
                return p[this.ptr + 8 >> 2]
            }, this.set_refcount = function (e) {
                d[this.ptr >> 2] = e
            }, this.set_caught = function (e) {
                f[this.ptr + 12 >> 0] = e = e ? 1 : 0
            }, this.get_caught = function () {
                return 0 != f[this.ptr + 12 >> 0]
            }, this.set_rethrown = function (e) {
                f[this.ptr + 13 >> 0] = e = e ? 1 : 0
            }, this.get_rethrown = function () {
                return 0 != f[this.ptr + 13 >> 0]
            }, this.init = function (e, t) {
                this.set_adjusted_ptr(0), this.set_type(e), this.set_destructor(t), this.set_refcount(0), this.set_caught(!1), this.set_rethrown(!1)
            }, this.add_ref = function () {
                var e = d[this.ptr >> 2];
                d[this.ptr >> 2] = e + 1
            }, this.release_ref = function () {
                var e = d[this.ptr >> 2];
                return d[this.ptr >> 2] = e - 1, 1 === e
            }, this.set_adjusted_ptr = function (e) {
                p[this.ptr + 16 >> 2] = e
            }, this.get_adjusted_ptr = function () {
                return p[this.ptr + 16 >> 2]
            }, this.get_exception_ptr = function () {
                if (Ut(this.get_type())) return p[this.excPtr >> 2];
                var e = this.get_adjusted_ptr();
                return 0 !== e ? e : this.excPtr
            }
        }

        de(c = "decoder-pro-simd.wasm") || (G = c, c = _.locateFile ? _.locateFile(G, e) : e + G);
        var v = {
            isAbs: e => "/" === e.charAt(0),
            splitPath: e => /^(\/?|)([\s\S]*?)((?:\.{1,2}|[^\/]+?|)(\.[^.\/]*|))(?:[\/]*)$/.exec(e).slice(1),
            normalizeArray: (e, t) => {
                for (var r = 0, i = e.length - 1; 0 <= i; i--) {
                    var n = e[i];
                    "." === n ? e.splice(i, 1) : ".." === n ? (e.splice(i, 1), r++) : r && (e.splice(i, 1), r--)
                }
                if (t) for (; r; r--) e.unshift("..");
                return e
            },
            normalize: e => {
                var t = v.isAbs(e), r = "/" === e.substr(-1);
                return (e = (e = v.normalizeArray(e.split("/").filter(e => !!e), !t).join("/")) || t ? e : ".") && r && (e += "/"), (t ? "/" : "") + e
            },
            dirname: e => {
                var e = v.splitPath(e), t = e[0], e = e[1];
                return t || e ? t + (e = e && e.substr(0, e.length - 1)) : "."
            },
            basename: e => {
                if ("/" === e) return "/";
                var t = (e = (e = v.normalize(e)).replace(/\/$/, "")).lastIndexOf("/");
                return -1 === t ? e : e.substr(t + 1)
            },
            join: function () {
                var e = Array.prototype.slice.call(arguments, 0);
                return v.normalize(e.join("/"))
            },
            join2: (e, t) => v.normalize(e + "/" + t)
        }, w = {
            resolve: function () {
                for (var e = "", t = !1, r = arguments.length - 1; -1 <= r && !t; r--) {
                    var i = 0 <= r ? arguments[r] : E.cwd();
                    if ("string" != typeof i) throw new TypeError("Arguments to path.resolve must be strings");
                    if (!i) return "";
                    e = i + "/" + e, t = v.isAbs(i)
                }
                return (t ? "/" : "") + v.normalizeArray(e.split("/").filter(e => !!e), !t).join("/") || "."
            }, relative: (e, t) => {
                function r(e) {
                    for (var t = 0; t < e.length && "" === e[t]; t++) ;
                    for (var r = e.length - 1; 0 <= r && "" === e[r]; r--) ;
                    return r < t ? [] : e.slice(t, r - t + 1)
                }

                e = w.resolve(e).substr(1), t = w.resolve(t).substr(1);
                for (var i = r(e.split("/")), n = r(t.split("/")), s = Math.min(i.length, n.length), a = s, o = 0; o < s; o++) if (i[o] !== n[o]) {
                    a = o;
                    break
                }
                for (var l = [], o = a; o < i.length; o++) l.push("..");
                return (l = l.concat(n.slice(a))).join("/")
            }
        };

        function ce(e, t, r) {
            r = 0 < r ? r : re(e) + 1, r = new Array(r), e = te(e, r, 0, r.length);
            return t && (r.length = e), r
        }

        var i = {
            ttys: [], init: function () {
            }, shutdown: function () {
            }, register: function (e, t) {
                i.ttys[e] = {input: [], output: [], ops: t}, E.registerDevice(e, i.stream_ops)
            }, stream_ops: {
                open: function (e) {
                    var t = i.ttys[e.node.rdev];
                    if (!t) throw new E.ErrnoError(43);
                    e.tty = t, e.seekable = !1
                }, close: function (e) {
                    e.tty.ops.flush(e.tty)
                }, flush: function (e) {
                    e.tty.ops.flush(e.tty)
                }, read: function (e, t, r, i, n) {
                    if (!e.tty || !e.tty.ops.get_char) throw new E.ErrnoError(60);
                    for (var s, a = 0, o = 0; o < i; o++) {
                        try {
                            s = e.tty.ops.get_char(e.tty)
                        } catch (e) {
                            throw new E.ErrnoError(29)
                        }
                        if (void 0 === s && 0 === a) throw new E.ErrnoError(6);
                        if (null == s) break;
                        a++, t[r + o] = s
                    }
                    return a && (e.node.timestamp = Date.now()), a
                }, write: function (e, t, r, i, n) {
                    if (!e.tty || !e.tty.ops.put_char) throw new E.ErrnoError(60);
                    try {
                        for (var s = 0; s < i; s++) e.tty.ops.put_char(e.tty, t[r + s])
                    } catch (e) {
                        throw new E.ErrnoError(29)
                    }
                    return i && (e.node.timestamp = Date.now()), s
                }
            }, default_tty_ops: {
                get_char: function (e) {
                    if (!e.input.length) {
                        var t = null;
                        if ($) {
                            var r = Buffer.alloc(256), i = 0;
                            try {
                                i = M.readSync(process.stdin.fd, r, 0, 256, -1)
                            } catch (e) {
                                if (!e.toString().includes("EOF")) throw e;
                                i = 0
                            }
                            t = 0 < i ? r.slice(0, i).toString("utf-8") : null
                        } else "undefined" != typeof window && "function" == typeof window.prompt ? null !== (t = window.prompt("Input: ")) && (t += "\n") : "function" == typeof readline && null !== (t = readline()) && (t += "\n");
                        if (!t) return null;
                        e.input = ce(t, !0)
                    }
                    return e.input.shift()
                }, put_char: function (e, t) {
                    null === t || 10 === t ? (j(a(e.output, 0)), e.output = []) : 0 != t && e.output.push(t)
                }, flush: function (e) {
                    e.output && 0 < e.output.length && (j(a(e.output, 0)), e.output = [])
                }
            }, default_tty1_ops: {
                put_char: function (e, t) {
                    null === t || 10 === t ? (o(a(e.output, 0)), e.output = []) : 0 != t && e.output.push(t)
                }, flush: function (e) {
                    e.output && 0 < e.output.length && (o(a(e.output, 0)), e.output = [])
                }
            }
        };

        function me(e) {
            t = e, e = 65536 * Math.ceil(t / 65536);
            var t = Et(65536, e);
            return t ? (e = e, u.fill(0, t, t + e), t) : 0
        }

        var S = {
            ops_table: null, mount: function (e) {
                return S.createNode(null, "/", 16895, 0)
            }, createNode: function (e, t, r, i) {
                if (E.isBlkdev(r) || E.isFIFO(r)) throw new E.ErrnoError(63);
                S.ops_table || (S.ops_table = {
                    dir: {
                        node: {
                            getattr: S.node_ops.getattr,
                            setattr: S.node_ops.setattr,
                            lookup: S.node_ops.lookup,
                            mknod: S.node_ops.mknod,
                            rename: S.node_ops.rename,
                            unlink: S.node_ops.unlink,
                            rmdir: S.node_ops.rmdir,
                            readdir: S.node_ops.readdir,
                            symlink: S.node_ops.symlink
                        }, stream: {llseek: S.stream_ops.llseek}
                    },
                    file: {
                        node: {getattr: S.node_ops.getattr, setattr: S.node_ops.setattr},
                        stream: {
                            llseek: S.stream_ops.llseek,
                            read: S.stream_ops.read,
                            write: S.stream_ops.write,
                            allocate: S.stream_ops.allocate,
                            mmap: S.stream_ops.mmap,
                            msync: S.stream_ops.msync
                        }
                    },
                    link: {
                        node: {
                            getattr: S.node_ops.getattr,
                            setattr: S.node_ops.setattr,
                            readlink: S.node_ops.readlink
                        }, stream: {}
                    },
                    chrdev: {
                        node: {getattr: S.node_ops.getattr, setattr: S.node_ops.setattr},
                        stream: E.chrdev_stream_ops
                    }
                });
                r = E.createNode(e, t, r, i);
                return E.isDir(r.mode) ? (r.node_ops = S.ops_table.dir.node, r.stream_ops = S.ops_table.dir.stream, r.contents = {}) : E.isFile(r.mode) ? (r.node_ops = S.ops_table.file.node, r.stream_ops = S.ops_table.file.stream, r.usedBytes = 0, r.contents = null) : E.isLink(r.mode) ? (r.node_ops = S.ops_table.link.node, r.stream_ops = S.ops_table.link.stream) : E.isChrdev(r.mode) && (r.node_ops = S.ops_table.chrdev.node, r.stream_ops = S.ops_table.chrdev.stream), r.timestamp = Date.now(), e && (e.contents[t] = r, e.timestamp = r.timestamp), r
            }, getFileDataAsTypedArray: function (e) {
                return e.contents ? e.contents.subarray ? e.contents.subarray(0, e.usedBytes) : new Uint8Array(e.contents) : new Uint8Array(0)
            }, expandFileStorage: function (e, t) {
                var r = e.contents ? e.contents.length : 0;
                t <= r || (t = Math.max(t, r * (r < 1048576 ? 2 : 1.125) >>> 0), 0 != r && (t = Math.max(t, 256)), r = e.contents, e.contents = new Uint8Array(t), 0 < e.usedBytes && e.contents.set(r.subarray(0, e.usedBytes), 0))
            }, resizeFileStorage: function (e, t) {
                var r;
                e.usedBytes != t && (0 == t ? (e.contents = null, e.usedBytes = 0) : (r = e.contents, e.contents = new Uint8Array(t), r && e.contents.set(r.subarray(0, Math.min(t, e.usedBytes))), e.usedBytes = t))
            }, node_ops: {
                getattr: function (e) {
                    var t = {};
                    return t.dev = E.isChrdev(e.mode) ? e.id : 1, t.ino = e.id, t.mode = e.mode, t.nlink = 1, t.uid = 0, t.gid = 0, t.rdev = e.rdev, E.isDir(e.mode) ? t.size = 4096 : E.isFile(e.mode) ? t.size = e.usedBytes : E.isLink(e.mode) ? t.size = e.link.length : t.size = 0, t.atime = new Date(e.timestamp), t.mtime = new Date(e.timestamp), t.ctime = new Date(e.timestamp), t.blksize = 4096, t.blocks = Math.ceil(t.size / t.blksize), t
                }, setattr: function (e, t) {
                    void 0 !== t.mode && (e.mode = t.mode), void 0 !== t.timestamp && (e.timestamp = t.timestamp), void 0 !== t.size && S.resizeFileStorage(e, t.size)
                }, lookup: function (e, t) {
                    throw E.genericErrors[44]
                }, mknod: function (e, t, r, i) {
                    return S.createNode(e, t, r, i)
                }, rename: function (e, t, r) {
                    if (E.isDir(e.mode)) {
                        var i;
                        try {
                            i = E.lookupNode(t, r)
                        } catch (e) {
                        }
                        if (i) for (var n in i.contents) throw new E.ErrnoError(55)
                    }
                    delete e.parent.contents[e.name], e.parent.timestamp = Date.now(), e.name = r, t.contents[r] = e, t.timestamp = e.parent.timestamp, e.parent = t
                }, unlink: function (e, t) {
                    delete e.contents[t], e.timestamp = Date.now()
                }, rmdir: function (e, t) {
                    for (var r in E.lookupNode(e, t).contents) throw new E.ErrnoError(55);
                    delete e.contents[t], e.timestamp = Date.now()
                }, readdir: function (e) {
                    var t, r = [".", ".."];
                    for (t in e.contents) e.contents.hasOwnProperty(t) && r.push(t);
                    return r
                }, symlink: function (e, t, r) {
                    e = S.createNode(e, t, 41471, 0);
                    return e.link = r, e
                }, readlink: function (e) {
                    if (E.isLink(e.mode)) return e.link;
                    throw new E.ErrnoError(28)
                }
            }, stream_ops: {
                read: function (e, t, r, i, n) {
                    var s = e.node.contents;
                    if (n >= e.node.usedBytes) return 0;
                    var a = Math.min(e.node.usedBytes - n, i);
                    if (8 < a && s.subarray) t.set(s.subarray(n, n + a), r); else for (var o = 0; o < a; o++) t[r + o] = s[n + o];
                    return a
                }, write: function (e, t, r, i, n, s) {
                    if (!i) return 0;
                    var a = e.node;
                    if (a.timestamp = Date.now(), t.subarray && (!a.contents || a.contents.subarray)) {
                        if (s) return a.contents = t.subarray(r, r + i), a.usedBytes = i;
                        if (0 === a.usedBytes && 0 === n) return a.contents = t.slice(r, r + i), a.usedBytes = i;
                        if (n + i <= a.usedBytes) return a.contents.set(t.subarray(r, r + i), n), i
                    }
                    if (S.expandFileStorage(a, n + i), a.contents.subarray && t.subarray) a.contents.set(t.subarray(r, r + i), n); else for (var o = 0; o < i; o++) a.contents[n + o] = t[r + o];
                    return a.usedBytes = Math.max(a.usedBytes, n + i), i
                }, llseek: function (e, t, r) {
                    if (1 === r ? t += e.position : 2 === r && E.isFile(e.node.mode) && (t += e.node.usedBytes), t < 0) throw new E.ErrnoError(28);
                    return t
                }, allocate: function (e, t, r) {
                    S.expandFileStorage(e.node, t + r), e.node.usedBytes = Math.max(e.node.usedBytes, t + r)
                }, mmap: function (e, t, r, i, n) {
                    if (!E.isFile(e.node.mode)) throw new E.ErrnoError(43);
                    var s, a, e = e.node.contents;
                    if (2 & n || e.buffer !== q) {
                        if ((0 < r || r + t < e.length) && (e = e.subarray ? e.subarray(r, r + t) : Array.prototype.slice.call(e, r, r + t)), a = !0, !(s = me(t))) throw new E.ErrnoError(48);
                        f.set(e, s)
                    } else a = !1, s = e.byteOffset;
                    return {ptr: s, allocated: a}
                }, msync: function (e, t, r, i, n) {
                    if (E.isFile(e.node.mode)) return 2 & n || S.stream_ops.write(e, t, 0, i, r, !1), 0;
                    throw new E.ErrnoError(43)
                }
            }
        }, E = {
            root: null,
            mounts: [],
            devices: {},
            streams: [],
            nextInode: 1,
            nameTable: null,
            currentPath: "/",
            initialized: !1,
            ignorePermissions: !0,
            ErrnoError: null,
            genericErrors: {},
            filesystems: null,
            syncFSRequests: 0,
            lookupPath: function (e) {
                var t = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {};
                if (!(e = w.resolve(E.cwd(), e))) return {path: "", node: null};
                if (8 < (t = Object.assign({
                    follow_mount: !0,
                    recurse_count: 0
                }, t)).recurse_count) throw new E.ErrnoError(32);
                for (var r = v.normalizeArray(e.split("/").filter(e => !!e), !1), i = E.root, n = "/", s = 0; s < r.length; s++) {
                    var a = s === r.length - 1;
                    if (a && t.parent) break;
                    if (i = E.lookupNode(i, r[s]), n = v.join2(n, r[s]), !E.isMountpoint(i) || a && !t.follow_mount || (i = i.mounted.root), !a || t.follow) for (var o = 0; E.isLink(i.mode);) {
                        var l = E.readlink(n), n = w.resolve(v.dirname(n), l),
                            i = E.lookupPath(n, {recurse_count: t.recurse_count + 1}).node;
                        if (40 < o++) throw new E.ErrnoError(32)
                    }
                }
                return {path: n, node: i}
            },
            getPath: e => {
                for (var t, r; ;) {
                    if (E.isRoot(e)) return r = e.mount.mountpoint, t ? "/" !== r[r.length - 1] ? r + "/" + t : r + t : r;
                    t = t ? e.name + "/" + t : e.name, e = e.parent
                }
            },
            hashName: (e, t) => {
                for (var r = 0, i = 0; i < t.length; i++) r = (r << 5) - r + t.charCodeAt(i) | 0;
                return (e + r >>> 0) % E.nameTable.length
            },
            hashAddNode: e => {
                var t = E.hashName(e.parent.id, e.name);
                e.name_next = E.nameTable[t], E.nameTable[t] = e
            },
            hashRemoveNode: e => {
                var t = E.hashName(e.parent.id, e.name);
                if (E.nameTable[t] === e) E.nameTable[t] = e.name_next; else for (var r = E.nameTable[t]; r;) {
                    if (r.name_next === e) {
                        r.name_next = e.name_next;
                        break
                    }
                    r = r.name_next
                }
            },
            lookupNode: (e, t) => {
                var r = E.mayLookup(e);
                if (r) throw new E.ErrnoError(r, e);
                for (var r = E.hashName(e.id, t), i = E.nameTable[r]; i; i = i.name_next) {
                    var n = i.name;
                    if (i.parent.id === e.id && n === t) return i
                }
                return E.lookup(e, t)
            },
            createNode: (e, t, r, i) => {
                e = new E.FSNode(e, t, r, i);
                return E.hashAddNode(e), e
            },
            destroyNode: e => {
                E.hashRemoveNode(e)
            },
            isRoot: e => e === e.parent,
            isMountpoint: e => !!e.mounted,
            isFile: e => 32768 == (61440 & e),
            isDir: e => 16384 == (61440 & e),
            isLink: e => 40960 == (61440 & e),
            isChrdev: e => 8192 == (61440 & e),
            isBlkdev: e => 24576 == (61440 & e),
            isFIFO: e => 4096 == (61440 & e),
            isSocket: e => 49152 == (49152 & e),
            flagModes: {r: 0, "r+": 2, w: 577, "w+": 578, a: 1089, "a+": 1090},
            modeStringToFlags: e => {
                var t = E.flagModes[e];
                if (void 0 === t) throw new Error("Unknown file open mode: " + e);
                return t
            },
            flagsToPermissionString: e => {
                var t = ["r", "w", "rw"][3 & e];
                return 512 & e && (t += "w"), t
            },
            nodePermissions: (e, t) => E.ignorePermissions || (!t.includes("r") || 292 & e.mode) && (!t.includes("w") || 146 & e.mode) && (!t.includes("x") || 73 & e.mode) ? 0 : 2,
            mayLookup: e => {
                return E.nodePermissions(e, "x") || (e.node_ops.lookup ? 0 : 2)
            },
            mayCreate: (e, t) => {
                try {
                    return E.lookupNode(e, t), 20
                } catch (e) {
                }
                return E.nodePermissions(e, "wx")
            },
            mayDelete: (e, t, r) => {
                var i;
                try {
                    i = E.lookupNode(e, t)
                } catch (e) {
                    return e.errno
                }
                t = E.nodePermissions(e, "wx");
                if (t) return t;
                if (r) {
                    if (!E.isDir(i.mode)) return 54;
                    if (E.isRoot(i) || E.getPath(i) === E.cwd()) return 10
                } else if (E.isDir(i.mode)) return 31;
                return 0
            },
            mayOpen: (e, t) => e ? E.isLink(e.mode) ? 32 : E.isDir(e.mode) && ("r" !== E.flagsToPermissionString(t) || 512 & t) ? 31 : E.nodePermissions(e, E.flagsToPermissionString(t)) : 44,
            MAX_OPEN_FDS: 4096,
            nextfd: function () {
                for (var e = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : 0, t = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : E.MAX_OPEN_FDS, r = e; r <= t; r++) if (!E.streams[r]) return r;
                throw new E.ErrnoError(33)
            },
            getStream: e => E.streams[e],
            createStream: (e, t, r) => {
                E.FSStream || (E.FSStream = function () {
                    this.shared = {}
                }, E.FSStream.prototype = {}, Object.defineProperties(E.FSStream.prototype, {
                    object: {
                        get: function () {
                            return this.node
                        }, set: function (e) {
                            this.node = e
                        }
                    }, isRead: {
                        get: function () {
                            return 1 != (2097155 & this.flags)
                        }
                    }, isWrite: {
                        get: function () {
                            return 0 != (2097155 & this.flags)
                        }
                    }, isAppend: {
                        get: function () {
                            return 1024 & this.flags
                        }
                    }, flags: {
                        get: function () {
                            return this.shared.flags
                        }, set: function (e) {
                            this.shared.flags = e
                        }
                    }, position: {
                        get: function () {
                            return this.shared.position
                        }, set: function (e) {
                            this.shared.position = e
                        }
                    }
                })), e = Object.assign(new E.FSStream, e);
                t = E.nextfd(t, r);
                return e.fd = t, E.streams[t] = e
            },
            closeStream: e => {
                E.streams[e] = null
            },
            chrdev_stream_ops: {
                open: e => {
                    var t = E.getDevice(e.node.rdev);
                    e.stream_ops = t.stream_ops, e.stream_ops.open && e.stream_ops.open(e)
                }, llseek: () => {
                    throw new E.ErrnoError(70)
                }
            },
            major: e => e >> 8,
            minor: e => 255 & e,
            makedev: (e, t) => e << 8 | t,
            registerDevice: (e, t) => {
                E.devices[e] = {stream_ops: t}
            },
            getDevice: e => E.devices[e],
            getMounts: e => {
                for (var t = [], r = [e]; r.length;) {
                    var i = r.pop();
                    t.push(i), r.push.apply(r, i.mounts)
                }
                return t
            },
            syncfs: (t, r) => {
                "function" == typeof t && (r = t, t = !1), E.syncFSRequests++, 1 < E.syncFSRequests && o("warning: " + E.syncFSRequests + " FS.syncfs operations in flight at once, probably just doing extra work");
                var i = E.getMounts(E.root.mount), n = 0;

                function s(e) {
                    return E.syncFSRequests--, r(e)
                }

                function a(e) {
                    if (e) return a.errored ? void 0 : (a.errored = !0, s(e));
                    ++n >= i.length && s(null)
                }

                i.forEach(e => {
                    if (!e.type.syncfs) return a(null);
                    e.type.syncfs(e, t, a)
                })
            },
            mount: (e, t, r) => {
                var i, n = "/" === r, s = !r;
                if (n && E.root) throw new E.ErrnoError(10);
                if (!n && !s) {
                    s = E.lookupPath(r, {follow_mount: !1});
                    if (r = s.path, i = s.node, E.isMountpoint(i)) throw new E.ErrnoError(10);
                    if (!E.isDir(i.mode)) throw new E.ErrnoError(54)
                }
                s = {type: e, opts: t, mountpoint: r, mounts: []}, t = e.mount(s);
                return (t.mount = s).root = t, n ? E.root = t : i && (i.mounted = s, i.mount && i.mount.mounts.push(s)), t
            },
            unmount: e => {
                e = E.lookupPath(e, {follow_mount: !1});
                if (!E.isMountpoint(e.node)) throw new E.ErrnoError(28);
                var e = e.node, t = e.mounted, i = E.getMounts(t), t = (Object.keys(E.nameTable).forEach(e => {
                    for (var t = E.nameTable[e]; t;) {
                        var r = t.name_next;
                        i.includes(t.mount) && E.destroyNode(t), t = r
                    }
                }), e.mounted = null, e.mount.mounts.indexOf(t));
                e.mount.mounts.splice(t, 1)
            },
            lookup: (e, t) => e.node_ops.lookup(e, t),
            mknod: (e, t, r) => {
                var i = E.lookupPath(e, {parent: !0}).node, e = v.basename(e);
                if (!e || "." === e || ".." === e) throw new E.ErrnoError(28);
                var n = E.mayCreate(i, e);
                if (n) throw new E.ErrnoError(n);
                if (i.node_ops.mknod) return i.node_ops.mknod(i, e, t, r);
                throw new E.ErrnoError(63)
            },
            create: (e, t) => E.mknod(e, t = (t = void 0 !== t ? t : 438) & 4095 | 32768, 0),
            mkdir: (e, t) => E.mknod(e, t = (t = void 0 !== t ? t : 511) & 1023 | 16384, 0),
            mkdirTree: (e, t) => {
                for (var r = e.split("/"), i = "", n = 0; n < r.length; ++n) if (r[n]) {
                    i += "/" + r[n];
                    try {
                        E.mkdir(i, t)
                    } catch (e) {
                        if (20 != e.errno) throw e
                    }
                }
            },
            mkdev: (e, t, r) => (void 0 === r && (r = t, t = 438), E.mknod(e, t |= 8192, r)),
            symlink: (e, t) => {
                if (!w.resolve(e)) throw new E.ErrnoError(44);
                var r = E.lookupPath(t, {parent: !0}).node;
                if (!r) throw new E.ErrnoError(44);
                var t = v.basename(t), i = E.mayCreate(r, t);
                if (i) throw new E.ErrnoError(i);
                if (r.node_ops.symlink) return r.node_ops.symlink(r, t, e);
                throw new E.ErrnoError(63)
            },
            rename: (e, t) => {
                var r = v.dirname(e), i = v.dirname(t), n = v.basename(e), s = v.basename(t),
                    a = E.lookupPath(e, {parent: !0}).node, o = E.lookupPath(t, {parent: !0}).node;
                if (!a || !o) throw new E.ErrnoError(44);
                if (a.mount !== o.mount) throw new E.ErrnoError(75);
                var l, d = E.lookupNode(a, n);
                if ("." !== w.relative(e, i).charAt(0)) throw new E.ErrnoError(28);
                if ("." !== w.relative(t, r).charAt(0)) throw new E.ErrnoError(55);
                try {
                    l = E.lookupNode(o, s)
                } catch (e) {
                }
                if (d !== l) {
                    i = E.isDir(d.mode), t = E.mayDelete(a, n, i);
                    if (t) throw new E.ErrnoError(t);
                    if (t = l ? E.mayDelete(o, s, i) : E.mayCreate(o, s)) throw new E.ErrnoError(t);
                    if (!a.node_ops.rename) throw new E.ErrnoError(63);
                    if (E.isMountpoint(d) || l && E.isMountpoint(l)) throw new E.ErrnoError(10);
                    if (o !== a && (t = E.nodePermissions(a, "w"))) throw new E.ErrnoError(t);
                    E.hashRemoveNode(d);
                    try {
                        a.node_ops.rename(d, o, s)
                    } catch (e) {
                        throw e
                    } finally {
                        E.hashAddNode(d)
                    }
                }
            },
            rmdir: e => {
                var t = E.lookupPath(e, {parent: !0}).node, e = v.basename(e), r = E.lookupNode(t, e),
                    i = E.mayDelete(t, e, !0);
                if (i) throw new E.ErrnoError(i);
                if (!t.node_ops.rmdir) throw new E.ErrnoError(63);
                if (E.isMountpoint(r)) throw new E.ErrnoError(10);
                t.node_ops.rmdir(t, e), E.destroyNode(r)
            },
            readdir: e => {
                e = E.lookupPath(e, {follow: !0}).node;
                if (e.node_ops.readdir) return e.node_ops.readdir(e);
                throw new E.ErrnoError(54)
            },
            unlink: e => {
                var t = E.lookupPath(e, {parent: !0}).node;
                if (!t) throw new E.ErrnoError(44);
                var e = v.basename(e), r = E.lookupNode(t, e), i = E.mayDelete(t, e, !1);
                if (i) throw new E.ErrnoError(i);
                if (!t.node_ops.unlink) throw new E.ErrnoError(63);
                if (E.isMountpoint(r)) throw new E.ErrnoError(10);
                t.node_ops.unlink(t, e), E.destroyNode(r)
            },
            readlink: e => {
                e = E.lookupPath(e).node;
                if (!e) throw new E.ErrnoError(44);
                if (e.node_ops.readlink) return w.resolve(E.getPath(e.parent), e.node_ops.readlink(e));
                throw new E.ErrnoError(28)
            },
            stat: (e, t) => {
                e = E.lookupPath(e, {follow: !t}).node;
                if (!e) throw new E.ErrnoError(44);
                if (e.node_ops.getattr) return e.node_ops.getattr(e);
                throw new E.ErrnoError(63)
            },
            lstat: e => E.stat(e, !0),
            chmod: (e, t, r) => {
                r = "string" == typeof e ? E.lookupPath(e, {follow: !r}).node : e;
                if (!r.node_ops.setattr) throw new E.ErrnoError(63);
                r.node_ops.setattr(r, {mode: 4095 & t | -4096 & r.mode, timestamp: Date.now()})
            },
            lchmod: (e, t) => {
                E.chmod(e, t, !0)
            },
            fchmod: (e, t) => {
                e = E.getStream(e);
                if (!e) throw new E.ErrnoError(8);
                E.chmod(e.node, t)
            },
            chown: (e, t, r, i) => {
                i = "string" == typeof e ? E.lookupPath(e, {follow: !i}).node : e;
                if (!i.node_ops.setattr) throw new E.ErrnoError(63);
                i.node_ops.setattr(i, {timestamp: Date.now()})
            },
            lchown: (e, t, r) => {
                E.chown(e, t, r, !0)
            },
            fchown: (e, t, r) => {
                e = E.getStream(e);
                if (!e) throw new E.ErrnoError(8);
                E.chown(e.node, t, r)
            },
            truncate: (e, t) => {
                if (t < 0) throw new E.ErrnoError(28);
                e = "string" == typeof e ? E.lookupPath(e, {follow: !0}).node : e;
                if (!e.node_ops.setattr) throw new E.ErrnoError(63);
                if (E.isDir(e.mode)) throw new E.ErrnoError(31);
                if (!E.isFile(e.mode)) throw new E.ErrnoError(28);
                var r = E.nodePermissions(e, "w");
                if (r) throw new E.ErrnoError(r);
                e.node_ops.setattr(e, {size: t, timestamp: Date.now()})
            },
            ftruncate: (e, t) => {
                e = E.getStream(e);
                if (!e) throw new E.ErrnoError(8);
                if (0 == (2097155 & e.flags)) throw new E.ErrnoError(28);
                E.truncate(e.node, t)
            },
            utime: (e, t, r) => {
                e = E.lookupPath(e, {follow: !0}).node;
                e.node_ops.setattr(e, {timestamp: Math.max(t, r)})
            },
            open: (e, t, r) => {
                if ("" === e) throw new E.ErrnoError(44);
                var i;
                if (r = void 0 === r ? 438 : r, r = 64 & (t = "string" == typeof t ? E.modeStringToFlags(t) : t) ? 4095 & r | 32768 : 0, "object" == typeof e) i = e; else {
                    e = v.normalize(e);
                    try {
                        i = E.lookupPath(e, {follow: !(131072 & t)}).node
                    } catch (e) {
                    }
                }
                var n = !1;
                if (64 & t) if (i) {
                    if (128 & t) throw new E.ErrnoError(20)
                } else i = E.mknod(e, r, 0), n = !0;
                if (!i) throw new E.ErrnoError(44);
                if (E.isChrdev(i.mode) && (t &= -513), 65536 & t && !E.isDir(i.mode)) throw new E.ErrnoError(54);
                if (!n) {
                    r = E.mayOpen(i, t);
                    if (r) throw new E.ErrnoError(r)
                }
                512 & t && !n && E.truncate(i, 0), t &= -131713;
                r = E.createStream({
                    node: i,
                    path: E.getPath(i),
                    flags: t,
                    seekable: !0,
                    position: 0,
                    stream_ops: i.stream_ops,
                    ungotten: [],
                    error: !1
                });
                return r.stream_ops.open && r.stream_ops.open(r), !_.logReadFiles || 1 & t || (E.readFiles || (E.readFiles = {}), e in E.readFiles || (E.readFiles[e] = 1)), r
            },
            close: e => {
                if (E.isClosed(e)) throw new E.ErrnoError(8);
                e.getdents && (e.getdents = null);
                try {
                    e.stream_ops.close && e.stream_ops.close(e)
                } catch (e) {
                    throw e
                } finally {
                    E.closeStream(e.fd)
                }
                e.fd = null
            },
            isClosed: e => null === e.fd,
            llseek: (e, t, r) => {
                if (E.isClosed(e)) throw new E.ErrnoError(8);
                if (!e.seekable || !e.stream_ops.llseek) throw new E.ErrnoError(70);
                if (0 != r && 1 != r && 2 != r) throw new E.ErrnoError(28);
                return e.position = e.stream_ops.llseek(e, t, r), e.ungotten = [], e.position
            },
            read: (e, t, r, i, n) => {
                if (i < 0 || n < 0) throw new E.ErrnoError(28);
                if (E.isClosed(e)) throw new E.ErrnoError(8);
                if (1 == (2097155 & e.flags)) throw new E.ErrnoError(8);
                if (E.isDir(e.node.mode)) throw new E.ErrnoError(31);
                if (!e.stream_ops.read) throw new E.ErrnoError(28);
                var s = void 0 !== n;
                if (s) {
                    if (!e.seekable) throw new E.ErrnoError(70)
                } else n = e.position;
                t = e.stream_ops.read(e, t, r, i, n);
                return s || (e.position += t), t
            },
            write: (e, t, r, i, n, s) => {
                if (i < 0 || n < 0) throw new E.ErrnoError(28);
                if (E.isClosed(e)) throw new E.ErrnoError(8);
                if (0 == (2097155 & e.flags)) throw new E.ErrnoError(8);
                if (E.isDir(e.node.mode)) throw new E.ErrnoError(31);
                if (!e.stream_ops.write) throw new E.ErrnoError(28);
                e.seekable && 1024 & e.flags && E.llseek(e, 0, 2);
                var a = void 0 !== n;
                if (a) {
                    if (!e.seekable) throw new E.ErrnoError(70)
                } else n = e.position;
                t = e.stream_ops.write(e, t, r, i, n, s);
                return a || (e.position += t), t
            },
            allocate: (e, t, r) => {
                if (E.isClosed(e)) throw new E.ErrnoError(8);
                if (t < 0 || r <= 0) throw new E.ErrnoError(28);
                if (0 == (2097155 & e.flags)) throw new E.ErrnoError(8);
                if (!E.isFile(e.node.mode) && !E.isDir(e.node.mode)) throw new E.ErrnoError(43);
                if (!e.stream_ops.allocate) throw new E.ErrnoError(138);
                e.stream_ops.allocate(e, t, r)
            },
            mmap: (e, t, r, i, n) => {
                if (0 != (2 & i) && 0 == (2 & n) && 2 != (2097155 & e.flags)) throw new E.ErrnoError(2);
                if (1 == (2097155 & e.flags)) throw new E.ErrnoError(2);
                if (e.stream_ops.mmap) return e.stream_ops.mmap(e, t, r, i, n);
                throw new E.ErrnoError(43)
            },
            msync: (e, t, r, i, n) => e && e.stream_ops.msync ? e.stream_ops.msync(e, t, r, i, n) : 0,
            munmap: e => 0,
            ioctl: (e, t, r) => {
                if (e.stream_ops.ioctl) return e.stream_ops.ioctl(e, t, r);
                throw new E.ErrnoError(59)
            },
            readFile: function (e) {
                let t = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {};
                if (t.flags = t.flags || 0, t.encoding = t.encoding || "binary", "utf8" !== t.encoding && "binary" !== t.encoding) throw new Error('Invalid encoding type "' + t.encoding + '"');
                var r, i = E.open(e, t.flags), e = E.stat(e).size, n = new Uint8Array(e);
                return E.read(i, n, 0, e, 0), "utf8" === t.encoding ? r = a(n, 0) : "binary" === t.encoding && (r = n), E.close(i), r
            },
            writeFile: function (e, t) {
                let r = 2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : {};
                r.flags = r.flags || 577;
                e = E.open(e, r.flags, r.mode);
                if ("string" == typeof t) {
                    var i = new Uint8Array(re(t) + 1), n = te(t, i, 0, i.length);
                    E.write(e, i, 0, n, void 0, r.canOwn)
                } else {
                    if (!ArrayBuffer.isView(t)) throw new Error("Unsupported data type");
                    E.write(e, t, 0, t.byteLength, void 0, r.canOwn)
                }
                E.close(e)
            },
            cwd: () => E.currentPath,
            chdir: e => {
                e = E.lookupPath(e, {follow: !0});
                if (null === e.node) throw new E.ErrnoError(44);
                if (!E.isDir(e.node.mode)) throw new E.ErrnoError(54);
                var t = E.nodePermissions(e.node, "x");
                if (t) throw new E.ErrnoError(t);
                E.currentPath = e.path
            },
            createDefaultDirectories: () => {
                E.mkdir("/tmp"), E.mkdir("/home"), E.mkdir("/home/web_user")
            },
            createDefaultDevices: () => {
                E.mkdir("/dev"), E.registerDevice(E.makedev(1, 3), {
                    read: () => 0,
                    write: (e, t, r, i, n) => i
                }), E.mkdev("/dev/null", E.makedev(1, 3)), i.register(E.makedev(5, 0), i.default_tty_ops), i.register(E.makedev(6, 0), i.default_tty1_ops), E.mkdev("/dev/tty", E.makedev(5, 0)), E.mkdev("/dev/tty1", E.makedev(6, 0));
                var e = function () {
                    var e;
                    if ("object" == typeof crypto && "function" == typeof crypto.getRandomValues) return e = new Uint8Array(1), () => (crypto.getRandomValues(e), e[0]);
                    if ($) try {
                        var t = Tt.default;
                        return () => t.randomBytes(1)[0]
                    } catch (e) {
                    }
                    return () => b("randomDevice")
                }();
                E.createDevice("/dev", "random", e), E.createDevice("/dev", "urandom", e), E.mkdir("/dev/shm"), E.mkdir("/dev/shm/tmp")
            },
            createSpecialDirectories: () => {
                E.mkdir("/proc");
                var t = E.mkdir("/proc/self");
                E.mkdir("/proc/self/fd"), E.mount({
                    mount: () => {
                        var e = E.createNode(t, "fd", 16895, 73);
                        return e.node_ops = {
                            lookup: (e, t) => {
                                var r = E.getStream(+t);
                                if (!r) throw new E.ErrnoError(8);
                                t = {parent: null, mount: {mountpoint: "fake"}, node_ops: {readlink: () => r.path}};
                                return t.parent = t
                            }
                        }, e
                    }
                }, {}, "/proc/self/fd")
            },
            createStandardStreams: () => {
                _.stdin ? E.createDevice("/dev", "stdin", _.stdin) : E.symlink("/dev/tty", "/dev/stdin"), _.stdout ? E.createDevice("/dev", "stdout", null, _.stdout) : E.symlink("/dev/tty", "/dev/stdout"), _.stderr ? E.createDevice("/dev", "stderr", null, _.stderr) : E.symlink("/dev/tty1", "/dev/stderr"), E.open("/dev/stdin", 0), E.open("/dev/stdout", 1), E.open("/dev/stderr", 1)
            },
            ensureErrnoError: () => {
                E.ErrnoError || (E.ErrnoError = function (e, t) {
                    this.node = t, this.setErrno = function (e) {
                        this.errno = e
                    }, this.setErrno(e), this.message = "FS error"
                }, E.ErrnoError.prototype = new Error, E.ErrnoError.prototype.constructor = E.ErrnoError, [44].forEach(e => {
                    E.genericErrors[e] = new E.ErrnoError(e), E.genericErrors[e].stack = "<generic error, no stack>"
                }))
            },
            staticInit: () => {
                E.ensureErrnoError(), E.nameTable = new Array(4096), E.mount(S, {}, "/"), E.createDefaultDirectories(), E.createDefaultDevices(), E.createSpecialDirectories(), E.filesystems = {MEMFS: S}
            },
            init: (e, t, r) => {
                E.init.initialized = !0, E.ensureErrnoError(), _.stdin = e || _.stdin, _.stdout = t || _.stdout, _.stderr = r || _.stderr, E.createStandardStreams()
            },
            quit: () => {
                E.init.initialized = !1;
                for (var e = 0; e < E.streams.length; e++) {
                    var t = E.streams[e];
                    t && E.close(t)
                }
            },
            getMode: (e, t) => {
                var r = 0;
                return e && (r |= 365), t && (r |= 146), r
            },
            findObject: (e, t) => {
                e = E.analyzePath(e, t);
                return e.exists ? e.object : null
            },
            analyzePath: (e, t) => {
                try {
                    e = (i = E.lookupPath(e, {follow: !t})).path
                } catch (e) {
                }
                var r = {
                    isRoot: !1,
                    exists: !1,
                    error: 0,
                    name: null,
                    path: null,
                    object: null,
                    parentExists: !1,
                    parentPath: null,
                    parentObject: null
                };
                try {
                    var i = E.lookupPath(e, {parent: !0});
                    r.parentExists = !0, r.parentPath = i.path, r.parentObject = i.node, r.name = v.basename(e), i = E.lookupPath(e, {follow: !t}), r.exists = !0, r.path = i.path, r.object = i.node, r.name = i.node.name, r.isRoot = "/" === i.path
                } catch (e) {
                    r.error = e.errno
                }
                return r
            },
            createPath: (e, t, r, i) => {
                e = "string" == typeof e ? e : E.getPath(e);
                for (var n = t.split("/").reverse(); n.length;) {
                    var s = n.pop();
                    if (s) {
                        var a = v.join2(e, s);
                        try {
                            E.mkdir(a)
                        } catch (e) {
                        }
                        e = a
                    }
                }
                return a
            },
            createFile: (e, t, r, i, n) => {
                e = v.join2("string" == typeof e ? e : E.getPath(e), t), t = E.getMode(i, n);
                return E.create(e, t)
            },
            createDataFile: (e, t, r, i, n, s) => {
                var a = t,
                    t = (e && (e = "string" == typeof e ? e : E.getPath(e), a = t ? v.join2(e, t) : e), E.getMode(i, n)),
                    e = E.create(a, t);
                if (r) {
                    if ("string" == typeof r) {
                        for (var o = new Array(r.length), l = 0, d = r.length; l < d; ++l) o[l] = r.charCodeAt(l);
                        r = o
                    }
                    E.chmod(e, 146 | t);
                    i = E.open(e, 577);
                    E.write(i, r, 0, r.length, 0, s), E.close(i), E.chmod(e, t)
                }
                return e
            },
            createDevice: (e, t, l, a) => {
                var e = v.join2("string" == typeof e ? e : E.getPath(e), t), t = E.getMode(!!l, !!a),
                    r = (E.createDevice.major || (E.createDevice.major = 64), E.makedev(E.createDevice.major++, 0));
                return E.registerDevice(r, {
                    open: e => {
                        e.seekable = !1
                    }, close: e => {
                        a && a.buffer && a.buffer.length && a(10)
                    }, read: (e, t, r, i, n) => {
                        for (var s, a = 0, o = 0; o < i; o++) {
                            try {
                                s = l()
                            } catch (e) {
                                throw new E.ErrnoError(29)
                            }
                            if (void 0 === s && 0 === a) throw new E.ErrnoError(6);
                            if (null == s) break;
                            a++, t[r + o] = s
                        }
                        return a && (e.node.timestamp = Date.now()), a
                    }, write: (e, t, r, i, n) => {
                        for (var s = 0; s < i; s++) try {
                            a(t[r + s])
                        } catch (e) {
                            throw new E.ErrnoError(29)
                        }
                        return i && (e.node.timestamp = Date.now()), s
                    }
                }), E.mkdev(e, t, r)
            },
            forceLoadFile: e => {
                if (e.isDevice || e.isFolder || e.link || e.contents) return !0;
                if ("undefined" != typeof XMLHttpRequest) throw new Error("Lazy loading should have been performed (contents set) in createLazyFile, but it was not. Lazy loading only works in web workers. Use --embed-file or --preload-file in emcc on the main thread.");
                if (!t) throw new Error("Cannot load without read() or XMLHttpRequest.");
                try {
                    e.contents = ce(t(e.url), !0), e.usedBytes = e.contents.length
                } catch (e) {
                    throw new E.ErrnoError(29)
                }
            },
            createLazyFile: (e, t, a, r, i) => {
                function n() {
                    this.lengthKnown = !1, this.chunks = []
                }

                if (n.prototype.get = function (e) {
                    var t;
                    if (!(e > this.length - 1 || e < 0)) return t = e % this.chunkSize, e = e / this.chunkSize | 0, this.getter(e)[t]
                }, n.prototype.setDataGetter = function (e) {
                    this.getter = e
                }, n.prototype.cacheLength = function () {
                    var e = new XMLHttpRequest;
                    if (e.open("HEAD", a, !1), e.send(null), !(200 <= e.status && e.status < 300 || 304 === e.status)) throw new Error("Couldn't load " + a + ". Status: " + e.status);
                    var t, i = Number(e.getResponseHeader("Content-length")),
                        r = (t = e.getResponseHeader("Accept-Ranges")) && "bytes" === t,
                        e = (t = e.getResponseHeader("Content-Encoding")) && "gzip" === t, n = 1048576,
                        s = (r || (n = i), this);
                    s.setDataGetter(e => {
                        var t = e * n, r = (e + 1) * n - 1, r = Math.min(r, i - 1);
                        if (void 0 === s.chunks[e] && (s.chunks[e] = ((e, t) => {
                            if (t < e) throw new Error("invalid range (" + e + ", " + t + ") or no bytes requested!");
                            if (i - 1 < t) throw new Error("only " + i + " bytes available! programmer error!");
                            var r = new XMLHttpRequest;
                            if (r.open("GET", a, !1), i !== n && r.setRequestHeader("Range", "bytes=" + e + "-" + t), r.responseType = "arraybuffer", r.overrideMimeType && r.overrideMimeType("text/plain; charset=x-user-defined"), r.send(null), 200 <= r.status && r.status < 300 || 304 === r.status) return void 0 !== r.response ? new Uint8Array(r.response || []) : ce(r.responseText || "", !0);
                            throw new Error("Couldn't load " + a + ". Status: " + r.status)
                        })(t, r)), void 0 === s.chunks[e]) throw new Error("doXHR failed!");
                        return s.chunks[e]
                    }), !e && i || (n = i = 1, i = this.getter(0).length, n = i, j("LazyFiles on gzip forces download of the whole file when length is accessed")), this._length = i, this._chunkSize = n, this.lengthKnown = !0
                }, "undefined" != typeof XMLHttpRequest) {
                    if (!h) throw"Cannot do synchronous binary XHRs outside webworkers in modern browsers. Use --embed-file or --preload-file in emcc";
                    var s = new n, s = (Object.defineProperties(s, {
                        length: {
                            get: function () {
                                return this.lengthKnown || this.cacheLength(), this._length
                            }
                        }, chunkSize: {
                            get: function () {
                                return this.lengthKnown || this.cacheLength(), this._chunkSize
                            }
                        }
                    }), {isDevice: !1, contents: s})
                } else s = {isDevice: !1, url: a};
                var o = E.createFile(e, t, s, r, i),
                    l = (s.contents ? o.contents = s.contents : s.url && (o.contents = null, o.url = s.url), Object.defineProperties(o, {
                        usedBytes: {
                            get: function () {
                                return this.contents.length
                            }
                        }
                    }), {});

                function d(e, t, r, i, n) {
                    var s = e.node.contents;
                    if (n >= s.length) return 0;
                    var a = Math.min(s.length - n, i);
                    if (s.slice) for (var o = 0; o < a; o++) t[r + o] = s[n + o]; else for (o = 0; o < a; o++) t[r + o] = s.get(n + o);
                    return a
                }

                return Object.keys(o.stream_ops).forEach(e => {
                    var t = o.stream_ops[e];
                    l[e] = function () {
                        return E.forceLoadFile(o), t.apply(null, arguments)
                    }
                }), l.read = (e, t, r, i, n) => (E.forceLoadFile(o), d(e, t, r, i, n)), l.mmap = (e, t, r, i, n) => {
                    E.forceLoadFile(o);
                    var s = me(t);
                    if (s) return d(e, f, s, t, r), {ptr: s, allocated: !0};
                    throw new E.ErrnoError(48)
                }, o.stream_ops = l, o
            },
            createPreloadedFile: (r, i, e, n, s, a, o, l, d, h) => {
                var t, f, u, p = i ? w.resolve(v.join2(r, i)) : r;

                function c(e) {
                    function t(e) {
                        h && h(), l || E.createDataFile(r, i, e, n, s, d), a && a(), le()
                    }

                    Browser.handledByPreloadPlugin(e, p, t, () => {
                        o && o(), le()
                    }) || t(e)
                }

                oe(), "string" == typeof e ? (f = o, u = "al " + (t = e), m(t, e => {
                    Y(e, 'Loading data file "' + t + '" failed (no arrayBuffer).'), c(new Uint8Array(e)), u && le()
                }, e => {
                    if (!f) throw'Loading data file "' + t + '" failed.';
                    f()
                }), u && oe()) : c(e)
            },
            indexedDB: () => window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || window.msIndexedDB,
            DB_NAME: () => "EM_FS_" + window.location.pathname,
            DB_VERSION: 20,
            DB_STORE_NAME: "FILE_DATA",
            saveFilesToDB: (a, o, l) => {
                o = o || (() => {
                }), l = l || (() => {
                });
                var e = E.indexedDB();
                try {
                    var d = e.open(E.DB_NAME(), E.DB_VERSION)
                } catch (a) {
                    return l(a)
                }
                d.onupgradeneeded = () => {
                    j("creating db"), d.result.createObjectStore(E.DB_STORE_NAME)
                }, d.onsuccess = () => {
                    var e = d.result.transaction([E.DB_STORE_NAME], "readwrite"), t = e.objectStore(E.DB_STORE_NAME),
                        r = 0, i = 0, n = a.length;

                    function s() {
                        (0 == i ? o : l)()
                    }

                    a.forEach(e => {
                        e = t.put(E.analyzePath(e).object.contents, e);
                        e.onsuccess = () => {
                            ++r + i == n && s()
                        }, e.onerror = () => {
                            r + ++i == n && s()
                        }
                    }), e.onerror = l
                }, d.onerror = l
            },
            loadFilesFromDB: (o, l, d) => {
                l = l || (() => {
                }), d = d || (() => {
                });
                var e = E.indexedDB();
                try {
                    var h = e.open(E.DB_NAME(), E.DB_VERSION)
                } catch (o) {
                    return d(o)
                }
                h.onupgradeneeded = d, h.onsuccess = () => {
                    var e = h.result;
                    try {
                        var t = e.transaction([E.DB_STORE_NAME], "readonly")
                    } catch (e) {
                        return void d(e)
                    }
                    var r = t.objectStore(E.DB_STORE_NAME), i = 0, n = 0, s = o.length;

                    function a() {
                        (0 == n ? l : d)()
                    }

                    o.forEach(e => {
                        var t = r.get(e);
                        t.onsuccess = () => {
                            E.analyzePath(e).exists && E.unlink(e), E.createDataFile(v.dirname(e), v.basename(e), t.result, !0, !0, !0), ++i + n == s && a()
                        }, t.onerror = () => {
                            i + ++n == s && a()
                        }
                    }), t.onerror = d
                }, h.onerror = d
            }
        }, U = {
            DEFAULT_POLLMASK: 5, calculateAt: function (e, t, r) {
                if (v.isAbs(t)) return t;
                var i;
                if (-100 === e) i = E.cwd(); else {
                    e = E.getStream(e);
                    if (!e) throw new E.ErrnoError(8);
                    i = e.path
                }
                if (0 != t.length) return v.join2(i, t);
                if (r) return i;
                throw new E.ErrnoError(44)
            }, doStat: function (e, t, r) {
                try {
                    var i = e(t)
                } catch (e) {
                    if (e && e.node && v.normalize(t) !== v.normalize(E.getPath(e.node))) return -54;
                    throw e
                }
                return d[r >> 2] = i.dev, d[r + 4 >> 2] = 0, d[r + 8 >> 2] = i.ino, d[r + 12 >> 2] = i.mode, d[r + 16 >> 2] = i.nlink, d[r + 20 >> 2] = i.uid, d[r + 24 >> 2] = i.gid, d[r + 28 >> 2] = i.rdev, d[r + 32 >> 2] = 0, y = [i.size >>> 0, (g = i.size, 1 <= +Math.abs(g) ? 0 < g ? (0 | Math.min(+Math.floor(g / 4294967296), 4294967295)) >>> 0 : ~~+Math.ceil((g - (~~g >>> 0)) / 4294967296) >>> 0 : 0)], d[r + 40 >> 2] = y[0], d[r + 44 >> 2] = y[1], d[r + 48 >> 2] = 4096, d[r + 52 >> 2] = i.blocks, y = [Math.floor(i.atime.getTime() / 1e3) >>> 0, (g = Math.floor(i.atime.getTime() / 1e3), 1 <= +Math.abs(g) ? 0 < g ? (0 | Math.min(+Math.floor(g / 4294967296), 4294967295)) >>> 0 : ~~+Math.ceil((g - (~~g >>> 0)) / 4294967296) >>> 0 : 0)], d[r + 56 >> 2] = y[0], d[r + 60 >> 2] = y[1], d[r + 64 >> 2] = 0, y = [Math.floor(i.mtime.getTime() / 1e3) >>> 0, (g = Math.floor(i.mtime.getTime() / 1e3), 1 <= +Math.abs(g) ? 0 < g ? (0 | Math.min(+Math.floor(g / 4294967296), 4294967295)) >>> 0 : ~~+Math.ceil((g - (~~g >>> 0)) / 4294967296) >>> 0 : 0)], d[r + 72 >> 2] = y[0], d[r + 76 >> 2] = y[1], d[r + 80 >> 2] = 0, y = [Math.floor(i.ctime.getTime() / 1e3) >>> 0, (g = Math.floor(i.ctime.getTime() / 1e3), 1 <= +Math.abs(g) ? 0 < g ? (0 | Math.min(+Math.floor(g / 4294967296), 4294967295)) >>> 0 : ~~+Math.ceil((g - (~~g >>> 0)) / 4294967296) >>> 0 : 0)], d[r + 88 >> 2] = y[0], d[r + 92 >> 2] = y[1], d[r + 96 >> 2] = 0, y = [i.ino >>> 0, (g = i.ino, 1 <= +Math.abs(g) ? 0 < g ? (0 | Math.min(+Math.floor(g / 4294967296), 4294967295)) >>> 0 : ~~+Math.ceil((g - (~~g >>> 0)) / 4294967296) >>> 0 : 0)], d[r + 104 >> 2] = y[0], d[r + 108 >> 2] = y[1], 0
            }, doMsync: function (e, t, r, i, n) {
                e = u.slice(e, e + r);
                E.msync(t, e, n, r, i)
            }, varargs: void 0, get: function () {
                return U.varargs += 4, d[U.varargs - 4 >> 2]
            }, getStr: function (e) {
                return ee(e)
            }, getStreamFromFD: function (e) {
                e = E.getStream(e);
                if (e) return e;
                throw new E.ErrnoError(8)
            }
        };

        function _e(e) {
            switch (e) {
                case 1:
                    return 0;
                case 2:
                    return 1;
                case 4:
                    return 2;
                case 8:
                    return 3;
                default:
                    throw new TypeError("Unknown type size: " + e)
            }
        }

        var ge = void 0;

        function x(e) {
            for (var t = "", r = e; u[r];) t += ge[u[r++]];
            return t
        }

        var B = {}, A = {}, ye = {};

        function be(e) {
            if (void 0 === e) return "_unknown";
            var t = (e = e.replace(/[^a-zA-Z0-9_]/g, "$")).charCodeAt(0);
            return 48 <= t && t <= 57 ? "_" + e : e
        }

        function ve(e, t) {
            return e = be(e), new Function("body", "return function " + e + '() {\n    "use strict";    return body.apply(this, arguments);\n};\n')(t)
        }

        function we(e, t) {
            var r = ve(t, function (e) {
                this.name = t, this.message = e;
                e = new Error(e).stack;
                void 0 !== e && (this.stack = this.toString() + "\n" + e.replace(/^Error(:[^\n]*)?\n/, ""))
            });
            return r.prototype = Object.create(e.prototype), (r.prototype.constructor = r).prototype.toString = function () {
                return void 0 === this.message ? this.name : this.name + ": " + this.message
            }, r
        }

        var T = void 0;

        function k(e) {
            throw new T(e)
        }

        var Se = void 0;

        function Ee(e) {
            throw new Se(e)
        }

        function Ue(i, t, n) {
            function r(e) {
                var t = n(e);
                t.length !== i.length && Ee("Mismatched type converter count");
                for (var r = 0; r < i.length; ++r) C(i[r], t[r])
            }

            i.forEach(function (e) {
                ye[e] = t
            });
            var s = new Array(t.length), a = [], o = 0;
            t.forEach((e, t) => {
                A.hasOwnProperty(e) ? s[t] = A[e] : (a.push(e), B.hasOwnProperty(e) || (B[e] = []), B[e].push(() => {
                    s[t] = A[e], ++o === a.length && r(s)
                }))
            }), 0 === a.length && r(s)
        }

        function C(e, t, r) {
            r = 2 < arguments.length && void 0 !== r ? r : {};
            if (!("argPackAdvance" in t)) throw new TypeError("registerType registeredInstance requires argPackAdvance");
            var i = t.name;
            if (e || k('type "' + i + '" must have a positive integer typeid pointer'), A.hasOwnProperty(e)) {
                if (r.ignoreDuplicateRegistrations) return;
                k("Cannot register type '" + i + "' twice")
            }
            A[e] = t, delete ye[e], B.hasOwnProperty(e) && (r = B[e], delete B[e], r.forEach(e => e()))
        }

        function xe(e) {
            k(e.$$.ptrType.registeredClass.name + " instance already deleted")
        }

        var Be = !1;

        function Ae(e) {
        }

        function Te(e) {
            --e.count.value, 0 === e.count.value && ((e = e).smartPtr ? e.smartPtrType.rawDestructor(e.smartPtr) : e.ptrType.registeredClass.rawDestructor(e.ptr))
        }

        var ke = {};
        var Ce = [];

        function Fe() {
            for (; Ce.length;) {
                var e = Ce.pop();
                e.$$.deleteScheduled = !1, e.delete()
            }
        }

        var De = void 0;
        var Ie = {};

        function Pe(e, t) {
            return t.ptrType && t.ptr || Ee("makeClassHandle requires ptr and ptrType"), !!t.smartPtrType != !!t.smartPtr && Ee("Both smartPtrType and smartPtr must be specified"), t.count = {value: 1}, Le(Object.create(e, {$$: {value: t}}))
        }

        function Le(e) {
            return "undefined" == typeof FinalizationRegistry ? (Le = e => e, e) : (Be = new FinalizationRegistry(e => {
                Te(e.$$)
            }), Ae = e => Be.unregister(e), (Le = e => {
                var t = e.$$;
                return t.smartPtr && Be.register(e, {$$: t}, e), e
            })(e))
        }

        function F() {
        }

        function ze(e, t, r) {
            var i;
            void 0 === e[t].overloadTable && (i = e[t], e[t] = function () {
                return e[t].overloadTable.hasOwnProperty(arguments.length) || k("Function '" + r + "' called with an invalid number of arguments (" + arguments.length + ") - expects one of (" + e[t].overloadTable + ")!"), e[t].overloadTable[arguments.length].apply(this, arguments)
            }, e[t].overloadTable = [], e[t].overloadTable[i.argCount] = i)
        }

        function Re(e, t, r, i, n, s, a, o) {
            this.name = e, this.constructor = t, this.instancePrototype = r, this.rawDestructor = i, this.baseClass = n, this.getActualType = s, this.upcast = a, this.downcast = o, this.pureVirtualFunctions = []
        }

        function Me(e, t, r) {
            for (; t !== r;) t.upcast || k("Expected null or instance of " + r.name + ", got an instance of " + t.name), e = t.upcast(e), t = t.baseClass;
            return e
        }

        function Ne(e, t) {
            if (null === t) return this.isReference && k("null is not a valid " + this.name), 0;
            t.$$ || k('Cannot pass "' + et(t) + '" as a ' + this.name), t.$$.ptr || k("Cannot pass deleted object as a pointer of type " + this.name);
            var r = t.$$.ptrType.registeredClass;
            return Me(t.$$.ptr, r, this.registeredClass)
        }

        function Oe(e, t) {
            if (null === t) return this.isReference && k("null is not a valid " + this.name), this.isSmartPointer ? (i = this.rawConstructor(), null !== e && e.push(this.rawDestructor, i), i) : 0;
            t.$$ || k('Cannot pass "' + et(t) + '" as a ' + this.name), t.$$.ptr || k("Cannot pass deleted object as a pointer of type " + this.name), !this.isConst && t.$$.ptrType.isConst && k("Cannot convert argument of type " + (t.$$.smartPtrType || t.$$.ptrType).name + " to parameter type " + this.name);
            var r, i, n = t.$$.ptrType.registeredClass;
            if (i = Me(t.$$.ptr, n, this.registeredClass), this.isSmartPointer) switch (void 0 === t.$$.smartPtr && k("Passing raw pointer to smart pointer is illegal"), this.sharingPolicy) {
                case 0:
                    t.$$.smartPtrType === this ? i = t.$$.smartPtr : k("Cannot convert argument of type " + (t.$$.smartPtrType || t.$$.ptrType).name + " to parameter type " + this.name);
                    break;
                case 1:
                    i = t.$$.smartPtr;
                    break;
                case 2:
                    t.$$.smartPtrType === this ? i = t.$$.smartPtr : (r = t.clone(), i = this.rawShare(i, P.toHandle(function () {
                        r.delete()
                    })), null !== e && e.push(this.rawDestructor, i));
                    break;
                default:
                    k("Unsupporting sharing policy")
            }
            return i
        }

        function Ge(e, t) {
            if (null === t) return this.isReference && k("null is not a valid " + this.name), 0;
            t.$$ || k('Cannot pass "' + et(t) + '" as a ' + this.name), t.$$.ptr || k("Cannot pass deleted object as a pointer of type " + this.name), t.$$.ptrType.isConst && k("Cannot convert argument of type " + t.$$.ptrType.name + " to parameter type " + this.name);
            var r = t.$$.ptrType.registeredClass;
            return Me(t.$$.ptr, r, this.registeredClass)
        }

        function He(e) {
            return this.fromWireType(d[e >> 2])
        }

        function D(e, t, r, i, n, s, a, o, l, d, h) {
            this.name = e, this.registeredClass = t, this.isReference = r, this.isConst = i, this.isSmartPointer = n, this.pointeeType = s, this.sharingPolicy = a, this.rawGetPointee = o, this.rawConstructor = l, this.rawShare = d, this.rawDestructor = h, n || void 0 !== t.baseClass ? this.toWireType = Oe : (this.toWireType = i ? Ne : Ge, this.destructorFunction = null)
        }

        var Ve = [];

        function $e(e) {
            var t = Ve[e];
            return t || (e >= Ve.length && (Ve.length = e + 1), Ve[e] = t = J.get(e)), t
        }

        function I(e, t) {
            var n, s, a, r = (e = x(e)).includes("j") ? (n = e, s = t, a = [], function () {
                return a.length = 0, Object.assign(a, arguments), t = s, r = a, (e = n).includes("j") ? (i = t, e = _["dynCall_" + e], r && r.length ? e.apply(null, [i].concat(r)) : e.call(null, i)) : $e(t).apply(null, r);
                var e, t, r, i
            }) : $e(t);
            return "function" != typeof r && k("unknown function pointer with signature " + e + ": " + t), r
        }

        var je = void 0;

        function We(e) {
            var e = wt(e), t = x(e);
            return L(e), t
        }

        function Ye(e, t) {
            var r = [], i = {};
            throw t.forEach(function e(t) {
                i[t] || A[t] || (ye[t] ? ye[t].forEach(e) : (r.push(t), i[t] = !0))
            }), new je(e + ": " + r.map(We).join([", "]))
        }

        function qe(e, t) {
            for (var r = [], i = 0; i < e; i++) r.push(p[t + 4 * i >> 2]);
            return r
        }

        function Ke(e) {
            for (; e.length;) {
                var t = e.pop();
                e.pop()(t)
            }
        }

        function Xe(e, t) {
            if (!(e instanceof Function)) throw new TypeError("new_ called with constructor type " + typeof e + " which is not a function");
            var r = ve(e.name || "unknownFunctionName", function () {
            }), r = (r.prototype = e.prototype, new r), e = e.apply(r, t);
            return e instanceof Object ? e : r
        }

        function Ze(e, t, r, i, n) {
            var s = t.length;
            s < 2 && k("argTypes array size mismatch! Must at least get return value and 'this' types!");
            for (var r = null !== t[1] && null !== r, a = !1, o = 1; o < t.length; ++o) if (null !== t[o] && void 0 === t[o].destructorFunction) {
                a = !0;
                break
            }
            for (var l = "void" !== t[0].name, d = "", h = "", o = 0; o < s - 2; ++o) d += (0 !== o ? ", " : "") + "arg" + o, h += (0 !== o ? ", " : "") + "arg" + o + "Wired";
            var f = "return function " + be(e) + "(" + d + ") {\nif (arguments.length !== " + (s - 2) + ") {\nthrowBindingError('function " + e + " called with ' + arguments.length + ' arguments, expected " + (s - 2) + " args!');\n}\n",
                u = (a && (f += "var destructors = [];\n"), a ? "destructors" : "null"),
                p = ["throwBindingError", "invoker", "fn", "runDestructors", "retType", "classParam"],
                c = [k, i, n, Ke, t[0], t[1]];
            for (r && (f += "var thisWired = classParam.toWireType(" + u + ", this);\n"), o = 0; o < s - 2; ++o) f += "var arg" + o + "Wired = argType" + o + ".toWireType(" + u + ", arg" + o + "); // " + t[o + 2].name + "\n", p.push("argType" + o), c.push(t[o + 2]);
            if (f += (l ? "var rv = " : "") + "invoker(fn" + (0 < (h = r ? "thisWired" + (0 < h.length ? ", " : "") + h : h).length ? ", " : "") + h + ");\n", a) f += "runDestructors(destructors);\n"; else for (o = r ? 1 : 2; o < t.length; ++o) {
                var m = 1 === o ? "thisWired" : "arg" + (o - 2) + "Wired";
                null !== t[o].destructorFunction && (f += m + "_dtor(" + m + "); // " + t[o].name + "\n", p.push(m + "_dtor"), c.push(t[o].destructorFunction))
            }
            return l && (f += "var ret = retType.fromWireType(rv);\nreturn ret;\n"), p.push(f += "}\n"), Xe(Function, p).apply(null, c)
        }

        var Je = [], n = [{}, {value: void 0}, {value: null}, {value: !0}, {value: !1}];

        function Qe(e) {
            4 < e && 0 == --n[e].refcount && (n[e] = void 0, Je.push(e))
        }

        var P = {
            toValue: e => (e || k("Cannot use deleted val. handle = " + e), n[e].value), toHandle: e => {
                switch (e) {
                    case void 0:
                        return 1;
                    case null:
                        return 2;
                    case!0:
                        return 3;
                    case!1:
                        return 4;
                    default:
                        var t = Je.length ? Je.pop() : n.length;
                        return n[t] = {refcount: 1, value: e}, t
                }
            }
        };

        function et(e) {
            if (null === e) return "null";
            var t = typeof e;
            return "object" == t || "array" == t || "function" == t ? e.toString() : "" + e
        }

        var tt = "undefined" != typeof TextDecoder ? new TextDecoder("utf-16le") : void 0;

        function rt(e, t) {
            for (var r, i = e >> 1, n = i + t / 2; !(n <= i) && K[i];) ++i;
            if (32 < (r = i << 1) - e && tt) return tt.decode(u.subarray(e, r));
            for (var s = "", a = 0; !(t / 2 <= a); ++a) {
                var o = l[e + 2 * a >> 1];
                if (0 == o) break;
                s += String.fromCharCode(o)
            }
            return s
        }

        function it(e, t, r) {
            if ((r = void 0 === r ? 2147483647 : r) < 2) return 0;
            for (var i = t, n = (r -= 2) < 2 * e.length ? r / 2 : e.length, s = 0; s < n; ++s) {
                var a = e.charCodeAt(s);
                l[t >> 1] = a, t += 2
            }
            return l[t >> 1] = 0, t - i
        }

        function nt(e) {
            return 2 * e.length
        }

        function st(e, t) {
            for (var r = 0, i = ""; !(t / 4 <= r);) {
                var n, s = d[e + 4 * r >> 2];
                if (0 == s) break;
                ++r, 65536 <= s ? (n = s - 65536, i += String.fromCharCode(55296 | n >> 10, 56320 | 1023 & n)) : i += String.fromCharCode(s)
            }
            return i
        }

        function at(e, t, r) {
            if ((r = void 0 === r ? 2147483647 : r) < 4) return 0;
            for (var i = t, n = i + r - 4, s = 0; s < e.length; ++s) {
                var a = e.charCodeAt(s);
                if (55296 <= a && a <= 57343 && (a = 65536 + ((1023 & a) << 10) | 1023 & e.charCodeAt(++s)), d[t >> 2] = a, (t += 4) + 4 > n) break
            }
            return d[t >> 2] = 0, t - i
        }

        function ot(e) {
            for (var t = 0, r = 0; r < e.length; ++r) {
                var i = e.charCodeAt(r);
                55296 <= i && i <= 57343 && ++r, t += 4
            }
            return t
        }

        var lt = {};

        function dt(e) {
            var t = lt[e];
            return void 0 === t ? x(e) : t
        }

        var ht = [];

        function ft(e, t) {
            var r = A[e];
            return void 0 === r && k(t + " has unknown type " + We(e)), r
        }

        var ut = [], pt = {};

        function ct() {
            if (!ct.strings) {
                var e = {
                    USER: "web_user",
                    LOGNAME: "web_user",
                    PATH: "/",
                    PWD: "/",
                    HOME: "/home/web_user",
                    LANG: ("object" == typeof navigator && navigator.languages && navigator.languages[0] || "C").replace("-", "_") + ".UTF-8",
                    _: H || "./this.program"
                };
                for (t in pt) void 0 === pt[t] ? delete e[t] : e[t] = pt[t];
                var t, r = [];
                for (t in e) r.push(t + "=" + e[t]);
                ct.strings = r
            }
            return ct.strings
        }

        function mt(e, t, r, i) {
            this.parent = e = e || this, this.mount = e.mount, this.mounted = null, this.id = E.nextInode++, this.name = t, this.mode = r, this.node_ops = {}, this.stream_ops = {}, this.rdev = i
        }

        Object.defineProperties(mt.prototype, {
            read: {
                get: function () {
                    return 365 == (365 & this.mode)
                }, set: function (e) {
                    e ? this.mode |= 365 : this.mode &= -366
                }
            }, write: {
                get: function () {
                    return 146 == (146 & this.mode)
                }, set: function (e) {
                    e ? this.mode |= 146 : this.mode &= -147
                }
            }, isFolder: {
                get: function () {
                    return E.isDir(this.mode)
                }
            }, isDevice: {
                get: function () {
                    return E.isChrdev(this.mode)
                }
            }
        }), E.FSNode = mt, E.staticInit();
        for (var _t = new Array(256), gt = 0; gt < 256; ++gt) _t[gt] = String.fromCharCode(gt);
        ge = _t, T = _.BindingError = we(Error, "BindingError"), Se = _.InternalError = we(Error, "InternalError"), F.prototype.isAliasOf = function (e) {
            if (!(this instanceof F)) return !1;
            if (!(e instanceof F)) return !1;
            for (var t = this.$$.ptrType.registeredClass, r = this.$$.ptr, i = e.$$.ptrType.registeredClass, n = e.$$.ptr; t.baseClass;) r = t.upcast(r), t = t.baseClass;
            for (; i.baseClass;) n = i.upcast(n), i = i.baseClass;
            return t === i && r === n
        }, F.prototype.clone = function () {
            if (this.$$.ptr || xe(this), this.$$.preservePointerOnDelete) return this.$$.count.value += 1, this;
            var e = Le(Object.create(Object.getPrototypeOf(this), {
                $$: {
                    value: {
                        count: (e = this.$$).count,
                        deleteScheduled: e.deleteScheduled,
                        preservePointerOnDelete: e.preservePointerOnDelete,
                        ptr: e.ptr,
                        ptrType: e.ptrType,
                        smartPtr: e.smartPtr,
                        smartPtrType: e.smartPtrType
                    }
                }
            }));
            return e.$$.count.value += 1, e.$$.deleteScheduled = !1, e
        }, F.prototype.delete = function () {
            this.$$.ptr || xe(this), this.$$.deleteScheduled && !this.$$.preservePointerOnDelete && k("Object already scheduled for deletion"), Ae(this), Te(this.$$), this.$$.preservePointerOnDelete || (this.$$.smartPtr = void 0, this.$$.ptr = void 0)
        }, F.prototype.isDeleted = function () {
            return !this.$$.ptr
        }, F.prototype.deleteLater = function () {
            return this.$$.ptr || xe(this), this.$$.deleteScheduled && !this.$$.preservePointerOnDelete && k("Object already scheduled for deletion"), Ce.push(this), 1 === Ce.length && De && De(Fe), this.$$.deleteScheduled = !0, this
        }, _.getInheritedInstanceCount = function () {
            return Object.keys(Ie).length
        }, _.getLiveInheritedInstances = function () {
            var e, t = [];
            for (e in Ie) Ie.hasOwnProperty(e) && t.push(Ie[e]);
            return t
        }, _.flushPendingDeletes = Fe, _.setDelayFunction = function (e) {
            De = e, Ce.length && De && De(Fe)
        }, D.prototype.getPointee = function (e) {
            return e = this.rawGetPointee ? this.rawGetPointee(e) : e
        }, D.prototype.destructor = function (e) {
            this.rawDestructor && this.rawDestructor(e)
        }, D.prototype.argPackAdvance = 8, D.prototype.readValueFromPointer = He, D.prototype.deleteObject = function (e) {
            null !== e && e.delete()
        }, D.prototype.fromWireType = function (e) {
            var t = this.getPointee(e);
            if (!t) return this.destructor(e), null;
            if (i = function (e, t) {
                for (void 0 === t && k("ptr should not be undefined"); e.baseClass;) t = e.upcast(t), e = e.baseClass;
                return t
            }(i = this.registeredClass, i = t), void 0 !== (i = Ie[i])) {
                if (0 === i.$$.count.value) return i.$$.ptr = t, i.$$.smartPtr = e, i.clone();
                i = i.clone();
                return this.destructor(e), i
            }

            function r() {
                return this.isSmartPointer ? Pe(this.registeredClass.instancePrototype, {
                    ptrType: this.pointeeType,
                    ptr: t,
                    smartPtrType: this,
                    smartPtr: e
                }) : Pe(this.registeredClass.instancePrototype, {ptrType: this, ptr: e})
            }

            if (i = this.registeredClass.getActualType(t), !(i = ke[i])) return r.call(this);
            var i = this.isConst ? i.constPointerType : i.pointerType, n = function e(t, r, i) {
                if (r === i) return t;
                if (void 0 === i.baseClass) return null;
                t = e(t, r, i.baseClass);
                return null === t ? null : i.downcast(t)
            }(t, this.registeredClass, i.registeredClass);
            return null === n ? r.call(this) : this.isSmartPointer ? Pe(i.registeredClass.instancePrototype, {
                ptrType: i,
                ptr: n,
                smartPtrType: this,
                smartPtr: e
            }) : Pe(i.registeredClass.instancePrototype, {ptrType: i, ptr: n})
        }, je = _.UnboundTypeError = we(Error, "UnboundTypeError"), _.count_emval_handles = function () {
            for (var e = 0, t = 5; t < n.length; ++t) void 0 !== n[t] && ++e;
            return e
        }, _.get_first_emval = function () {
            for (var e = 5; e < n.length; ++e) if (void 0 !== n[e]) return n[e];
            return null
        };
        var yt = {
            J: function (e) {
                return bt(e + 24) + 24
            }, I: function (e, t, r) {
                throw new pe(e).init(t, r), e
            }, D: function (e, t, r) {
                U.varargs = r;
                try {
                    var i = U.getStreamFromFD(e);
                    switch (t) {
                        case 0:
                            return (n = U.get()) < 0 ? -28 : E.createStream(i, n).fd;
                        case 1:
                        case 2:
                        case 6:
                        case 7:
                            return 0;
                        case 3:
                            return i.flags;
                        case 4:
                            var n = U.get();
                            return i.flags |= n, 0;
                        case 5:
                            return n = U.get(), l[n + 0 >> 1] = 2, 0;
                        case 16:
                        case 8:
                        default:
                            return -28;
                        case 9:
                            return d[vt() >> 2] = 28, -1
                    }
                } catch (e) {
                    if (void 0 !== E && e instanceof E.ErrnoError) return -e.errno;
                    throw e
                }
            }, w: function (e, t, r, i) {
                U.varargs = i;
                try {
                    t = U.getStr(t), t = U.calculateAt(e, t);
                    var n = i ? U.get() : 0;
                    return E.open(t, r, n).fd
                } catch (e) {
                    if (void 0 !== E && e instanceof E.ErrnoError) return -e.errno;
                    throw e
                }
            }, v: function (e, t, r, i, n) {
            }, G: function (e, r, i, n, s) {
                var a = _e(i);
                C(e, {
                    name: r = x(r), fromWireType: function (e) {
                        return !!e
                    }, toWireType: function (e, t) {
                        return t ? n : s
                    }, argPackAdvance: 8, readValueFromPointer: function (e) {
                        var t;
                        if (1 === i) t = f; else if (2 === i) t = l; else {
                            if (4 !== i) throw new TypeError("Unknown boolean type size: " + r);
                            t = d
                        }
                        return this.fromWireType(t[e >> a])
                    }, destructorFunction: null
                })
            }, l: function (l, e, t, d, r, h, i, f, n, u, p, s, c) {
                p = x(p), h = I(r, h), f = f && I(i, f), u = u && I(n, u), c = I(s, c);
                var a, m = be(p);
                r = m, i = function () {
                    Ye("Cannot construct " + p + " due to unbound types", [d])
                }, _.hasOwnProperty(r) ? (k("Cannot register public name '" + r + "' twice"), ze(_, r, r), _.hasOwnProperty(a) && k("Cannot register multiple overloads of a function with the same number of arguments (" + a + ")!"), _[r].overloadTable[a] = i) : _[r] = i, Ue([l, e, t], d ? [d] : [], function (e) {
                    e = e[0], e = d ? (a = e.registeredClass).instancePrototype : F.prototype;
                    var t, r, i = ve(m, function () {
                            if (Object.getPrototypeOf(this) !== n) throw new T("Use 'new' to construct " + p);
                            if (void 0 === s.constructor_body) throw new T(p + " has no accessible constructor");
                            var e = s.constructor_body[arguments.length];
                            if (void 0 === e) throw new T("Tried to invoke ctor of " + p + " with invalid number of parameters (" + arguments.length + ") - expected (" + Object.keys(s.constructor_body).toString() + ") parameters instead!");
                            return e.apply(this, arguments)
                        }), n = Object.create(e, {constructor: {value: i}}),
                        s = (i.prototype = n, new Re(p, i, n, c, a, h, f, u)), e = new D(p, s, !0, !1, !1),
                        a = new D(p + "*", s, !1, !1, !1), o = new D(p + " const*", s, !1, !0, !1);
                    return ke[l] = {
                        pointerType: a,
                        constPointerType: o
                    }, t = m, i = i, _.hasOwnProperty(t) || Ee("Replacing nonexistant public symbol"), _[t].overloadTable, _[t] = i, _[t].argCount = r, [e, a, o]
                })
            }, r: function (e, i, t, r, n, s) {
                Y(0 < i);
                var a = qe(i, t);
                n = I(r, n), Ue([], [e], function (t) {
                    var r = "constructor " + (t = t[0]).name;
                    if (void 0 === t.registeredClass.constructor_body && (t.registeredClass.constructor_body = []), void 0 !== t.registeredClass.constructor_body[i - 1]) throw new T("Cannot register multiple constructors with identical number of parameters (" + (i - 1) + ") for class '" + t.name + "'! Overload resolution is currently only performed using the parameter count, not actual type info!");
                    return t.registeredClass.constructor_body[i - 1] = () => {
                        Ye("Cannot construct " + t.name + " due to unbound types", a)
                    }, Ue([], a, function (e) {
                        return e.splice(1, 0, null), t.registeredClass.constructor_body[i - 1] = Ze(r, e, null, n, s), []
                    }), []
                })
            }, g: function (e, s, a, t, r, o, l, d) {
                var h = qe(a, t);
                s = x(s), o = I(r, o), Ue([], [e], function (t) {
                    var r = (t = t[0]).name + "." + s;

                    function e() {
                        Ye("Cannot call " + r + " due to unbound types", h)
                    }

                    s.startsWith("@@") && (s = Symbol[s.substring(2)]), d && t.registeredClass.pureVirtualFunctions.push(s);
                    var i = t.registeredClass.instancePrototype, n = i[s];
                    return void 0 === n || void 0 === n.overloadTable && n.className !== t.name && n.argCount === a - 2 ? (e.argCount = a - 2, e.className = t.name, i[s] = e) : (ze(i, s, r), i[s].overloadTable[a - 2] = e), Ue([], h, function (e) {
                        e = Ze(r, e, t, o, l);
                        return void 0 === i[s].overloadTable ? (e.argCount = a - 2, i[s] = e) : i[s].overloadTable[a - 2] = e, []
                    }), []
                })
            }, F: function (e, t) {
                C(e, {
                    name: t = x(t), fromWireType: function (e) {
                        var t = P.toValue(e);
                        return Qe(e), t
                    }, toWireType: function (e, t) {
                        return P.toHandle(t)
                    }, argPackAdvance: 8, readValueFromPointer: He, destructorFunction: null
                })
            }, p: function (e, t, r) {
                r = _e(r);
                C(e, {
                    name: t = x(t), fromWireType: function (e) {
                        return e
                    }, toWireType: function (e, t) {
                        return t
                    }, argPackAdvance: 8, readValueFromPointer: function (e, t) {
                        switch (t) {
                            case 2:
                                return function (e) {
                                    return this.fromWireType(X[e >> 2])
                                };
                            case 3:
                                return function (e) {
                                    return this.fromWireType(Z[e >> 3])
                                };
                            default:
                                throw new TypeError("Unknown float type: " + e)
                        }
                    }(t, r), destructorFunction: null
                })
            }, d: function (e, t, r, i, n) {
                t = x(t);
                var s, a = _e(r), o = e => e,
                    r = (0 === i && (s = 32 - 8 * r, o = e => e << s >>> s), t.includes("unsigned"));
                C(e, {
                    name: t, fromWireType: o, toWireType: r ? function (e, t) {
                        return this.name, t >>> 0
                    } : function (e, t) {
                        return this.name, t
                    }, argPackAdvance: 8, readValueFromPointer: function (e, t, r) {
                        switch (t) {
                            case 0:
                                return r ? function (e) {
                                    return f[e]
                                } : function (e) {
                                    return u[e]
                                };
                            case 1:
                                return r ? function (e) {
                                    return l[e >> 1]
                                } : function (e) {
                                    return K[e >> 1]
                                };
                            case 2:
                                return r ? function (e) {
                                    return d[e >> 2]
                                } : function (e) {
                                    return p[e >> 2]
                                };
                            default:
                                throw new TypeError("Unknown integer type: " + e)
                        }
                    }(t, a, 0 !== i), destructorFunction: null
                })
            }, b: function (e, t, r) {
                var i = [Int8Array, Uint8Array, Int16Array, Uint16Array, Int32Array, Uint32Array, Float32Array, Float64Array][t];

                function n(e) {
                    var t = p, r = t[e >>= 2], t = t[e + 1];
                    return new i(q, t, r)
                }

                C(e, {
                    name: r = x(r),
                    fromWireType: n,
                    argPackAdvance: 8,
                    readValueFromPointer: n
                }, {ignoreDuplicateRegistrations: !0})
            }, q: function (e, t) {
                var d = "std::string" === (t = x(t));
                C(e, {
                    name: t, fromWireType: function (e) {
                        var t, r = p[e >> 2], i = e + 4;
                        if (d) for (var n = i, s = 0; s <= r; ++s) {
                            var a, o = i + s;
                            s != r && 0 != u[o] || (a = ee(n, o - n), void 0 === t ? t = a : t = t + String.fromCharCode(0) + a, n = o + 1)
                        } else {
                            for (var l = new Array(r), s = 0; s < r; ++s) l[s] = String.fromCharCode(u[i + s]);
                            t = l.join("")
                        }
                        return L(e), t
                    }, toWireType: function (e, t) {
                        var r, i = "string" == typeof (t = t instanceof ArrayBuffer ? new Uint8Array(t) : t),
                            n = (i || t instanceof Uint8Array || t instanceof Uint8ClampedArray || t instanceof Int8Array || k("Cannot pass non-string to std::string"), r = d && i ? re(t) : t.length, bt(4 + r + 1)),
                            s = n + 4;
                        if (p[n >> 2] = r, d && i) te(t, u, s, r + 1); else if (i) for (var a = 0; a < r; ++a) {
                            var o = t.charCodeAt(a);
                            255 < o && (L(s), k("String has UTF-16 code units that do not fit in 8 bits")), u[s + a] = o
                        } else for (a = 0; a < r; ++a) u[s + a] = t[a];
                        return null !== e && e.push(L, n), n
                    }, argPackAdvance: 8, readValueFromPointer: He, destructorFunction: function (e) {
                        L(e)
                    }
                })
            }, k: function (e, l, n) {
                var d, s, h, a, f;
                n = x(n), 2 === l ? (d = rt, s = it, a = nt, h = () => K, f = 1) : 4 === l && (d = st, s = at, a = ot, h = () => p, f = 2), C(e, {
                    name: n,
                    fromWireType: function (e) {
                        for (var t, r = p[e >> 2], i = h(), n = e + 4, s = 0; s <= r; ++s) {
                            var a, o = e + 4 + s * l;
                            s != r && 0 != i[o >> f] || (a = d(n, o - n), void 0 === t ? t = a : t = t + String.fromCharCode(0) + a, n = o + l)
                        }
                        return L(e), t
                    },
                    toWireType: function (e, t) {
                        "string" != typeof t && k("Cannot pass non-string to C++ string type " + n);
                        var r = a(t), i = bt(4 + r + l);
                        return p[i >> 2] = r >> f, s(t, i + 4, r + l), null !== e && e.push(L, i), i
                    },
                    argPackAdvance: 8,
                    readValueFromPointer: He,
                    destructorFunction: function (e) {
                        L(e)
                    }
                })
            }, H: function (e, t) {
                C(e, {
                    isVoid: !0, name: t = x(t), argPackAdvance: 0, fromWireType: function () {
                    }, toWireType: function (e, t) {
                    }
                })
            }, j: function () {
                return Date.now()
            }, f: function (e, t, r, i) {
                (e = ht[e])(t = P.toValue(t), r = dt(r), null, i)
            }, c: Qe, e: function (e, t) {
                var r = function (e, t) {
                    for (var r = new Array(e), i = 0; i < e; ++i) r[i] = ft(p[t + 4 * i >> 2], "parameter " + i);
                    return r
                }(e, t), t = r[0], i = t.name + "_$" + r.slice(1).map(function (e) {
                    return e.name
                }).join("_") + "$", n = ut[i];
                if (void 0 !== n) return n;
                for (var s = ["retType"], a = [t], o = "", l = 0; l < e - 1; ++l) o += (0 !== l ? ", " : "") + "arg" + l, s.push("argType" + l), a.push(r[1 + l]);
                for (var d = "return function " + be("methodCaller_" + i) + "(handle, name, destructors, args) {\n", h = 0, l = 0; l < e - 1; ++l) d += "    var arg" + l + " = argType" + l + ".readValueFromPointer(args" + (h ? "+" + h : "") + ");\n", h += r[l + 1].argPackAdvance;
                for (d += "    var rv = handle[name](" + o + ");\n", l = 0; l < e - 1; ++l) r[l + 1].deleteObject && (d += "    argType" + l + ".deleteObject(arg" + l + ");\n");
                t.isVoid || (d += "    return retType.toWireType(destructors, rv);\n"), s.push(d += "};\n");
                var t = Xe(Function, s).apply(null, a), f = ht.length;
                return ht.push(t), ut[i] = n = f
            }, s: function (e) {
                4 < e && (n[e].refcount += 1)
            }, m: function (e) {
                return P.toHandle(dt(e))
            }, K: function () {
                return P.toHandle({})
            }, E: function (e) {
                return P.toHandle(ee(e))
            }, n: function (e, t, r) {
                e = P.toValue(e), t = P.toValue(t), r = P.toValue(r), e[t] = r
            }, t: function (e, t) {
                e = (e = ft(e, "_emval_take_value")).readValueFromPointer(t);
                return P.toHandle(e)
            }, a: function () {
                b("")
            }, A: function (e, t, r) {
                u.copyWithin(e, t, t + r)
            }, i: function (e) {
                u.length, b("OOM")
            }, y: function (a, o) {
                var l = 0;
                return ct().forEach(function (e, t) {
                    for (var r = o + l, i = (p[a + 4 * t >> 2] = r, e), n = r, s = 0; s < i.length; ++s) f[n++ >> 0] = i.charCodeAt(s);
                    f[n >> 0] = 0, l += e.length + 1
                }), 0
            }, z: function (e, t) {
                var r = ct(), i = (p[e >> 2] = r.length, 0);
                return r.forEach(function (e) {
                    i += e.length + 1
                }), p[t >> 2] = i, 0
            }, o: function (e) {
                try {
                    var t = U.getStreamFromFD(e);
                    return E.close(t), 0
                } catch (e) {
                    if (void 0 !== E && e instanceof E.ErrnoError) return e.errno;
                    throw e
                }
            }, x: function (e, t) {
                try {
                    var r = U.getStreamFromFD(e), i = r.tty ? 2 : E.isDir(r.mode) ? 3 : E.isLink(r.mode) ? 7 : 4;
                    return f[t >> 0] = i, 0
                } catch (e) {
                    if (void 0 !== E && e instanceof E.ErrnoError) return e.errno;
                    throw e
                }
            }, C: function (e, t, r, i) {
                try {
                    var n = function (e, t, r) {
                        for (var i = 0, n = 0; n < r; n++) {
                            var s = p[t >> 2], a = p[t + 4 >> 2], s = (t += 8, E.read(e, f, s, a, void 0));
                            if (s < 0) return -1;
                            if (i += s, s < a) break
                        }
                        return i
                    }(U.getStreamFromFD(e), t, r);
                    return d[i >> 2] = n, 0
                } catch (e) {
                    if (void 0 !== E && e instanceof E.ErrnoError) return e.errno;
                    throw e
                }
            }, u: function (e, t, r, i, n) {
                try {
                    var s = r + 2097152 >>> 0 < 4194305 - !!t ? (t >>> 0) + 4294967296 * r : NaN;
                    if (isNaN(s)) return 61;
                    var a = U.getStreamFromFD(e);
                    return E.llseek(a, s, i), y = [a.position >>> 0, (g = a.position, 1 <= +Math.abs(g) ? 0 < g ? (0 | Math.min(+Math.floor(g / 4294967296), 4294967295)) >>> 0 : ~~+Math.ceil((g - (~~g >>> 0)) / 4294967296) >>> 0 : 0)], d[n >> 2] = y[0], d[n + 4 >> 2] = y[1], a.getdents && 0 === s && 0 === i && (a.getdents = null), 0
                } catch (e) {
                    if (void 0 !== E && e instanceof E.ErrnoError) return e.errno;
                    throw e
                }
            }, B: function (e, t, r, i) {
                try {
                    var n = function (e, t, r) {
                        for (var i = 0, n = 0; n < r; n++) {
                            var s = p[t >> 2], a = p[t + 4 >> 2], s = (t += 8, E.write(e, f, s, a, void 0));
                            if (s < 0) return -1;
                            i += s
                        }
                        return i
                    }(U.getStreamFromFD(e), t, r);
                    return p[i >> 2] = n, 0
                } catch (e) {
                    if (void 0 !== E && e instanceof E.ErrnoError) return e.errno;
                    throw e
                }
            }, h: function (e) {
            }
        }, L = (!function () {
            var t = {a: yt};

            function r(e, t) {
                var e = e.exports;
                _.asm = e, e = _.asm.L.buffer, q = e, _.HEAP8 = f = new Int8Array(e), _.HEAP16 = l = new Int16Array(e), _.HEAP32 = d = new Int32Array(e), _.HEAPU8 = u = new Uint8Array(e), _.HEAPU16 = K = new Uint16Array(e), _.HEAPU32 = p = new Uint32Array(e), _.HEAPF32 = X = new Float32Array(e), _.HEAPF64 = Z = new Float64Array(e), J = _.asm.P, e = _.asm.M, ne.unshift(e), le()
            }

            function i(e) {
                r(e.instance)
            }

            function n(e) {
                return function () {
                    if (!s && (V || h)) {
                        if ("function" == typeof fetch && !he(c)) return fetch(c, {credentials: "same-origin"}).then(function (e) {
                            if (e.ok) return e.arrayBuffer();
                            throw"failed to load wasm binary file at '" + c + "'"
                        }).catch(function () {
                            return fe(c)
                        });
                        if (m) return new Promise(function (t, e) {
                            m(c, function (e) {
                                t(new Uint8Array(e))
                            }, e)
                        })
                    }
                    return Promise.resolve().then(function () {
                        return fe(c)
                    })
                }().then(function (e) {
                    return WebAssembly.instantiate(e, t)
                }).then(function (e) {
                    return e
                }).then(e, function (e) {
                    o("failed to asynchronously prepare wasm: " + e), b(e)
                })
            }

            if (oe(), _.instantiateWasm) try {
                return _.instantiateWasm(t, r)
            } catch (t) {
                return o("Module.instantiateWasm callback failed with error: " + t)
            }
            s || "function" != typeof WebAssembly.instantiateStreaming || de(c) || he(c) || $ || "function" != typeof fetch ? n(i) : fetch(c, {credentials: "same-origin"}).then(function (e) {
                return WebAssembly.instantiateStreaming(e, t).then(i, function (e) {
                    return o("wasm streaming compile failed: " + e), o("falling back to ArrayBuffer instantiation"), n(i)
                })
            })
        }(), _.___wasm_call_ctors = function () {
            return (_.___wasm_call_ctors = _.asm.M).apply(null, arguments)
        }, _._free = function () {
            return (L = _._free = _.asm.N).apply(null, arguments)
        }), bt = _._malloc = function () {
            return (bt = _._malloc = _.asm.O).apply(null, arguments)
        }, vt = _.___errno_location = function () {
            return (vt = _.___errno_location = _.asm.Q).apply(null, arguments)
        }, wt = _.___getTypeName = function () {
            return (wt = _.___getTypeName = _.asm.R).apply(null, arguments)
        };
        _.___embind_register_native_and_builtin_types = function () {
            return (_.___embind_register_native_and_builtin_types = _.asm.S).apply(null, arguments)
        };
        var St, Et = _._emscripten_builtin_memalign = function () {
            return (Et = _._emscripten_builtin_memalign = _.asm.T).apply(null, arguments)
        }, Ut = _.___cxa_is_pointer_type = function () {
            return (Ut = _.___cxa_is_pointer_type = _.asm.U).apply(null, arguments)
        };

        function xt() {
            function e() {
                if (!St && (St = !0, _.calledRun = !0, !W)) {
                    if (_.noFSInit || E.init.initialized || E.init(), E.ignorePermissions = !1, ue(ne), _.onRuntimeInitialized && _.onRuntimeInitialized(), _.postRun) for ("function" == typeof _.postRun && (_.postRun = [_.postRun]); _.postRun.length;) e = _.postRun.shift(), se.unshift(e);
                    var e;
                    ue(se)
                }
            }

            if (!(0 < r)) {
                if (_.preRun) for ("function" == typeof _.preRun && (_.preRun = [_.preRun]); _.preRun.length;) t = _.preRun.shift(), ie.unshift(t);
                var t;
                ue(ie), 0 < r || (_.setStatus ? (_.setStatus("Running..."), setTimeout(function () {
                    setTimeout(function () {
                        _.setStatus("")
                    }, 1), e()
                }, 1)) : e())
            }
        }

        if (_.dynCall_viiijj = function () {
            return (_.dynCall_viiijj = _.asm.V).apply(null, arguments)
        }, _.dynCall_jij = function () {
            return (_.dynCall_jij = _.asm.W).apply(null, arguments)
        }, _.dynCall_jii = function () {
            return (_.dynCall_jii = _.asm.X).apply(null, arguments)
        }, _.dynCall_jiji = function () {
            return (_.dynCall_jiji = _.asm.Y).apply(null, arguments)
        }, _._ff_h264_cabac_tables = 217036, ae = function e() {
            St || xt(), St || (ae = e)
        }, _.preInit) for ("function" == typeof _.preInit && (_.preInit = [_.preInit]); 0 < _.preInit.length;) _.preInit.pop()();
        xt(), z.exports = _
    }), E = 1e-6, n = "undefined" != typeof Float32Array ? Float32Array : Array;

    function B() {
        var e = new n(16);
        return n != Float32Array && (e[1] = 0, e[2] = 0, e[3] = 0, e[4] = 0, e[6] = 0, e[7] = 0, e[8] = 0, e[9] = 0, e[11] = 0, e[12] = 0, e[13] = 0, e[14] = 0), e[0] = 1, e[5] = 1, e[10] = 1, e[15] = 1, e
    }

    function A(e) {
        e[0] = 1, e[1] = 0, e[2] = 0, e[3] = 0, e[4] = 0, e[5] = 1, e[6] = 0, e[7] = 0, e[8] = 0, e[9] = 0, e[10] = 1, e[11] = 0, e[12] = 0, e[13] = 0, e[14] = 0, e[15] = 1
    }

    Math.hypot || (Math.hypot = function () {
        for (var e = 0, t = arguments.length; t--;) e += arguments[t] * arguments[t];
        return Math.sqrt(e)
    });

    function T(e, t, r) {
        var i = new n(3);
        return i[0] = e, i[1] = t, i[2] = r, i
    }

    e = new n(3), n != Float32Array && (e[0] = 0, e[1] = 0, e[2] = 0);
    var ie = (g, e) => {
        e && g.pixelStorei(g.UNPACK_ALIGNMENT, 1);
        e = s(g.VERTEX_SHADER, "\n            attribute vec4 aVertexPosition;\n            attribute vec2 aTexturePosition;\n            uniform mat4 uModelMatrix;\n            uniform mat4 uViewMatrix;\n            uniform mat4 uProjectionMatrix;\n            varying lowp vec2 vTexturePosition;\n            void main(void) {\n              gl_Position = uProjectionMatrix * uViewMatrix * uModelMatrix * aVertexPosition;\n              vTexturePosition = aTexturePosition;\n            }\n        "), t = s(g.FRAGMENT_SHADER, "\n            precision highp float;\n            varying highp vec2 vTexturePosition;\n            uniform int isyuv;\n            uniform sampler2D rgbaTexture;\n            uniform sampler2D yTexture;\n            uniform sampler2D uTexture;\n            uniform sampler2D vTexture;\n\n            const mat4 YUV2RGB = mat4( 1.1643828125, 0, 1.59602734375, -.87078515625,\n                                       1.1643828125, -.39176171875, -.81296875, .52959375,\n                                       1.1643828125, 2.017234375, 0, -1.081390625,\n                                       0, 0, 0, 1);\n\n\n            void main(void) {\n\n                if (isyuv>0) {\n\n                    highp float y = texture2D(yTexture,  vTexturePosition).r;\n                    highp float u = texture2D(uTexture,  vTexturePosition).r;\n                    highp float v = texture2D(vTexture,  vTexturePosition).r;\n                    gl_FragColor = vec4(y, u, v, 1) * YUV2RGB;\n\n                } else {\n                    gl_FragColor =  texture2D(rgbaTexture, vTexturePosition);\n                }\n            }\n        "), r = g.createProgram(), g.attachShader(r, e), g.attachShader(r, t), g.linkProgram(r);
        var t, r,
            e = g.getProgramParameter(r, g.LINK_STATUS) ? r : (console.log("Unable to initialize the shader program: " + g.getProgramInfoLog(r)), null);
        let y = {
                program: e,
                attribLocations: {
                    vertexPosition: g.getAttribLocation(e, "aVertexPosition"),
                    texturePosition: g.getAttribLocation(e, "aTexturePosition")
                },
                uniformLocations: {
                    projectionMatrix: g.getUniformLocation(e, "uProjectionMatrix"),
                    modelMatrix: g.getUniformLocation(e, "uModelMatrix"),
                    viewMatrix: g.getUniformLocation(e, "uViewMatrix"),
                    rgbatexture: g.getUniformLocation(e, "rgbaTexture"),
                    ytexture: g.getUniformLocation(e, "yTexture"),
                    utexture: g.getUniformLocation(e, "uTexture"),
                    vtexture: g.getUniformLocation(e, "vTexture"),
                    isyuv: g.getUniformLocation(e, "isyuv")
                }
            },
            b = (t = g.createBuffer(), g.bindBuffer(g.ARRAY_BUFFER, t), g.bufferData(g.ARRAY_BUFFER, new Float32Array([-1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1]), g.STATIC_DRAW), r = (r = []).concat([0, 1], [1, 1], [1, 0], [0, 0]), e = g.createBuffer(), g.bindBuffer(g.ARRAY_BUFFER, e), g.bufferData(g.ARRAY_BUFFER, new Float32Array(r), g.STATIC_DRAW), r = g.createBuffer(), g.bindBuffer(g.ELEMENT_ARRAY_BUFFER, r), g.bufferData(g.ELEMENT_ARRAY_BUFFER, new Uint16Array([0, 1, 2, 0, 2, 3]), g.STATIC_DRAW), {
                position: t,
                texPosition: e,
                indices: r
            }), i = n(), v = n(), w = n(), S = n();

        function n() {
            var e = g.createTexture();
            return g.bindTexture(g.TEXTURE_2D, e), g.texParameteri(g.TEXTURE_2D, g.TEXTURE_MAG_FILTER, g.LINEAR), g.texParameteri(g.TEXTURE_2D, g.TEXTURE_MIN_FILTER, g.LINEAR), g.texParameteri(g.TEXTURE_2D, g.TEXTURE_WRAP_S, g.CLAMP_TO_EDGE), g.texParameteri(g.TEXTURE_2D, g.TEXTURE_WRAP_T, g.CLAMP_TO_EDGE), e
        }

        function s(e, t) {
            e = g.createShader(e);
            return g.shaderSource(e, t), g.compileShader(e), g.getShaderParameter(e, g.COMPILE_STATUS) ? e : (console.log("An error occurred compiling the shaders: " + g.getShaderInfoLog(e)), g.deleteShader(e), null)
        }

        function a(e, t) {
            g.viewport(0, 0, e, t), g.clearColor(0, 0, 0, 0), g.clearDepth(1), g.enable(g.DEPTH_TEST), g.depthFunc(g.LEQUAL), g.clear(g.COLOR_BUFFER_BIT | g.DEPTH_BUFFER_BIT);
            const r = B();
            e = r, i = (n = t = 1) / ((_ = -1) - t), a = 1 / ((s = -1) - n), p = 1 / ((u = .1) - (f = 100)), e[0] = -2 * i, e[1] = 0, e[2] = 0, e[3] = 0, e[4] = 0, e[5] = -2 * a, e[6] = 0, e[7] = 0, e[8] = 0, e[9] = 0, e[10] = 2 * p, e[11] = 0, e[12] = (_ + t) * i, e[13] = (n + s) * a, e[14] = (f + u) * p, e[15] = 1;
            var i, n, s, a, o, l, d, h, f, u, p, c, m, _ = B(), t = (A(_), B());
            i = t, n = T(0, 0, 0), s = T(0, 0, -1), a = T(0, 1, 0), f = n[0], u = n[1], n = n[2], p = a[0], e = a[1], a = a[2], c = s[0], m = s[1], s = s[2], Math.abs(f - c) < E && Math.abs(u - m) < E && Math.abs(n - s) < E ? A(i) : (s = n - s, o = e * (s *= h = 1 / Math.hypot(c = f - c, m = u - m, s)) - a * (m *= h), a = a * (c *= h) - p * s, p = p * m - e * c, (h = Math.hypot(o, a, p)) ? (o *= h = 1 / h, a *= h, p *= h) : p = a = o = 0, e = m * p - s * a, l = s * o - c * p, d = c * a - m * o, (h = Math.hypot(e, l, d)) ? (e *= h = 1 / h, l *= h, d *= h) : d = l = e = 0, i[0] = o, i[1] = e, i[2] = c, i[3] = 0, i[4] = a, i[5] = l, i[6] = m, i[7] = 0, i[8] = p, i[9] = d, i[10] = s, i[11] = 0, i[12] = -(o * f + a * u + p * n), i[13] = -(e * f + l * u + d * n), i[14] = -(c * f + m * u + s * n), i[15] = 1);
            {
                const e = 3, t = g.FLOAT, r = !1, v = 0, w = 0;
                g.bindBuffer(g.ARRAY_BUFFER, b.position), g.vertexAttribPointer(y.attribLocations.vertexPosition, 3, t, !1, 0, 0), g.enableVertexAttribArray(y.attribLocations.vertexPosition)
            }
            {
                const e = 2, t = g.FLOAT, r = !1, v = 0, w = 0;
                g.bindBuffer(g.ARRAY_BUFFER, b.texPosition), g.vertexAttribPointer(y.attribLocations.texturePosition, 2, t, !1, 0, 0), g.enableVertexAttribArray(y.attribLocations.texturePosition)
            }
            g.activeTexture(g.TEXTURE0 + 3), g.bindTexture(g.TEXTURE_2D, v), g.activeTexture(g.TEXTURE0 + 4), g.bindTexture(g.TEXTURE_2D, w), g.activeTexture(g.TEXTURE0 + 5), g.bindTexture(g.TEXTURE_2D, S), g.bindBuffer(g.ELEMENT_ARRAY_BUFFER, b.indices), g.useProgram(y.program), g.uniformMatrix4fv(y.uniformLocations.projectionMatrix, !1, r), g.uniformMatrix4fv(y.uniformLocations.modelMatrix, !1, _), g.uniformMatrix4fv(y.uniformLocations.viewMatrix, !1, t), g.uniform1i(y.uniformLocations.rgbatexture, 2), g.uniform1i(y.uniformLocations.ytexture, 3), g.uniform1i(y.uniformLocations.utexture, 4), g.uniform1i(y.uniformLocations.vtexture, 5), g.uniform1i(y.uniformLocations.isyuv, 1);
            {
                const e = 6, t = g.UNSIGNED_SHORT, y = 0;
                g.drawElements(g.TRIANGLES, 6, t, 0)
            }
        }

        return {
            render: function (e, t, r, i, n) {
                g.activeTexture(g.TEXTURE0), g.bindTexture(g.TEXTURE_2D, v), g.texImage2D(g.TEXTURE_2D, 0, g.LUMINANCE, e, t, 0, g.LUMINANCE, g.UNSIGNED_BYTE, r), g.activeTexture(g.TEXTURE1), g.bindTexture(g.TEXTURE_2D, w), g.texImage2D(g.TEXTURE_2D, 0, g.LUMINANCE, e / 2, t / 2, 0, g.LUMINANCE, g.UNSIGNED_BYTE, i), g.activeTexture(g.TEXTURE2), g.bindTexture(g.TEXTURE_2D, S), g.texImage2D(g.TEXTURE_2D, 0, g.LUMINANCE, e / 2, t / 2, 0, g.LUMINANCE, g.UNSIGNED_BYTE, n), a(e, t)
            }, renderYUV: function (e, t, r) {
                var i = r.slice(0, e * t), n = r.slice(e * t, e * t * 5 / 4), r = r.slice(e * t * 5 / 4, e * t * 3 / 2);
                g.activeTexture(g.TEXTURE0), g.bindTexture(g.TEXTURE_2D, v), g.texImage2D(g.TEXTURE_2D, 0, g.LUMINANCE, e, t, 0, g.LUMINANCE, g.UNSIGNED_BYTE, i), g.activeTexture(g.TEXTURE1), g.bindTexture(g.TEXTURE_2D, w), g.texImage2D(g.TEXTURE_2D, 0, g.LUMINANCE, e / 2, t / 2, 0, g.LUMINANCE, g.UNSIGNED_BYTE, n), g.activeTexture(g.TEXTURE2), g.bindTexture(g.TEXTURE_2D, S), g.texImage2D(g.TEXTURE_2D, 0, g.LUMINANCE, e / 2, t / 2, 0, g.LUMINANCE, g.UNSIGNED_BYTE, r), a(e, t)
            }, destroy: function () {
                g.deleteProgram(y.program), g.deleteBuffer(b.position), g.deleteBuffer(b.texPosition), g.deleteBuffer(b.indices), g.deleteTexture(i), g.deleteTexture(v), g.deleteTexture(w), g.deleteTexture(S), y = null, b = null, i = null, v = null, w = null, S = null
            }
        }
    };
    const ne = "fetch", se = "player", G = "mp4", S = "debug", k = "warn", ae = {
            playType: se,
            container: "",
            videoBuffer: 1e3,
            videoBufferDelay: 1e3,
            networkDelay: 1e4,
            isResize: !0,
            isFullResize: !1,
            isFlv: !1,
            isHls: !1,
            isFmp4: !1,
            isFmp4Private: !1,
            isWebrtc: !1,
            isWebrtcForZLM: !1,
            isWebrtcForSRS: !1,
            isWebrtcForOthers: !1,
            isNakedFlow: !1,
            isMpeg4: !1,
            debug: !1,
            debugLevel: k,
            debugUuid: "",
            isMulti: !0,
            multiIndex: -1,
            hotKey: !1,
            loadingTimeout: 10,
            heartTimeout: 10,
            timeout: 10,
            pageVisibilityHiddenTimeout: 300,
            loadingTimeoutReplay: !0,
            heartTimeoutReplay: !0,
            loadingTimeoutReplayTimes: 3,
            heartTimeoutReplayTimes: 3,
            heartTimeoutReplayUseLastFrameShow: !1,
            replayUseLastFrameShow: !1,
            supportDblclickFullscreen: !1,
            showBandwidth: !1,
            showPerformance: !1,
            mseCorrectTimeDuration: 20,
            keepScreenOn: !0,
            isNotMute: !1,
            hasAudio: !0,
            hasVideo: !0,
            operateBtns: {
                fullscreen: !1,
                screenshot: !1,
                play: !1,
                audio: !1,
                record: !1,
                ptz: !1,
                quality: !1,
                zoom: !1,
                close: !1,
                scale: !1,
                performance: !1,
                logSave: !1,
                aiFace: !1,
                aiObject: !1,
                fullscreenFn: null,
                fullscreenExitFn: null,
                screenshotFn: null,
                playFn: null,
                pauseFn: null,
                recordFn: null,
                recordStopFn: null
            },
            extendOperateBtns: [],
            contextmenuBtns: [],
            watermarkConfig: {},
            controlAutoHide: !1,
            hasControl: !1,
            loadingIcon: !0,
            loadingText: "",
            background: "",
            backgroundLoadingShow: !1,
            loadingBackground: "",
            loadingBackgroundWidth: 0,
            loadingBackgroundHeight: 0,
            decoder: "decoder-pro.js",
            decoderAudio: "decoder-pro-audio.js",
            decoderHard: "decoder-pro-hard.js",
            decoderWASM: "",
            isDecoderUseCDN: !1,
            url: "",
            rotate: 0,
            mirrorRotate: "none",
            aspectRatio: "default",
            playbackConfig: {
                playList: [],
                fps: "",
                showControl: !0,
                controlType: "normal",
                duration: 0,
                startTime: "",
                showRateBtn: !1,
                rateConfig: [],
                showPrecision: "",
                showPrecisionBtn: !0,
                isCacheBeforeDecodeForFpsRender: !1,
                uiUsePlaybackPause: !1,
                isPlaybackPauseClearCache: !0,
                isUseFpsRender: !1,
                isUseLocalCalculateTime: !1,
                localOneFrameTimestamp: 40,
                supportWheel: !1,
                useWCS: !1
            },
            qualityConfig: [],
            defaultStreamQuality: "",
            scaleConfig: ["拉伸", "缩放", "正常"],
            forceNoOffscreen: !0,
            hiddenAutoPause: !1,
            protocol: 2,
            demuxType: "flv",
            useWasm: !1,
            useWCS: !1,
            useSIMD: !0,
            wcsUseVideoRender: !0,
            wcsUseWebgl2Render: !0,
            wasmUseVideoRender: !0,
            mseUseCanvasRender: !1,
            hlsUseCanvasRender: !1,
            useMSE: !1,
            useOffscreen: !1,
            useWebGPU: !1,
            mseDecodeErrorReplay: !0,
            wcsDecodeErrorReplay: !0,
            wasmDecodeErrorReplay: !0,
            simdDecodeErrorReplay: !0,
            autoWasm: !0,
            webglAlignmentErrorReplay: !0,
            webglContextLostErrorReplay: !0,
            openWebglAlignment: !1,
            syncAudioAndVideo: !1,
            playbackDelayTime: 1e3,
            playbackFps: 25,
            playbackForwardMaxRateDecodeIFrame: 4,
            playbackCurrentTimeMove: !0,
            useVideoRender: !0,
            useCanvasRender: !1,
            networkDelayTimeoutReplay: !1,
            recordType: G,
            checkFirstIFrame: !0,
            nakedFlowFps: 25,
            audioEngine: null,
            isShowRecordingUI: !0,
            isShowZoomingUI: !0,
            useFaceDetector: !1,
            useObjectDetector: !1,
            ptzClickType: "click",
            ptzStopEmitDelay: .3,
            ptzZoomShow: !1,
            ptzApertureShow: !1,
            ptzFocusShow: !1,
            ptzMoreArrowShow: !1,
            weiXinInAndroidAudioBufferSize: 4800,
            isCrypto: !1,
            isSm4Crypto: !1,
            sm4CryptoKey: "",
            cryptoKey: "",
            cryptoIV: "",
            cryptoKeyUrl: "",
            autoResize: !1,
            useWebFullScreen: !1,
            ptsMaxDiff: 3600,
            aiFaceDetectWidth: 192,
            aiObjectDetectWidth: 192,
            videoRenderSupportScale: !0,
            mediaSourceTsIsMaxDiffReplay: !0,
            controlHtml: "",
            isH265: !1,
            isWebrtcH265: !1,
            supportLockScreenPlayAudio: !0,
            supportHls265: !1,
            isEmitSEI: !1,
            pauseAndNextPlayUseLastFrameShow: !1,
            demuxUseWorker: !1,
            playFailedAndPausedReplay: !1,
            videoElementPlayingFailedReplay: !0
        }, oe = "initVideo", H = "render", le = "playAudio", de = "videoCode", he = "videoCodec", V = "workerFetch",
        fe = "workerEnd", ue = "streamEnd", pe = "streamAbps", $ = "streamVbps", j = "streamDts", ce = "streamSuccess",
        W = "fetchError", me = "H264(AVC)", _e = "H265(HEVC)", ge = 6, ye = "AbortError";

    function be(e) {
        return e[0] >> 4 == 10 && 0 === e[1]
    }

    v(function (e) {
        var a, t, o, r, i;
        a = "undefined" != typeof window && void 0 !== window.document ? window.document : {}, t = e.exports, o = function () {
            for (var e, t = [["requestFullscreen", "exitFullscreen", "fullscreenElement", "fullscreenEnabled", "fullscreenchange", "fullscreenerror"], ["webkitRequestFullscreen", "webkitExitFullscreen", "webkitFullscreenElement", "webkitFullscreenEnabled", "webkitfullscreenchange", "webkitfullscreenerror"], ["webkitRequestFullScreen", "webkitCancelFullScreen", "webkitCurrentFullScreenElement", "webkitCancelFullScreen", "webkitfullscreenchange", "webkitfullscreenerror"], ["mozRequestFullScreen", "mozCancelFullScreen", "mozFullScreenElement", "mozFullScreenEnabled", "mozfullscreenchange", "mozfullscreenerror"], ["msRequestFullscreen", "msExitFullscreen", "msFullscreenElement", "msFullscreenEnabled", "MSFullscreenChange", "MSFullscreenError"]], r = 0, i = t.length, n = {}; r < i; r++) if ((e = t[r]) && e[1] in a) {
                for (r = 0; r < e.length; r++) n[t[0][r]] = e[r];
                return n
            }
            return !1
        }(), r = {change: o.fullscreenchange, error: o.fullscreenerror}, i = {
            request: function (n, s) {
                return new Promise(function (e, t) {
                    var r = function () {
                        this.off("change", r), e()
                    }.bind(this), i = (this.on("change", r), (n = n || a.documentElement)[o.requestFullscreen](s));
                    i instanceof Promise && i.then(r).catch(t)
                }.bind(this))
            }, exit: function () {
                return new Promise(function (e, t) {
                    var r, i;
                    this.isFullscreen ? (r = function () {
                        this.off("change", r), e()
                    }.bind(this), this.on("change", r), (i = a[o.exitFullscreen]()) instanceof Promise && i.then(r).catch(t)) : e()
                }.bind(this))
            }, toggle: function (e, t) {
                return this.isFullscreen ? this.exit() : this.request(e, t)
            }, onchange: function (e) {
                this.on("change", e)
            }, onerror: function (e) {
                this.on("error", e)
            }, on: function (e, t) {
                e = r[e];
                e && a.addEventListener(e, t, !1)
            }, off: function (e, t) {
                e = r[e];
                e && a.removeEventListener(e, t, !1)
            }, raw: o
        }, o ? (Object.defineProperties(i, {
            isFullscreen: {
                get: function () {
                    return Boolean(a[o.fullscreenElement])
                }
            }, element: {
                enumerable: !0, get: function () {
                    return a[o.fullscreenElement]
                }
            }, isEnabled: {
                enumerable: !0, get: function () {
                    return Boolean(a[o.fullscreenEnabled])
                }
            }
        }), t ? e.exports = i : window.screenfull = i) : t ? e.exports = {isEnabled: !1} : window.screenfull = {isEnabled: !1}
    }).isEnabled;
    const ve = [96e3, 88200, 64e3, 48e3, 44100, 32e3, 24e3, 22050, 16e3, 12e3, 11025, 8e3, 7350];

    function Y() {
        return (new Date).getTime()
    }

    function we() {
        return (performance && "function" == typeof performance.now ? performance : Date).now()
    }

    try {
        if ("object" == typeof WebAssembly && "function" == typeof WebAssembly.instantiate) {
            var C = new WebAssembly.Module(Uint8Array.of(0, 97, 115, 109, 1, 0, 0, 0));
            if (C instanceof WebAssembly.Module) new WebAssembly.Instance(C), WebAssembly.Instance
        }
    } catch (e) {
    }

    function q(e) {
        return null == e
    }

    function Se(e) {
        e.close()
    }

    function Ee(r, i) {
        let n = (r = i ? r.filter(e => e.type === i) : r)[0], s = null, e = 1;
        var t;
        if (0 < r.length && ((t = r[1]) && 1e5 < t.ts - n.ts && (n = t, e = 2)), n) for (let t = e; t < r.length; t++) {
            let e = r[t];
            !(e = i && e.type !== i ? null : e) || 1e3 <= e.ts - n.ts && r[t - 1].ts - n.ts < 1e3 && (s = t + 1)
        }
        return s
    }

    function K(e) {
        return e[0] >> 4 == 1 && 0 === e[1]
    }

    function X(e) {
        return !0 === e || "true" === e
    }

    function Ue(e) {
        return !0 !== e && "true" !== e
    }

    const F = Symbol(32), D = Symbol(16), P = Symbol(8);

    class Z {
        constructor(e) {
            this.g = e, this.consumed = 0, e && (this.need = e.next().value)
        }

        setG(e) {
            this.g = e, this.demand(e.next().value, !0)
        }

        consume() {
            this.buffer && this.consumed && (this.buffer.copyWithin(0, this.consumed), this.buffer = this.buffer.subarray(0, this.buffer.length - this.consumed), this.consumed = 0)
        }

        demand(e, t) {
            return t && this.consume(), this.need = e, this.flush()
        }

        read(r) {
            return e = this, l = function* () {
                return this.lastReadPromise && (yield this.lastReadPromise), this.lastReadPromise = new Promise((t, e) => {
                    this.reject = e, this.resolve = e => {
                        delete this.lastReadPromise, delete this.resolve, delete this.need, t(e)
                    }, this.demand(r, !0) || null == (e = this.pull) || e.call(this, r)
                })
            }, new (o = (o = a = void 0) || Promise)(function (r, t) {
                function i(e) {
                    try {
                        s(l.next(e))
                    } catch (e) {
                        t(e)
                    }
                }

                function n(e) {
                    try {
                        s(l.throw(e))
                    } catch (e) {
                        t(e)
                    }
                }

                function s(e) {
                    var t;
                    e.done ? r(e.value) : ((t = e.value) instanceof o ? t : new o(function (e) {
                        e(t)
                    })).then(i, n)
                }

                s((l = l.apply(e, a || [])).next())
            });
            var e, a, o, l
        }

        readU32() {
            return this.read(F)
        }

        readU16() {
            return this.read(D)
        }

        readU8() {
            return this.read(P)
        }

        close() {
            var e;
            this.g && this.g.return(), this.buffer && this.buffer.subarray(0, 0), null != (e = this.reject) && e.call(this, new Error("EOF")), delete this.lastReadPromise
        }

        flush() {
            if (this.buffer && this.need) {
                let e = null;
                const i = this.buffer.subarray(this.consumed);
                let t = 0;
                var r = e => i.length < (t = e);
                if ("number" == typeof this.need) {
                    if (r(this.need)) return;
                    e = i.subarray(0, t)
                } else if (this.need === F) {
                    if (r(4)) return;
                    e = i[0] << 24 | i[1] << 16 | i[2] << 8 | i[3]
                } else if (this.need === D) {
                    if (r(2)) return;
                    e = i[0] << 8 | i[1]
                } else if (this.need === P) {
                    if (r(1)) return;
                    e = i[0]
                } else if ("buffer" in this.need) {
                    if ("byteOffset" in this.need) {
                        if (r(this.need.byteLength - this.need.byteOffset)) return;
                        new Uint8Array(this.need.buffer, this.need.byteOffset).set(i.subarray(0, t)), e = this.need
                    } else if (this.g) return void this.g.throw(new Error("Unsupported type"))
                } else {
                    if (r(this.need.byteLength)) return;
                    new Uint8Array(this.need).set(i.subarray(0, t)), e = this.need
                }
                return this.consumed += t, this.g ? this.demand(this.g.next(e).value, !0) : this.resolve && this.resolve(e), e
            }
        }

        write(e) {
            if (e instanceof Uint8Array ? this.malloc(e.length).set(e) : "buffer" in e ? this.malloc(e.byteLength).set(new Uint8Array(e.buffer, e.byteOffset, e.byteLength)) : this.malloc(e.byteLength).set(new Uint8Array(e)), !this.g && !this.resolve) return new Promise(e => this.pull = e);
            this.flush()
        }

        writeU32(e) {
            this.malloc(4).set([e >> 24 & 255, e >> 16 & 255, e >> 8 & 255, 255 & e]), this.flush()
        }

        writeU16(e) {
            this.malloc(2).set([e >> 8 & 255, 255 & e]), this.flush()
        }

        writeU8(e) {
            this.malloc(1)[0] = e, this.flush()
        }

        malloc(e) {
            if (this.buffer) {
                var t = this.buffer.length, r = t + e;
                if (r <= this.buffer.buffer.byteLength - this.buffer.byteOffset) this.buffer = new Uint8Array(this.buffer.buffer, this.buffer.byteOffset, r); else {
                    const e = new Uint8Array(r);
                    e.set(this.buffer), this.buffer = e
                }
                return this.buffer.subarray(t, r)
            }
            return this.buffer = new Uint8Array(e), this.buffer
        }
    }

    Z.U32 = F, Z.U16 = D, Z.U8 = P;

    class xe {
        constructor(s) {
            this.log = function (e) {
                if (s._opt.debug && s._opt.debugLevel == S) {
                    for (var t = s._opt.debugUuid ? `[${s._opt.debugUuid}]` : "", r = arguments.length, i = new Array(1 < r ? r - 1 : 0), n = 1; n < r; n++) i[n - 1] = arguments[n];
                    console.log(`JbPro${t}[✅✅✅][${e}]`, ...i)
                }
            }, this.warn = function (e) {
                if (s._opt.debug && (s._opt.debugLevel == S || s._opt.debugLevel == k)) {
                    for (var t = s._opt.debugUuid ? `[${s._opt.debugUuid}]` : "", r = arguments.length, i = new Array(1 < r ? r - 1 : 0), n = 1; n < r; n++) i[n - 1] = arguments[n];
                    console.log(`JbPro${t}[❗❗❗][${e}]`, ...i)
                }
            }, this.error = function (e) {
                for (var t = s._opt.debugUuid ? `[${s._opt.debugUuid}]` : "", r = arguments.length, i = new Array(1 < r ? r - 1 : 0), n = 1; n < r; n++) i[n - 1] = arguments[n];
                console.error(`JbPro${t}[❌❌❌][${e}]`, ...i)
            }
        }
    }

    class J {
        constructor(e) {
            this._buffer = e, this._buffer_index = 0, this._total_bytes = e.byteLength, this._total_bits = 8 * e.byteLength, this._current_word = 0, this._current_word_bits_left = 0
        }

        destroy() {
            this._buffer = null
        }

        _fillCurrentWord() {
            var r = this._total_bytes - this._buffer_index;
            if (r <= 0) console.error("ExpGolomb: _fillCurrentWord() but no bytes available", this._total_bytes, this._buffer_index); else {
                let e = Math.min(4, r), t = new Uint8Array(4);
                t.set(this._buffer.subarray(this._buffer_index, this._buffer_index + e)), this._current_word = new DataView(t.buffer).getUint32(0, !1), this._buffer_index += e, this._current_word_bits_left = 8 * e
            }
        }

        readBits(e) {
            if (32 < e && console.error("ExpGolomb: readBits() bits exceeded max 32bits!"), e <= this._current_word_bits_left) return t = this._current_word >>> 32 - e, this._current_word <<= e, this._current_word_bits_left -= e, t;
            var t = this._current_word_bits_left ? this._current_word : 0,
                e = (t >>>= 32 - this._current_word_bits_left, e - this._current_word_bits_left),
                e = (this._fillCurrentWord(), Math.min(e, this._current_word_bits_left)),
                r = this._current_word >>> 32 - e;
            return this._current_word <<= e, this._current_word_bits_left -= e, t << e | r
        }

        readBool() {
            return 1 === this.readBits(1)
        }

        readByte() {
            return this.readBits(8)
        }

        _skipLeadingZero() {
            let e;
            for (e = 0; e < this._current_word_bits_left; e++) if (0 != (this._current_word & 2147483648 >>> e)) return this._current_word <<= e, this._current_word_bits_left -= e, e;
            return this._fillCurrentWord(), e + this._skipLeadingZero()
        }

        readUEG() {
            var e = this._skipLeadingZero();
            return this.readBits(e + 1) - 1
        }

        readSEG() {
            var e = this.readUEG();
            return 1 & e ? e + 1 >>> 1 : -1 * (e >>> 1)
        }
    }

    class I {
        static _ebsp2rbsp(e) {
            let t = e, r = t.byteLength, i = new Uint8Array(r), n = 0;
            for (let e = 0; e < r; e++) 2 <= e && 3 === t[e] && 0 === t[e - 1] && 0 === t[e - 2] || (i[n] = t[e], n++);
            return new Uint8Array(i.buffer, 0, n)
        }

        static parseSPS(e) {
            let t = I._ebsp2rbsp(e), r = new J(t);
            r.readByte();
            var e = r.readByte(), i = (r.readByte(), r.readByte());
            r.readUEG();
            let n = I.getProfileString(e), s = I.getLevelString(i), a = 1, o = 420, l = 8;
            if ((100 === e || 110 === e || 122 === e || 244 === e || 44 === e || 83 === e || 86 === e || 118 === e || 128 === e || 138 === e || 144 === e) && (3 === (a = r.readUEG()) && r.readBits(1), a <= 3 && (o = [0, 420, 422, 444][a]), l = r.readUEG() + 8, r.readUEG(), r.readBits(1), r.readBool())) {
                var d = 3 !== a ? 8 : 12;
                for (let e = 0; e < d; e++) r.readBool() && (e < 6 ? I._skipScalingList(r, 16) : I._skipScalingList(r, 64))
            }
            r.readUEG();
            i = r.readUEG();
            if (0 === i) r.readUEG(); else if (1 === i) {
                r.readBits(1), r.readSEG(), r.readSEG();
                var h = r.readUEG();
                for (let e = 0; e < h; e++) r.readSEG()
            }
            var e = r.readUEG(), i = (r.readBits(1), r.readUEG()), f = r.readUEG(), u = r.readBits(1);
            0 === u && r.readBits(1), r.readBits(1);
            let p = 0, c = 0, m = 0, _ = 0,
                g = (r.readBool() && (p = r.readUEG(), c = r.readUEG(), m = r.readUEG(), _ = r.readUEG()), 1), y = 1,
                b = 0, v = !0, w = 0, S = 0,
                E = (r.readBool() && (r.readBool() && (0 < (A = r.readByte()) && A < 16 ? (g = [1, 12, 10, 16, 40, 24, 20, 32, 80, 18, 15, 64, 160, 4, 3, 2][A - 1], y = [1, 11, 11, 11, 33, 11, 11, 11, 33, 11, 11, 33, 99, 3, 2, 1][A - 1]) : 255 === A && (g = r.readByte() << 8 | r.readByte(), y = r.readByte() << 8 | r.readByte())), r.readBool() && r.readBool(), r.readBool() && (r.readBits(4), r.readBool() && r.readBits(24)), r.readBool() && (r.readUEG(), r.readUEG()), r.readBool() && (A = r.readBits(32), B = r.readBits(32), v = r.readBool(), w = B, S = 2 * A, b = w / S)), 1),
                U = (1 === g && 1 === y || (E = g / y), 0), x = 0;
            x = 0 === a ? (U = 1, 2 - u) : (U = 3 === a ? 1 : 2, (1 === a ? 2 : 1) * (2 - u));
            var B = 16 * (i + 1), A = 16 * (f + 1) * (2 - u),
                i = (B -= (p + c) * U, A -= (m + _) * x, Math.ceil(B * E));
            return r.destroy(), r = null, {
                profile_string: n,
                level_string: s,
                bit_depth: l,
                ref_frames: e,
                chroma_format: o,
                chroma_format_string: I.getChromaFormatString(o),
                frame_rate: {fixed: v, fps: b, fps_den: S, fps_num: w},
                sar_ratio: {width: g, height: y},
                codec_size: {width: B, height: A},
                present_size: {width: i, height: A}
            }
        }

        static parseSPS$2(e) {
            let r = e.subarray(1, 4), i = "avc1.";
            for (let t = 0; t < 3; t++) {
                let e = r[t].toString(16);
                e.length < 2 && (e = "0" + e), i += e
            }
            let t = I._ebsp2rbsp(e), n = new J(t);
            n.readByte();
            var e = n.readByte(), s = (n.readByte(), n.readByte());
            n.readUEG();
            let a = I.getProfileString(e), o = I.getLevelString(s), l = 1, d = 420, h = 8, f = 8;
            if ((100 === e || 110 === e || 122 === e || 244 === e || 44 === e || 83 === e || 86 === e || 118 === e || 128 === e || 138 === e || 144 === e) && (3 === (l = n.readUEG()) && n.readBits(1), l <= 3 && (d = [0, 420, 422, 444][l]), h = n.readUEG() + 8, f = n.readUEG() + 8, n.readBits(1), n.readBool())) {
                var u = 3 !== l ? 8 : 12;
                for (let e = 0; e < u; e++) n.readBool() && (e < 6 ? I._skipScalingList(n, 16) : I._skipScalingList(n, 64))
            }
            n.readUEG();
            var p = n.readUEG();
            if (0 === p) n.readUEG(); else if (1 === p) {
                n.readBits(1), n.readSEG(), n.readSEG();
                var c = n.readUEG();
                for (let e = 0; e < c; e++) n.readSEG()
            }
            var p = n.readUEG(), m = (n.readBits(1), n.readUEG()), _ = n.readUEG(), g = n.readBits(1);
            0 === g && n.readBits(1), n.readBits(1);
            let y = 0, b = 0, v = 0, w = 0,
                S = (n.readBool() && (y = n.readUEG(), b = n.readUEG(), v = n.readUEG(), w = n.readUEG()), 1), E = 1,
                U = 0, x = !0, B = 0, A = 0,
                T = (n.readBool() && (n.readBool() && (0 < (D = n.readByte()) && D < 16 ? (S = [1, 12, 10, 16, 40, 24, 20, 32, 80, 18, 15, 64, 160, 4, 3, 2][D - 1], E = [1, 11, 11, 11, 33, 11, 11, 11, 33, 11, 11, 33, 99, 3, 2, 1][D - 1]) : 255 === D && (S = n.readByte() << 8 | n.readByte(), E = n.readByte() << 8 | n.readByte())), n.readBool() && n.readBool(), n.readBool() && (n.readBits(4), n.readBool() && n.readBits(24)), n.readBool() && (n.readUEG(), n.readUEG()), n.readBool() && (D = n.readBits(32), F = n.readBits(32), x = n.readBool(), B = F, A = 2 * D, U = B / A)), 1),
                k = (1 === S && 1 === E || (T = S / E), 0), C = 0;
            C = 0 === l ? (k = 1, 2 - g) : (k = 3 === l ? 1 : 2, (1 === l ? 2 : 1) * (2 - g));
            var F = 16 * (m + 1), D = 16 * (_ + 1) * (2 - g),
                m = (F -= (y + b) * k, D -= (v + w) * C, Math.ceil(F * T));
            return n.destroy(), n = null, {
                codec_mimetype: i,
                profile_idc: e,
                level_idc: s,
                profile_string: a,
                level_string: o,
                chroma_format_idc: l,
                bit_depth: h,
                bit_depth_luma: h,
                bit_depth_chroma: f,
                ref_frames: p,
                chroma_format: d,
                chroma_format_string: I.getChromaFormatString(d),
                frame_rate: {fixed: x, fps: U, fps_den: A, fps_num: B},
                sar_ratio: {width: S, height: E},
                codec_size: {width: F, height: D},
                present_size: {width: m, height: D}
            }
        }

        static _skipScalingList(t, r) {
            let i = 8, n = 8, s;
            for (let e = 0; e < r; e++) 0 !== n && (s = t.readSEG(), n = (i + s + 256) % 256), i = 0 === n ? i : n
        }

        static getProfileString(e) {
            switch (e) {
                case 66:
                    return "Baseline";
                case 77:
                    return "Main";
                case 88:
                    return "Extended";
                case 100:
                    return "High";
                case 110:
                    return "High10";
                case 122:
                    return "High422";
                case 244:
                    return "High444";
                default:
                    return "Unknown"
            }
        }

        static getLevelString(e) {
            return (e / 10).toFixed(1)
        }

        static getChromaFormatString(e) {
            switch (e) {
                case 420:
                    return "4:2:0";
                case 422:
                    return "4:2:2";
                case 444:
                    return "4:4:4";
                default:
                    return "Unknown"
            }
        }
    }

    class L {
        constructor(e) {
            this.buffer = e, this.buflen = e.length, this.bufpos = 0, this.bufoff = 0, this.iserro = !1
        }

        read(e) {
            let t = 0, r;
            for (; e;) {
                if (e < 0 || this.bufpos >= this.buflen) return this.iserro = !0, 0;
                this.iserro = !1, r = 8 < this.bufoff + e ? 8 - this.bufoff : e, t = (t <<= r) + (this.buffer[this.bufpos] >> 8 - this.bufoff - r & 255 >> 8 - r), this.bufoff += r, e -= r, 8 == this.bufoff && (this.bufpos++, this.bufoff = 0)
            }
            return t
        }

        look(e) {
            var t = this.bufpos, r = this.bufoff, e = this.read(e);
            return this.bufpos = t, this.bufoff = r, e
        }

        read_golomb() {
            let e;
            for (e = 0; 0 === this.read(1) && !this.iserro; e++) ;
            return (1 << e) + this.read(e) - 1
        }
    }

    function Be(r) {
        const n = {}, i = new DataView(r.buffer);
        let e = i.getUint8(0), t = i.getUint8(1);
        if (i.getUint8(2), i.getUint8(3), 1 !== e || 0 === t) return {};
        var s = 1 + (3 & i.getUint8(4));
        if (3 != s && 4 != s) return {};
        var a = 31 & i.getUint8(5);
        if (0 == a) return {};
        let o = 6;
        for (let t = 0; t < a; t++) {
            var l = i.getUint16(o, !1);
            if (o += 2, 0 !== l) {
                let e = new Uint8Array(r.buffer, o, l);
                o += l;
                l = I.parseSPS(e);
                if (0 === t) {
                    n.sps = e, n.timescale = 1e3, n.codecWidth = l.codec_size.width, n.codecHeight = l.codec_size.height, n.presentWidth = l.present_size.width, n.presentHeight = l.present_size.height, n.profile = l.profile_string, n.level = l.level_string, n.bitDepth = l.bit_depth, n.chromaFormat = l.chroma_format, n.sarRatio = l.sar_ratio, n.frameRate = l.frame_rate, !1 !== l.frame_rate.fixed && 0 !== l.frame_rate.fps_num && 0 !== l.frame_rate.fps_den || (n.frameRate = {
                        fixed: !0,
                        fps: 23.976,
                        fps_num: 23976,
                        fps_den: 1e3
                    });
                    var l = n.frameRate.fps_den, d = n.frameRate.fps_num;
                    n.refSampleDuration = n.timescale * (l / d);
                    let r = e.subarray(1, 4), i = "avc1.";
                    for (let t = 0; t < 3; t++) {
                        let e = r[t].toString(16);
                        e.length < 2 && (e = "0" + e), i += e
                    }
                    n.codec = i
                }
            }
        }
        var h = i.getUint8(o);
        if (0 === h) return {};
        o++;
        for (let e = 0; e < h; e++) {
            var f, u = i.getUint16(o, !1);
            o += 2, 0 !== u && (f = new Uint8Array(r.buffer, o, u), o += u, n.pps = f)
        }
        if (n.videoType = "avc", n.sps) {
            const r = n.sps.byteLength, i = new Uint8Array([r >>> 24 & 255, r >>> 16 & 255, r >>> 8 & 255, 255 & r]),
                e = new Uint8Array(r + 4);
            e.set(i, 0), e.set(n.sps, 4), n.sps = e
        }
        if (n.pps) {
            const r = n.pps.byteLength, i = new Uint8Array([r >>> 24 & 255, r >>> 16 & 255, r >>> 8 & 255, 255 & r]),
                e = new Uint8Array(r + 4);
            e.set(i, 0), e.set(n.pps, 4), n.pps = e
        }
        return n
    }

    function Ae(e) {
        var {sps: e, pps: t} = e;
        const r = [23, 0, 0, 0, 0, 1, 66, 0, 30, 255];
        return r[0] = 23, r[6] = e[1], r[7] = e[2], r[8] = e[3], r[10] = 225, r[11] = e.byteLength >> 8 & 255, r[12] = 255 & e.byteLength, r.push(...e, 1, t.byteLength >> 8 & 255, 255 & t.byteLength, ...t), new Uint8Array(r)
    }

    function Te(e, t) {
        let r = [];
        r[0] = t ? 23 : 39, r[1] = 1, r[2] = 0, r[3] = 0, r[4] = 0;
        const i = new Uint8Array(r.length + e.byteLength);
        return i.set(r, 0), i.set(e, r.length), i
    }

    function Q(e) {
        return 31 & e[0]
    }

    function ke(e) {
        return e === ge
    }

    function Ce(e) {
        return 7 !== e && 8 !== e && !ke(e)
    }

    const Fe = e => {
        let t = e, r = t.byteLength, i = new Uint8Array(r), n = 0;
        for (let e = 0; e < r; e++) 2 <= e && 3 === t[e] && 0 === t[e - 1] && 0 === t[e - 2] || (i[n] = t[e], n++);
        return new Uint8Array(i.buffer, 0, n)
    };

    function De(r, e) {
        var i = 1 < arguments.length && void 0 !== e ? e : 4;
        if (!(r.length < 4)) {
            const n = r.length, s = [];
            let e, t = 0;
            for (; t + i < n;) if (e = function (e, t) {
                return (e[t = 1 < arguments.length && void 0 !== t ? t : 0] << 24 >>> 0) + (e[t + 1] << 16) + (e[t + 2] << 8) + (e[t + 3] || 0)
            }(r, t), 3 === i && (e >>>= 8), t += i, e) {
                if (t + e > n) break;
                s.push(r.subarray(t, t + e)), t += e
            }
            return s
        }
    }

    function ee(e) {
        const t = e.byteLength, r = new Uint8Array(4),
            i = (r[0] = t >>> 24 & 255, r[1] = t >>> 16 & 255, r[2] = t >>> 8 & 255, r[3] = 255 & t, new Uint8Array(t + 4));
        return i.set(r, 0), i.set(e, 4), i
    }

    function Ie(e) {
        let n = {width: 0, height: 0, profile: 0, level: 0};
        e = e.slice(5);
        do {
            let t = {};
            if (e.length < 23) {
                console.warn("parseHEVCDecoderConfigurationRecord$2", `arrayBuffer.length ${e.length} < 23`);
                break
            }
            if (t.configurationVersion = e[0], 1 != t.configurationVersion) break;
            t.general_profile_space = e[1] >> 6 & 3, t.general_tier_flag = e[1] >> 5 & 1, t.general_profile_idc = 31 & e[1], t.general_profile_compatibility_flags = e[2] << 24 | e[3] << 16 | e[4] << 8 | e[5], t.general_constraint_indicator_flags = e[6] << 24 | e[7] << 16 | e[8] << 8 | e[9], t.general_constraint_indicator_flags = t.general_constraint_indicator_flags << 16 | e[10] << 8 | e[11], t.general_level_idc = e[12], t.min_spatial_segmentation_idc = (15 & e[13]) << 8 | e[14], t.parallelismType = 3 & e[15], t.chromaFormat = 3 & e[16], t.bitDepthLumaMinus8 = 7 & e[17], t.bitDepthChromaMinus8 = 7 & e[18], t.avgFrameRate = e[19] << 8 | e[20], t.constantFrameRate = e[21] >> 6 & 3, t.numTemporalLayers = e[21] >> 3 & 7, t.temporalIdNested = e[21] >> 2 & 1, t.lengthSizeMinusOne = 3 & e[21];
            let r = e[22], i = e.slice(23);
            for (let e = 0; e < r && !(i.length < 3); e++) {
                var s = 63 & i[0], a = i[1] << 8 | i[2];
                i = i.slice(3);
                for (let e = 0; e < a && !(i.length < 2); e++) {
                    var o = i[0] << 8 | i[1];
                    if (i.length < 2 + o) break;
                    if (i = i.slice(2), 33 == s) {
                        let e = new Uint8Array(o);
                        e.set(i.slice(0, o), 0), t.psps = function (e) {
                            let t = {}, r = e.length, i = [], n = new L(e);
                            n.read(1), n.read(6), n.read(6), n.read(3);
                            for (let e = 2; e < r; e++) e + 2 < r && 3 == n.look(24) ? (i.push(n.read(8)), i.push(n.read(8)), e += 2, n.read(8)) : i.push(n.read(8));
                            let s = new Uint8Array(i), a = new L(s);
                            {
                                var o;
                                t.sps_video_parameter_set_id = a.read(4), t.sps_max_sub_layers_minus1 = a.read(3), t.sps_temporal_id_nesting_flag = a.read(1), t.profile_tier_level = function (t, r) {
                                    let i = {};
                                    i.profile_space = t.read(2), i.tier_flag = t.read(1), i.profile_idc = t.read(5), i.profile_compatibility_flags = t.read(32), i.general_progressive_source_flag = t.read(1), i.general_interlaced_source_flag = t.read(1), i.general_non_packed_constraint_flag = t.read(1), i.general_frame_only_constraint_flag = t.read(1), t.read(32), t.read(12), i.level_idc = t.read(8), i.sub_layer_profile_present_flag = [], i.sub_layer_level_present_flag = [];
                                    for (let e = 0; e < r; e++) i.sub_layer_profile_present_flag[e] = t.read(1), i.sub_layer_level_present_flag[e] = t.read(1);
                                    if (0 < r) for (let e = r; e < 8; e++) t.read(2);
                                    i.sub_layer_profile_space = [], i.sub_layer_tier_flag = [], i.sub_layer_profile_idc = [], i.sub_layer_profile_compatibility_flag = [], i.sub_layer_progressive_source_flag = [], i.sub_layer_interlaced_source_flag = [], i.sub_layer_non_packed_constraint_flag = [], i.sub_layer_frame_only_constraint_flag = [], i.sub_layer_level_idc = [];
                                    for (let e = 0; e < r; e++) i.sub_layer_profile_present_flag[e] && (i.sub_layer_profile_space[e] = t.read(2), i.sub_layer_tier_flag[e] = t.read(1), i.sub_layer_profile_idc[e] = t.read(5), i.sub_layer_profile_compatibility_flag[e] = t.read(32), i.sub_layer_progressive_source_flag[e] = t.read(1), i.sub_layer_interlaced_source_flag[e] = t.read(1), i.sub_layer_non_packed_constraint_flag[e] = t.read(1), i.sub_layer_frame_only_constraint_flag[e] = t.read(1), t.read(32), t.read(12)), i.sub_layer_level_present_flag[e] ? i.sub_layer_level_idc[e] = t.read(8) : i.sub_layer_level_idc[e] = 1;
                                    return i
                                }(a, t.sps_max_sub_layers_minus1), t.sps_seq_parameter_set_id = a.read_golomb(), t.chroma_format_idc = a.read_golomb(), 3 == t.chroma_format_idc ? t.separate_colour_plane_flag = a.read(1) : t.separate_colour_plane_flag = 0, t.pic_width_in_luma_samples = a.read_golomb(), t.pic_height_in_luma_samples = a.read_golomb(), t.conformance_window_flag = a.read(1), t.conformance_window_flag ? (e = 1 + (t.chroma_format_idc < 2), o = 1 + (t.chroma_format_idc < 3), t.conf_win_left_offset = a.read_golomb() * o, t.conf_win_right_offset = a.read_golomb() * o, t.conf_win_top_offset = a.read_golomb() * e, t.conf_win_bottom_offset = a.read_golomb() * e) : (t.conf_win_left_offset = 0, t.conf_win_right_offset = 0, t.conf_win_top_offset = 0, t.conf_win_bottom_offset = 0)
                            }
                            return t
                        }(e, t), n.profile = t.general_profile_idc, n.level = t.general_level_idc / 30, n.width = t.psps.pic_width_in_luma_samples - (t.psps.conf_win_left_offset + t.psps.conf_win_right_offset), n.height = t.psps.pic_height_in_luma_samples - (t.psps.conf_win_top_offset + t.psps.conf_win_bottom_offset)
                    }
                    i = i.slice(o)
                }
            }
        } while (0);
        return n.codecWidth = n.width || 1920, n.codecHeight = n.height || 1080, n.presentHeight = n.codecHeight, n.presentWidth = n.codecWidth, n.timescale = 1e3, n.refSampleDuration = 1e3 / 23976 * 1e3, n.videoType = "hevc", n
    }

    function Pe(e) {
        var {vps: e, pps: t, sps: r} = e, i = {configurationVersion: 1}, n = (e => {
            let t = Fe(e), r = new J(t);
            return r.readByte(), r.readByte(), r.readBits(4), r.readBits(2), r.readBits(6), {
                num_temporal_layers: r.readBits(3) + 1,
                temporal_id_nested: r.readBool()
            }
        })(e), s = (e => {
            let t = Fe(e), s = new J(t), r = (s.readByte(), s.readByte(), 0), i = 0, n = 0, a = 0;
            s.readBits(4);
            var o = s.readBits(3);
            s.readBool();
            let l = s.readBits(2), d = s.readBool(), h = s.readBits(5), f = s.readByte(), u = s.readByte(),
                p = s.readByte(), c = s.readByte(), m = s.readByte(), _ = s.readByte(), g = s.readByte(),
                z = s.readByte(), R = s.readByte(), M = s.readByte(), y = s.readByte(), b = [], N = [];
            for (let e = 0; e < o; e++) b.push(s.readBool()), N.push(s.readBool());
            if (0 < o) for (let e = o; e < 8; e++) s.readBits(2);
            for (let e = 0; e < o; e++) b[e] && (s.readByte(), s.readByte(), s.readByte(), s.readByte(), s.readByte(), s.readByte(), s.readByte(), s.readByte(), s.readByte(), s.readByte(), s.readByte()), b[e] && s.readByte();
            s.readUEG();
            var v, e = s.readUEG(), O = (3 == e && s.readBits(1), s.readUEG()), G = s.readUEG(),
                w = (s.readBool() && (r += s.readUEG(), i += s.readUEG(), n += s.readUEG(), a += s.readUEG()), s.readUEG()),
                H = s.readUEG(), V = s.readUEG();
            for (let e = s.readBool() ? 0 : o; e <= o; e++) s.readUEG(), s.readUEG(), s.readUEG();
            if (s.readUEG(), s.readUEG(), s.readUEG(), s.readUEG(), s.readUEG(), s.readUEG(), s.readBool() && s.readBool()) for (let t = 0; t < 4; t++) for (let e = 0; e < (3 === t ? 2 : 6); e++) if (s.readBool()) {
                var $ = Math.min(64, 1 << 4 + (t << 1));
                1 < t && s.readSEG();
                for (let e = 0; e < $; e++) s.readSEG()
            } else s.readUEG();
            s.readBool(), s.readBool(), s.readBool() && (s.readByte(), s.readUEG(), s.readUEG(), s.readBool());
            let S = s.readUEG(), E = 0;
            for (let t = 0; t < S; t++) {
                let e = !1;
                if (e = 0 !== t ? s.readBool() : e) {
                    t === S && s.readUEG(), s.readBool(), s.readUEG();
                    let r = 0;
                    for (let e = 0; e <= E; e++) {
                        let e = s.readBool(), t = !1;
                        e || (t = s.readBool()), (e || t) && r++
                    }
                    E = r
                } else {
                    var U = s.readUEG(), x = s.readUEG();
                    E = U + x;
                    for (let e = 0; e < U; e++) s.readUEG(), s.readBool();
                    for (let e = 0; e < x; e++) s.readUEG(), s.readBool()
                }
            }
            if (s.readBool()) {
                var j = s.readUEG();
                for (let e = 0; e < j; e++) {
                    for (let e = 0; e < V + 4; e++) s.readBits(1);
                    s.readBits(1)
                }
            }
            let B = 0, A = 1, T = 1, k = !1, C = 1, F = 1;
            if (s.readBool(), s.readBool(), s.readBool()) {
                if (s.readBool() && (0 < (v = s.readByte()) && v < 16 ? (A = [1, 12, 10, 16, 40, 24, 20, 32, 80, 18, 15, 64, 160, 4, 3, 2][v - 1], T = [1, 11, 11, 11, 33, 11, 11, 11, 33, 11, 11, 33, 99, 3, 2, 1][v - 1]) : 255 === v && (A = s.readBits(16), T = s.readBits(16))), s.readBool() && s.readBool(), s.readBool() && (s.readBits(3), s.readBool(), s.readBool() && (s.readByte(), s.readByte(), s.readByte())), s.readBool() && (s.readUEG(), s.readUEG()), s.readBool(), s.readBool(), s.readBool(), s.readBool() && (r += s.readUEG(), i += s.readUEG(), n += s.readUEG(), a += s.readUEG()), s.readBool() && (C = s.readBits(32), F = s.readBits(32), s.readBool() && (s.readUEG(), s.readBool()))) {
                    let r, i, n = !1;
                    r = s.readBool(), i = s.readBool(), (r || i) && ((n = s.readBool()) && (s.readByte(), s.readBits(5), s.readBool(), s.readBits(5)), s.readBits(4), s.readBits(4), n && s.readBits(4), s.readBits(5), s.readBits(5), s.readBits(5));
                    for (let e = 0; e <= o; e++) {
                        var D = s.readBool();
                        k = D;
                        let e = !1, t = !1;
                        if ((e = D ? e : s.readBool()) ? s.readSEG() : t = s.readBool(), t || (cpbcnt = s.readUEG() + 1), r) for (let e = 0; e < 1; e++) s.readUEG(), s.readUEG(), n && (s.readUEG(), s.readUEG());
                        if (i) for (let e = 0; e < 1; e++) s.readUEG(), s.readUEG(), n && (s.readUEG(), s.readUEG())
                    }
                }
                s.readBool() && (s.readBool(), s.readBool(), s.readBool(), B = s.readUEG(), s.readUEG(), s.readUEG(), s.readUEG(), s.readUEG())
            }
            s.readBool();
            let W = `hvc1.${h}.1.L${y}.B0`, I = O, P = G, L = 1;
            return 1 !== A && 1 !== T && (L = A / T), s.destroy(), s = null, {
                codec_mimetype: W,
                level_string: (y / 30).toFixed(1),
                profile_idc: h,
                bit_depth: w + 8,
                ref_frames: 1,
                chroma_format: e,
                chroma_format_string: (e => {
                    switch (e) {
                        case 0:
                            return "4:0:0";
                        case 1:
                            return "4:2:0";
                        case 2:
                            return "4:2:2";
                        case 3:
                            return "4:4:4";
                        default:
                            return "Unknown"
                    }
                })(e),
                general_level_idc: y,
                general_profile_space: l,
                general_tier_flag: d,
                general_profile_idc: h,
                general_profile_compatibility_flags_1: f,
                general_profile_compatibility_flags_2: u,
                general_profile_compatibility_flags_3: p,
                general_profile_compatibility_flags_4: c,
                general_constraint_indicator_flags_1: m,
                general_constraint_indicator_flags_2: _,
                general_constraint_indicator_flags_3: g,
                general_constraint_indicator_flags_4: z,
                general_constraint_indicator_flags_5: R,
                general_constraint_indicator_flags_6: M,
                min_spatial_segmentation_idc: B,
                constant_frame_rate: 0,
                chroma_format_idc: e,
                bit_depth_luma_minus8: w,
                bit_depth_chroma_minus8: H,
                frame_rate: {fixed: k, fps: F / C, fps_den: C, fps_num: F},
                sar_ratio: {width: A, height: T},
                codec_size: {width: I, height: P},
                present_size: {width: I * L, height: P}
            }
        })(r), a = (e => {
            let t = Fe(e), r = new J(t),
                i = (r.readByte(), r.readByte(), r.readUEG(), r.readUEG(), r.readBool(), r.readBool(), r.readBits(3), r.readBool(), r.readBool(), r.readUEG(), r.readUEG(), r.readSEG(), r.readBool(), r.readBool(), r.readBool() && r.readUEG(), r.readSEG(), r.readSEG(), r.readBool(), r.readBool(), r.readBool(), r.readBool(), r.readBool()),
                n = r.readBool(), s = 1;
            return n && i ? s = 0 : n ? s = 3 : i && (s = 2), {parallelismType: s}
        })(t), i = Object.assign(i, n, s, a);
        let o = 23 + (5 + e.byteLength) + (5 + r.byteLength) + (5 + t.byteLength), l = new Uint8Array(o);
        l[0] = 1, l[1] = (3 & i.general_profile_space) << 6 | (i.general_tier_flag ? 1 : 0) << 5 | 31 & i.general_profile_idc, l[2] = i.general_profile_compatibility_flags_1 || 0, l[3] = i.general_profile_compatibility_flags_2 || 0, l[4] = i.general_profile_compatibility_flags_3 || 0, l[5] = i.general_profile_compatibility_flags_4 || 0, l[6] = i.general_constraint_indicator_flags_1 || 0, l[7] = i.general_constraint_indicator_flags_2 || 0, l[8] = i.general_constraint_indicator_flags_3 || 0, l[9] = i.general_constraint_indicator_flags_4 || 0, l[10] = i.general_constraint_indicator_flags_5 || 0, l[11] = i.general_constraint_indicator_flags_6 || 0, l[12] = 60, l[13] = 240 | (3840 & i.min_spatial_segmentation_idc) >> 8, l[14] = 255 & i.min_spatial_segmentation_idc, l[15] = 252 | 3 & i.parallelismType, l[16] = 252 | 3 & i.chroma_format_idc, l[17] = 248 | 7 & i.bit_depth_luma_minus8, l[18] = 248 | 7 & i.bit_depth_chroma_minus8, l[19] = 0, l[20] = 0, l[21] = (3 & i.constant_frame_rate) << 6 | (7 & i.num_temporal_layers) << 3 | (i.temporal_id_nested ? 1 : 0) << 2 | 3, l[22] = 3, l[23] = 160, l[24] = 0, l[25] = 1, l[26] = (65280 & e.byteLength) >> 8, l[27] = (255 & e.byteLength) >> 0, l.set(e, 28), l[23 + (5 + e.byteLength) + 0] = 161, l[23 + (5 + e.byteLength) + 1] = 0, l[23 + (5 + e.byteLength) + 2] = 1, l[23 + (5 + e.byteLength) + 3] = (65280 & r.byteLength) >> 8, l[23 + (5 + e.byteLength) + 4] = (255 & r.byteLength) >> 0, l.set(r, 23 + (5 + e.byteLength) + 5), l[23 + (5 + e.byteLength + 5 + r.byteLength) + 0] = 162, l[23 + (5 + e.byteLength + 5 + r.byteLength) + 1] = 0, l[23 + (5 + e.byteLength + 5 + r.byteLength) + 2] = 1, l[23 + (5 + e.byteLength + 5 + r.byteLength) + 3] = (65280 & t.byteLength) >> 8, l[23 + (5 + e.byteLength + 5 + r.byteLength) + 4] = (255 & t.byteLength) >> 0, l.set(t, 23 + (5 + e.byteLength + 5 + r.byteLength) + 5);
        const d = [28, 0, 0, 0, 0], h = new Uint8Array(d.length + l.byteLength);
        return h.set(d, 0), h.set(l, d.length), h
    }

    function Le(e, t) {
        let r = [];
        r[0] = t ? 28 : 44, r[1] = 1, r[2] = 0, r[3] = 0, r[4] = 0;
        const i = new Uint8Array(r.length + e.byteLength);
        return i.set(r, 0), i.set(e, r.length), i
    }

    function te(e) {
        return (126 & e[0]) >> 1
    }

    function ze(e) {
        return !(32 <= e && e <= 40)
    }

    function Re(e) {
        return 16 <= e && e <= 21
    }

    function z(e) {
        return parseInt(e) === e
    }

    function R(e) {
        if (z(e.length)) {
            for (var t = 0; t < e.length; t++) if (!z(e[t]) || e[t] < 0 || 255 < e[t]) return;
            return 1
        }
    }

    function s(e, t) {
        if (e.buffer && "Uint8Array" === e.name) return e = t ? e.slice ? e.slice() : Array.prototype.slice.call(e) : e;
        if (Array.isArray(e)) {
            if (R(e)) return new Uint8Array(e);
            throw new Error("Array contains invalid value: " + e)
        }
        if (z(e.length) && R(e)) return new Uint8Array(e);
        throw new Error("unsupported array-like object")
    }

    function l(e) {
        return new Uint8Array(e)
    }

    function a(e, t, r, i, n) {
        null == i && null == n || (e = e.slice ? e.slice(i, n) : Array.prototype.slice.call(e, i, n)), t.set(e, r)
    }

    var M, g = {
            toBytes: function (e) {
                var t = [], r = 0;
                for (e = encodeURI(e); r < e.length;) {
                    var i = e.charCodeAt(r++);
                    37 === i ? (t.push(parseInt(e.substr(r, 2), 16)), r += 2) : t.push(i)
                }
                return s(t)
            }, fromBytes: function (e) {
                for (var t = [], r = 0; r < e.length;) {
                    var i = e[r];
                    i < 128 ? (t.push(String.fromCharCode(i)), r++) : 191 < i && i < 224 ? (t.push(String.fromCharCode((31 & i) << 6 | 63 & e[r + 1])), r += 2) : (t.push(String.fromCharCode((15 & i) << 12 | (63 & e[r + 1]) << 6 | 63 & e[r + 2])), r += 3)
                }
                return t.join("")
            }
        }, y = (M = "0123456789abcdef", {
            toBytes: function (e) {
                for (var t = [], r = 0; r < e.length; r += 2) t.push(parseInt(e.substr(r, 2), 16));
                return t
            }, fromBytes: function (e) {
                for (var t = [], r = 0; r < e.length; r++) {
                    var i = e[r];
                    t.push(M[(240 & i) >> 4] + M[15 & i])
                }
                return t.join("")
            }
        }), N = {16: 10, 24: 12, 32: 14},
        O = [1, 2, 4, 8, 16, 32, 64, 128, 27, 54, 108, 216, 171, 77, 154, 47, 94, 188, 99, 198, 151, 53, 106, 212, 179, 125, 250, 239, 197, 145],
        f = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22],
        d = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125],
        Me = [3328402341, 4168907908, 4000806809, 4135287693, 4294111757, 3597364157, 3731845041, 2445657428, 1613770832, 33620227, 3462883241, 1445669757, 3892248089, 3050821474, 1303096294, 3967186586, 2412431941, 528646813, 2311702848, 4202528135, 4026202645, 2992200171, 2387036105, 4226871307, 1101901292, 3017069671, 1604494077, 1169141738, 597466303, 1403299063, 3832705686, 2613100635, 1974974402, 3791519004, 1033081774, 1277568618, 1815492186, 2118074177, 4126668546, 2211236943, 1748251740, 1369810420, 3521504564, 4193382664, 3799085459, 2883115123, 1647391059, 706024767, 134480908, 2512897874, 1176707941, 2646852446, 806885416, 932615841, 168101135, 798661301, 235341577, 605164086, 461406363, 3756188221, 3454790438, 1311188841, 2142417613, 3933566367, 302582043, 495158174, 1479289972, 874125870, 907746093, 3698224818, 3025820398, 1537253627, 2756858614, 1983593293, 3084310113, 2108928974, 1378429307, 3722699582, 1580150641, 327451799, 2790478837, 3117535592, 0, 3253595436, 1075847264, 3825007647, 2041688520, 3059440621, 3563743934, 2378943302, 1740553945, 1916352843, 2487896798, 2555137236, 2958579944, 2244988746, 3151024235, 3320835882, 1336584933, 3992714006, 2252555205, 2588757463, 1714631509, 293963156, 2319795663, 3925473552, 67240454, 4269768577, 2689618160, 2017213508, 631218106, 1269344483, 2723238387, 1571005438, 2151694528, 93294474, 1066570413, 563977660, 1882732616, 4059428100, 1673313503, 2008463041, 2950355573, 1109467491, 537923632, 3858759450, 4260623118, 3218264685, 2177748300, 403442708, 638784309, 3287084079, 3193921505, 899127202, 2286175436, 773265209, 2479146071, 1437050866, 4236148354, 2050833735, 3362022572, 3126681063, 840505643, 3866325909, 3227541664, 427917720, 2655997905, 2749160575, 1143087718, 1412049534, 999329963, 193497219, 2353415882, 3354324521, 1807268051, 672404540, 2816401017, 3160301282, 369822493, 2916866934, 3688947771, 1681011286, 1949973070, 336202270, 2454276571, 201721354, 1210328172, 3093060836, 2680341085, 3184776046, 1135389935, 3294782118, 965841320, 831886756, 3554993207, 4068047243, 3588745010, 2345191491, 1849112409, 3664604599, 26054028, 2983581028, 2622377682, 1235855840, 3630984372, 2891339514, 4092916743, 3488279077, 3395642799, 4101667470, 1202630377, 268961816, 1874508501, 4034427016, 1243948399, 1546530418, 941366308, 1470539505, 1941222599, 2546386513, 3421038627, 2715671932, 3899946140, 1042226977, 2521517021, 1639824860, 227249030, 260737669, 3765465232, 2084453954, 1907733956, 3429263018, 2420656344, 100860677, 4160157185, 470683154, 3261161891, 1781871967, 2924959737, 1773779408, 394692241, 2579611992, 974986535, 664706745, 3655459128, 3958962195, 731420851, 571543859, 3530123707, 2849626480, 126783113, 865375399, 765172662, 1008606754, 361203602, 3387549984, 2278477385, 2857719295, 1344809080, 2782912378, 59542671, 1503764984, 160008576, 437062935, 1707065306, 3622233649, 2218934982, 3496503480, 2185314755, 697932208, 1512910199, 504303377, 2075177163, 2824099068, 1841019862, 739644986],
        Ne = [2781242211, 2230877308, 2582542199, 2381740923, 234877682, 3184946027, 2984144751, 1418839493, 1348481072, 50462977, 2848876391, 2102799147, 434634494, 1656084439, 3863849899, 2599188086, 1167051466, 2636087938, 1082771913, 2281340285, 368048890, 3954334041, 3381544775, 201060592, 3963727277, 1739838676, 4250903202, 3930435503, 3206782108, 4149453988, 2531553906, 1536934080, 3262494647, 484572669, 2923271059, 1783375398, 1517041206, 1098792767, 49674231, 1334037708, 1550332980, 4098991525, 886171109, 150598129, 2481090929, 1940642008, 1398944049, 1059722517, 201851908, 1385547719, 1699095331, 1587397571, 674240536, 2704774806, 252314885, 3039795866, 151914247, 908333586, 2602270848, 1038082786, 651029483, 1766729511, 3447698098, 2682942837, 454166793, 2652734339, 1951935532, 775166490, 758520603, 3000790638, 4004797018, 4217086112, 4137964114, 1299594043, 1639438038, 3464344499, 2068982057, 1054729187, 1901997871, 2534638724, 4121318227, 1757008337, 0, 750906861, 1614815264, 535035132, 3363418545, 3988151131, 3201591914, 1183697867, 3647454910, 1265776953, 3734260298, 3566750796, 3903871064, 1250283471, 1807470800, 717615087, 3847203498, 384695291, 3313910595, 3617213773, 1432761139, 2484176261, 3481945413, 283769337, 100925954, 2180939647, 4037038160, 1148730428, 3123027871, 3813386408, 4087501137, 4267549603, 3229630528, 2315620239, 2906624658, 3156319645, 1215313976, 82966005, 3747855548, 3245848246, 1974459098, 1665278241, 807407632, 451280895, 251524083, 1841287890, 1283575245, 337120268, 891687699, 801369324, 3787349855, 2721421207, 3431482436, 959321879, 1469301956, 4065699751, 2197585534, 1199193405, 2898814052, 3887750493, 724703513, 2514908019, 2696962144, 2551808385, 3516813135, 2141445340, 1715741218, 2119445034, 2872807568, 2198571144, 3398190662, 700968686, 3547052216, 1009259540, 2041044702, 3803995742, 487983883, 1991105499, 1004265696, 1449407026, 1316239930, 504629770, 3683797321, 168560134, 1816667172, 3837287516, 1570751170, 1857934291, 4014189740, 2797888098, 2822345105, 2754712981, 936633572, 2347923833, 852879335, 1133234376, 1500395319, 3084545389, 2348912013, 1689376213, 3533459022, 3762923945, 3034082412, 4205598294, 133428468, 634383082, 2949277029, 2398386810, 3913789102, 403703816, 3580869306, 2297460856, 1867130149, 1918643758, 607656988, 4049053350, 3346248884, 1368901318, 600565992, 2090982877, 2632479860, 557719327, 3717614411, 3697393085, 2249034635, 2232388234, 2430627952, 1115438654, 3295786421, 2865522278, 3633334344, 84280067, 33027830, 303828494, 2747425121, 1600795957, 4188952407, 3496589753, 2434238086, 1486471617, 658119965, 3106381470, 953803233, 334231800, 3005978776, 857870609, 3151128937, 1890179545, 2298973838, 2805175444, 3056442267, 574365214, 2450884487, 550103529, 1233637070, 4289353045, 2018519080, 2057691103, 2399374476, 4166623649, 2148108681, 387583245, 3664101311, 836232934, 3330556482, 3100665960, 3280093505, 2955516313, 2002398509, 287182607, 3413881008, 4238890068, 3597515707, 975967766],
        Oe = [1671808611, 2089089148, 2006576759, 2072901243, 4061003762, 1807603307, 1873927791, 3310653893, 810573872, 16974337, 1739181671, 729634347, 4263110654, 3613570519, 2883997099, 1989864566, 3393556426, 2191335298, 3376449993, 2106063485, 4195741690, 1508618841, 1204391495, 4027317232, 2917941677, 3563566036, 2734514082, 2951366063, 2629772188, 2767672228, 1922491506, 3227229120, 3082974647, 4246528509, 2477669779, 644500518, 911895606, 1061256767, 4144166391, 3427763148, 878471220, 2784252325, 3845444069, 4043897329, 1905517169, 3631459288, 827548209, 356461077, 67897348, 3344078279, 593839651, 3277757891, 405286936, 2527147926, 84871685, 2595565466, 118033927, 305538066, 2157648768, 3795705826, 3945188843, 661212711, 2999812018, 1973414517, 152769033, 2208177539, 745822252, 439235610, 455947803, 1857215598, 1525593178, 2700827552, 1391895634, 994932283, 3596728278, 3016654259, 695947817, 3812548067, 795958831, 2224493444, 1408607827, 3513301457, 0, 3979133421, 543178784, 4229948412, 2982705585, 1542305371, 1790891114, 3410398667, 3201918910, 961245753, 1256100938, 1289001036, 1491644504, 3477767631, 3496721360, 4012557807, 2867154858, 4212583931, 1137018435, 1305975373, 861234739, 2241073541, 1171229253, 4178635257, 33948674, 2139225727, 1357946960, 1011120188, 2679776671, 2833468328, 1374921297, 2751356323, 1086357568, 2408187279, 2460827538, 2646352285, 944271416, 4110742005, 3168756668, 3066132406, 3665145818, 560153121, 271589392, 4279952895, 4077846003, 3530407890, 3444343245, 202643468, 322250259, 3962553324, 1608629855, 2543990167, 1154254916, 389623319, 3294073796, 2817676711, 2122513534, 1028094525, 1689045092, 1575467613, 422261273, 1939203699, 1621147744, 2174228865, 1339137615, 3699352540, 577127458, 712922154, 2427141008, 2290289544, 1187679302, 3995715566, 3100863416, 339486740, 3732514782, 1591917662, 186455563, 3681988059, 3762019296, 844522546, 978220090, 169743370, 1239126601, 101321734, 611076132, 1558493276, 3260915650, 3547250131, 2901361580, 1655096418, 2443721105, 2510565781, 3828863972, 2039214713, 3878868455, 3359869896, 928607799, 1840765549, 2374762893, 3580146133, 1322425422, 2850048425, 1823791212, 1459268694, 4094161908, 3928346602, 1706019429, 2056189050, 2934523822, 135794696, 3134549946, 2022240376, 628050469, 779246638, 472135708, 2800834470, 3032970164, 3327236038, 3894660072, 3715932637, 1956440180, 522272287, 1272813131, 3185336765, 2340818315, 2323976074, 1888542832, 1044544574, 3049550261, 1722469478, 1222152264, 50660867, 4127324150, 236067854, 1638122081, 895445557, 1475980887, 3117443513, 2257655686, 3243809217, 489110045, 2662934430, 3778599393, 4162055160, 2561878936, 288563729, 1773916777, 3648039385, 2391345038, 2493985684, 2612407707, 505560094, 2274497927, 3911240169, 3460925390, 1442818645, 678973480, 3749357023, 2358182796, 2717407649, 2306869641, 219617805, 3218761151, 3862026214, 1120306242, 1756942440, 1103331905, 2578459033, 762796589, 252780047, 2966125488, 1425844308, 3151392187, 372911126],
        Ge = [1667474886, 2088535288, 2004326894, 2071694838, 4075949567, 1802223062, 1869591006, 3318043793, 808472672, 16843522, 1734846926, 724270422, 4278065639, 3621216949, 2880169549, 1987484396, 3402253711, 2189597983, 3385409673, 2105378810, 4210693615, 1499065266, 1195886990, 4042263547, 2913856577, 3570689971, 2728590687, 2947541573, 2627518243, 2762274643, 1920112356, 3233831835, 3082273397, 4261223649, 2475929149, 640051788, 909531756, 1061110142, 4160160501, 3435941763, 875846760, 2779116625, 3857003729, 4059105529, 1903268834, 3638064043, 825316194, 353713962, 67374088, 3351728789, 589522246, 3284360861, 404236336, 2526454071, 84217610, 2593830191, 117901582, 303183396, 2155911963, 3806477791, 3958056653, 656894286, 2998062463, 1970642922, 151591698, 2206440989, 741110872, 437923380, 454765878, 1852748508, 1515908788, 2694904667, 1381168804, 993742198, 3604373943, 3014905469, 690584402, 3823320797, 791638366, 2223281939, 1398011302, 3520161977, 0, 3991743681, 538992704, 4244381667, 2981218425, 1532751286, 1785380564, 3419096717, 3200178535, 960056178, 1246420628, 1280103576, 1482221744, 3486468741, 3503319995, 4025428677, 2863326543, 4227536621, 1128514950, 1296947098, 859002214, 2240123921, 1162203018, 4193849577, 33687044, 2139062782, 1347481760, 1010582648, 2678045221, 2829640523, 1364325282, 2745433693, 1077985408, 2408548869, 2459086143, 2644360225, 943212656, 4126475505, 3166494563, 3065430391, 3671750063, 555836226, 269496352, 4294908645, 4092792573, 3537006015, 3452783745, 202118168, 320025894, 3974901699, 1600119230, 2543297077, 1145359496, 387397934, 3301201811, 2812801621, 2122220284, 1027426170, 1684319432, 1566435258, 421079858, 1936954854, 1616945344, 2172753945, 1330631070, 3705438115, 572679748, 707427924, 2425400123, 2290647819, 1179044492, 4008585671, 3099120491, 336870440, 3739122087, 1583276732, 185277718, 3688593069, 3772791771, 842159716, 976899700, 168435220, 1229577106, 101059084, 606366792, 1549591736, 3267517855, 3553849021, 2897014595, 1650632388, 2442242105, 2509612081, 3840161747, 2038008818, 3890688725, 3368567691, 926374254, 1835907034, 2374863873, 3587531953, 1313788572, 2846482505, 1819063512, 1448540844, 4109633523, 3941213647, 1701162954, 2054852340, 2930698567, 134748176, 3132806511, 2021165296, 623210314, 774795868, 471606328, 2795958615, 3031746419, 3334885783, 3907527627, 3722280097, 1953799400, 522133822, 1263263126, 3183336545, 2341176845, 2324333839, 1886425312, 1044267644, 3048588401, 1718004428, 1212733584, 50529542, 4143317495, 235803164, 1633788866, 892690282, 1465383342, 3115962473, 2256965911, 3250673817, 488449850, 2661202215, 3789633753, 4177007595, 2560144171, 286339874, 1768537042, 3654906025, 2391705863, 2492770099, 2610673197, 505291324, 2273808917, 3924369609, 3469625735, 1431699370, 673740880, 3755965093, 2358021891, 2711746649, 2307489801, 218961690, 3217021541, 3873845719, 1111672452, 1751693520, 1094828930, 2576986153, 757954394, 252645662, 2964376443, 1414855848, 3149649517, 370555436],
        He = [1374988112, 2118214995, 437757123, 975658646, 1001089995, 530400753, 2902087851, 1273168787, 540080725, 2910219766, 2295101073, 4110568485, 1340463100, 3307916247, 641025152, 3043140495, 3736164937, 632953703, 1172967064, 1576976609, 3274667266, 2169303058, 2370213795, 1809054150, 59727847, 361929877, 3211623147, 2505202138, 3569255213, 1484005843, 1239443753, 2395588676, 1975683434, 4102977912, 2572697195, 666464733, 3202437046, 4035489047, 3374361702, 2110667444, 1675577880, 3843699074, 2538681184, 1649639237, 2976151520, 3144396420, 4269907996, 4178062228, 1883793496, 2403728665, 2497604743, 1383856311, 2876494627, 1917518562, 3810496343, 1716890410, 3001755655, 800440835, 2261089178, 3543599269, 807962610, 599762354, 33778362, 3977675356, 2328828971, 2809771154, 4077384432, 1315562145, 1708848333, 101039829, 3509871135, 3299278474, 875451293, 2733856160, 92987698, 2767645557, 193195065, 1080094634, 1584504582, 3178106961, 1042385657, 2531067453, 3711829422, 1306967366, 2438237621, 1908694277, 67556463, 1615861247, 429456164, 3602770327, 2302690252, 1742315127, 2968011453, 126454664, 3877198648, 2043211483, 2709260871, 2084704233, 4169408201, 0, 159417987, 841739592, 504459436, 1817866830, 4245618683, 260388950, 1034867998, 908933415, 168810852, 1750902305, 2606453969, 607530554, 202008497, 2472011535, 3035535058, 463180190, 2160117071, 1641816226, 1517767529, 470948374, 3801332234, 3231722213, 1008918595, 303765277, 235474187, 4069246893, 766945465, 337553864, 1475418501, 2943682380, 4003061179, 2743034109, 4144047775, 1551037884, 1147550661, 1543208500, 2336434550, 3408119516, 3069049960, 3102011747, 3610369226, 1113818384, 328671808, 2227573024, 2236228733, 3535486456, 2935566865, 3341394285, 496906059, 3702665459, 226906860, 2009195472, 733156972, 2842737049, 294930682, 1206477858, 2835123396, 2700099354, 1451044056, 573804783, 2269728455, 3644379585, 2362090238, 2564033334, 2801107407, 2776292904, 3669462566, 1068351396, 742039012, 1350078989, 1784663195, 1417561698, 4136440770, 2430122216, 775550814, 2193862645, 2673705150, 1775276924, 1876241833, 3475313331, 3366754619, 270040487, 3902563182, 3678124923, 3441850377, 1851332852, 3969562369, 2203032232, 3868552805, 2868897406, 566021896, 4011190502, 3135740889, 1248802510, 3936291284, 699432150, 832877231, 708780849, 3332740144, 899835584, 1951317047, 4236429990, 3767586992, 866637845, 4043610186, 1106041591, 2144161806, 395441711, 1984812685, 1139781709, 3433712980, 3835036895, 2664543715, 1282050075, 3240894392, 1181045119, 2640243204, 25965917, 4203181171, 4211818798, 3009879386, 2463879762, 3910161971, 1842759443, 2597806476, 933301370, 1509430414, 3943906441, 3467192302, 3076639029, 3776767469, 2051518780, 2631065433, 1441952575, 404016761, 1942435775, 1408749034, 1610459739, 3745345300, 2017778566, 3400528769, 3110650942, 941896748, 3265478751, 371049330, 3168937228, 675039627, 4279080257, 967311729, 135050206, 3635733660, 1683407248, 2076935265, 3576870512, 1215061108, 3501741890],
        Ve = [1347548327, 1400783205, 3273267108, 2520393566, 3409685355, 4045380933, 2880240216, 2471224067, 1428173050, 4138563181, 2441661558, 636813900, 4233094615, 3620022987, 2149987652, 2411029155, 1239331162, 1730525723, 2554718734, 3781033664, 46346101, 310463728, 2743944855, 3328955385, 3875770207, 2501218972, 3955191162, 3667219033, 768917123, 3545789473, 692707433, 1150208456, 1786102409, 2029293177, 1805211710, 3710368113, 3065962831, 401639597, 1724457132, 3028143674, 409198410, 2196052529, 1620529459, 1164071807, 3769721975, 2226875310, 486441376, 2499348523, 1483753576, 428819965, 2274680428, 3075636216, 598438867, 3799141122, 1474502543, 711349675, 129166120, 53458370, 2592523643, 2782082824, 4063242375, 2988687269, 3120694122, 1559041666, 730517276, 2460449204, 4042459122, 2706270690, 3446004468, 3573941694, 533804130, 2328143614, 2637442643, 2695033685, 839224033, 1973745387, 957055980, 2856345839, 106852767, 1371368976, 4181598602, 1033297158, 2933734917, 1179510461, 3046200461, 91341917, 1862534868, 4284502037, 605657339, 2547432937, 3431546947, 2003294622, 3182487618, 2282195339, 954669403, 3682191598, 1201765386, 3917234703, 3388507166, 0, 2198438022, 1211247597, 2887651696, 1315723890, 4227665663, 1443857720, 507358933, 657861945, 1678381017, 560487590, 3516619604, 975451694, 2970356327, 261314535, 3535072918, 2652609425, 1333838021, 2724322336, 1767536459, 370938394, 182621114, 3854606378, 1128014560, 487725847, 185469197, 2918353863, 3106780840, 3356761769, 2237133081, 1286567175, 3152976349, 4255350624, 2683765030, 3160175349, 3309594171, 878443390, 1988838185, 3704300486, 1756818940, 1673061617, 3403100636, 272786309, 1075025698, 545572369, 2105887268, 4174560061, 296679730, 1841768865, 1260232239, 4091327024, 3960309330, 3497509347, 1814803222, 2578018489, 4195456072, 575138148, 3299409036, 446754879, 3629546796, 4011996048, 3347532110, 3252238545, 4270639778, 915985419, 3483825537, 681933534, 651868046, 2755636671, 3828103837, 223377554, 2607439820, 1649704518, 3270937875, 3901806776, 1580087799, 4118987695, 3198115200, 2087309459, 2842678573, 3016697106, 1003007129, 2802849917, 1860738147, 2077965243, 164439672, 4100872472, 32283319, 2827177882, 1709610350, 2125135846, 136428751, 3874428392, 3652904859, 3460984630, 3572145929, 3593056380, 2939266226, 824852259, 818324884, 3224740454, 930369212, 2801566410, 2967507152, 355706840, 1257309336, 4148292826, 243256656, 790073846, 2373340630, 1296297904, 1422699085, 3756299780, 3818836405, 457992840, 3099667487, 2135319889, 77422314, 1560382517, 1945798516, 788204353, 1521706781, 1385356242, 870912086, 325965383, 2358957921, 2050466060, 2388260884, 2313884476, 4006521127, 901210569, 3990953189, 1014646705, 1503449823, 1062597235, 2031621326, 3212035895, 3931371469, 1533017514, 350174575, 2256028891, 2177544179, 1052338372, 741876788, 1606591296, 1914052035, 213705253, 2334669897, 1107234197, 1899603969, 3725069491, 2631447780, 2422494913, 1635502980, 1893020342, 1950903388, 1120974935],
        $e = [2807058932, 1699970625, 2764249623, 1586903591, 1808481195, 1173430173, 1487645946, 59984867, 4199882800, 1844882806, 1989249228, 1277555970, 3623636965, 3419915562, 1149249077, 2744104290, 1514790577, 459744698, 244860394, 3235995134, 1963115311, 4027744588, 2544078150, 4190530515, 1608975247, 2627016082, 2062270317, 1507497298, 2200818878, 567498868, 1764313568, 3359936201, 2305455554, 2037970062, 1047239e3, 1910319033, 1337376481, 2904027272, 2892417312, 984907214, 1243112415, 830661914, 861968209, 2135253587, 2011214180, 2927934315, 2686254721, 731183368, 1750626376, 4246310725, 1820824798, 4172763771, 3542330227, 48394827, 2404901663, 2871682645, 671593195, 3254988725, 2073724613, 145085239, 2280796200, 2779915199, 1790575107, 2187128086, 472615631, 3029510009, 4075877127, 3802222185, 4107101658, 3201631749, 1646252340, 4270507174, 1402811438, 1436590835, 3778151818, 3950355702, 3963161475, 4020912224, 2667994737, 273792366, 2331590177, 104699613, 95345982, 3175501286, 2377486676, 1560637892, 3564045318, 369057872, 4213447064, 3919042237, 1137477952, 2658625497, 1119727848, 2340947849, 1530455833, 4007360968, 172466556, 266959938, 516552836, 0, 2256734592, 3980931627, 1890328081, 1917742170, 4294704398, 945164165, 3575528878, 958871085, 3647212047, 2787207260, 1423022939, 775562294, 1739656202, 3876557655, 2530391278, 2443058075, 3310321856, 547512796, 1265195639, 437656594, 3121275539, 719700128, 3762502690, 387781147, 218828297, 3350065803, 2830708150, 2848461854, 428169201, 122466165, 3720081049, 1627235199, 648017665, 4122762354, 1002783846, 2117360635, 695634755, 3336358691, 4234721005, 4049844452, 3704280881, 2232435299, 574624663, 287343814, 612205898, 1039717051, 840019705, 2708326185, 793451934, 821288114, 1391201670, 3822090177, 376187827, 3113855344, 1224348052, 1679968233, 2361698556, 1058709744, 752375421, 2431590963, 1321699145, 3519142200, 2734591178, 188127444, 2177869557, 3727205754, 2384911031, 3215212461, 2648976442, 2450346104, 3432737375, 1180849278, 331544205, 3102249176, 4150144569, 2952102595, 2159976285, 2474404304, 766078933, 313773861, 2570832044, 2108100632, 1668212892, 3145456443, 2013908262, 418672217, 3070356634, 2594734927, 1852171925, 3867060991, 3473416636, 3907448597, 2614737639, 919489135, 164948639, 2094410160, 2997825956, 590424639, 2486224549, 1723872674, 3157750862, 3399941250, 3501252752, 3625268135, 2555048196, 3673637356, 1343127501, 4130281361, 3599595085, 2957853679, 1297403050, 81781910, 3051593425, 2283490410, 532201772, 1367295589, 3926170974, 895287692, 1953757831, 1093597963, 492483431, 3528626907, 1446242576, 1192455638, 1636604631, 209336225, 344873464, 1015671571, 669961897, 3375740769, 3857572124, 2973530695, 3747192018, 1933530610, 3464042516, 935293895, 3454686199, 2858115069, 1863638845, 3683022916, 4085369519, 3292445032, 875313188, 1080017571, 3279033885, 621591778, 1233856572, 2504130317, 24197544, 3017672716, 3835484340, 3247465558, 2220981195, 3060847922, 1551124588, 1463996600],
        je = [4104605777, 1097159550, 396673818, 660510266, 2875968315, 2638606623, 4200115116, 3808662347, 821712160, 1986918061, 3430322568, 38544885, 3856137295, 718002117, 893681702, 1654886325, 2975484382, 3122358053, 3926825029, 4274053469, 796197571, 1290801793, 1184342925, 3556361835, 2405426947, 2459735317, 1836772287, 1381620373, 3196267988, 1948373848, 3764988233, 3385345166, 3263785589, 2390325492, 1480485785, 3111247143, 3780097726, 2293045232, 548169417, 3459953789, 3746175075, 439452389, 1362321559, 1400849762, 1685577905, 1806599355, 2174754046, 137073913, 1214797936, 1174215055, 3731654548, 2079897426, 1943217067, 1258480242, 529487843, 1437280870, 3945269170, 3049390895, 3313212038, 923313619, 679998e3, 3215307299, 57326082, 377642221, 3474729866, 2041877159, 133361907, 1776460110, 3673476453, 96392454, 878845905, 2801699524, 777231668, 4082475170, 2330014213, 4142626212, 2213296395, 1626319424, 1906247262, 1846563261, 562755902, 3708173718, 1040559837, 3871163981, 1418573201, 3294430577, 114585348, 1343618912, 2566595609, 3186202582, 1078185097, 3651041127, 3896688048, 2307622919, 425408743, 3371096953, 2081048481, 1108339068, 2216610296, 0, 2156299017, 736970802, 292596766, 1517440620, 251657213, 2235061775, 2933202493, 758720310, 265905162, 1554391400, 1532285339, 908999204, 174567692, 1474760595, 4002861748, 2610011675, 3234156416, 3693126241, 2001430874, 303699484, 2478443234, 2687165888, 585122620, 454499602, 151849742, 2345119218, 3064510765, 514443284, 4044981591, 1963412655, 2581445614, 2137062819, 19308535, 1928707164, 1715193156, 4219352155, 1126790795, 600235211, 3992742070, 3841024952, 836553431, 1669664834, 2535604243, 3323011204, 1243905413, 3141400786, 4180808110, 698445255, 2653899549, 2989552604, 2253581325, 3252932727, 3004591147, 1891211689, 2487810577, 3915653703, 4237083816, 4030667424, 2100090966, 865136418, 1229899655, 953270745, 3399679628, 3557504664, 4118925222, 2061379749, 3079546586, 2915017791, 983426092, 2022837584, 1607244650, 2118541908, 2366882550, 3635996816, 972512814, 3283088770, 1568718495, 3499326569, 3576539503, 621982671, 2895723464, 410887952, 2623762152, 1002142683, 645401037, 1494807662, 2595684844, 1335535747, 2507040230, 4293295786, 3167684641, 367585007, 3885750714, 1865862730, 2668221674, 2960971305, 2763173681, 1059270954, 2777952454, 2724642869, 1320957812, 2194319100, 2429595872, 2815956275, 77089521, 3973773121, 3444575871, 2448830231, 1305906550, 4021308739, 2857194700, 2516901860, 3518358430, 1787304780, 740276417, 1699839814, 1592394909, 2352307457, 2272556026, 188821243, 1729977011, 3687994002, 274084841, 3594982253, 3613494426, 2701949495, 4162096729, 322734571, 2837966542, 1640576439, 484830689, 1202797690, 3537852828, 4067639125, 349075736, 3342319475, 4157467219, 4255800159, 1030690015, 1155237496, 2951971274, 1757691577, 607398968, 2738905026, 499347990, 3794078908, 1011452712, 227885567, 2818666809, 213114376, 3034881240, 1455525988, 3414450555, 850817237, 1817998408, 3092726480],
        We = [0, 235474187, 470948374, 303765277, 941896748, 908933415, 607530554, 708780849, 1883793496, 2118214995, 1817866830, 1649639237, 1215061108, 1181045119, 1417561698, 1517767529, 3767586992, 4003061179, 4236429990, 4069246893, 3635733660, 3602770327, 3299278474, 3400528769, 2430122216, 2664543715, 2362090238, 2193862645, 2835123396, 2801107407, 3035535058, 3135740889, 3678124923, 3576870512, 3341394285, 3374361702, 3810496343, 3977675356, 4279080257, 4043610186, 2876494627, 2776292904, 3076639029, 3110650942, 2472011535, 2640243204, 2403728665, 2169303058, 1001089995, 899835584, 666464733, 699432150, 59727847, 226906860, 530400753, 294930682, 1273168787, 1172967064, 1475418501, 1509430414, 1942435775, 2110667444, 1876241833, 1641816226, 2910219766, 2743034109, 2976151520, 3211623147, 2505202138, 2606453969, 2302690252, 2269728455, 3711829422, 3543599269, 3240894392, 3475313331, 3843699074, 3943906441, 4178062228, 4144047775, 1306967366, 1139781709, 1374988112, 1610459739, 1975683434, 2076935265, 1775276924, 1742315127, 1034867998, 866637845, 566021896, 800440835, 92987698, 193195065, 429456164, 395441711, 1984812685, 2017778566, 1784663195, 1683407248, 1315562145, 1080094634, 1383856311, 1551037884, 101039829, 135050206, 437757123, 337553864, 1042385657, 807962610, 573804783, 742039012, 2531067453, 2564033334, 2328828971, 2227573024, 2935566865, 2700099354, 3001755655, 3168937228, 3868552805, 3902563182, 4203181171, 4102977912, 3736164937, 3501741890, 3265478751, 3433712980, 1106041591, 1340463100, 1576976609, 1408749034, 2043211483, 2009195472, 1708848333, 1809054150, 832877231, 1068351396, 766945465, 599762354, 159417987, 126454664, 361929877, 463180190, 2709260871, 2943682380, 3178106961, 3009879386, 2572697195, 2538681184, 2236228733, 2336434550, 3509871135, 3745345300, 3441850377, 3274667266, 3910161971, 3877198648, 4110568485, 4211818798, 2597806476, 2497604743, 2261089178, 2295101073, 2733856160, 2902087851, 3202437046, 2968011453, 3936291284, 3835036895, 4136440770, 4169408201, 3535486456, 3702665459, 3467192302, 3231722213, 2051518780, 1951317047, 1716890410, 1750902305, 1113818384, 1282050075, 1584504582, 1350078989, 168810852, 67556463, 371049330, 404016761, 841739592, 1008918595, 775550814, 540080725, 3969562369, 3801332234, 4035489047, 4269907996, 3569255213, 3669462566, 3366754619, 3332740144, 2631065433, 2463879762, 2160117071, 2395588676, 2767645557, 2868897406, 3102011747, 3069049960, 202008497, 33778362, 270040487, 504459436, 875451293, 975658646, 675039627, 641025152, 2084704233, 1917518562, 1615861247, 1851332852, 1147550661, 1248802510, 1484005843, 1451044056, 933301370, 967311729, 733156972, 632953703, 260388950, 25965917, 328671808, 496906059, 1206477858, 1239443753, 1543208500, 1441952575, 2144161806, 1908694277, 1675577880, 1842759443, 3610369226, 3644379585, 3408119516, 3307916247, 4011190502, 3776767469, 4077384432, 4245618683, 2809771154, 2842737049, 3144396420, 3043140495, 2673705150, 2438237621, 2203032232, 2370213795],
        Ye = [0, 185469197, 370938394, 487725847, 741876788, 657861945, 975451694, 824852259, 1483753576, 1400783205, 1315723890, 1164071807, 1950903388, 2135319889, 1649704518, 1767536459, 2967507152, 3152976349, 2801566410, 2918353863, 2631447780, 2547432937, 2328143614, 2177544179, 3901806776, 3818836405, 4270639778, 4118987695, 3299409036, 3483825537, 3535072918, 3652904859, 2077965243, 1893020342, 1841768865, 1724457132, 1474502543, 1559041666, 1107234197, 1257309336, 598438867, 681933534, 901210569, 1052338372, 261314535, 77422314, 428819965, 310463728, 3409685355, 3224740454, 3710368113, 3593056380, 3875770207, 3960309330, 4045380933, 4195456072, 2471224067, 2554718734, 2237133081, 2388260884, 3212035895, 3028143674, 2842678573, 2724322336, 4138563181, 4255350624, 3769721975, 3955191162, 3667219033, 3516619604, 3431546947, 3347532110, 2933734917, 2782082824, 3099667487, 3016697106, 2196052529, 2313884476, 2499348523, 2683765030, 1179510461, 1296297904, 1347548327, 1533017514, 1786102409, 1635502980, 2087309459, 2003294622, 507358933, 355706840, 136428751, 53458370, 839224033, 957055980, 605657339, 790073846, 2373340630, 2256028891, 2607439820, 2422494913, 2706270690, 2856345839, 3075636216, 3160175349, 3573941694, 3725069491, 3273267108, 3356761769, 4181598602, 4063242375, 4011996048, 3828103837, 1033297158, 915985419, 730517276, 545572369, 296679730, 446754879, 129166120, 213705253, 1709610350, 1860738147, 1945798516, 2029293177, 1239331162, 1120974935, 1606591296, 1422699085, 4148292826, 4233094615, 3781033664, 3931371469, 3682191598, 3497509347, 3446004468, 3328955385, 2939266226, 2755636671, 3106780840, 2988687269, 2198438022, 2282195339, 2501218972, 2652609425, 1201765386, 1286567175, 1371368976, 1521706781, 1805211710, 1620529459, 2105887268, 1988838185, 533804130, 350174575, 164439672, 46346101, 870912086, 954669403, 636813900, 788204353, 2358957921, 2274680428, 2592523643, 2441661558, 2695033685, 2880240216, 3065962831, 3182487618, 3572145929, 3756299780, 3270937875, 3388507166, 4174560061, 4091327024, 4006521127, 3854606378, 1014646705, 930369212, 711349675, 560487590, 272786309, 457992840, 106852767, 223377554, 1678381017, 1862534868, 1914052035, 2031621326, 1211247597, 1128014560, 1580087799, 1428173050, 32283319, 182621114, 401639597, 486441376, 768917123, 651868046, 1003007129, 818324884, 1503449823, 1385356242, 1333838021, 1150208456, 1973745387, 2125135846, 1673061617, 1756818940, 2970356327, 3120694122, 2802849917, 2887651696, 2637442643, 2520393566, 2334669897, 2149987652, 3917234703, 3799141122, 4284502037, 4100872472, 3309594171, 3460984630, 3545789473, 3629546796, 2050466060, 1899603969, 1814803222, 1730525723, 1443857720, 1560382517, 1075025698, 1260232239, 575138148, 692707433, 878443390, 1062597235, 243256656, 91341917, 409198410, 325965383, 3403100636, 3252238545, 3704300486, 3620022987, 3874428392, 3990953189, 4042459122, 4227665663, 2460449204, 2578018489, 2226875310, 2411029155, 3198115200, 3046200461, 2827177882, 2743944855],
        qe = [0, 218828297, 437656594, 387781147, 875313188, 958871085, 775562294, 590424639, 1750626376, 1699970625, 1917742170, 2135253587, 1551124588, 1367295589, 1180849278, 1265195639, 3501252752, 3720081049, 3399941250, 3350065803, 3835484340, 3919042237, 4270507174, 4085369519, 3102249176, 3051593425, 2734591178, 2952102595, 2361698556, 2177869557, 2530391278, 2614737639, 3145456443, 3060847922, 2708326185, 2892417312, 2404901663, 2187128086, 2504130317, 2555048196, 3542330227, 3727205754, 3375740769, 3292445032, 3876557655, 3926170974, 4246310725, 4027744588, 1808481195, 1723872674, 1910319033, 2094410160, 1608975247, 1391201670, 1173430173, 1224348052, 59984867, 244860394, 428169201, 344873464, 935293895, 984907214, 766078933, 547512796, 1844882806, 1627235199, 2011214180, 2062270317, 1507497298, 1423022939, 1137477952, 1321699145, 95345982, 145085239, 532201772, 313773861, 830661914, 1015671571, 731183368, 648017665, 3175501286, 2957853679, 2807058932, 2858115069, 2305455554, 2220981195, 2474404304, 2658625497, 3575528878, 3625268135, 3473416636, 3254988725, 3778151818, 3963161475, 4213447064, 4130281361, 3599595085, 3683022916, 3432737375, 3247465558, 3802222185, 4020912224, 4172763771, 4122762354, 3201631749, 3017672716, 2764249623, 2848461854, 2331590177, 2280796200, 2431590963, 2648976442, 104699613, 188127444, 472615631, 287343814, 840019705, 1058709744, 671593195, 621591778, 1852171925, 1668212892, 1953757831, 2037970062, 1514790577, 1463996600, 1080017571, 1297403050, 3673637356, 3623636965, 3235995134, 3454686199, 4007360968, 3822090177, 4107101658, 4190530515, 2997825956, 3215212461, 2830708150, 2779915199, 2256734592, 2340947849, 2627016082, 2443058075, 172466556, 122466165, 273792366, 492483431, 1047239e3, 861968209, 612205898, 695634755, 1646252340, 1863638845, 2013908262, 1963115311, 1446242576, 1530455833, 1277555970, 1093597963, 1636604631, 1820824798, 2073724613, 1989249228, 1436590835, 1487645946, 1337376481, 1119727848, 164948639, 81781910, 331544205, 516552836, 1039717051, 821288114, 669961897, 719700128, 2973530695, 3157750862, 2871682645, 2787207260, 2232435299, 2283490410, 2667994737, 2450346104, 3647212047, 3564045318, 3279033885, 3464042516, 3980931627, 3762502690, 4150144569, 4199882800, 3070356634, 3121275539, 2904027272, 2686254721, 2200818878, 2384911031, 2570832044, 2486224549, 3747192018, 3528626907, 3310321856, 3359936201, 3950355702, 3867060991, 4049844452, 4234721005, 1739656202, 1790575107, 2108100632, 1890328081, 1402811438, 1586903591, 1233856572, 1149249077, 266959938, 48394827, 369057872, 418672217, 1002783846, 919489135, 567498868, 752375421, 209336225, 24197544, 376187827, 459744698, 945164165, 895287692, 574624663, 793451934, 1679968233, 1764313568, 2117360635, 1933530610, 1343127501, 1560637892, 1243112415, 1192455638, 3704280881, 3519142200, 3336358691, 3419915562, 3907448597, 3857572124, 4075877127, 4294704398, 3029510009, 3113855344, 2927934315, 2744104290, 2159976285, 2377486676, 2594734927, 2544078150],
        Ke = [0, 151849742, 303699484, 454499602, 607398968, 758720310, 908999204, 1059270954, 1214797936, 1097159550, 1517440620, 1400849762, 1817998408, 1699839814, 2118541908, 2001430874, 2429595872, 2581445614, 2194319100, 2345119218, 3034881240, 3186202582, 2801699524, 2951971274, 3635996816, 3518358430, 3399679628, 3283088770, 4237083816, 4118925222, 4002861748, 3885750714, 1002142683, 850817237, 698445255, 548169417, 529487843, 377642221, 227885567, 77089521, 1943217067, 2061379749, 1640576439, 1757691577, 1474760595, 1592394909, 1174215055, 1290801793, 2875968315, 2724642869, 3111247143, 2960971305, 2405426947, 2253581325, 2638606623, 2487810577, 3808662347, 3926825029, 4044981591, 4162096729, 3342319475, 3459953789, 3576539503, 3693126241, 1986918061, 2137062819, 1685577905, 1836772287, 1381620373, 1532285339, 1078185097, 1229899655, 1040559837, 923313619, 740276417, 621982671, 439452389, 322734571, 137073913, 19308535, 3871163981, 4021308739, 4104605777, 4255800159, 3263785589, 3414450555, 3499326569, 3651041127, 2933202493, 2815956275, 3167684641, 3049390895, 2330014213, 2213296395, 2566595609, 2448830231, 1305906550, 1155237496, 1607244650, 1455525988, 1776460110, 1626319424, 2079897426, 1928707164, 96392454, 213114376, 396673818, 514443284, 562755902, 679998e3, 865136418, 983426092, 3708173718, 3557504664, 3474729866, 3323011204, 4180808110, 4030667424, 3945269170, 3794078908, 2507040230, 2623762152, 2272556026, 2390325492, 2975484382, 3092726480, 2738905026, 2857194700, 3973773121, 3856137295, 4274053469, 4157467219, 3371096953, 3252932727, 3673476453, 3556361835, 2763173681, 2915017791, 3064510765, 3215307299, 2156299017, 2307622919, 2459735317, 2610011675, 2081048481, 1963412655, 1846563261, 1729977011, 1480485785, 1362321559, 1243905413, 1126790795, 878845905, 1030690015, 645401037, 796197571, 274084841, 425408743, 38544885, 188821243, 3613494426, 3731654548, 3313212038, 3430322568, 4082475170, 4200115116, 3780097726, 3896688048, 2668221674, 2516901860, 2366882550, 2216610296, 3141400786, 2989552604, 2837966542, 2687165888, 1202797690, 1320957812, 1437280870, 1554391400, 1669664834, 1787304780, 1906247262, 2022837584, 265905162, 114585348, 499347990, 349075736, 736970802, 585122620, 972512814, 821712160, 2595684844, 2478443234, 2293045232, 2174754046, 3196267988, 3079546586, 2895723464, 2777952454, 3537852828, 3687994002, 3234156416, 3385345166, 4142626212, 4293295786, 3841024952, 3992742070, 174567692, 57326082, 410887952, 292596766, 777231668, 660510266, 1011452712, 893681702, 1108339068, 1258480242, 1343618912, 1494807662, 1715193156, 1865862730, 1948373848, 2100090966, 2701949495, 2818666809, 3004591147, 3122358053, 2235061775, 2352307457, 2535604243, 2653899549, 3915653703, 3764988233, 4219352155, 4067639125, 3444575871, 3294430577, 3746175075, 3594982253, 836553431, 953270745, 600235211, 718002117, 367585007, 484830689, 133361907, 251657213, 2041877159, 1891211689, 1806599355, 1654886325, 1568718495, 1418573201, 1335535747, 1184342925];

    function Xe(e) {
        for (var t = [], r = 0; r < e.length; r += 4) t.push(e[r] << 24 | e[r + 1] << 16 | e[r + 2] << 8 | e[r + 3]);
        return t
    }

    function i(e) {
        if (!(this instanceof i)) throw Error("AES must be instanitated with `new`");
        Object.defineProperty(this, "key", {value: s(e, !0)}), this._prepare()
    }

    function t(e) {
        if (!(this instanceof t)) throw Error("AES must be instanitated with `new`");
        this.description = "Electronic Code Block", this.name = "ecb", this._aes = new i(e)
    }

    function r(e, t) {
        if (!(this instanceof r)) throw Error("AES must be instanitated with `new`");
        if (this.description = "Cipher Block Chaining", this.name = "cbc", t) {
            if (16 != t.length) throw new Error("invalid initialation vector size (must be 16 bytes)")
        } else t = l(16);
        this._lastCipherblock = s(t, !0), this._aes = new i(e)
    }

    function o(e, t, r) {
        if (!(this instanceof o)) throw Error("AES must be instanitated with `new`");
        if (this.description = "Cipher Feedback", this.name = "cfb", t) {
            if (16 != t.length) throw new Error("invalid initialation vector size (must be 16 size)")
        } else t = l(16);
        this.segmentSize = r = r || 1, this._shiftRegister = s(t, !0), this._aes = new i(e)
    }

    function h(e, t) {
        if (!(this instanceof h)) throw Error("AES must be instanitated with `new`");
        if (this.description = "Output Feedback", this.name = "ofb", t) {
            if (16 != t.length) throw new Error("invalid initialation vector size (must be 16 bytes)")
        } else t = l(16);
        this._lastPrecipher = s(t, !0), this._lastPrecipherIndex = 16, this._aes = new i(e)
    }

    function u(e) {
        if (!(this instanceof u)) throw Error("Counter must be instanitated with `new`");
        "number" == typeof (e = 0 === e || e ? e : 1) ? (this._counter = l(16), this.setValue(e)) : this.setBytes(e)
    }

    function p(e, t) {
        if (!(this instanceof p)) throw Error("AES must be instanitated with `new`");
        this.description = "Counter", this.name = "ctr", t instanceof u || (t = new u(t)), this._counter = t, this._remainingCounter = null, this._remainingCounterIndex = 16, this._aes = new i(e)
    }

    i.prototype._prepare = function () {
        var e = N[this.key.length];
        if (null == e) throw new Error("invalid key size (must be 16, 24 or 32 bytes)");
        this._Ke = [], this._Kd = [];
        for (var t = 0; t <= e; t++) this._Ke.push([0, 0, 0, 0]), this._Kd.push([0, 0, 0, 0]);
        for (var r, i = 4 * (e + 1), n = this.key.length / 4, s = Xe(this.key), t = 0; t < n; t++) this._Ke[r = t >> 2][t % 4] = s[t], this._Kd[e - r][t % 4] = s[t];
        for (var a, o = 0, l = n; l < i;) {
            if (a = s[n - 1], s[0] ^= f[a >> 16 & 255] << 24 ^ f[a >> 8 & 255] << 16 ^ f[255 & a] << 8 ^ f[a >> 24 & 255] ^ O[o] << 24, o += 1, 8 != n) for (t = 1; t < n; t++) s[t] ^= s[t - 1]; else {
                for (t = 1; t < n / 2; t++) s[t] ^= s[t - 1];
                for (a = s[n / 2 - 1], s[n / 2] ^= f[255 & a] ^ f[a >> 8 & 255] << 8 ^ f[a >> 16 & 255] << 16 ^ f[a >> 24 & 255] << 24, t = n / 2 + 1; t < n; t++) s[t] ^= s[t - 1]
            }
            for (t = 0; t < n && l < i;) this._Ke[d = l >> 2][h = l % 4] = s[t], this._Kd[e - d][h] = s[t++], l++
        }
        for (var d = 1; d < e; d++) for (var h = 0; h < 4; h++) a = this._Kd[d][h], this._Kd[d][h] = We[a >> 24 & 255] ^ Ye[a >> 16 & 255] ^ qe[a >> 8 & 255] ^ Ke[255 & a]
    }, i.prototype.encrypt = function (e) {
        if (16 != e.length) throw new Error("invalid plaintext size (must be 16 bytes)");
        for (var t = this._Ke.length - 1, r = [0, 0, 0, 0], i = Xe(e), n = 0; n < 4; n++) i[n] ^= this._Ke[0][n];
        for (var s = 1; s < t; s++) {
            for (n = 0; n < 4; n++) r[n] = Me[i[n] >> 24 & 255] ^ Ne[i[(n + 1) % 4] >> 16 & 255] ^ Oe[i[(n + 2) % 4] >> 8 & 255] ^ Ge[255 & i[(n + 3) % 4]] ^ this._Ke[s][n];
            i = r.slice()
        }
        for (var a, o = l(16), n = 0; n < 4; n++) a = this._Ke[t][n], o[4 * n] = 255 & (f[i[n] >> 24 & 255] ^ a >> 24), o[4 * n + 1] = 255 & (f[i[(n + 1) % 4] >> 16 & 255] ^ a >> 16), o[4 * n + 2] = 255 & (f[i[(n + 2) % 4] >> 8 & 255] ^ a >> 8), o[4 * n + 3] = 255 & (f[255 & i[(n + 3) % 4]] ^ a);
        return o
    }, i.prototype.decrypt = function (e) {
        if (16 != e.length) throw new Error("invalid ciphertext size (must be 16 bytes)");
        for (var t = this._Kd.length - 1, r = [0, 0, 0, 0], i = Xe(e), n = 0; n < 4; n++) i[n] ^= this._Kd[0][n];
        for (var s = 1; s < t; s++) {
            for (n = 0; n < 4; n++) r[n] = He[i[n] >> 24 & 255] ^ Ve[i[(n + 3) % 4] >> 16 & 255] ^ $e[i[(n + 2) % 4] >> 8 & 255] ^ je[255 & i[(n + 1) % 4]] ^ this._Kd[s][n];
            i = r.slice()
        }
        for (var a, o = l(16), n = 0; n < 4; n++) a = this._Kd[t][n], o[4 * n] = 255 & (d[i[n] >> 24 & 255] ^ a >> 24), o[4 * n + 1] = 255 & (d[i[(n + 3) % 4] >> 16 & 255] ^ a >> 16), o[4 * n + 2] = 255 & (d[i[(n + 2) % 4] >> 8 & 255] ^ a >> 8), o[4 * n + 3] = 255 & (d[255 & i[(n + 1) % 4]] ^ a);
        return o
    }, t.prototype.encrypt = function (e) {
        if ((e = s(e)).length % 16 != 0) throw new Error("invalid plaintext size (must be multiple of 16 bytes)");
        for (var t = l(e.length), r = l(16), i = 0; i < e.length; i += 16) a(e, r, 0, i, i + 16), a(r = this._aes.encrypt(r), t, i);
        return t
    }, t.prototype.decrypt = function (e) {
        if ((e = s(e)).length % 16 != 0) throw new Error("invalid ciphertext size (must be multiple of 16 bytes)");
        for (var t = l(e.length), r = l(16), i = 0; i < e.length; i += 16) a(e, r, 0, i, i + 16), a(r = this._aes.decrypt(r), t, i);
        return t
    }, r.prototype.encrypt = function (e) {
        if ((e = s(e)).length % 16 != 0) throw new Error("invalid plaintext size (must be multiple of 16 bytes)");
        for (var t = l(e.length), r = l(16), i = 0; i < e.length; i += 16) {
            a(e, r, 0, i, i + 16);
            for (var n = 0; n < 16; n++) r[n] ^= this._lastCipherblock[n];
            this._lastCipherblock = this._aes.encrypt(r), a(this._lastCipherblock, t, i)
        }
        return t
    }, r.prototype.decrypt = function (e) {
        if ((e = s(e)).length % 16 != 0) throw new Error("invalid ciphertext size (must be multiple of 16 bytes)");
        for (var t = l(e.length), r = l(16), i = 0; i < e.length; i += 16) {
            a(e, r, 0, i, i + 16);
            for (var r = this._aes.decrypt(r), n = 0; n < 16; n++) t[i + n] = r[n] ^ this._lastCipherblock[n];
            a(e, this._lastCipherblock, 0, i, i + 16)
        }
        return t
    }, o.prototype.encrypt = function (e) {
        if (e.length % this.segmentSize != 0) throw new Error("invalid plaintext size (must be segmentSize bytes)");
        for (var t = s(e, !0), r = 0; r < t.length; r += this.segmentSize) {
            for (var i = this._aes.encrypt(this._shiftRegister), n = 0; n < this.segmentSize; n++) t[r + n] ^= i[n];
            a(this._shiftRegister, this._shiftRegister, 0, this.segmentSize), a(t, this._shiftRegister, 16 - this.segmentSize, r, r + this.segmentSize)
        }
        return t
    }, o.prototype.decrypt = function (e) {
        if (e.length % this.segmentSize != 0) throw new Error("invalid ciphertext size (must be segmentSize bytes)");
        for (var t = s(e, !0), r = 0; r < t.length; r += this.segmentSize) {
            for (var i = this._aes.encrypt(this._shiftRegister), n = 0; n < this.segmentSize; n++) t[r + n] ^= i[n];
            a(this._shiftRegister, this._shiftRegister, 0, this.segmentSize), a(e, this._shiftRegister, 16 - this.segmentSize, r, r + this.segmentSize)
        }
        return t
    }, h.prototype.decrypt = h.prototype.encrypt = function (e) {
        for (var t = s(e, !0), r = 0; r < t.length; r++) 16 === this._lastPrecipherIndex && (this._lastPrecipher = this._aes.encrypt(this._lastPrecipher), this._lastPrecipherIndex = 0), t[r] ^= this._lastPrecipher[this._lastPrecipherIndex++];
        return t
    }, u.prototype.setValue = function (e) {
        if ("number" != typeof e || parseInt(e) != e) throw new Error("invalid counter value (must be an integer)");
        if (e > Number.MAX_SAFE_INTEGER) throw new Error("integer value out of safe range");
        for (var t = 15; 0 <= t; --t) this._counter[t] = e % 256, e = parseInt(e / 256)
    }, u.prototype.setBytes = function (e) {
        if (16 != (e = s(e, !0)).length) throw new Error("invalid counter bytes size (must be 16 bytes)");
        this._counter = e
    }, u.prototype.increment = function () {
        for (var e = 15; 0 <= e; e--) {
            if (255 !== this._counter[e]) {
                this._counter[e]++;
                break
            }
            this._counter[e] = 0
        }
    };
    p.prototype.decrypt = p.prototype.encrypt = function (e) {
        for (var t = s(e, !0), r = 0; r < t.length; r++) 16 === this._remainingCounterIndex && (this._remainingCounter = this._aes.encrypt(this._counter._counter), this._remainingCounterIndex = 0, this._counter.increment()), t[r] ^= this._remainingCounter[this._remainingCounterIndex++];
        return t
    };
    const Ze = {
        AES: i,
        Counter: u,
        ModeOfOperation: {ecb: t, cbc: r, cfb: o, ofb: h, ctr: p},
        utils: {hex: y, utf8: g},
        padding: {
            pkcs7: {
                pad: function (e) {
                    var t = 16 - (e = s(e, !0)).length % 16, r = l(e.length + t);
                    a(e, r);
                    for (var i = e.length; i < r.length; i++) r[i] = t;
                    return r
                }, strip: function (e) {
                    if ((e = s(e, !0)).length < 16) throw new Error("PKCS#7 invalid length");
                    var t = e[e.length - 1];
                    if (16 < t) throw new Error("PKCS#7 padding byte out of range");
                    for (var r = e.length - t, i = 0; i < t; i++) if (e[r + i] !== t) throw new Error("PKCS#7 invalid padding byte");
                    var n = l(r);
                    return a(e, n, 0, 0, r), n
                }
            }
        },
        _arrayTest: {coerceArray: s, createArray: l, copyArray: a}
    };
    var re = v(function (e, t) {
        function f(e) {
            if (!(e instanceof ArrayBuffer)) throw"Needs an array buffer";
            this.buffer = e, this.dataview = new DataView(e), this.position = 0
        }

        function l(e, t, r) {
            this._byteOffset = t || 0, e instanceof ArrayBuffer ? this.buffer = e : "object" == typeof e ? (this.dataView = e, t && (this._byteOffset += t)) : this.buffer = new ArrayBuffer(e || 0), this.position = 0, this.endianness = null == r ? l.LITTLE_ENDIAN : r
        }

        function r(e) {
            this.buffers = [], this.bufferIndex = -1, e && (this.insertBuffer(e), this.bufferIndex = 0)
        }

        function i() {
            var n = [],
                i = (n[3] = "ES_Descriptor", n[4] = "DecoderConfigDescriptor", n[5] = "DecoderSpecificInfo", n[6] = "SLConfigDescriptor", this.getDescriptorName = function (e) {
                    return n[e]
                }, this), s = {};
            return this.parseOneDescriptor = function (e) {
                for (var t = 0, r = e.readUint8(), i = e.readUint8(); 128 & i;) t = (127 & i) << 7, i = e.readUint8();
                return u.debug("MPEG4DescriptorParser", "Found " + (n[r] || "Descriptor " + r) + ", size " + (t += 127 & i) + " at position " + e.getPosition()), (r = new (n[r] ? s[n[r]] : s.Descriptor)(t)).parse(e), r
            }, s.Descriptor = function (e, t) {
                this.tag = e, this.size = t, this.descs = []
            }, s.Descriptor.prototype.parse = function (e) {
                this.data = e.readUint8Array(this.size)
            }, s.Descriptor.prototype.findDescriptor = function (e) {
                for (var t = 0; t < this.descs.length; t++) if (this.descs[t].tag == e) return this.descs[t];
                return null
            }, s.Descriptor.prototype.parseRemainingDescriptors = function (e) {
                for (var t = e.position; e.position < t + this.size;) {
                    var r = i.parseOneDescriptor(e);
                    this.descs.push(r)
                }
            }, s.ES_Descriptor = function (e) {
                s.Descriptor.call(this, 3, e)
            }, s.ES_Descriptor.prototype = new s.Descriptor, s.ES_Descriptor.prototype.parse = function (e) {
                var t;
                this.ES_ID = e.readUint16(), this.flags = e.readUint8(), this.size -= 3, 128 & this.flags ? (this.dependsOn_ES_ID = e.readUint16(), this.size -= 2) : this.dependsOn_ES_ID = 0, 64 & this.flags ? (t = e.readUint8(), this.URL = e.readString(t), this.size -= t + 1) : this.URL = "", 32 & this.flags ? (this.OCR_ES_ID = e.readUint16(), this.size -= 2) : this.OCR_ES_ID = 0, this.parseRemainingDescriptors(e)
            }, s.ES_Descriptor.prototype.getOTI = function (e) {
                var t = this.findDescriptor(4);
                return t ? t.oti : 0
            }, s.ES_Descriptor.prototype.getAudioConfig = function (e) {
                var t = this.findDescriptor(4);
                if (!t) return null;
                var r, t = t.findDescriptor(5);
                return t && t.data ? 31 === (r = (248 & t.data[0]) >> 3) && 2 <= t.data.length ? 32 + ((7 & t.data[0]) << 3) + ((224 & t.data[1]) >> 5) : r : null
            }, s.DecoderConfigDescriptor = function (e) {
                s.Descriptor.call(this, 4, e)
            }, s.DecoderConfigDescriptor.prototype = new s.Descriptor, s.DecoderConfigDescriptor.prototype.parse = function (e) {
                this.oti = e.readUint8(), this.streamType = e.readUint8(), this.bufferSize = e.readUint24(), this.maxBitrate = e.readUint32(), this.avgBitrate = e.readUint32(), this.size -= 13, this.parseRemainingDescriptors(e)
            }, s.DecoderSpecificInfo = function (e) {
                s.Descriptor.call(this, 5, e)
            }, s.DecoderSpecificInfo.prototype = new s.Descriptor, s.SLConfigDescriptor = function (e) {
                s.Descriptor.call(this, 6, e)
            }, s.SLConfigDescriptor.prototype = new s.Descriptor, this
        }

        function n() {
        }

        function s() {
        }

        function B(e) {
            this.stream = e || new r, this.boxes = [], this.mdats = [], this.moofs = [], this.isProgressive = !1, this.moovStartFound = !1, this.onMoovStart = null, this.moovStartSent = !1, this.onReady = null, this.readySent = !1, this.onSegment = null, this.onSamples = null, this.onError = null, this.sampleListBuilt = !1, this.fragmentedTracks = [], this.extractedTracks = [], this.isFragmentationInitialized = !1, this.sampleProcessingStarted = !1, this.nextMoofNumber = 0, this.itemListBuilt = !1, this.onSidx = null, this.sidxSent = !1
        }

        a = new Date, o = 4;
        var a, o, u = {
            setLogLevel: function (e) {
                o = e == this.debug ? 1 : e == this.info ? 2 : e == this.warn ? 3 : (this.error, 4)
            }, debug: function (e, t) {
                void 0 === console.debug && (console.debug = console.log), o <= 1 && console.debug("[" + u.getDurationString(new Date - a, 1e3) + "]", "[" + e + "]", t)
            }, log: function (e, t) {
                this.debug(e.msg)
            }, info: function (e, t) {
                o <= 2 && console.info("[" + u.getDurationString(new Date - a, 1e3) + "]", "[" + e + "]", t)
            }, warn: function (e, t) {
                o <= 3 && console.warn("[" + u.getDurationString(new Date - a, 1e3) + "]", "[" + e + "]", t)
            }, error: function (e, t) {
                o <= 4 && console.error("[" + u.getDurationString(new Date - a, 1e3) + "]", "[" + e + "]", t)
            }
        }, d = (u.getDurationString = function (e, t) {
            var r;

            function i(e, t) {
                for (var r = ("" + e).split("."); r[0].length < t;) r[0] = "0" + r[0];
                return r.join(".")
            }

            e < 0 ? (r = !0, e = -e) : r = !1;
            var e = e / (t || 1), t = Math.floor(e / 3600), n = (e -= 3600 * t, Math.floor(e / 60)),
                s = 1e3 * (e -= 60 * n);
            return s -= 1e3 * (e = Math.floor(e)), s = Math.floor(s), (r ? "-" : "") + t + ":" + i(n, 2) + ":" + i(e, 2) + "." + i(s, 3)
        }, u.printRanges = function (e) {
            var t = e.length;
            if (0 < t) {
                for (var r = "", i = 0; i < t; i++) 0 < i && (r += ","), r += "[" + u.getDurationString(e.start(i)) + "," + u.getDurationString(e.end(i)) + "]";
                return r
            }
            return "(empty)"
        }, t.Log = u, f.prototype.getPosition = function () {
            return this.position
        }, f.prototype.getEndPosition = function () {
            return this.buffer.byteLength
        }, f.prototype.getLength = function () {
            return this.buffer.byteLength
        }, f.prototype.seek = function (e) {
            e = Math.max(0, Math.min(this.buffer.byteLength, e));
            return this.position = isNaN(e) || !isFinite(e) ? 0 : e, !0
        }, f.prototype.isEos = function () {
            return this.getPosition() >= this.getEndPosition()
        }, f.prototype.readAnyInt = function (e, t) {
            var r = 0;
            if (this.position + e <= this.buffer.byteLength) {
                switch (e) {
                    case 1:
                        r = t ? this.dataview.getInt8(this.position) : this.dataview.getUint8(this.position);
                        break;
                    case 2:
                        r = t ? this.dataview.getInt16(this.position) : this.dataview.getUint16(this.position);
                        break;
                    case 3:
                        if (t) throw"No method for reading signed 24 bits values";
                        r = this.dataview.getUint8(this.position) << 16, r = (r |= this.dataview.getUint8(this.position + 1) << 8) | this.dataview.getUint8(this.position + 2);
                        break;
                    case 4:
                        r = t ? this.dataview.getInt32(this.position) : this.dataview.getUint32(this.position);
                        break;
                    case 8:
                        if (t) throw"No method for reading signed 64 bits values";
                        r = this.dataview.getUint32(this.position) << 32, r |= this.dataview.getUint32(this.position + 4);
                        break;
                    default:
                        throw"readInt method not implemented for size: " + e
                }
                return this.position += e, r
            }
            throw"Not enough bytes in buffer"
        }, f.prototype.readUint8 = function () {
            return this.readAnyInt(1, !1)
        }, f.prototype.readUint16 = function () {
            return this.readAnyInt(2, !1)
        }, f.prototype.readUint24 = function () {
            return this.readAnyInt(3, !1)
        }, f.prototype.readUint32 = function () {
            return this.readAnyInt(4, !1)
        }, f.prototype.readUint64 = function () {
            return this.readAnyInt(8, !1)
        }, f.prototype.readString = function (e) {
            if (this.position + e <= this.buffer.byteLength) {
                for (var t = "", r = 0; r < e; r++) t += String.fromCharCode(this.readUint8());
                return t
            }
            throw"Not enough bytes in buffer"
        }, f.prototype.readCString = function () {
            for (var e = []; ;) {
                var t = this.readUint8();
                if (0 === t) break;
                e.push(t)
            }
            return String.fromCharCode.apply(null, e)
        }, f.prototype.readInt8 = function () {
            return this.readAnyInt(1, !0)
        }, f.prototype.readInt16 = function () {
            return this.readAnyInt(2, !0)
        }, f.prototype.readInt32 = function () {
            return this.readAnyInt(4, !0)
        }, f.prototype.readInt64 = function () {
            return this.readAnyInt(8, !1)
        }, f.prototype.readUint8Array = function (e) {
            for (var t = new Uint8Array(e), r = 0; r < e; r++) t[r] = this.readUint8();
            return t
        }, f.prototype.readInt16Array = function (e) {
            for (var t = new Int16Array(e), r = 0; r < e; r++) t[r] = this.readInt16();
            return t
        }, f.prototype.readUint16Array = function (e) {
            for (var t = new Int16Array(e), r = 0; r < e; r++) t[r] = this.readUint16();
            return t
        }, f.prototype.readUint32Array = function (e) {
            for (var t = new Uint32Array(e), r = 0; r < e; r++) t[r] = this.readUint32();
            return t
        }, f.prototype.readInt32Array = function (e) {
            for (var t = new Int32Array(e), r = 0; r < e; r++) t[r] = this.readInt32();
            return t
        }, t.MP4BoxStream = f, (l.prototype = {}).getPosition = function () {
            return this.position
        }, l.prototype._realloc = function (e) {
            if (this._dynamicSize) {
                var t = this._byteOffset + this.position + e, r = this._buffer.byteLength;
                if (t <= r) t > this._byteLength && (this._byteLength = t); else {
                    for (r < 1 && (r = 1); r < t;) r *= 2;
                    var e = new ArrayBuffer(r), i = new Uint8Array(this._buffer);
                    new Uint8Array(e, 0, i.length).set(i), this.buffer = e, this._byteLength = t
                }
            }
        }, l.prototype._trimAlloc = function () {
            var e, t, r;
            this._byteLength != this._buffer.byteLength && (e = new ArrayBuffer(this._byteLength), t = new Uint8Array(e), r = new Uint8Array(this._buffer, 0, t.length), t.set(r), this.buffer = e)
        }, l.BIG_ENDIAN = !1, l.LITTLE_ENDIAN = !0, l.prototype._byteLength = 0, Object.defineProperty(l.prototype, "byteLength", {
            get: function () {
                return this._byteLength - this._byteOffset
            }
        }), Object.defineProperty(l.prototype, "buffer", {
            get: function () {
                return this._trimAlloc(), this._buffer
            }, set: function (e) {
                this._buffer = e, this._dataView = new DataView(this._buffer, this._byteOffset), this._byteLength = this._buffer.byteLength
            }
        }), Object.defineProperty(l.prototype, "byteOffset", {
            get: function () {
                return this._byteOffset
            }, set: function (e) {
                this._byteOffset = e, this._dataView = new DataView(this._buffer, this._byteOffset), this._byteLength = this._buffer.byteLength
            }
        }), Object.defineProperty(l.prototype, "dataView", {
            get: function () {
                return this._dataView
            }, set: function (e) {
                this._byteOffset = e.byteOffset, this._buffer = e.buffer, this._dataView = new DataView(this._buffer, this._byteOffset), this._byteLength = this._byteOffset + e.byteLength
            }
        }), l.prototype.seek = function (e) {
            e = Math.max(0, Math.min(this.byteLength, e));
            this.position = isNaN(e) || !isFinite(e) ? 0 : e
        }, l.prototype.isEof = function () {
            return this.position >= this._byteLength
        }, l.prototype.mapUint8Array = function (e) {
            this._realloc(+e);
            var t = new Uint8Array(this._buffer, this.byteOffset + this.position, e);
            return this.position += +e, t
        }, l.prototype.readInt32Array = function (e, t) {
            e = null == e ? this.byteLength - this.position / 4 : e;
            var r = new Int32Array(e);
            return l.memcpy(r.buffer, 0, this.buffer, this.byteOffset + this.position, e * r.BYTES_PER_ELEMENT), l.arrayToNative(r, null == t ? this.endianness : t), this.position += r.byteLength, r
        }, l.prototype.readInt16Array = function (e, t) {
            e = null == e ? this.byteLength - this.position / 2 : e;
            var r = new Int16Array(e);
            return l.memcpy(r.buffer, 0, this.buffer, this.byteOffset + this.position, e * r.BYTES_PER_ELEMENT), l.arrayToNative(r, null == t ? this.endianness : t), this.position += r.byteLength, r
        }, l.prototype.readInt8Array = function (e) {
            e = null == e ? this.byteLength - this.position : e;
            var t = new Int8Array(e);
            return l.memcpy(t.buffer, 0, this.buffer, this.byteOffset + this.position, e * t.BYTES_PER_ELEMENT), this.position += t.byteLength, t
        }, l.prototype.readUint32Array = function (e, t) {
            e = null == e ? this.byteLength - this.position / 4 : e;
            var r = new Uint32Array(e);
            return l.memcpy(r.buffer, 0, this.buffer, this.byteOffset + this.position, e * r.BYTES_PER_ELEMENT), l.arrayToNative(r, null == t ? this.endianness : t), this.position += r.byteLength, r
        }, l.prototype.readUint16Array = function (e, t) {
            e = null == e ? this.byteLength - this.position / 2 : e;
            var r = new Uint16Array(e);
            return l.memcpy(r.buffer, 0, this.buffer, this.byteOffset + this.position, e * r.BYTES_PER_ELEMENT), l.arrayToNative(r, null == t ? this.endianness : t), this.position += r.byteLength, r
        }, l.prototype.readUint8Array = function (e) {
            e = null == e ? this.byteLength - this.position : e;
            var t = new Uint8Array(e);
            return l.memcpy(t.buffer, 0, this.buffer, this.byteOffset + this.position, e * t.BYTES_PER_ELEMENT), this.position += t.byteLength, t
        }, l.prototype.readFloat64Array = function (e, t) {
            e = null == e ? this.byteLength - this.position / 8 : e;
            var r = new Float64Array(e);
            return l.memcpy(r.buffer, 0, this.buffer, this.byteOffset + this.position, e * r.BYTES_PER_ELEMENT), l.arrayToNative(r, null == t ? this.endianness : t), this.position += r.byteLength, r
        }, l.prototype.readFloat32Array = function (e, t) {
            e = null == e ? this.byteLength - this.position / 4 : e;
            var r = new Float32Array(e);
            return l.memcpy(r.buffer, 0, this.buffer, this.byteOffset + this.position, e * r.BYTES_PER_ELEMENT), l.arrayToNative(r, null == t ? this.endianness : t), this.position += r.byteLength, r
        }, l.prototype.readInt32 = function (e) {
            e = this._dataView.getInt32(this.position, null == e ? this.endianness : e);
            return this.position += 4, e
        }, l.prototype.readInt16 = function (e) {
            e = this._dataView.getInt16(this.position, null == e ? this.endianness : e);
            return this.position += 2, e
        }, l.prototype.readInt8 = function () {
            var e = this._dataView.getInt8(this.position);
            return this.position += 1, e
        }, l.prototype.readUint32 = function (e) {
            e = this._dataView.getUint32(this.position, null == e ? this.endianness : e);
            return this.position += 4, e
        }, l.prototype.readUint16 = function (e) {
            e = this._dataView.getUint16(this.position, null == e ? this.endianness : e);
            return this.position += 2, e
        }, l.prototype.readUint8 = function () {
            var e = this._dataView.getUint8(this.position);
            return this.position += 1, e
        }, l.prototype.readFloat32 = function (e) {
            e = this._dataView.getFloat32(this.position, null == e ? this.endianness : e);
            return this.position += 4, e
        }, l.prototype.readFloat64 = function (e) {
            e = this._dataView.getFloat64(this.position, null == e ? this.endianness : e);
            return this.position += 8, e
        }, l.endianness = 0 < new Int8Array(new Int16Array([1]).buffer)[0], l.memcpy = function (e, t, r, i, n) {
            e = new Uint8Array(e, t, n), t = new Uint8Array(r, i, n);
            e.set(t)
        }, l.arrayToNative = function (e, t) {
            return t == this.endianness ? e : this.flipArrayEndianness(e)
        }, l.nativeToEndian = function (e, t) {
            return this.endianness == t ? e : this.flipArrayEndianness(e)
        }, l.flipArrayEndianness = function (e) {
            for (var t = new Uint8Array(e.buffer, e.byteOffset, e.byteLength), r = 0; r < e.byteLength; r += e.BYTES_PER_ELEMENT) for (var i = r + e.BYTES_PER_ELEMENT - 1, n = r; n < i; i--, n++) {
                var s = t[n];
                t[n] = t[i], t[i] = s
            }
            return e
        }, l.prototype.failurePosition = 0, String.fromCharCodeUint8 = function (e) {
            for (var t = [], r = 0; r < e.length; r++) t[r] = e[r];
            return String.fromCharCode.apply(null, t)
        }, l.prototype.readString = function (e, t) {
            return null == t || "ASCII" == t ? String.fromCharCodeUint8.apply(null, [this.mapUint8Array(null == e ? this.byteLength - this.position : e)]) : new TextDecoder(t).decode(this.mapUint8Array(e))
        }, l.prototype.readCString = function (e) {
            var t = this.byteLength - this.position, r = new Uint8Array(this._buffer, this._byteOffset + this.position),
                i = t;
            null != e && (i = Math.min(e, t));
            for (var n = 0; n < i && 0 !== r[n]; n++) ;
            var s = String.fromCharCodeUint8.apply(null, [this.mapUint8Array(n)]);
            return null != e ? this.position += i - n : n != t && (this.position += 1), s
        }, Math.pow(2, 32)), b = (l.prototype.readInt64 = function () {
            return this.readInt32() * d + this.readUint32()
        }, l.prototype.readUint64 = function () {
            return this.readUint32() * d + this.readUint32()
        }, l.prototype.readInt64 = function () {
            return this.readUint32() * d + this.readUint32()
        }, l.prototype.readUint24 = function () {
            return (this.readUint8() << 16) + (this.readUint8() << 8) + this.readUint8()
        }, (t.DataStream = l).prototype.save = function (e) {
            var t = new Blob([this.buffer]);
            if (!window.URL || !URL.createObjectURL) throw"DataStream.save: Can't create object URL.";
            var t = window.URL.createObjectURL(t), r = document.createElement("a");
            document.body.appendChild(r), r.setAttribute("href", t), r.setAttribute("download", e), r.setAttribute("target", "_self"), r.click(), window.URL.revokeObjectURL(t)
        }, l.prototype._dynamicSize = !0, Object.defineProperty(l.prototype, "dynamicSize", {
            get: function () {
                return this._dynamicSize
            }, set: function (e) {
                e || this._trimAlloc(), this._dynamicSize = e
            }
        }), l.prototype.shift = function (e) {
            var t = new ArrayBuffer(this._byteLength - e), r = new Uint8Array(t),
                i = new Uint8Array(this._buffer, e, r.length);
            r.set(i), this.buffer = t, this.position -= e
        }, l.prototype.writeInt32Array = function (e, t) {
            if (this._realloc(4 * e.length), e instanceof Int32Array && this.byteOffset + this.position % e.BYTES_PER_ELEMENT === 0) l.memcpy(this._buffer, this.byteOffset + this.position, e.buffer, 0, e.byteLength), this.mapInt32Array(e.length, t); else for (var r = 0; r < e.length; r++) this.writeInt32(e[r], t)
        }, l.prototype.writeInt16Array = function (e, t) {
            if (this._realloc(2 * e.length), e instanceof Int16Array && this.byteOffset + this.position % e.BYTES_PER_ELEMENT === 0) l.memcpy(this._buffer, this.byteOffset + this.position, e.buffer, 0, e.byteLength), this.mapInt16Array(e.length, t); else for (var r = 0; r < e.length; r++) this.writeInt16(e[r], t)
        }, l.prototype.writeInt8Array = function (e) {
            if (this._realloc(+e.length), e instanceof Int8Array && this.byteOffset + this.position % e.BYTES_PER_ELEMENT === 0) l.memcpy(this._buffer, this.byteOffset + this.position, e.buffer, 0, e.byteLength), this.mapInt8Array(e.length); else for (var t = 0; t < e.length; t++) this.writeInt8(e[t])
        }, l.prototype.writeUint32Array = function (e, t) {
            if (this._realloc(4 * e.length), e instanceof Uint32Array && this.byteOffset + this.position % e.BYTES_PER_ELEMENT === 0) l.memcpy(this._buffer, this.byteOffset + this.position, e.buffer, 0, e.byteLength), this.mapUint32Array(e.length, t); else for (var r = 0; r < e.length; r++) this.writeUint32(e[r], t)
        }, l.prototype.writeUint16Array = function (e, t) {
            if (this._realloc(2 * e.length), e instanceof Uint16Array && this.byteOffset + this.position % e.BYTES_PER_ELEMENT === 0) l.memcpy(this._buffer, this.byteOffset + this.position, e.buffer, 0, e.byteLength), this.mapUint16Array(e.length, t); else for (var r = 0; r < e.length; r++) this.writeUint16(e[r], t)
        }, l.prototype.writeUint8Array = function (e) {
            if (this._realloc(+e.length), e instanceof Uint8Array && this.byteOffset + this.position % e.BYTES_PER_ELEMENT === 0) l.memcpy(this._buffer, this.byteOffset + this.position, e.buffer, 0, e.byteLength), this.mapUint8Array(e.length); else for (var t = 0; t < e.length; t++) this.writeUint8(e[t])
        }, l.prototype.writeFloat64Array = function (e, t) {
            if (this._realloc(8 * e.length), e instanceof Float64Array && this.byteOffset + this.position % e.BYTES_PER_ELEMENT === 0) l.memcpy(this._buffer, this.byteOffset + this.position, e.buffer, 0, e.byteLength), this.mapFloat64Array(e.length, t); else for (var r = 0; r < e.length; r++) this.writeFloat64(e[r], t)
        }, l.prototype.writeFloat32Array = function (e, t) {
            if (this._realloc(4 * e.length), e instanceof Float32Array && this.byteOffset + this.position % e.BYTES_PER_ELEMENT === 0) l.memcpy(this._buffer, this.byteOffset + this.position, e.buffer, 0, e.byteLength), this.mapFloat32Array(e.length, t); else for (var r = 0; r < e.length; r++) this.writeFloat32(e[r], t)
        }, l.prototype.writeInt32 = function (e, t) {
            this._realloc(4), this._dataView.setInt32(this.position, e, null == t ? this.endianness : t), this.position += 4
        }, l.prototype.writeInt16 = function (e, t) {
            this._realloc(2), this._dataView.setInt16(this.position, e, null == t ? this.endianness : t), this.position += 2
        }, l.prototype.writeInt8 = function (e) {
            this._realloc(1), this._dataView.setInt8(this.position, e), this.position += 1
        }, l.prototype.writeUint32 = function (e, t) {
            this._realloc(4), this._dataView.setUint32(this.position, e, null == t ? this.endianness : t), this.position += 4
        }, l.prototype.writeUint16 = function (e, t) {
            this._realloc(2), this._dataView.setUint16(this.position, e, null == t ? this.endianness : t), this.position += 2
        }, l.prototype.writeUint8 = function (e) {
            this._realloc(1), this._dataView.setUint8(this.position, e), this.position += 1
        }, l.prototype.writeFloat32 = function (e, t) {
            this._realloc(4), this._dataView.setFloat32(this.position, e, null == t ? this.endianness : t), this.position += 4
        }, l.prototype.writeFloat64 = function (e, t) {
            this._realloc(8), this._dataView.setFloat64(this.position, e, null == t ? this.endianness : t), this.position += 8
        }, l.prototype.writeUCS2String = function (e, t, r) {
            null == r && (r = e.length);
            for (var i = 0; i < e.length && i < r; i++) this.writeUint16(e.charCodeAt(i), t);
            for (; i < r; i++) this.writeUint16(0)
        }, l.prototype.writeString = function (e, t, r) {
            var i = 0;
            if (null == t || "ASCII" == t) if (null != r) {
                for (var n = Math.min(e.length, r), i = 0; i < n; i++) this.writeUint8(e.charCodeAt(i));
                for (; i < r; i++) this.writeUint8(0)
            } else for (i = 0; i < e.length; i++) this.writeUint8(e.charCodeAt(i)); else this.writeUint8Array(new TextEncoder(t).encode(e.substring(0, r)))
        }, l.prototype.writeCString = function (e, t) {
            var r = 0;
            if (null != t) {
                for (var i = Math.min(e.length, t), r = 0; r < i; r++) this.writeUint8(e.charCodeAt(r));
                for (; r < t; r++) this.writeUint8(0)
            } else {
                for (r = 0; r < e.length; r++) this.writeUint8(e.charCodeAt(r));
                this.writeUint8(0)
            }
        }, l.prototype.writeStruct = function (e, t) {
            for (var r = 0; r < e.length; r += 2) {
                var i = e[r + 1];
                this.writeType(i, t[e[r]], t)
            }
        }, l.prototype.writeType = function (e, t, r) {
            var i;
            if ("function" == typeof e) return e(this, t);
            if ("object" == typeof e && !(e instanceof Array)) return e.set(this, t, r);
            var n = null, s = "ASCII", r = this.position;
            switch ("string" == typeof e && /:/.test(e) && (e = (i = e.split(":"))[0], n = parseInt(i[1])), "string" == typeof e && /,/.test(e) && (e = (i = e.split(","))[0], s = parseInt(i[1])), e) {
                case"uint8":
                    this.writeUint8(t);
                    break;
                case"int8":
                    this.writeInt8(t);
                    break;
                case"uint16":
                    this.writeUint16(t, this.endianness);
                    break;
                case"int16":
                    this.writeInt16(t, this.endianness);
                    break;
                case"uint32":
                    this.writeUint32(t, this.endianness);
                    break;
                case"int32":
                    this.writeInt32(t, this.endianness);
                    break;
                case"float32":
                    this.writeFloat32(t, this.endianness);
                    break;
                case"float64":
                    this.writeFloat64(t, this.endianness);
                    break;
                case"uint16be":
                    this.writeUint16(t, l.BIG_ENDIAN);
                    break;
                case"int16be":
                    this.writeInt16(t, l.BIG_ENDIAN);
                    break;
                case"uint32be":
                    this.writeUint32(t, l.BIG_ENDIAN);
                    break;
                case"int32be":
                    this.writeInt32(t, l.BIG_ENDIAN);
                    break;
                case"float32be":
                    this.writeFloat32(t, l.BIG_ENDIAN);
                    break;
                case"float64be":
                    this.writeFloat64(t, l.BIG_ENDIAN);
                    break;
                case"uint16le":
                    this.writeUint16(t, l.LITTLE_ENDIAN);
                    break;
                case"int16le":
                    this.writeInt16(t, l.LITTLE_ENDIAN);
                    break;
                case"uint32le":
                    this.writeUint32(t, l.LITTLE_ENDIAN);
                    break;
                case"int32le":
                    this.writeInt32(t, l.LITTLE_ENDIAN);
                    break;
                case"float32le":
                    this.writeFloat32(t, l.LITTLE_ENDIAN);
                    break;
                case"float64le":
                    this.writeFloat64(t, l.LITTLE_ENDIAN);
                    break;
                case"cstring":
                    this.writeCString(t, n);
                    break;
                case"string":
                    this.writeString(t, s, n);
                    break;
                case"u16string":
                    this.writeUCS2String(t, this.endianness, n);
                    break;
                case"u16stringle":
                    this.writeUCS2String(t, l.LITTLE_ENDIAN, n);
                    break;
                case"u16stringbe":
                    this.writeUCS2String(t, l.BIG_ENDIAN, n);
                    break;
                default:
                    if (3 == e.length) {
                        for (var a = e[1], o = 0; o < t.length; o++) this.writeType(a, t[o]);
                        break
                    }
                    this.writeStruct(e, t)
            }
            null != n && (this.position = r, this._realloc(n), this.position = r + n)
        }, l.prototype.writeUint64 = function (e) {
            var t = Math.floor(e / d);
            this.writeUint32(t), this.writeUint32(4294967295 & e)
        }, l.prototype.writeUint24 = function (e) {
            this.writeUint8((16711680 & e) >> 16), this.writeUint8((65280 & e) >> 8), this.writeUint8(255 & e)
        }, l.prototype.adjustUint32 = function (e, t) {
            var r = this.position;
            this.seek(e), this.writeUint32(t), this.seek(r)
        }, l.prototype.mapInt32Array = function (e, t) {
            this._realloc(4 * e);
            var r = new Int32Array(this._buffer, this.byteOffset + this.position, e);
            return l.arrayToNative(r, null == t ? this.endianness : t), this.position += 4 * e, r
        }, l.prototype.mapInt16Array = function (e, t) {
            this._realloc(2 * e);
            var r = new Int16Array(this._buffer, this.byteOffset + this.position, e);
            return l.arrayToNative(r, null == t ? this.endianness : t), this.position += 2 * e, r
        }, l.prototype.mapInt8Array = function (e) {
            this._realloc(+e);
            var t = new Int8Array(this._buffer, this.byteOffset + this.position, e);
            return this.position += +e, t
        }, l.prototype.mapUint32Array = function (e, t) {
            this._realloc(4 * e);
            var r = new Uint32Array(this._buffer, this.byteOffset + this.position, e);
            return l.arrayToNative(r, null == t ? this.endianness : t), this.position += 4 * e, r
        }, l.prototype.mapUint16Array = function (e, t) {
            this._realloc(2 * e);
            var r = new Uint16Array(this._buffer, this.byteOffset + this.position, e);
            return l.arrayToNative(r, null == t ? this.endianness : t), this.position += 2 * e, r
        }, l.prototype.mapFloat64Array = function (e, t) {
            this._realloc(8 * e);
            var r = new Float64Array(this._buffer, this.byteOffset + this.position, e);
            return l.arrayToNative(r, null == t ? this.endianness : t), this.position += 8 * e, r
        }, l.prototype.mapFloat32Array = function (e, t) {
            this._realloc(4 * e);
            var r = new Float32Array(this._buffer, this.byteOffset + this.position, e);
            return l.arrayToNative(r, null == t ? this.endianness : t), this.position += 4 * e, r
        }, (r.prototype = new l(new ArrayBuffer, 0, l.BIG_ENDIAN)).initialized = function () {
            var e;
            return -1 < this.bufferIndex || (0 < this.buffers.length ? 0 === (e = this.buffers[0]).fileStart ? (this.buffer = e, this.bufferIndex = 0, u.debug("MultiBufferStream", "Stream ready for parsing"), !0) : (u.warn("MultiBufferStream", "The first buffer should have a fileStart of 0"), this.logBufferLevel(), !1) : (u.warn("MultiBufferStream", "No buffer to start parsing from"), this.logBufferLevel(), !1))
        }, ArrayBuffer.concat = function (e, t) {
            u.debug("ArrayBuffer", "Trying to create a new buffer of size: " + (e.byteLength + t.byteLength));
            var r = new Uint8Array(e.byteLength + t.byteLength);
            return r.set(new Uint8Array(e), 0), r.set(new Uint8Array(t), e.byteLength), r.buffer
        }, r.prototype.reduceBuffer = function (e, t, r) {
            var i;
            return (i = new Uint8Array(r)).set(new Uint8Array(e, t, r)), i.buffer.fileStart = e.fileStart + t, i.buffer.usedBytes = 0, i.buffer
        }, r.prototype.insertBuffer = function (e) {
            for (var t = !0, r = 0; r < this.buffers.length; r++) {
                var i = this.buffers[r];
                if (e.fileStart <= i.fileStart) {
                    if (e.fileStart === i.fileStart) {
                        if (e.byteLength > i.byteLength) {
                            this.buffers.splice(r, 1), r--;
                            continue
                        }
                        u.warn("MultiBufferStream", "Buffer (fileStart: " + e.fileStart + " - Length: " + e.byteLength + ") already appended, ignoring")
                    } else e.fileStart + e.byteLength <= i.fileStart || (e = this.reduceBuffer(e, 0, i.fileStart - e.fileStart)), u.debug("MultiBufferStream", "Appending new buffer (fileStart: " + e.fileStart + " - Length: " + e.byteLength + ")"), this.buffers.splice(r, 0, e), 0 === r && (this.buffer = e);
                    t = !1;
                    break
                }
                if (e.fileStart < i.fileStart + i.byteLength) {
                    var i = i.fileStart + i.byteLength - e.fileStart, n = e.byteLength - i;
                    if (!(0 < n)) {
                        t = !1;
                        break
                    }
                    e = this.reduceBuffer(e, i, n)
                }
            }
            t && (u.debug("MultiBufferStream", "Appending new buffer (fileStart: " + e.fileStart + " - Length: " + e.byteLength + ")"), this.buffers.push(e), 0 === r && (this.buffer = e))
        }, r.prototype.logBufferLevel = function (e) {
            for (var t, r, i = [], n = "", s = 0, a = 0, o = 0; o < this.buffers.length; o++) t = this.buffers[o], 0 === o ? (i.push(r = {}), r.start = t.fileStart, r.end = t.fileStart + t.byteLength, n += "[" + r.start + "-") : r.end === t.fileStart ? r.end = t.fileStart + t.byteLength : ((r = {}).start = t.fileStart, n += i[i.length - 1].end - 1 + "], [" + r.start + "-", r.end = t.fileStart + t.byteLength, i.push(r)), s += t.usedBytes, a += t.byteLength;
            0 < i.length && (n += r.end - 1 + "]");
            e = e ? u.info : u.debug;
            0 === this.buffers.length ? e("MultiBufferStream", "No more buffer in memory") : e("MultiBufferStream", this.buffers.length + " stored buffer(s) (" + s + "/" + a + " bytes), continuous ranges: " + n)
        }, r.prototype.cleanBuffers = function () {
            for (var e, t = 0; t < this.buffers.length; t++) (e = this.buffers[t]).usedBytes === e.byteLength && (u.debug("MultiBufferStream", "Removing buffer #" + t), this.buffers.splice(t, 1), t--)
        }, r.prototype.mergeNextBuffer = function () {
            var e, t, r, i;
            return this.bufferIndex + 1 < this.buffers.length && ((e = this.buffers[this.bufferIndex + 1]).fileStart === this.buffer.fileStart + this.buffer.byteLength && (t = this.buffer.byteLength, r = this.buffer.usedBytes, i = this.buffer.fileStart, this.buffers[this.bufferIndex] = ArrayBuffer.concat(this.buffer, e), this.buffer = this.buffers[this.bufferIndex], this.buffers.splice(this.bufferIndex + 1, 1), this.buffer.usedBytes = r, this.buffer.fileStart = i, u.debug("ISOFile", "Concatenating buffer for box parsing (length: " + t + "->" + this.buffer.byteLength + ")"), !0))
        }, r.prototype.findPosition = function (e, t, r) {
            for (var i = null, n = -1, s = !0 === e ? 0 : this.bufferIndex; s < this.buffers.length && (i = this.buffers[s]).fileStart <= t;) n = s, r && (i.fileStart + i.byteLength <= t ? i.usedBytes = i.byteLength : i.usedBytes = t - i.fileStart, this.logBufferLevel()), s++;
            return -1 !== n && (i = this.buffers[n]).fileStart + i.byteLength >= t ? (u.debug("MultiBufferStream", "Found position in existing buffer #" + n), n) : -1
        }, r.prototype.findEndContiguousBuf = function (e) {
            var t, r, e = void 0 !== e ? e : this.bufferIndex, i = this.buffers[e];
            if (this.buffers.length > e + 1) for (t = e + 1; t < this.buffers.length && (r = this.buffers[t]).fileStart === i.fileStart + i.byteLength; t++) i = r;
            return i.fileStart + i.byteLength
        }, r.prototype.getEndFilePositionAfter = function (e) {
            var t = this.findPosition(!0, e, !1);
            return -1 !== t ? this.findEndContiguousBuf(t) : e
        }, r.prototype.addUsedBytes = function (e) {
            this.buffer.usedBytes += e, this.logBufferLevel()
        }, r.prototype.setAllUsedBytes = function () {
            this.buffer.usedBytes = this.buffer.byteLength, this.logBufferLevel()
        }, r.prototype.seek = function (e, t, r) {
            return -1 !== (t = this.findPosition(t, e, r)) ? (this.buffer = this.buffers[t], this.bufferIndex = t, this.position = e - this.buffer.fileStart, u.debug("MultiBufferStream", "Repositioning parser at buffer position: " + this.position), !0) : (u.debug("MultiBufferStream", "Position " + e + " not found in buffered data"), !1)
        }, r.prototype.getPosition = function () {
            if (-1 === this.bufferIndex || null === this.buffers[this.bufferIndex]) throw"Error accessing position in the MultiBufferStream";
            return this.buffers[this.bufferIndex].fileStart + this.position
        }, r.prototype.getLength = function () {
            return this.byteLength
        }, r.prototype.getEndPosition = function () {
            if (-1 === this.bufferIndex || null === this.buffers[this.bufferIndex]) throw"Error accessing position in the MultiBufferStream";
            return this.buffers[this.bufferIndex].fileStart + this.byteLength
        }, t.MultiBufferStream = r, t.MPEG4DescriptorParser = i, {
            ERR_INVALID_DATA: -1,
            ERR_NOT_ENOUGH_DATA: 0,
            OK: 1,
            BASIC_BOXES: ["mdat", "idat", "free", "skip", "meco", "strk"],
            FULL_BOXES: ["hmhd", "nmhd", "iods", "xml ", "bxml", "ipro", "mere"],
            CONTAINER_BOXES: [["moov", ["trak", "pssh"]], ["trak"], ["edts"], ["mdia"], ["minf"], ["dinf"], ["stbl", ["sgpd", "sbgp"]], ["mvex", ["trex"]], ["moof", ["traf"]], ["traf", ["trun", "sgpd", "sbgp"]], ["vttc"], ["tref"], ["iref"], ["mfra", ["tfra"]], ["meco"], ["hnti"], ["hinf"], ["strk"], ["strd"], ["sinf"], ["rinf"], ["schi"], ["trgr"], ["udta", ["kind"]], ["iprp", ["ipma"]], ["ipco"]],
            boxCodes: [],
            fullBoxCodes: [],
            containerBoxCodes: [],
            sampleEntryCodes: {},
            sampleGroupEntryCodes: [],
            trackGroupTypes: [],
            UUIDBoxes: {},
            UUIDs: [],
            initialize: function () {
                b.FullBox.prototype = new b.Box, b.ContainerBox.prototype = new b.Box, b.SampleEntry.prototype = new b.Box, b.TrackGroupTypeBox.prototype = new b.FullBox, b.BASIC_BOXES.forEach(function (e) {
                    b.createBoxCtor(e)
                }), b.FULL_BOXES.forEach(function (e) {
                    b.createFullBoxCtor(e)
                }), b.CONTAINER_BOXES.forEach(function (e) {
                    b.createContainerBoxCtor(e[0], null, e[1])
                })
            },
            Box: function (e, t, r) {
                this.type = e, this.size = t, this.uuid = r
            },
            FullBox: function (e, t, r) {
                b.Box.call(this, e, t, r), this.flags = 0, this.version = 0
            },
            ContainerBox: function (e, t, r) {
                b.Box.call(this, e, t, r), this.boxes = []
            },
            SampleEntry: function (e, t, r, i) {
                b.ContainerBox.call(this, e, t), this.hdr_size = r, this.start = i
            },
            SampleGroupEntry: function (e) {
                this.grouping_type = e
            },
            TrackGroupTypeBox: function (e, t) {
                b.FullBox.call(this, e, t)
            },
            createBoxCtor: function (t, e) {
                b.boxCodes.push(t), b[t + "Box"] = function (e) {
                    b.Box.call(this, t, e)
                }, b[t + "Box"].prototype = new b.Box, e && (b[t + "Box"].prototype.parse = e)
            },
            createFullBoxCtor: function (t, r) {
                b[t + "Box"] = function (e) {
                    b.FullBox.call(this, t, e)
                }, b[t + "Box"].prototype = new b.FullBox, b[t + "Box"].prototype.parse = function (e) {
                    this.parseFullHeader(e), r && r.call(this, e)
                }
            },
            addSubBoxArrays: function (e) {
                if (e) for (var t = (this.subBoxNames = e).length, r = 0; r < t; r++) this[e[r] + "s"] = []
            },
            createContainerBoxCtor: function (t, e, r) {
                b[t + "Box"] = function (e) {
                    b.ContainerBox.call(this, t, e), b.addSubBoxArrays.call(this, r)
                }, b[t + "Box"].prototype = new b.ContainerBox, e && (b[t + "Box"].prototype.parse = e)
            },
            createMediaSampleEntryCtor: function (e, t, r) {
                b.sampleEntryCodes[e] = [], b[e + "SampleEntry"] = function (e, t) {
                    b.SampleEntry.call(this, e, t), b.addSubBoxArrays.call(this, r)
                }, b[e + "SampleEntry"].prototype = new b.SampleEntry, t && (b[e + "SampleEntry"].prototype.parse = t)
            },
            createSampleEntryCtor: function (t, r, e, i) {
                b.sampleEntryCodes[t].push(r), b[r + "SampleEntry"] = function (e) {
                    b[t + "SampleEntry"].call(this, r, e), b.addSubBoxArrays.call(this, i)
                }, b[r + "SampleEntry"].prototype = new b[t + "SampleEntry"], e && (b[r + "SampleEntry"].prototype.parse = e)
            },
            createEncryptedSampleEntryCtor: function (e, t, r) {
                b.createSampleEntryCtor.call(this, e, t, r, ["sinf"])
            },
            createSampleGroupCtor: function (t, e) {
                b[t + "SampleGroupEntry"] = function (e) {
                    b.SampleGroupEntry.call(this, t, e)
                }, b[t + "SampleGroupEntry"].prototype = new b.SampleGroupEntry, e && (b[t + "SampleGroupEntry"].prototype.parse = e)
            },
            createTrackGroupCtor: function (t, e) {
                b[t + "TrackGroupTypeBox"] = function (e) {
                    b.TrackGroupTypeBox.call(this, t, e)
                }, b[t + "TrackGroupTypeBox"].prototype = new b.TrackGroupTypeBox, e && (b[t + "TrackGroupTypeBox"].prototype.parse = e)
            },
            createUUIDBox: function (t, r, i, n) {
                b.UUIDs.push(t), b.UUIDBoxes[t] = function (e) {
                    (r ? b.FullBox : i ? b.ContainerBox : b.Box).call(this, "uuid", e, t)
                }, b.UUIDBoxes[t].prototype = new (r ? b.FullBox : i ? b.ContainerBox : b.Box), n && (b.UUIDBoxes[t].prototype.parse = r ? function (e) {
                    this.parseFullHeader(e), n && n.call(this, e)
                } : n)
            }
        });
        b.initialize(), b.TKHD_FLAG_ENABLED = 1, b.TKHD_FLAG_IN_MOVIE = 2, b.TKHD_FLAG_IN_PREVIEW = 4, b.TFHD_FLAG_BASE_DATA_OFFSET = 1, b.TFHD_FLAG_SAMPLE_DESC = 2, b.TFHD_FLAG_SAMPLE_DUR = 8, b.TFHD_FLAG_SAMPLE_SIZE = 16, b.TFHD_FLAG_SAMPLE_FLAGS = 32, b.TFHD_FLAG_DUR_EMPTY = 65536, b.TFHD_FLAG_DEFAULT_BASE_IS_MOOF = 131072, b.TRUN_FLAGS_DATA_OFFSET = 1, b.TRUN_FLAGS_FIRST_FLAG = 4, b.TRUN_FLAGS_DURATION = 256, b.TRUN_FLAGS_SIZE = 512, b.TRUN_FLAGS_FLAGS = 1024, b.TRUN_FLAGS_CTS_OFFSET = 2048, b.Box.prototype.add = function (e) {
            return this.addBox(new b[e + "Box"])
        }, b.Box.prototype.addBox = function (e) {
            return this.boxes.push(e), this[e.type + "s"] ? this[e.type + "s"].push(e) : this[e.type] = e, e
        }, b.Box.prototype.set = function (e, t) {
            return this[e] = t, this
        }, b.Box.prototype.addEntry = function (e, t) {
            t = t || "entries";
            return this[t] || (this[t] = []), this[t].push(e), this
        }, (t.BoxParser = b).parseUUID = function (e) {
            return b.parseHex16(e)
        }, b.parseHex16 = function (e) {
            for (var t = "", r = 0; r < 16; r++) {
                var i = e.readUint8().toString(16);
                t += 1 === i.length ? "0" + i : i
            }
            return t
        }, b.parseOneBox = function (e, t, r) {
            var i, n, s = e.getPosition(), a = 0;
            if (e.getEndPosition() - s < 8) return u.debug("BoxParser", "Not enough data in stream to parse the type and size of the box"), {code: b.ERR_NOT_ENOUGH_DATA};
            if (r && r < 8) return u.debug("BoxParser", "Not enough bytes left in the parent box to parse a new box"), {code: b.ERR_NOT_ENOUGH_DATA};
            var o = e.readUint32(), l = e.readString(4), d = l;
            if (u.debug("BoxParser", "Found box of type '" + l + "' and size " + o + " at position " + s), a = 8, "uuid" == l) {
                if (e.getEndPosition() - e.getPosition() < 16 || r - a < 16) return e.seek(s), u.debug("BoxParser", "Not enough bytes left in the parent box to parse a UUID box"), {code: b.ERR_NOT_ENOUGH_DATA};
                a += 16, d = n = b.parseUUID(e)
            }
            if (1 == o) {
                if (e.getEndPosition() - e.getPosition() < 8 || r && r - a < 8) return e.seek(s), u.warn("BoxParser", 'Not enough data in stream to parse the extended size of the "' + l + '" box'), {code: b.ERR_NOT_ENOUGH_DATA};
                o = e.readUint64(), a += 8
            } else if (0 === o) if (r) o = r; else if ("mdat" !== l) return u.error("BoxParser", "Unlimited box size not supported for type: '" + l + "'"), i = new b.Box(l, o), {
                code: b.OK,
                box: i,
                size: i.size
            };
            return 0 !== o && o < a ? (u.error("BoxParser", "Box of type " + l + " has an invalid size " + o + " (too small to be a box)"), {
                code: b.ERR_NOT_ENOUGH_DATA,
                type: l,
                size: o,
                hdr_size: a,
                start: s
            }) : 0 !== o && r && r < o ? (u.error("BoxParser", "Box of type '" + l + "' has a size " + o + " greater than its container size " + r), {
                code: b.ERR_NOT_ENOUGH_DATA,
                type: l,
                size: o,
                hdr_size: a,
                start: s
            }) : 0 !== o && s + o > e.getEndPosition() ? (e.seek(s), u.info("BoxParser", "Not enough data in stream to parse the entire '" + l + "' box"), {
                code: b.ERR_NOT_ENOUGH_DATA,
                type: l,
                size: o,
                hdr_size: a,
                start: s
            }) : t ? {
                code: b.OK,
                type: l,
                size: o,
                hdr_size: a,
                start: s
            } : (b[l + "Box"] ? i = new b[l + "Box"](o) : "uuid" !== l ? (u.warn("BoxParser", "Unknown box type: '" + l + "'"), (i = new b.Box(l, o)).has_unparsed_data = !0) : b.UUIDBoxes[n] ? i = new b.UUIDBoxes[n](o) : (u.warn("BoxParser", "Unknown uuid type: '" + n + "'"), (i = new b.Box(l, o)).uuid = n, i.has_unparsed_data = !0), i.hdr_size = a, i.start = s, i.write === b.Box.prototype.write && "mdat" !== i.type && (u.info("BoxParser", "'" + d + "' box writing not yet implemented, keeping unparsed data in memory for later write"), i.parseDataAndRewind(e)), i.parse(e), (r = e.getPosition() - (i.start + i.size)) < 0 ? (u.warn("BoxParser", "Parsing of box '" + d + "' did not read the entire indicated box data size (missing " + -r + " bytes), seeking forward"), e.seek(i.start + i.size)) : 0 < r && (u.error("BoxParser", "Parsing of box '" + d + "' read " + r + " more bytes than the indicated box data size, seeking backwards"), 0 !== i.size && e.seek(i.start + i.size)), {
                code: b.OK,
                box: i,
                size: i.size
            })
        }, b.Box.prototype.parse = function (e) {
            "mdat" != this.type ? this.data = e.readUint8Array(this.size - this.hdr_size) : 0 === this.size ? e.seek(e.getEndPosition()) : e.seek(this.start + this.size)
        }, b.Box.prototype.parseDataAndRewind = function (e) {
            this.data = e.readUint8Array(this.size - this.hdr_size), e.position -= this.size - this.hdr_size
        }, b.FullBox.prototype.parseDataAndRewind = function (e) {
            this.parseFullHeader(e), this.data = e.readUint8Array(this.size - this.hdr_size), this.hdr_size -= 4, e.position -= this.size - this.hdr_size
        }, b.FullBox.prototype.parseFullHeader = function (e) {
            this.version = e.readUint8(), this.flags = e.readUint24(), this.hdr_size += 4
        }, b.FullBox.prototype.parse = function (e) {
            this.parseFullHeader(e), this.data = e.readUint8Array(this.size - this.hdr_size)
        }, b.ContainerBox.prototype.parse = function (e) {
            for (; e.getPosition() < this.start + this.size;) {
                if ((r = b.parseOneBox(e, !1, this.size - (e.getPosition() - this.start))).code !== b.OK) return;
                var t, r = r.box;
                this.boxes.push(r), this.subBoxNames && -1 != this.subBoxNames.indexOf(r.type) ? this[this.subBoxNames[this.subBoxNames.indexOf(r.type)] + "s"].push(r) : this[t = "uuid" !== r.type ? r.type : r.uuid] ? u.warn("Box of type " + t + " already stored in field of this type") : this[t] = r
            }
        }, b.Box.prototype.parseLanguage = function (e) {
            this.language = e.readUint16();
            e = [];
            e[0] = this.language >> 10 & 31, e[1] = this.language >> 5 & 31, e[2] = 31 & this.language, this.languageString = String.fromCharCode(e[0] + 96, e[1] + 96, e[2] + 96)
        }, b.SAMPLE_ENTRY_TYPE_VISUAL = "Visual", b.SAMPLE_ENTRY_TYPE_AUDIO = "Audio", b.SAMPLE_ENTRY_TYPE_HINT = "Hint", b.SAMPLE_ENTRY_TYPE_METADATA = "Metadata", b.SAMPLE_ENTRY_TYPE_SUBTITLE = "Subtitle", b.SAMPLE_ENTRY_TYPE_SYSTEM = "System", b.SAMPLE_ENTRY_TYPE_TEXT = "Text", b.SampleEntry.prototype.parseHeader = function (e) {
            e.readUint8Array(6), this.data_reference_index = e.readUint16(), this.hdr_size += 8
        }, b.SampleEntry.prototype.parse = function (e) {
            this.parseHeader(e), this.data = e.readUint8Array(this.size - this.hdr_size)
        }, b.SampleEntry.prototype.parseDataAndRewind = function (e) {
            this.parseHeader(e), this.data = e.readUint8Array(this.size - this.hdr_size), this.hdr_size -= 8, e.position -= this.size - this.hdr_size
        }, b.SampleEntry.prototype.parseFooter = function (e) {
            b.ContainerBox.prototype.parse.call(this, e)
        }, b.createMediaSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_HINT), b.createMediaSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_METADATA), b.createMediaSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_SUBTITLE), b.createMediaSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_SYSTEM), b.createMediaSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_TEXT), b.createMediaSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, function (e) {
            var t;
            this.parseHeader(e), e.readUint16(), e.readUint16(), e.readUint32Array(3), this.width = e.readUint16(), this.height = e.readUint16(), this.horizresolution = e.readUint32(), this.vertresolution = e.readUint32(), e.readUint32(), this.frame_count = e.readUint16(), t = Math.min(31, e.readUint8()), this.compressorname = e.readString(t), t < 31 && e.readString(31 - t), this.depth = e.readUint16(), e.readUint16(), this.parseFooter(e)
        }), b.createMediaSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_AUDIO, function (e) {
            this.parseHeader(e), e.readUint32Array(2), this.channel_count = e.readUint16(), this.samplesize = e.readUint16(), e.readUint16(), e.readUint16(), this.samplerate = e.readUint32() / 65536, this.parseFooter(e)
        }), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "avc1"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "avc2"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "avc3"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "avc4"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "av01"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "hvc1"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "hev1"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "vvc1"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "vvi1"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "vvs1"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "vvcN"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "vp08"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "vp09"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_AUDIO, "mp4a"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_AUDIO, "ac-3"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_AUDIO, "ec-3"), b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_AUDIO, "Opus"), b.createEncryptedSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_VISUAL, "encv"), b.createEncryptedSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_AUDIO, "enca"), b.createEncryptedSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_SUBTITLE, "encu"), b.createEncryptedSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_SYSTEM, "encs"), b.createEncryptedSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_TEXT, "enct"), b.createEncryptedSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_METADATA, "encm"), b.createBoxCtor("a1lx", function (e) {
            var t = 16 * (1 + (1 & e.readUint8()));
            this.layer_size = [];
            for (var r = 0; r < 3; r++) this.layer_size[r] = 16 == t ? e.readUint16() : e.readUint32()
        }), b.createBoxCtor("a1op", function (e) {
            this.op_index = e.readUint8()
        }), b.createFullBoxCtor("auxC", function (e) {
            this.aux_type = e.readCString();
            var t = this.size - this.hdr_size - (this.aux_type.length + 1);
            this.aux_subtype = e.readUint8Array(t)
        }), b.createBoxCtor("av1C", function (e) {
            var t = e.readUint8();
            if (t >> 7 & !1) u.error("av1C marker problem"); else if (this.version = 127 & t, 1 === this.version) if (t = e.readUint8(), this.seq_profile = t >> 5 & 7, this.seq_level_idx_0 = 31 & t, t = e.readUint8(), this.seq_tier_0 = t >> 7 & 1, this.high_bitdepth = t >> 6 & 1, this.twelve_bit = t >> 5 & 1, this.monochrome = t >> 4 & 1, this.chroma_subsampling_x = t >> 3 & 1, this.chroma_subsampling_y = t >> 2 & 1, this.chroma_sample_position = 3 & t, t = e.readUint8(), this.reserved_1 = t >> 5 & 7, 0 === this.reserved_1) {
                if (this.initial_presentation_delay_present = t >> 4 & 1, 1 === this.initial_presentation_delay_present) this.initial_presentation_delay_minus_one = 15 & t; else if (this.reserved_2 = 15 & t, 0 !== this.reserved_2) return void u.error("av1C reserved_2 parsing problem");
                t = this.size - this.hdr_size - 4;
                this.configOBUs = e.readUint8Array(t)
            } else u.error("av1C reserved_1 parsing problem"); else u.error("av1C version " + this.version + " not supported")
        }), b.createBoxCtor("avcC", function (e) {
            var t, r;
            for (this.configurationVersion = e.readUint8(), this.AVCProfileIndication = e.readUint8(), this.profile_compatibility = e.readUint8(), this.AVCLevelIndication = e.readUint8(), this.lengthSizeMinusOne = 3 & e.readUint8(), this.nb_SPS_nalus = 31 & e.readUint8(), r = this.size - this.hdr_size - 6, this.SPS = [], t = 0; t < this.nb_SPS_nalus; t++) this.SPS[t] = {}, this.SPS[t].length = e.readUint16(), this.SPS[t].nalu = e.readUint8Array(this.SPS[t].length), r -= 2 + this.SPS[t].length;
            for (this.nb_PPS_nalus = e.readUint8(), r--, this.PPS = [], t = 0; t < this.nb_PPS_nalus; t++) this.PPS[t] = {}, this.PPS[t].length = e.readUint16(), this.PPS[t].nalu = e.readUint8Array(this.PPS[t].length), r -= 2 + this.PPS[t].length;
            0 < r && (this.ext = e.readUint8Array(r))
        }), b.createBoxCtor("btrt", function (e) {
            this.bufferSizeDB = e.readUint32(), this.maxBitrate = e.readUint32(), this.avgBitrate = e.readUint32()
        }), b.createBoxCtor("clap", function (e) {
            this.cleanApertureWidthN = e.readUint32(), this.cleanApertureWidthD = e.readUint32(), this.cleanApertureHeightN = e.readUint32(), this.cleanApertureHeightD = e.readUint32(), this.horizOffN = e.readUint32(), this.horizOffD = e.readUint32(), this.vertOffN = e.readUint32(), this.vertOffD = e.readUint32()
        }), b.createBoxCtor("clli", function (e) {
            this.max_content_light_level = e.readUint16(), this.max_pic_average_light_level = e.readUint16()
        }), b.createFullBoxCtor("co64", function (e) {
            var t, r = e.readUint32();
            if (this.chunk_offsets = [], 0 === this.version) for (t = 0; t < r; t++) this.chunk_offsets.push(e.readUint64())
        }), b.createFullBoxCtor("CoLL", function (e) {
            this.maxCLL = e.readUint16(), this.maxFALL = e.readUint16()
        }), b.createBoxCtor("colr", function (e) {
            var t;
            this.colour_type = e.readString(4), "nclx" === this.colour_type ? (this.colour_primaries = e.readUint16(), this.transfer_characteristics = e.readUint16(), this.matrix_coefficients = e.readUint16(), t = e.readUint8(), this.full_range_flag = t >> 7) : "rICC" !== this.colour_type && "prof" !== this.colour_type || (this.ICC_profile = e.readUint8Array(this.size - 4))
        }), b.createFullBoxCtor("cprt", function (e) {
            this.parseLanguage(e), this.notice = e.readCString()
        }), b.createFullBoxCtor("cslg", function (e) {
            0 === this.version && (this.compositionToDTSShift = e.readInt32(), this.leastDecodeToDisplayDelta = e.readInt32(), this.greatestDecodeToDisplayDelta = e.readInt32(), this.compositionStartTime = e.readInt32(), this.compositionEndTime = e.readInt32())
        }), b.createFullBoxCtor("ctts", function (e) {
            var t, r = e.readUint32();
            if (this.sample_counts = [], this.sample_offsets = [], 0 === this.version) for (t = 0; t < r; t++) {
                this.sample_counts.push(e.readUint32());
                var i = e.readInt32();
                i < 0 && u.warn("BoxParser", "ctts box uses negative values without using version 1"), this.sample_offsets.push(i)
            } else if (1 == this.version) for (t = 0; t < r; t++) this.sample_counts.push(e.readUint32()), this.sample_offsets.push(e.readInt32())
        }), b.createBoxCtor("dac3", function (e) {
            var t = e.readUint8(), r = e.readUint8(), e = e.readUint8();
            this.fscod = t >> 6, this.bsid = t >> 1 & 31, this.bsmod = (1 & t) << 2 | r >> 6 & 3, this.acmod = r >> 3 & 7, this.lfeon = r >> 2 & 1, this.bit_rate_code = 3 & r | e >> 5 & 7
        }), b.createBoxCtor("dec3", function (e) {
            var t = e.readUint16();
            this.data_rate = t >> 3, this.num_ind_sub = 7 & t, this.ind_subs = [];
            for (var r = 0; r < this.num_ind_sub + 1; r++) {
                var i = {}, n = (this.ind_subs.push(i), e.readUint8()), s = e.readUint8(), a = e.readUint8();
                i.fscod = n >> 6, i.bsid = n >> 1 & 31, i.bsmod = (1 & n) << 4 | s >> 4 & 15, i.acmod = s >> 1 & 7, i.lfeon = 1 & s, i.num_dep_sub = a >> 1 & 15, 0 < i.num_dep_sub && (i.chan_loc = (1 & a) << 8 | e.readUint8())
            }
        }), b.createFullBoxCtor("dfLa", function (e) {
            var t = [],
                r = ["STREAMINFO", "PADDING", "APPLICATION", "SEEKTABLE", "VORBIS_COMMENT", "CUESHEET", "PICTURE", "RESERVED"];
            for (this.parseFullHeader(e); ;) {
                var i = e.readUint8(), n = Math.min(127 & i, r.length - 1);
                if (n ? e.readUint8Array(e.readUint24()) : (e.readUint8Array(13), this.samplerate = e.readUint32() >> 12, e.readUint8Array(20)), t.push(r[n]), 128 & i) break
            }
            this.numMetadataBlocks = t.length + " (" + t.join(", ") + ")"
        }), b.createBoxCtor("dimm", function (e) {
            this.bytessent = e.readUint64()
        }), b.createBoxCtor("dmax", function (e) {
            this.time = e.readUint32()
        }), b.createBoxCtor("dmed", function (e) {
            this.bytessent = e.readUint64()
        }), b.createBoxCtor("dOps", function (e) {
            if (this.Version = e.readUint8(), this.OutputChannelCount = e.readUint8(), this.PreSkip = e.readUint16(), this.InputSampleRate = e.readUint32(), this.OutputGain = e.readInt16(), this.ChannelMappingFamily = e.readUint8(), 0 !== this.ChannelMappingFamily) {
                this.StreamCount = e.readUint8(), this.CoupledCount = e.readUint8(), this.ChannelMapping = [];
                for (var t = 0; t < this.OutputChannelCount; t++) this.ChannelMapping[t] = e.readUint8()
            }
        }), b.createFullBoxCtor("dref", function (e) {
            var t;
            this.entries = [];
            for (var r = e.readUint32(), i = 0; i < r; i++) {
                if ((t = b.parseOneBox(e, !1, this.size - (e.getPosition() - this.start))).code !== b.OK) return;
                t = t.box, this.entries.push(t)
            }
        }), b.createBoxCtor("drep", function (e) {
            this.bytessent = e.readUint64()
        }), b.createFullBoxCtor("elng", function (e) {
            this.extended_language = e.readString(this.size - this.hdr_size)
        }), b.createFullBoxCtor("elst", function (e) {
            this.entries = [];
            for (var t = e.readUint32(), r = 0; r < t; r++) {
                var i = {};
                this.entries.push(i), 1 === this.version ? (i.segment_duration = e.readUint64(), i.media_time = e.readInt64()) : (i.segment_duration = e.readUint32(), i.media_time = e.readInt32()), i.media_rate_integer = e.readInt16(), i.media_rate_fraction = e.readInt16()
            }
        }), b.createFullBoxCtor("emsg", function (e) {
            1 == this.version ? (this.timescale = e.readUint32(), this.presentation_time = e.readUint64(), this.event_duration = e.readUint32(), this.id = e.readUint32(), this.scheme_id_uri = e.readCString(), this.value = e.readCString()) : (this.scheme_id_uri = e.readCString(), this.value = e.readCString(), this.timescale = e.readUint32(), this.presentation_time_delta = e.readUint32(), this.event_duration = e.readUint32(), this.id = e.readUint32());
            var t = this.size - this.hdr_size - (16 + (this.scheme_id_uri.length + 1) + (this.value.length + 1));
            1 == this.version && (t -= 4), this.message_data = e.readUint8Array(t)
        }), b.createFullBoxCtor("esds", function (e) {
            var e = e.readUint8Array(this.size - this.hdr_size), t = new i;
            this.esd = t.parseOneDescriptor(new l(e.buffer, 0, l.BIG_ENDIAN))
        }), b.createBoxCtor("fiel", function (e) {
            this.fieldCount = e.readUint8(), this.fieldOrdering = e.readUint8()
        }), b.createBoxCtor("frma", function (e) {
            this.data_format = e.readString(4)
        }),b.createBoxCtor("ftyp", function (e) {
            var t = this.size - this.hdr_size;
            this.major_brand = e.readString(4), this.minor_version = e.readUint32(), t -= 8, this.compatible_brands = [];
            for (var r = 0; 4 <= t;) this.compatible_brands[r] = e.readString(4), t -= 4, r++
        }),b.createFullBoxCtor("hdlr", function (e) {
            0 === this.version && (e.readUint32(), this.handler = e.readString(4), e.readUint32Array(3), this.name = e.readString(this.size - this.hdr_size - 20), "\0" === this.name[this.name.length - 1] && (this.name = this.name.slice(0, -1)))
        }),b.createBoxCtor("hvcC", function (e) {
            this.configurationVersion = e.readUint8(), r = e.readUint8(), this.general_profile_space = r >> 6, this.general_tier_flag = (32 & r) >> 5, this.general_profile_idc = 31 & r, this.general_profile_compatibility = e.readUint32(), this.general_constraint_indicator = e.readUint8Array(6), this.general_level_idc = e.readUint8(), this.min_spatial_segmentation_idc = 4095 & e.readUint16(), this.parallelismType = 3 & e.readUint8(), this.chroma_format_idc = 3 & e.readUint8(), this.bit_depth_luma_minus8 = 7 & e.readUint8(), this.bit_depth_chroma_minus8 = 7 & e.readUint8(), this.avgFrameRate = e.readUint16(), r = e.readUint8(), this.constantFrameRate = r >> 6, this.numTemporalLayers = (13 & r) >> 3, this.temporalIdNested = (4 & r) >> 2, this.lengthSizeMinusOne = 3 & r, this.nalu_arrays = [];
            for (var t, r, i = e.readUint8(), n = 0; n < i; n++) for (var s = [], a = (this.nalu_arrays.push(s), r = e.readUint8(), s.completeness = (128 & r) >> 7, s.nalu_type = 63 & r, e.readUint16()), o = 0; o < a; o++) {
                var l = {};
                s.push(l), t = e.readUint16(), l.data = e.readUint8Array(t)
            }
        }),b.createFullBoxCtor("iinf", function (e) {
            var t;
            0 === this.version ? this.entry_count = e.readUint16() : this.entry_count = e.readUint32(), this.item_infos = [];
            for (var r = 0; r < this.entry_count; r++) {
                if ((t = b.parseOneBox(e, !1, this.size - (e.getPosition() - this.start))).code !== b.OK) return;
                "infe" !== t.box.type && u.error("BoxParser", "Expected 'infe' box, got " + t.box.type), this.item_infos[r] = t.box
            }
        }),b.createFullBoxCtor("iloc", function (e) {
            var t = e.readUint8(),
                r = (this.offset_size = t >> 4 & 15, this.length_size = 15 & t, t = e.readUint8(), this.base_offset_size = t >> 4 & 15, 1 === this.version || 2 === this.version ? this.index_size = 15 & t : this.index_size = 0, this.items = [], 0);
            if (this.version < 2) r = e.readUint16(); else {
                if (2 !== this.version) throw"version of iloc box not supported";
                r = e.readUint32()
            }
            for (var i = 0; i < r; i++) {
                var n = {};
                if (this.items.push(n), this.version < 2) n.item_ID = e.readUint16(); else {
                    if (2 !== this.version) throw"version of iloc box not supported";
                    n.item_ID = e.readUint16()
                }
                switch (1 === this.version || 2 === this.version ? n.construction_method = 15 & e.readUint16() : n.construction_method = 0, n.data_reference_index = e.readUint16(), this.base_offset_size) {
                    case 0:
                        n.base_offset = 0;
                        break;
                    case 4:
                        n.base_offset = e.readUint32();
                        break;
                    case 8:
                        n.base_offset = e.readUint64();
                        break;
                    default:
                        throw"Error reading base offset size"
                }
                var s = e.readUint16();
                n.extents = [];
                for (var a = 0; a < s; a++) {
                    var o = {};
                    if (n.extents.push(o), 1 === this.version || 2 === this.version) switch (this.index_size) {
                        case 0:
                            o.extent_index = 0;
                            break;
                        case 4:
                            o.extent_index = e.readUint32();
                            break;
                        case 8:
                            o.extent_index = e.readUint64();
                            break;
                        default:
                            throw"Error reading extent index"
                    }
                    switch (this.offset_size) {
                        case 0:
                            o.extent_offset = 0;
                            break;
                        case 4:
                            o.extent_offset = e.readUint32();
                            break;
                        case 8:
                            o.extent_offset = e.readUint64();
                            break;
                        default:
                            throw"Error reading extent index"
                    }
                    switch (this.length_size) {
                        case 0:
                            o.extent_length = 0;
                            break;
                        case 4:
                            o.extent_length = e.readUint32();
                            break;
                        case 8:
                            o.extent_length = e.readUint64();
                            break;
                        default:
                            throw"Error reading extent index"
                    }
                }
            }
        }),b.createBoxCtor("imir", function (e) {
            e = e.readUint8();
            this.reserved = e >> 7, this.axis = 1 & e
        }),b.createFullBoxCtor("infe", function (e) {
            if (0 !== this.version && 1 !== this.version || (this.item_ID = e.readUint16(), this.item_protection_index = e.readUint16(), this.item_name = e.readCString(), this.content_type = e.readCString(), this.content_encoding = e.readCString()), 1 === this.version) return this.extension_type = e.readString(4), u.warn("BoxParser", "Cannot parse extension type"), void e.seek(this.start + this.size);
            2 <= this.version && (2 === this.version ? this.item_ID = e.readUint16() : 3 === this.version && (this.item_ID = e.readUint32()), this.item_protection_index = e.readUint16(), this.item_type = e.readString(4), this.item_name = e.readCString(), "mime" === this.item_type ? (this.content_type = e.readCString(), this.content_encoding = e.readCString()) : "uri " === this.item_type && (this.item_uri_type = e.readCString()))
        }),b.createFullBoxCtor("ipma", function (e) {
            var t, r;
            for (entry_count = e.readUint32(), this.associations = [], t = 0; t < entry_count; t++) {
                var i = {},
                    n = (this.associations.push(i), this.version < 1 ? i.id = e.readUint16() : i.id = e.readUint32(), e.readUint8());
                for (i.props = [], r = 0; r < n; r++) {
                    var s = e.readUint8(), a = {};
                    i.props.push(a), a.essential = (128 & s) >> 7 == 1, 1 & this.flags ? a.property_index = (127 & s) << 8 | e.readUint8() : a.property_index = 127 & s
                }
            }
        }),b.createFullBoxCtor("iref", function (e) {
            var t;
            for (this.references = []; e.getPosition() < this.start + this.size;) {
                if ((t = b.parseOneBox(e, !0, this.size - (e.getPosition() - this.start))).code !== b.OK) return;
                (t = new (0 === this.version ? b.SingleItemTypeReferenceBox : b.SingleItemTypeReferenceBoxLarge)(t.type, t.size, t.hdr_size, t.start)).write === b.Box.prototype.write && "mdat" !== t.type && (u.warn("BoxParser", t.type + " box writing not yet implemented, keeping unparsed data in memory for later write"), t.parseDataAndRewind(e)), t.parse(e), this.references.push(t)
            }
        }),b.createBoxCtor("irot", function (e) {
            this.angle = 3 & e.readUint8()
        }),b.createFullBoxCtor("ispe", function (e) {
            this.image_width = e.readUint32(), this.image_height = e.readUint32()
        }),b.createFullBoxCtor("kind", function (e) {
            this.schemeURI = e.readCString(), this.value = e.readCString()
        }),b.createFullBoxCtor("leva", function (e) {
            var t = e.readUint8();
            this.levels = [];
            for (var r = 0; r < t; r++) {
                var i = {}, n = ((this.levels[r] = i).track_ID = e.readUint32(), e.readUint8());
                switch (i.padding_flag = n >> 7, i.assignment_type = 127 & n, i.assignment_type) {
                    case 0:
                        i.grouping_type = e.readString(4);
                        break;
                    case 1:
                        i.grouping_type = e.readString(4), i.grouping_type_parameter = e.readUint32();
                        break;
                    case 2:
                    case 3:
                        break;
                    case 4:
                        i.sub_track_id = e.readUint32();
                        break;
                    default:
                        u.warn("BoxParser", "Unknown leva assignement type")
                }
            }
        }),b.createBoxCtor("lsel", function (e) {
            this.layer_id = e.readUint16()
        }),b.createBoxCtor("maxr", function (e) {
            this.period = e.readUint32(), this.bytes = e.readUint32()
        }),b.createBoxCtor("mdcv", function (e) {
            this.display_primaries = [], this.display_primaries[0] = {}, this.display_primaries[0].x = e.readUint16(), this.display_primaries[0].y = e.readUint16(), this.display_primaries[1] = {}, this.display_primaries[1].x = e.readUint16(), this.display_primaries[1].y = e.readUint16(), this.display_primaries[2] = {}, this.display_primaries[2].x = e.readUint16(), this.display_primaries[2].y = e.readUint16(), this.white_point = {}, this.white_point.x = e.readUint16(), this.white_point.y = e.readUint16(), this.max_display_mastering_luminance = e.readUint32(), this.min_display_mastering_luminance = e.readUint32()
        }),b.createFullBoxCtor("mdhd", function (e) {
            1 == this.version ? (this.creation_time = e.readUint64(), this.modification_time = e.readUint64(), this.timescale = e.readUint32(), this.duration = e.readUint64()) : (this.creation_time = e.readUint32(), this.modification_time = e.readUint32(), this.timescale = e.readUint32(), this.duration = e.readUint32()), this.parseLanguage(e), e.readUint16()
        }),b.createFullBoxCtor("mehd", function (e) {
            1 & this.flags && (u.warn("BoxParser", "mehd box incorrectly uses flags set to 1, converting version to 1"), this.version = 1), 1 == this.version ? this.fragment_duration = e.readUint64() : this.fragment_duration = e.readUint32()
        }),b.createFullBoxCtor("meta", function (e) {
            this.boxes = [], b.ContainerBox.prototype.parse.call(this, e)
        }),b.createFullBoxCtor("mfhd", function (e) {
            this.sequence_number = e.readUint32()
        }),b.createFullBoxCtor("mfro", function (e) {
            this._size = e.readUint32()
        }),b.createFullBoxCtor("mvhd", function (e) {
            1 == this.version ? (this.creation_time = e.readUint64(), this.modification_time = e.readUint64(), this.timescale = e.readUint32(), this.duration = e.readUint64()) : (this.creation_time = e.readUint32(), this.modification_time = e.readUint32(), this.timescale = e.readUint32(), this.duration = e.readUint32()), this.rate = e.readUint32(), this.volume = e.readUint16() >> 8, e.readUint16(), e.readUint32Array(2), this.matrix = e.readUint32Array(9), e.readUint32Array(6), this.next_track_id = e.readUint32()
        }),b.createBoxCtor("npck", function (e) {
            this.packetssent = e.readUint32()
        }),b.createBoxCtor("nump", function (e) {
            this.packetssent = e.readUint64()
        }),b.createFullBoxCtor("padb", function (e) {
            var t = e.readUint32();
            this.padbits = [];
            for (var r = 0; r < Math.floor((t + 1) / 2); r++) this.padbits = e.readUint8()
        }),b.createBoxCtor("pasp", function (e) {
            this.hSpacing = e.readUint32(), this.vSpacing = e.readUint32()
        }),b.createBoxCtor("payl", function (e) {
            this.text = e.readString(this.size - this.hdr_size)
        }),b.createBoxCtor("payt", function (e) {
            this.payloadID = e.readUint32();
            var t = e.readUint8();
            this.rtpmap_string = e.readString(t)
        }),b.createFullBoxCtor("pdin", function (e) {
            var t = (this.size - this.hdr_size) / 8;
            this.rate = [], this.initial_delay = [];
            for (var r = 0; r < t; r++) this.rate[r] = e.readUint32(), this.initial_delay[r] = e.readUint32()
        }),b.createFullBoxCtor("pitm", function (e) {
            0 === this.version ? this.item_id = e.readUint16() : this.item_id = e.readUint32()
        }),b.createFullBoxCtor("pixi", function (e) {
            var t;
            for (this.num_channels = e.readUint8(), this.bits_per_channels = [], t = 0; t < this.num_channels; t++) this.bits_per_channels[t] = e.readUint8()
        }),b.createBoxCtor("pmax", function (e) {
            this.bytes = e.readUint32()
        }),b.createFullBoxCtor("prft", function (e) {
            this.ref_track_id = e.readUint32(), this.ntp_timestamp = e.readUint64(), 0 === this.version ? this.media_time = e.readUint32() : this.media_time = e.readUint64()
        }),b.createFullBoxCtor("pssh", function (e) {
            if (this.system_id = b.parseHex16(e), 0 < this.version) {
                var t = e.readUint32();
                this.kid = [];
                for (var r = 0; r < t; r++) this.kid[r] = b.parseHex16(e)
            }
            var i = e.readUint32();
            0 < i && (this.data = e.readUint8Array(i))
        }),b.createFullBoxCtor("clef", function (e) {
            this.width = e.readUint32(), this.height = e.readUint32()
        }),b.createFullBoxCtor("enof", function (e) {
            this.width = e.readUint32(), this.height = e.readUint32()
        }),b.createFullBoxCtor("prof", function (e) {
            this.width = e.readUint32(), this.height = e.readUint32()
        }),b.createContainerBoxCtor("tapt", null, ["clef", "prof", "enof"]),b.createBoxCtor("rtp ", function (e) {
            this.descriptionformat = e.readString(4), this.sdptext = e.readString(this.size - this.hdr_size - 4)
        }),b.createFullBoxCtor("saio", function (e) {
            1 & this.flags && (this.aux_info_type = e.readUint32(), this.aux_info_type_parameter = e.readUint32());
            var t = e.readUint32();
            this.offset = [];
            for (var r = 0; r < t; r++) 0 === this.version ? this.offset[r] = e.readUint32() : this.offset[r] = e.readUint64()
        }),b.createFullBoxCtor("saiz", function (e) {
            1 & this.flags && (this.aux_info_type = e.readUint32(), this.aux_info_type_parameter = e.readUint32()), this.default_sample_info_size = e.readUint8();
            var t = e.readUint32();
            if (this.sample_info_size = [], 0 === this.default_sample_info_size) for (var r = 0; r < t; r++) this.sample_info_size[r] = e.readUint8()
        }),b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_METADATA, "mett", function (e) {
            this.parseHeader(e), this.content_encoding = e.readCString(), this.mime_format = e.readCString(), this.parseFooter(e)
        }),b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_METADATA, "metx", function (e) {
            this.parseHeader(e), this.content_encoding = e.readCString(), this.namespace = e.readCString(), this.schema_location = e.readCString(), this.parseFooter(e)
        }),b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_SUBTITLE, "sbtt", function (e) {
            this.parseHeader(e), this.content_encoding = e.readCString(), this.mime_format = e.readCString(), this.parseFooter(e)
        }),b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_SUBTITLE, "stpp", function (e) {
            this.parseHeader(e), this.namespace = e.readCString(), this.schema_location = e.readCString(), this.auxiliary_mime_types = e.readCString(), this.parseFooter(e)
        }),b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_SUBTITLE, "stxt", function (e) {
            this.parseHeader(e), this.content_encoding = e.readCString(), this.mime_format = e.readCString(), this.parseFooter(e)
        }),b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_SUBTITLE, "tx3g", function (e) {
            this.parseHeader(e), this.displayFlags = e.readUint32(), this.horizontal_justification = e.readInt8(), this.vertical_justification = e.readInt8(), this.bg_color_rgba = e.readUint8Array(4), this.box_record = e.readInt16Array(4), this.style_record = e.readUint8Array(12), this.parseFooter(e)
        }),b.createSampleEntryCtor(b.SAMPLE_ENTRY_TYPE_METADATA, "wvtt", function (e) {
            this.parseHeader(e), this.parseFooter(e)
        }),b.createSampleGroupCtor("alst", function (e) {
            var t, r = e.readUint16();
            for (this.first_output_sample = e.readUint16(), this.sample_offset = [], t = 0; t < r; t++) this.sample_offset[t] = e.readUint32();
            var i = this.description_length - 4 - 4 * r;
            for (this.num_output_samples = [], this.num_total_samples = [], t = 0; t < i / 4; t++) this.num_output_samples[t] = e.readUint16(), this.num_total_samples[t] = e.readUint16()
        }),b.createSampleGroupCtor("avll", function (e) {
            this.layerNumber = e.readUint8(), this.accurateStatisticsFlag = e.readUint8(), this.avgBitRate = e.readUint16(), this.avgFrameRate = e.readUint16()
        }),b.createSampleGroupCtor("avss", function (e) {
            this.subSequenceIdentifier = e.readUint16(), this.layerNumber = e.readUint8();
            var t = e.readUint8();
            this.durationFlag = t >> 7, this.avgRateFlag = t >> 6 & 1, this.durationFlag && (this.duration = e.readUint32()), this.avgRateFlag && (this.accurateStatisticsFlag = e.readUint8(), this.avgBitRate = e.readUint16(), this.avgFrameRate = e.readUint16()), this.dependency = [];
            for (var r = e.readUint8(), i = 0; i < r; i++) {
                var n = {};
                this.dependency.push(n), n.subSeqDirectionFlag = e.readUint8(), n.layerNumber = e.readUint8(), n.subSequenceIdentifier = e.readUint16()
            }
        }),b.createSampleGroupCtor("dtrt", function (e) {
            u.warn("BoxParser", "Sample Group type: " + this.grouping_type + " not fully parsed")
        }),b.createSampleGroupCtor("mvif", function (e) {
            u.warn("BoxParser", "Sample Group type: " + this.grouping_type + " not fully parsed")
        }),b.createSampleGroupCtor("prol", function (e) {
            this.roll_distance = e.readInt16()
        }),b.createSampleGroupCtor("rap ", function (e) {
            e = e.readUint8();
            this.num_leading_samples_known = e >> 7, this.num_leading_samples = 127 & e
        }),b.createSampleGroupCtor("rash", function (e) {
            if (this.operation_point_count = e.readUint16(), this.description_length !== 2 + (1 === this.operation_point_count ? 2 : 6 * this.operation_point_count) + 9) u.warn("BoxParser", "Mismatch in " + this.grouping_type + " sample group length"), this.data = e.readUint8Array(this.description_length - 2); else {
                if (1 === this.operation_point_count) this.target_rate_share = e.readUint16(); else {
                    this.target_rate_share = [], this.available_bitrate = [];
                    for (var t = 0; t < this.operation_point_count; t++) this.available_bitrate[t] = e.readUint32(), this.target_rate_share[t] = e.readUint16()
                }
                this.maximum_bitrate = e.readUint32(), this.minimum_bitrate = e.readUint32(), this.discard_priority = e.readUint8()
            }
        }),b.createSampleGroupCtor("roll", function (e) {
            this.roll_distance = e.readInt16()
        }),b.SampleGroupEntry.prototype.parse = function (e) {
            u.warn("BoxParser", "Unknown Sample Group type: " + this.grouping_type), this.data = e.readUint8Array(this.description_length)
        },b.createSampleGroupCtor("scif", function (e) {
            u.warn("BoxParser", "Sample Group type: " + this.grouping_type + " not fully parsed")
        }),b.createSampleGroupCtor("scnm", function (e) {
            u.warn("BoxParser", "Sample Group type: " + this.grouping_type + " not fully parsed")
        }),b.createSampleGroupCtor("seig", function (e) {
            this.reserved = e.readUint8();
            var t = e.readUint8();
            this.crypt_byte_block = t >> 4, this.skip_byte_block = 15 & t, this.isProtected = e.readUint8(), this.Per_Sample_IV_Size = e.readUint8(), this.KID = b.parseHex16(e), this.constant_IV_size = 0, this.constant_IV = 0, 1 === this.isProtected && 0 === this.Per_Sample_IV_Size && (this.constant_IV_size = e.readUint8(), this.constant_IV = e.readUint8Array(this.constant_IV_size))
        }),b.createSampleGroupCtor("stsa", function (e) {
            u.warn("BoxParser", "Sample Group type: " + this.grouping_type + " not fully parsed")
        }),b.createSampleGroupCtor("sync", function (e) {
            e = e.readUint8();
            this.NAL_unit_type = 63 & e
        }),b.createSampleGroupCtor("tele", function (e) {
            e = e.readUint8();
            this.level_independently_decodable = e >> 7
        }),b.createSampleGroupCtor("tsas", function (e) {
            u.warn("BoxParser", "Sample Group type: " + this.grouping_type + " not fully parsed")
        }),b.createSampleGroupCtor("tscl", function (e) {
            u.warn("BoxParser", "Sample Group type: " + this.grouping_type + " not fully parsed")
        }),b.createSampleGroupCtor("vipr", function (e) {
            u.warn("BoxParser", "Sample Group type: " + this.grouping_type + " not fully parsed")
        }),b.createFullBoxCtor("sbgp", function (e) {
            this.grouping_type = e.readString(4), 1 === this.version ? this.grouping_type_parameter = e.readUint32() : this.grouping_type_parameter = 0, this.entries = [];
            for (var t = e.readUint32(), r = 0; r < t; r++) {
                var i = {};
                this.entries.push(i), i.sample_count = e.readInt32(), i.group_description_index = e.readInt32()
            }
        }),b.createFullBoxCtor("schm", function (e) {
            this.scheme_type = e.readString(4), this.scheme_version = e.readUint32(), 1 & this.flags && (this.scheme_uri = e.readString(this.size - this.hdr_size - 8))
        }),b.createBoxCtor("sdp ", function (e) {
            this.sdptext = e.readString(this.size - this.hdr_size)
        }),b.createFullBoxCtor("sdtp", function (e) {
            var t, r = this.size - this.hdr_size;
            this.is_leading = [], this.sample_depends_on = [], this.sample_is_depended_on = [], this.sample_has_redundancy = [];
            for (var i = 0; i < r; i++) t = e.readUint8(), this.is_leading[i] = t >> 6, this.sample_depends_on[i] = t >> 4 & 3, this.sample_is_depended_on[i] = t >> 2 & 3, this.sample_has_redundancy[i] = 3 & t
        }),b.createFullBoxCtor("senc"),b.createFullBoxCtor("sgpd", function (e) {
            this.grouping_type = e.readString(4), u.debug("BoxParser", "Found Sample Groups of type " + this.grouping_type), 1 === this.version ? this.default_length = e.readUint32() : this.default_length = 0, 2 <= this.version && (this.default_group_description_index = e.readUint32()), this.entries = [];
            for (var t = e.readUint32(), r = 0; r < t; r++) {
                var i = new (b[this.grouping_type + "SampleGroupEntry"] ? b[this.grouping_type + "SampleGroupEntry"] : b.SampleGroupEntry)(this.grouping_type);
                this.entries.push(i), 1 === this.version && 0 === this.default_length ? i.description_length = e.readUint32() : i.description_length = this.default_length, i.write === b.SampleGroupEntry.prototype.write && (u.info("BoxParser", "SampleGroup for type " + this.grouping_type + " writing not yet implemented, keeping unparsed data in memory for later write"), i.data = e.readUint8Array(i.description_length), e.position -= i.description_length), i.parse(e)
            }
        }),b.createFullBoxCtor("sidx", function (e) {
            this.reference_ID = e.readUint32(), this.timescale = e.readUint32(), 0 === this.version ? (this.earliest_presentation_time = e.readUint32(), this.first_offset = e.readUint32()) : (this.earliest_presentation_time = e.readUint64(), this.first_offset = e.readUint64()), e.readUint16(), this.references = [];
            for (var t = e.readUint16(), r = 0; r < t; r++) {
                var i = {}, n = (this.references.push(i), e.readUint32());
                i.reference_type = n >> 31 & 1, i.referenced_size = 2147483647 & n, i.subsegment_duration = e.readUint32(), n = e.readUint32(), i.starts_with_SAP = n >> 31 & 1, i.SAP_type = n >> 28 & 7, i.SAP_delta_time = 268435455 & n
            }
        }),b.SingleItemTypeReferenceBox = function (e, t, r, i) {
            b.Box.call(this, e, t), this.hdr_size = r, this.start = i
        },b.SingleItemTypeReferenceBox.prototype = new b.Box,b.SingleItemTypeReferenceBox.prototype.parse = function (e) {
            this.from_item_ID = e.readUint16();
            var t = e.readUint16();
            this.references = [];
            for (var r = 0; r < t; r++) this.references[r] = e.readUint16()
        },b.SingleItemTypeReferenceBoxLarge = function (e, t, r, i) {
            b.Box.call(this, e, t), this.hdr_size = r, this.start = i
        },b.SingleItemTypeReferenceBoxLarge.prototype = new b.Box,b.SingleItemTypeReferenceBoxLarge.prototype.parse = function (e) {
            this.from_item_ID = e.readUint32();
            var t = e.readUint16();
            this.references = [];
            for (var r = 0; r < t; r++) this.references[r] = e.readUint32()
        },b.createFullBoxCtor("SmDm", function (e) {
            this.primaryRChromaticity_x = e.readUint16(), this.primaryRChromaticity_y = e.readUint16(), this.primaryGChromaticity_x = e.readUint16(), this.primaryGChromaticity_y = e.readUint16(), this.primaryBChromaticity_x = e.readUint16(), this.primaryBChromaticity_y = e.readUint16(), this.whitePointChromaticity_x = e.readUint16(), this.whitePointChromaticity_y = e.readUint16(), this.luminanceMax = e.readUint32(), this.luminanceMin = e.readUint32()
        }),b.createFullBoxCtor("smhd", function (e) {
            this.balance = e.readUint16(), e.readUint16()
        }),b.createFullBoxCtor("ssix", function (e) {
            this.subsegments = [];
            for (var t = e.readUint32(), r = 0; r < t; r++) {
                var i = {};
                this.subsegments.push(i), i.ranges = [];
                for (var n = e.readUint32(), s = 0; s < n; s++) {
                    var a = {};
                    i.ranges.push(a), a.level = e.readUint8(), a.range_size = e.readUint24()
                }
            }
        }),b.createFullBoxCtor("stco", function (e) {
            var t = e.readUint32();
            if (this.chunk_offsets = [], 0 === this.version) for (var r = 0; r < t; r++) this.chunk_offsets.push(e.readUint32())
        }),b.createFullBoxCtor("stdp", function (e) {
            var t = (this.size - this.hdr_size) / 2;
            this.priority = [];
            for (var r = 0; r < t; r++) this.priority[r] = e.readUint16()
        }),b.createFullBoxCtor("sthd"),b.createFullBoxCtor("stri", function (e) {
            this.switch_group = e.readUint16(), this.alternate_group = e.readUint16(), this.sub_track_id = e.readUint32();
            var t = (this.size - this.hdr_size - 8) / 4;
            this.attribute_list = [];
            for (var r = 0; r < t; r++) this.attribute_list[r] = e.readUint32()
        }),b.createFullBoxCtor("stsc", function (e) {
            var t, r = e.readUint32();
            if (this.first_chunk = [], this.samples_per_chunk = [], this.sample_description_index = [], 0 === this.version) for (t = 0; t < r; t++) this.first_chunk.push(e.readUint32()), this.samples_per_chunk.push(e.readUint32()), this.sample_description_index.push(e.readUint32())
        }),b.createFullBoxCtor("stsd", function (e) {
            var t, r, i, n;
            for (this.entries = [], i = e.readUint32(), t = 1; t <= i; t++) {
                if ((r = b.parseOneBox(e, !0, this.size - (e.getPosition() - this.start))).code !== b.OK) return;
                b[r.type + "SampleEntry"] ? ((n = new b[r.type + "SampleEntry"](r.size)).hdr_size = r.hdr_size, n.start = r.start) : (u.warn("BoxParser", "Unknown sample entry type: " + r.type), n = new b.SampleEntry(r.type, r.size, r.hdr_size, r.start)), n.write === b.SampleEntry.prototype.write && (u.info("BoxParser", "SampleEntry " + n.type + " box writing not yet implemented, keeping unparsed data in memory for later write"), n.parseDataAndRewind(e)), n.parse(e), this.entries.push(n)
            }
        }),b.createFullBoxCtor("stsg", function (e) {
            this.grouping_type = e.readUint32();
            var t = e.readUint16();
            this.group_description_index = [];
            for (var r = 0; r < t; r++) this.group_description_index[r] = e.readUint32()
        }),b.createFullBoxCtor("stsh", function (e) {
            var t, r = e.readUint32();
            if (this.shadowed_sample_numbers = [], this.sync_sample_numbers = [], 0 === this.version) for (t = 0; t < r; t++) this.shadowed_sample_numbers.push(e.readUint32()), this.sync_sample_numbers.push(e.readUint32())
        }),b.createFullBoxCtor("stss", function (e) {
            var t, r = e.readUint32();
            if (0 === this.version) for (this.sample_numbers = [], t = 0; t < r; t++) this.sample_numbers.push(e.readUint32())
        }),b.createFullBoxCtor("stsz", function (e) {
            var t;
            if (this.sample_sizes = [], 0 === this.version) for (this.sample_size = e.readUint32(), this.sample_count = e.readUint32(), t = 0; t < this.sample_count; t++) 0 === this.sample_size ? this.sample_sizes.push(e.readUint32()) : this.sample_sizes[t] = this.sample_size
        }),b.createFullBoxCtor("stts", function (e) {
            var t, r, i = e.readUint32();
            if (this.sample_counts = [], this.sample_deltas = [], 0 === this.version) for (t = 0; t < i; t++) this.sample_counts.push(e.readUint32()), (r = e.readInt32()) < 0 && (u.warn("BoxParser", "File uses negative stts sample delta, using value 1 instead, sync may be lost!"), r = 1), this.sample_deltas.push(r)
        }),b.createFullBoxCtor("stvi", function (e) {
            var t = e.readUint32();
            this.single_view_allowed = 3 & t, this.stereo_scheme = e.readUint32();
            var r, t = e.readUint32();
            for (this.stereo_indication_type = e.readString(t), this.boxes = []; e.getPosition() < this.start + this.size;) {
                if ((r = b.parseOneBox(e, !1, this.size - (e.getPosition() - this.start))).code !== b.OK) return;
                r = r.box, this.boxes.push(r), this[r.type] = r
            }
        }),b.createBoxCtor("styp", function (e) {
            b.ftypBox.prototype.parse.call(this, e)
        }),b.createFullBoxCtor("stz2", function (e) {
            var t, r;
            if (this.sample_sizes = [], 0 === this.version) if (this.reserved = e.readUint24(), this.field_size = e.readUint8(), r = e.readUint32(), 4 === this.field_size) for (t = 0; t < r; t += 2) {
                var i = e.readUint8();
                this.sample_sizes[t] = i >> 4 & 15, this.sample_sizes[t + 1] = 15 & i
            } else if (8 === this.field_size) for (t = 0; t < r; t++) this.sample_sizes[t] = e.readUint8(); else if (16 === this.field_size) for (t = 0; t < r; t++) this.sample_sizes[t] = e.readUint16(); else u.error("BoxParser", "Error in length field in stz2 box")
        }),b.createFullBoxCtor("subs", function (e) {
            var t, r, i, n = e.readUint32();
            for (this.entries = [], t = 0; t < n; t++) {
                var s = {};
                if ((this.entries[t] = s).sample_delta = e.readUint32(), s.subsamples = [], 0 < (i = e.readUint16())) for (r = 0; r < i; r++) {
                    var a = {};
                    s.subsamples.push(a), 1 == this.version ? a.size = e.readUint32() : a.size = e.readUint16(), a.priority = e.readUint8(), a.discardable = e.readUint8(), a.codec_specific_parameters = e.readUint32()
                }
            }
        }),b.createFullBoxCtor("tenc", function (e) {
            var t;
            e.readUint8(), 0 === this.version ? e.readUint8() : (t = e.readUint8(), this.default_crypt_byte_block = t >> 4 & 15, this.default_skip_byte_block = 15 & t), this.default_isProtected = e.readUint8(), this.default_Per_Sample_IV_Size = e.readUint8(), this.default_KID = b.parseHex16(e), 1 === this.default_isProtected && 0 === this.default_Per_Sample_IV_Size && (this.default_constant_IV_size = e.readUint8(), this.default_constant_IV = e.readUint8Array(this.default_constant_IV_size))
        }),b.createFullBoxCtor("tfdt", function (e) {
            1 == this.version ? this.baseMediaDecodeTime = e.readUint64() : this.baseMediaDecodeTime = e.readUint32()
        }),b.createFullBoxCtor("tfhd", function (e) {
            var t = 0;
            this.track_id = e.readUint32(), this.size - this.hdr_size > t && this.flags & b.TFHD_FLAG_BASE_DATA_OFFSET ? (this.base_data_offset = e.readUint64(), t += 8) : this.base_data_offset = 0, this.size - this.hdr_size > t && this.flags & b.TFHD_FLAG_SAMPLE_DESC ? (this.default_sample_description_index = e.readUint32(), t += 4) : this.default_sample_description_index = 0, this.size - this.hdr_size > t && this.flags & b.TFHD_FLAG_SAMPLE_DUR ? (this.default_sample_duration = e.readUint32(), t += 4) : this.default_sample_duration = 0, this.size - this.hdr_size > t && this.flags & b.TFHD_FLAG_SAMPLE_SIZE ? (this.default_sample_size = e.readUint32(), t += 4) : this.default_sample_size = 0, this.size - this.hdr_size > t && this.flags & b.TFHD_FLAG_SAMPLE_FLAGS ? this.default_sample_flags = e.readUint32() : this.default_sample_flags = 0
        }),b.createFullBoxCtor("tfra", function (e) {
            this.track_ID = e.readUint32(), e.readUint24();
            var t = e.readUint8();
            this.length_size_of_traf_num = t >> 4 & 3, this.length_size_of_trun_num = t >> 2 & 3, this.length_size_of_sample_num = 3 & t, this.entries = [];
            for (var r = e.readUint32(), i = 0; i < r; i++) 1 === this.version ? (this.time = e.readUint64(), this.moof_offset = e.readUint64()) : (this.time = e.readUint32(), this.moof_offset = e.readUint32()), this.traf_number = e["readUint" + 8 * (this.length_size_of_traf_num + 1)](), this.trun_number = e["readUint" + 8 * (this.length_size_of_trun_num + 1)](), this.sample_number = e["readUint" + 8 * (this.length_size_of_sample_num + 1)]()
        }),b.createFullBoxCtor("tkhd", function (e) {
            1 == this.version ? (this.creation_time = e.readUint64(), this.modification_time = e.readUint64(), this.track_id = e.readUint32(), e.readUint32(), this.duration = e.readUint64()) : (this.creation_time = e.readUint32(), this.modification_time = e.readUint32(), this.track_id = e.readUint32(), e.readUint32(), this.duration = e.readUint32()), e.readUint32Array(2), this.layer = e.readInt16(), this.alternate_group = e.readInt16(), this.volume = e.readInt16() >> 8, e.readUint16(), this.matrix = e.readInt32Array(9), this.width = e.readUint32(), this.height = e.readUint32()
        }),b.createBoxCtor("tmax", function (e) {
            this.time = e.readUint32()
        }),b.createBoxCtor("tmin", function (e) {
            this.time = e.readUint32()
        }),b.createBoxCtor("totl", function (e) {
            this.bytessent = e.readUint32()
        }),b.createBoxCtor("tpay", function (e) {
            this.bytessent = e.readUint32()
        }),b.createBoxCtor("tpyl", function (e) {
            this.bytessent = e.readUint64()
        }),b.TrackGroupTypeBox.prototype.parse = function (e) {
            this.parseFullHeader(e), this.track_group_id = e.readUint32()
        },b.createTrackGroupCtor("msrc"),b.TrackReferenceTypeBox = function (e, t, r, i) {
            b.Box.call(this, e, t), this.hdr_size = r, this.start = i
        },b.TrackReferenceTypeBox.prototype = new b.Box,b.TrackReferenceTypeBox.prototype.parse = function (e) {
            this.track_ids = e.readUint32Array((this.size - this.hdr_size) / 4)
        },b.trefBox.prototype.parse = function (e) {
            for (var t; e.getPosition() < this.start + this.size;) {
                if ((t = b.parseOneBox(e, !0, this.size - (e.getPosition() - this.start))).code !== b.OK) return;
                (t = new b.TrackReferenceTypeBox(t.type, t.size, t.hdr_size, t.start)).write === b.Box.prototype.write && "mdat" !== t.type && (u.info("BoxParser", "TrackReference " + t.type + " box writing not yet implemented, keeping unparsed data in memory for later write"), t.parseDataAndRewind(e)), t.parse(e), this.boxes.push(t)
            }
        },b.createFullBoxCtor("trep", function (e) {
            for (this.track_ID = e.readUint32(), this.boxes = []; e.getPosition() < this.start + this.size;) {
                if ((ret = b.parseOneBox(e, !1, this.size - (e.getPosition() - this.start))).code !== b.OK) return;
                box = ret.box, this.boxes.push(box)
            }
        }),b.createFullBoxCtor("trex", function (e) {
            this.track_id = e.readUint32(), this.default_sample_description_index = e.readUint32(), this.default_sample_duration = e.readUint32(), this.default_sample_size = e.readUint32(), this.default_sample_flags = e.readUint32()
        }),b.createBoxCtor("trpy", function (e) {
            this.bytessent = e.readUint64()
        }),b.createFullBoxCtor("trun", function (e) {
            var t = 0;
            if (this.sample_count = e.readUint32(), this.size - this.hdr_size > (t += 4) && this.flags & b.TRUN_FLAGS_DATA_OFFSET ? (this.data_offset = e.readInt32(), t += 4) : this.data_offset = 0, this.size - this.hdr_size > t && this.flags & b.TRUN_FLAGS_FIRST_FLAG ? (this.first_sample_flags = e.readUint32(), t += 4) : this.first_sample_flags = 0, this.sample_duration = [], this.sample_size = [], this.sample_flags = [], this.sample_composition_time_offset = [], this.size - this.hdr_size > t) for (var r = 0; r < this.sample_count; r++) this.flags & b.TRUN_FLAGS_DURATION && (this.sample_duration[r] = e.readUint32()), this.flags & b.TRUN_FLAGS_SIZE && (this.sample_size[r] = e.readUint32()), this.flags & b.TRUN_FLAGS_FLAGS && (this.sample_flags[r] = e.readUint32()), this.flags & b.TRUN_FLAGS_CTS_OFFSET && (0 === this.version ? this.sample_composition_time_offset[r] = e.readUint32() : this.sample_composition_time_offset[r] = e.readInt32())
        }),b.createFullBoxCtor("tsel", function (e) {
            this.switch_group = e.readUint32();
            var t = (this.size - this.hdr_size - 4) / 4;
            this.attribute_list = [];
            for (var r = 0; r < t; r++) this.attribute_list[r] = e.readUint32()
        }),b.createFullBoxCtor("txtC", function (e) {
            this.config = e.readCString()
        }),b.createFullBoxCtor("url ", function (e) {
            1 !== this.flags && (this.location = e.readCString())
        }),b.createFullBoxCtor("urn ", function (e) {
            this.name = e.readCString(), 0 < this.size - this.hdr_size - this.name.length - 1 && (this.location = e.readCString())
        }),b.createUUIDBox("a5d40b30e81411ddba2f0800200c9a66", !0, !1, function (e) {
            this.LiveServerManifest = e.readString(this.size - this.hdr_size).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;")
        }),b.createUUIDBox("d08a4f1810f34a82b6c832d8aba183d3", !0, !1, function (e) {
            this.system_id = b.parseHex16(e);
            var t = e.readUint32();
            0 < t && (this.data = e.readUint8Array(t))
        }),b.createUUIDBox("a2394f525a9b4f14a2446c427c648df4", !0, !1),b.createUUIDBox("8974dbce7be74c5184f97148f9882554", !0, !1, function (e) {
            this.default_AlgorithmID = e.readUint24(), this.default_IV_size = e.readUint8(), this.default_KID = b.parseHex16(e)
        }),b.createUUIDBox("d4807ef2ca3946958e5426cb9e46a79f", !0, !1, function (e) {
            this.fragment_count = e.readUint8(), this.entries = [];
            for (var t = 0; t < this.fragment_count; t++) {
                var r = {}, i = 0, n = 0,
                    n = 1 === this.version ? (i = e.readUint64(), e.readUint64()) : (i = e.readUint32(), e.readUint32());
                r.absolute_time = i, r.absolute_duration = n, this.entries.push(r)
            }
        }),b.createUUIDBox("6d1d9b0542d544e680e2141daff757b2", !0, !1, function (e) {
            1 === this.version ? (this.absolute_time = e.readUint64(), this.duration = e.readUint64()) : (this.absolute_time = e.readUint32(), this.duration = e.readUint32())
        }),b.createFullBoxCtor("vmhd", function (e) {
            this.graphicsmode = e.readUint16(), this.opcolor = e.readUint16Array(3)
        }),b.createFullBoxCtor("vpcC", function (e) {
            var t;
            1 === this.version ? (this.profile = e.readUint8(), this.level = e.readUint8(), t = e.readUint8(), this.bitDepth = t >> 4, this.chromaSubsampling = t >> 1 & 7, this.videoFullRangeFlag = 1 & t, this.colourPrimaries = e.readUint8(), this.transferCharacteristics = e.readUint8(), this.matrixCoefficients = e.readUint8()) : (this.profile = e.readUint8(), this.level = e.readUint8(), t = e.readUint8(), this.bitDepth = t >> 4 & 15, this.colorSpace = 15 & t, t = e.readUint8(), this.chromaSubsampling = t >> 4 & 15, this.transferFunction = t >> 1 & 7, this.videoFullRangeFlag = 1 & t), this.codecIntializationDataSize = e.readUint16(), this.codecIntializationData = e.readUint8Array(this.codecIntializationDataSize)
        }),b.createBoxCtor("vttC", function (e) {
            this.text = e.readString(this.size - this.hdr_size)
        }),b.createFullBoxCtor("vvcC", function (e) {
            var t, r = {
                held_bits: void 0, num_held_bits: 0, stream_read_1_bytes: function (e) {
                    this.held_bits = e.readUint8(), this.num_held_bits = 8
                }, stream_read_2_bytes: function (e) {
                    this.held_bits = e.readUint16(), this.num_held_bits = 16
                }, extract_bits: function (e) {
                    var t = this.held_bits >> this.num_held_bits - e & (1 << e) - 1;
                    return this.num_held_bits -= e, t
                }
            };
            if (r.stream_read_1_bytes(e), r.extract_bits(5), this.lengthSizeMinusOne = r.extract_bits(2), this.ptl_present_flag = r.extract_bits(1), this.ptl_present_flag) {
                if (r.stream_read_2_bytes(e), this.ols_idx = r.extract_bits(9), this.num_sublayers = r.extract_bits(3), this.constant_frame_rate = r.extract_bits(2), this.chroma_format_idc = r.extract_bits(2), r.stream_read_1_bytes(e), this.bit_depth_minus8 = r.extract_bits(3), r.extract_bits(5), r.stream_read_2_bytes(e), r.extract_bits(2), this.num_bytes_constraint_info = r.extract_bits(6), this.general_profile_idc = r.extract_bits(7), this.general_tier_flag = r.extract_bits(1), this.general_level_idc = e.readUint8(), r.stream_read_1_bytes(e), this.ptl_frame_only_constraint_flag = r.extract_bits(1), this.ptl_multilayer_enabled_flag = r.extract_bits(1), this.general_constraint_info = new Uint8Array(this.num_bytes_constraint_info), this.num_bytes_constraint_info) {
                    for (o = 0; o < this.num_bytes_constraint_info - 1; o++) {
                        var i = r.extract_bits(6), n = (r.stream_read_1_bytes(e), r.extract_bits(2));
                        this.general_constraint_info[o] = i << 2 | n
                    }
                    this.general_constraint_info[this.num_bytes_constraint_info - 1] = r.extract_bits(6)
                } else r.extract_bits(6);
                for (r.stream_read_1_bytes(e), this.ptl_sublayer_present_mask = 0, t = this.num_sublayers - 2; 0 <= t; --t) {
                    var s = r.extract_bits(1);
                    this.ptl_sublayer_present_mask |= s << t
                }
                for (t = this.num_sublayers; t <= 8 && 1 < this.num_sublayers; ++t) r.extract_bits(1);
                for (t = this.num_sublayers - 2; 0 <= t; --t) this.ptl_sublayer_present_mask & 1 << t && (this.sublayer_level_idc[t] = e.readUint8());
                if (this.ptl_num_sub_profiles = e.readUint8(), this.general_sub_profile_idc = [], this.ptl_num_sub_profiles) for (o = 0; o < this.ptl_num_sub_profiles; o++) this.general_sub_profile_idc.push(e.readUint32());
                this.max_picture_width = e.readUint16(), this.max_picture_height = e.readUint16(), this.avg_frame_rate = e.readUint16()
            }
            this.nalu_arrays = [];
            for (var a = e.readUint8(), o = 0; o < a; o++) {
                var l = [],
                    d = (this.nalu_arrays.push(l), r.stream_read_1_bytes(e), l.completeness = r.extract_bits(1), r.extract_bits(2), l.nalu_type = r.extract_bits(5), 1);
                for (13 != l.nalu_type && 12 != l.nalu_type && (d = e.readUint16()), t = 0; t < d; t++) {
                    var h = e.readUint16();
                    l.push({data: e.readUint8Array(h), length: h})
                }
            }
        }),b.createFullBoxCtor("vvnC", function (e) {
            var t = strm.readUint8();
            this.lengthSizeMinusOne = 3 & t
        }),b.SampleEntry.prototype.isVideo = function () {
            return !1
        },b.SampleEntry.prototype.isAudio = function () {
            return !1
        },b.SampleEntry.prototype.isSubtitle = function () {
            return !1
        },b.SampleEntry.prototype.isMetadata = function () {
            return !1
        },b.SampleEntry.prototype.isHint = function () {
            return !1
        },b.SampleEntry.prototype.getCodec = function () {
            return this.type.replace(".", "")
        },b.SampleEntry.prototype.getWidth = function () {
            return ""
        },b.SampleEntry.prototype.getHeight = function () {
            return ""
        },b.SampleEntry.prototype.getChannelCount = function () {
            return ""
        },b.SampleEntry.prototype.getSampleRate = function () {
            return ""
        },b.SampleEntry.prototype.getSampleSize = function () {
            return ""
        },b.VisualSampleEntry.prototype.isVideo = function () {
            return !0
        },b.VisualSampleEntry.prototype.getWidth = function () {
            return this.width
        },b.VisualSampleEntry.prototype.getHeight = function () {
            return this.height
        },b.AudioSampleEntry.prototype.isAudio = function () {
            return !0
        },b.AudioSampleEntry.prototype.getChannelCount = function () {
            return this.channel_count
        },b.AudioSampleEntry.prototype.getSampleRate = function () {
            return this.samplerate
        },b.AudioSampleEntry.prototype.getSampleSize = function () {
            return this.samplesize
        },b.SubtitleSampleEntry.prototype.isSubtitle = function () {
            return !0
        },b.MetadataSampleEntry.prototype.isMetadata = function () {
            return !0
        },b.decimalToHex = function (e, t) {
            var r = Number(e).toString(16);
            for (t = null == t ? 2 : t; r.length < t;) r = "0" + r;
            return r
        },b.avc1SampleEntry.prototype.getCodec = b.avc2SampleEntry.prototype.getCodec = b.avc3SampleEntry.prototype.getCodec = b.avc4SampleEntry.prototype.getCodec = function () {
            var e = b.SampleEntry.prototype.getCodec.call(this);
            return this.avcC ? e + "." + b.decimalToHex(this.avcC.AVCProfileIndication) + b.decimalToHex(this.avcC.profile_compatibility) + b.decimalToHex(this.avcC.AVCLevelIndication) : e
        },b.hev1SampleEntry.prototype.getCodec = b.hvc1SampleEntry.prototype.getCodec = function () {
            var e = b.SampleEntry.prototype.getCodec.call(this);
            if (this.hvcC) {
                switch (e += ".", this.hvcC.general_profile_space) {
                    case 0:
                        e += "";
                        break;
                    case 1:
                        e += "A";
                        break;
                    case 2:
                        e += "B";
                        break;
                    case 3:
                        e += "C"
                }
                for (var e = e + this.hvcC.general_profile_idc + ".", t = this.hvcC.general_profile_compatibility, r = 0, i = 0; i < 32 && (r |= 1 & t, 31 != i); i++) r <<= 1, t >>= 1;
                e = e + b.decimalToHex(r, 0) + ".", 0 === this.hvcC.general_tier_flag ? e += "L" : e += "H", e += this.hvcC.general_level_idc;
                var n = !1, s = "";
                for (i = 5; 0 <= i; i--) (this.hvcC.general_constraint_indicator[i] || n) && (s = "." + b.decimalToHex(this.hvcC.general_constraint_indicator[i], 0) + s, n = !0);
                e += s
            }
            return e
        },b.vvc1SampleEntry.prototype.getCodec = b.vvi1SampleEntry.prototype.getCodec = function () {
            var e = b.SampleEntry.prototype.getCodec.call(this);
            if (this.vvcC) {
                e += "." + this.vvcC.general_profile_idc, this.vvcC.general_tier_flag ? e += ".H" : e += ".L", e += this.vvcC.general_level_idc;
                var t = "";
                if (this.vvcC.general_constraint_info) {
                    var r, i = [], n = 0,
                        n = (n |= this.vvcC.ptl_frame_only_constraint << 7) | this.vvcC.ptl_multilayer_enabled << 6;
                    for (l = 0; l < this.vvcC.general_constraint_info.length; ++l) n |= this.vvcC.general_constraint_info[l] >> 2 & 63, i.push(n), n && (r = l), n = this.vvcC.general_constraint_info[l] >> 2 & 3;
                    if (void 0 === r) t = ".CA"; else {
                        for (var t = ".C", s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567", a = 0, o = 0, l = 0; l <= r; ++l) for (a = a << 8 | i[l], o += 8; 5 <= o;) t += s[a >> o - 5 & 31], a &= (1 << (o -= 5)) - 1;
                        o && (t += s[31 & (a <<= 5 - o)])
                    }
                }
                e += t
            }
            return e
        },b.mp4aSampleEntry.prototype.getCodec = function () {
            var e, t, r = b.SampleEntry.prototype.getCodec.call(this);
            return this.esds && this.esds.esd ? (e = this.esds.esd.getOTI(), t = this.esds.esd.getAudioConfig(), r + "." + b.decimalToHex(e) + (t ? "." + t : "")) : r
        },b.stxtSampleEntry.prototype.getCodec = function () {
            var e = b.SampleEntry.prototype.getCodec.call(this);
            return this.mime_format ? e + "." + this.mime_format : e
        },b.vp08SampleEntry.prototype.getCodec = b.vp09SampleEntry.prototype.getCodec = function () {
            var e = b.SampleEntry.prototype.getCodec.call(this), t = this.vpcC.level, r = this.vpcC.bitDepth;
            return e + ".0" + this.vpcC.profile + "." + (t = 0 == t ? "00" : t) + "." + (r = 8 == r ? "08" : r)
        },b.av01SampleEntry.prototype.getCodec = function () {
            var e, t = b.SampleEntry.prototype.getCodec.call(this), r = this.av1C.seq_level_idx_0;
            return 2 === this.av1C.seq_profile && 1 === this.av1C.high_bitdepth ? e = 1 === this.av1C.twelve_bit ? "12" : "10" : this.av1C.seq_profile <= 2 && (e = 1 === this.av1C.high_bitdepth ? "10" : "08"), t + "." + this.av1C.seq_profile + "." + (r = r < 10 ? "0" + r : r) + (this.av1C.seq_tier_0 ? "H" : "M") + "." + e
        },b.Box.prototype.writeHeader = function (e, t) {
            this.size += 8, this.size > d && (this.size += 8), "uuid" === this.type && (this.size += 16), u.debug("BoxWriter", "Writing box " + this.type + " of size: " + this.size + " at position " + e.getPosition() + (t || "")), this.size > d ? e.writeUint32(1) : (this.sizePosition = e.getPosition(), e.writeUint32(this.size)), e.writeString(this.type, null, 4), "uuid" === this.type && e.writeUint8Array(this.uuid), this.size > d && e.writeUint64(this.size)
        },b.FullBox.prototype.writeHeader = function (e) {
            this.size += 4, b.Box.prototype.writeHeader.call(this, e, " v=" + this.version + " f=" + this.flags), e.writeUint8(this.version), e.writeUint24(this.flags)
        },b.Box.prototype.write = function (e) {
            "mdat" === this.type ? this.data && (this.size = this.data.length, this.writeHeader(e), e.writeUint8Array(this.data)) : (this.size = this.data ? this.data.length : 0, this.writeHeader(e), this.data && e.writeUint8Array(this.data))
        },b.ContainerBox.prototype.write = function (e) {
            this.size = 0, this.writeHeader(e);
            for (var t = 0; t < this.boxes.length; t++) this.boxes[t] && (this.boxes[t].write(e), this.size += this.boxes[t].size);
            u.debug("BoxWriter", "Adjusting box " + this.type + " with new size " + this.size), e.adjustUint32(this.sizePosition, this.size)
        },b.TrackReferenceTypeBox.prototype.write = function (e) {
            this.size = 4 * this.track_ids.length, this.writeHeader(e), e.writeUint32Array(this.track_ids)
        },b.avcCBox.prototype.write = function (e) {
            var t;
            for (this.size = 7, t = 0; t < this.SPS.length; t++) this.size += 2 + this.SPS[t].length;
            for (t = 0; t < this.PPS.length; t++) this.size += 2 + this.PPS[t].length;
            for (this.ext && (this.size += this.ext.length), this.writeHeader(e), e.writeUint8(this.configurationVersion), e.writeUint8(this.AVCProfileIndication), e.writeUint8(this.profile_compatibility), e.writeUint8(this.AVCLevelIndication), e.writeUint8(this.lengthSizeMinusOne + 252), e.writeUint8(this.SPS.length + 224), t = 0; t < this.SPS.length; t++) e.writeUint16(this.SPS[t].length), e.writeUint8Array(this.SPS[t].nalu);
            for (e.writeUint8(this.PPS.length), t = 0; t < this.PPS.length; t++) e.writeUint16(this.PPS[t].length), e.writeUint8Array(this.PPS[t].nalu);
            this.ext && e.writeUint8Array(this.ext)
        },b.co64Box.prototype.write = function (e) {
            var t;
            for (this.version = 0, this.flags = 0, this.size = 4 + 8 * this.chunk_offsets.length, this.writeHeader(e), e.writeUint32(this.chunk_offsets.length), t = 0; t < this.chunk_offsets.length; t++) e.writeUint64(this.chunk_offsets[t])
        },b.cslgBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 20, this.writeHeader(e), e.writeInt32(this.compositionToDTSShift), e.writeInt32(this.leastDecodeToDisplayDelta), e.writeInt32(this.greatestDecodeToDisplayDelta), e.writeInt32(this.compositionStartTime), e.writeInt32(this.compositionEndTime)
        },b.cttsBox.prototype.write = function (e) {
            var t;
            for (this.version = 0, this.flags = 0, this.size = 4 + 8 * this.sample_counts.length, this.writeHeader(e), e.writeUint32(this.sample_counts.length), t = 0; t < this.sample_counts.length; t++) e.writeUint32(this.sample_counts[t]), 1 === this.version ? e.writeInt32(this.sample_offsets[t]) : e.writeUint32(this.sample_offsets[t])
        },b.drefBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 4, this.writeHeader(e), e.writeUint32(this.entries.length);
            for (var t = 0; t < this.entries.length; t++) this.entries[t].write(e), this.size += this.entries[t].size;
            u.debug("BoxWriter", "Adjusting box " + this.type + " with new size " + this.size), e.adjustUint32(this.sizePosition, this.size)
        },b.elngBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = this.extended_language.length, this.writeHeader(e), e.writeString(this.extended_language)
        },b.elstBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 4 + 12 * this.entries.length, this.writeHeader(e), e.writeUint32(this.entries.length);
            for (var t = 0; t < this.entries.length; t++) {
                var r = this.entries[t];
                e.writeUint32(r.segment_duration), e.writeInt32(r.media_time), e.writeInt16(r.media_rate_integer), e.writeInt16(r.media_rate_fraction)
            }
        },b.emsgBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 16 + this.message_data.length + (this.scheme_id_uri.length + 1) + (this.value.length + 1), this.writeHeader(e), e.writeCString(this.scheme_id_uri), e.writeCString(this.value), e.writeUint32(this.timescale), e.writeUint32(this.presentation_time_delta), e.writeUint32(this.event_duration), e.writeUint32(this.id), e.writeUint8Array(this.message_data)
        },b.ftypBox.prototype.write = function (e) {
            this.size = 8 + 4 * this.compatible_brands.length, this.writeHeader(e), e.writeString(this.major_brand, null, 4), e.writeUint32(this.minor_version);
            for (var t = 0; t < this.compatible_brands.length; t++) e.writeString(this.compatible_brands[t], null, 4)
        },b.hdlrBox.prototype.write = function (e) {
            this.size = 20 + this.name.length + 1, this.version = 0, this.flags = 0, this.writeHeader(e), e.writeUint32(0), e.writeString(this.handler, null, 4), e.writeUint32(0), e.writeUint32(0), e.writeUint32(0), e.writeCString(this.name)
        },b.kindBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = this.schemeURI.length + 1 + (this.value.length + 1), this.writeHeader(e), e.writeCString(this.schemeURI), e.writeCString(this.value)
        },b.mdhdBox.prototype.write = function (e) {
            this.size = 20, this.flags = 0, this.version = 0, this.writeHeader(e), e.writeUint32(this.creation_time), e.writeUint32(this.modification_time), e.writeUint32(this.timescale), e.writeUint32(this.duration), e.writeUint16(this.language), e.writeUint16(0)
        },b.mehdBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 4, this.writeHeader(e), e.writeUint32(this.fragment_duration)
        },b.mfhdBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 4, this.writeHeader(e), e.writeUint32(this.sequence_number)
        },b.mvhdBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 96, this.writeHeader(e), e.writeUint32(this.creation_time), e.writeUint32(this.modification_time), e.writeUint32(this.timescale), e.writeUint32(this.duration), e.writeUint32(this.rate), e.writeUint16(this.volume << 8), e.writeUint16(0), e.writeUint32(0), e.writeUint32(0), e.writeUint32Array(this.matrix), e.writeUint32(0), e.writeUint32(0), e.writeUint32(0), e.writeUint32(0), e.writeUint32(0), e.writeUint32(0), e.writeUint32(this.next_track_id)
        },b.SampleEntry.prototype.writeHeader = function (e) {
            this.size = 8, b.Box.prototype.writeHeader.call(this, e), e.writeUint8(0), e.writeUint8(0), e.writeUint8(0), e.writeUint8(0), e.writeUint8(0), e.writeUint8(0), e.writeUint16(this.data_reference_index)
        },b.SampleEntry.prototype.writeFooter = function (e) {
            for (var t = 0; t < this.boxes.length; t++) this.boxes[t].write(e), this.size += this.boxes[t].size;
            u.debug("BoxWriter", "Adjusting box " + this.type + " with new size " + this.size), e.adjustUint32(this.sizePosition, this.size)
        },b.SampleEntry.prototype.write = function (e) {
            this.writeHeader(e), e.writeUint8Array(this.data), this.size += this.data.length, u.debug("BoxWriter", "Adjusting box " + this.type + " with new size " + this.size), e.adjustUint32(this.sizePosition, this.size)
        },b.VisualSampleEntry.prototype.write = function (e) {
            this.writeHeader(e), this.size += 70, e.writeUint16(0), e.writeUint16(0), e.writeUint32(0), e.writeUint32(0), e.writeUint32(0), e.writeUint16(this.width), e.writeUint16(this.height), e.writeUint32(this.horizresolution), e.writeUint32(this.vertresolution), e.writeUint32(0), e.writeUint16(this.frame_count), e.writeUint8(Math.min(31, this.compressorname.length)), e.writeString(this.compressorname, null, 31), e.writeUint16(this.depth), e.writeInt16(-1), this.writeFooter(e)
        },b.AudioSampleEntry.prototype.write = function (e) {
            this.writeHeader(e), this.size += 20, e.writeUint32(0), e.writeUint32(0), e.writeUint16(this.channel_count), e.writeUint16(this.samplesize), e.writeUint16(0), e.writeUint16(0), e.writeUint32(this.samplerate << 16), this.writeFooter(e)
        },b.stppSampleEntry.prototype.write = function (e) {
            this.writeHeader(e), this.size += this.namespace.length + 1 + this.schema_location.length + 1 + this.auxiliary_mime_types.length + 1, e.writeCString(this.namespace), e.writeCString(this.schema_location), e.writeCString(this.auxiliary_mime_types), this.writeFooter(e)
        },b.SampleGroupEntry.prototype.write = function (e) {
            e.writeUint8Array(this.data)
        },b.sbgpBox.prototype.write = function (e) {
            this.version = 1, this.flags = 0, this.size = 12 + 8 * this.entries.length, this.writeHeader(e), e.writeString(this.grouping_type, null, 4), e.writeUint32(this.grouping_type_parameter), e.writeUint32(this.entries.length);
            for (var t = 0; t < this.entries.length; t++) {
                var r = this.entries[t];
                e.writeInt32(r.sample_count), e.writeInt32(r.group_description_index)
            }
        },b.sgpdBox.prototype.write = function (e) {
            var t, r;
            for (this.flags = 0, this.size = 12, t = 0; t < this.entries.length; t++) r = this.entries[t], 1 === this.version && (0 === this.default_length && (this.size += 4), this.size += r.data.length);
            for (this.writeHeader(e), e.writeString(this.grouping_type, null, 4), 1 === this.version && e.writeUint32(this.default_length), 2 <= this.version && e.writeUint32(this.default_sample_description_index), e.writeUint32(this.entries.length), t = 0; t < this.entries.length; t++) r = this.entries[t], 1 === this.version && 0 === this.default_length && e.writeUint32(r.description_length), r.write(e)
        },b.sidxBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 20 + 12 * this.references.length, this.writeHeader(e), e.writeUint32(this.reference_ID), e.writeUint32(this.timescale), e.writeUint32(this.earliest_presentation_time), e.writeUint32(this.first_offset), e.writeUint16(0), e.writeUint16(this.references.length);
            for (var t = 0; t < this.references.length; t++) {
                var r = this.references[t];
                e.writeUint32(r.reference_type << 31 | r.referenced_size), e.writeUint32(r.subsegment_duration), e.writeUint32(r.starts_with_SAP << 31 | r.SAP_type << 28 | r.SAP_delta_time)
            }
        },b.smhdBox.prototype.write = function (e) {
            this.version = 0, this.flags = 1, this.size = 4, this.writeHeader(e), e.writeUint16(this.balance), e.writeUint16(0)
        },b.stcoBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 4 + 4 * this.chunk_offsets.length, this.writeHeader(e), e.writeUint32(this.chunk_offsets.length), e.writeUint32Array(this.chunk_offsets)
        },b.stscBox.prototype.write = function (e) {
            var t;
            for (this.version = 0, this.flags = 0, this.size = 4 + 12 * this.first_chunk.length, this.writeHeader(e), e.writeUint32(this.first_chunk.length), t = 0; t < this.first_chunk.length; t++) e.writeUint32(this.first_chunk[t]), e.writeUint32(this.samples_per_chunk[t]), e.writeUint32(this.sample_description_index[t])
        },b.stsdBox.prototype.write = function (e) {
            var t;
            for (this.version = 0, this.flags = 0, this.size = 0, this.writeHeader(e), e.writeUint32(this.entries.length), this.size += 4, t = 0; t < this.entries.length; t++) this.entries[t].write(e), this.size += this.entries[t].size;
            u.debug("BoxWriter", "Adjusting box " + this.type + " with new size " + this.size), e.adjustUint32(this.sizePosition, this.size)
        },b.stshBox.prototype.write = function (e) {
            var t;
            for (this.version = 0, this.flags = 0, this.size = 4 + 8 * this.shadowed_sample_numbers.length, this.writeHeader(e), e.writeUint32(this.shadowed_sample_numbers.length), t = 0; t < this.shadowed_sample_numbers.length; t++) e.writeUint32(this.shadowed_sample_numbers[t]), e.writeUint32(this.sync_sample_numbers[t])
        },b.stssBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 4 + 4 * this.sample_numbers.length, this.writeHeader(e), e.writeUint32(this.sample_numbers.length), e.writeUint32Array(this.sample_numbers)
        },b.stszBox.prototype.write = function (e) {
            var t, r = !0;
            if (this.version = 0, (this.flags = 0) < this.sample_sizes.length) for (t = 0; t + 1 < this.sample_sizes.length;) {
                if (this.sample_sizes[t + 1] !== this.sample_sizes[0]) {
                    r = !1;
                    break
                }
                t++
            } else r = !1;
            this.size = 8, r || (this.size += 4 * this.sample_sizes.length), this.writeHeader(e), r ? e.writeUint32(this.sample_sizes[0]) : e.writeUint32(0), e.writeUint32(this.sample_sizes.length), r || e.writeUint32Array(this.sample_sizes)
        },b.sttsBox.prototype.write = function (e) {
            var t;
            for (this.version = 0, this.flags = 0, this.size = 4 + 8 * this.sample_counts.length, this.writeHeader(e), e.writeUint32(this.sample_counts.length), t = 0; t < this.sample_counts.length; t++) e.writeUint32(this.sample_counts[t]), e.writeUint32(this.sample_deltas[t])
        },b.tfdtBox.prototype.write = function (e) {
            var t = Math.pow(2, 32) - 1;
            this.version = this.baseMediaDecodeTime > t ? 1 : 0, this.flags = 0, this.size = 4, 1 === this.version && (this.size += 4), this.writeHeader(e), 1 === this.version ? e.writeUint64(this.baseMediaDecodeTime) : e.writeUint32(this.baseMediaDecodeTime)
        },b.tfhdBox.prototype.write = function (e) {
            this.version = 0, this.size = 4, this.flags & b.TFHD_FLAG_BASE_DATA_OFFSET && (this.size += 8), this.flags & b.TFHD_FLAG_SAMPLE_DESC && (this.size += 4), this.flags & b.TFHD_FLAG_SAMPLE_DUR && (this.size += 4), this.flags & b.TFHD_FLAG_SAMPLE_SIZE && (this.size += 4), this.flags & b.TFHD_FLAG_SAMPLE_FLAGS && (this.size += 4), this.writeHeader(e), e.writeUint32(this.track_id), this.flags & b.TFHD_FLAG_BASE_DATA_OFFSET && e.writeUint64(this.base_data_offset), this.flags & b.TFHD_FLAG_SAMPLE_DESC && e.writeUint32(this.default_sample_description_index), this.flags & b.TFHD_FLAG_SAMPLE_DUR && e.writeUint32(this.default_sample_duration), this.flags & b.TFHD_FLAG_SAMPLE_SIZE && e.writeUint32(this.default_sample_size), this.flags & b.TFHD_FLAG_SAMPLE_FLAGS && e.writeUint32(this.default_sample_flags)
        },b.tkhdBox.prototype.write = function (e) {
            this.version = 0, this.size = 80, this.writeHeader(e), e.writeUint32(this.creation_time), e.writeUint32(this.modification_time), e.writeUint32(this.track_id), e.writeUint32(0), e.writeUint32(this.duration), e.writeUint32(0), e.writeUint32(0), e.writeInt16(this.layer), e.writeInt16(this.alternate_group), e.writeInt16(this.volume << 8), e.writeUint16(0), e.writeInt32Array(this.matrix), e.writeUint32(this.width), e.writeUint32(this.height)
        },b.trexBox.prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = 20, this.writeHeader(e), e.writeUint32(this.track_id), e.writeUint32(this.default_sample_description_index), e.writeUint32(this.default_sample_duration), e.writeUint32(this.default_sample_size), e.writeUint32(this.default_sample_flags)
        },b.trunBox.prototype.write = function (e) {
            this.version = 0, this.size = 4, this.flags & b.TRUN_FLAGS_DATA_OFFSET && (this.size += 4), this.flags & b.TRUN_FLAGS_FIRST_FLAG && (this.size += 4), this.flags & b.TRUN_FLAGS_DURATION && (this.size += 4 * this.sample_duration.length), this.flags & b.TRUN_FLAGS_SIZE && (this.size += 4 * this.sample_size.length), this.flags & b.TRUN_FLAGS_FLAGS && (this.size += 4 * this.sample_flags.length), this.flags & b.TRUN_FLAGS_CTS_OFFSET && (this.size += 4 * this.sample_composition_time_offset.length), this.writeHeader(e), e.writeUint32(this.sample_count), this.flags & b.TRUN_FLAGS_DATA_OFFSET && (this.data_offset_position = e.getPosition(), e.writeInt32(this.data_offset)), this.flags & b.TRUN_FLAGS_FIRST_FLAG && e.writeUint32(this.first_sample_flags);
            for (var t = 0; t < this.sample_count; t++) this.flags & b.TRUN_FLAGS_DURATION && e.writeUint32(this.sample_duration[t]), this.flags & b.TRUN_FLAGS_SIZE && e.writeUint32(this.sample_size[t]), this.flags & b.TRUN_FLAGS_FLAGS && e.writeUint32(this.sample_flags[t]), this.flags & b.TRUN_FLAGS_CTS_OFFSET && (0 === this.version ? e.writeUint32(this.sample_composition_time_offset[t]) : e.writeInt32(this.sample_composition_time_offset[t]))
        },b["url Box"].prototype.write = function (e) {
            this.version = 0, this.location ? (this.flags = 0, this.size = this.location.length + 1) : (this.flags = 1, this.size = 0), this.writeHeader(e), this.location && e.writeCString(this.location)
        },b["urn Box"].prototype.write = function (e) {
            this.version = 0, this.flags = 0, this.size = this.name.length + 1 + (this.location ? this.location.length + 1 : 0), this.writeHeader(e), e.writeCString(this.name), this.location && e.writeCString(this.location)
        },b.vmhdBox.prototype.write = function (e) {
            this.version = 0, this.flags = 1, this.size = 8, this.writeHeader(e), e.writeUint16(this.graphicsmode), e.writeUint16Array(this.opcolor)
        },b.cttsBox.prototype.unpack = function (e) {
            for (var t, r = 0, i = 0; i < this.sample_counts.length; i++) for (t = 0; t < this.sample_counts[i]; t++) e[r].pts = e[r].dts + this.sample_offsets[i], r++
        },b.sttsBox.prototype.unpack = function (e) {
            for (var t, r = 0, i = 0; i < this.sample_counts.length; i++) for (t = 0; t < this.sample_counts[i]; t++) e[r].dts = 0 === r ? 0 : e[r - 1].dts + this.sample_deltas[i], r++
        },b.stcoBox.prototype.unpack = function (e) {
            for (var t = 0; t < this.chunk_offsets.length; t++) e[t].offset = this.chunk_offsets[t]
        },b.stscBox.prototype.unpack = function (e) {
            for (var t, r, i = 0, n = 0, s = 0; s < this.first_chunk.length; s++) for (t = 0; t < (s + 1 < this.first_chunk.length ? this.first_chunk[s + 1] : 1 / 0); t++) for (n++, r = 0; r < this.samples_per_chunk[s]; r++) {
                if (!e[i]) return;
                e[i].description_index = this.sample_description_index[s], e[i].chunk_index = n, i++
            }
        },b.stszBox.prototype.unpack = function (e) {
            for (var t = 0; t < this.sample_sizes.length; t++) e[t].size = this.sample_sizes[t]
        },b.DIFF_BOXES_PROP_NAMES = ["boxes", "entries", "references", "subsamples", "items", "item_infos", "extents", "associations", "subsegments", "ranges", "seekLists", "seekPoints", "esd", "levels"],b.DIFF_PRIMITIVE_ARRAY_PROP_NAMES = ["compatible_brands", "matrix", "opcolor", "sample_counts", "sample_counts", "sample_deltas", "first_chunk", "samples_per_chunk", "sample_sizes", "chunk_offsets", "sample_offsets", "sample_description_index", "sample_duration"],b.boxEqualFields = function (e, t) {
            if (e && !t) return !1;
            for (var r in e) if (!(-1 < b.DIFF_BOXES_PROP_NAMES.indexOf(r) || e[r] instanceof b.Box || t[r] instanceof b.Box || void 0 === e[r] || void 0 === t[r] || "function" == typeof e[r] || "function" == typeof t[r] || e.subBoxNames && -1 < e.subBoxNames.indexOf(r.slice(0, 4)) || t.subBoxNames && -1 < t.subBoxNames.indexOf(r.slice(0, 4)) || "data" === r || "start" === r || "size" === r || "creation_time" === r || "modification_time" === r || -1 < b.DIFF_PRIMITIVE_ARRAY_PROP_NAMES.indexOf(r) || e[r] === t[r])) return !1;
            return !0
        },b.boxEqual = function (e, t) {
            if (!b.boxEqualFields(e, t)) return !1;
            for (var r = 0; r < b.DIFF_BOXES_PROP_NAMES.length; r++) {
                var i = b.DIFF_BOXES_PROP_NAMES[r];
                if (e[i] && t[i] && !b.boxEqual(e[i], t[i])) return !1
            }
            return !0
        },n.prototype.parseSample = function (e) {
            var t, r = {resources: []}, i = new f(e.data.buffer);
            if (e.subsamples && 0 !== e.subsamples.length) {
                if (r.documentString = i.readString(e.subsamples[0].size), 1 < e.subsamples.length) for (t = 1; t < e.subsamples.length; t++) r.resources[t] = i.readUint8Array(e.subsamples[t].size)
            } else r.documentString = i.readString(e.data.length);
            return "undefined" != typeof DOMParser && (r.document = (new DOMParser).parseFromString(r.documentString, "application/xml")), r
        },s.prototype.parseSample = function (e) {
            return new f(e.data.buffer).readString(e.data.length)
        },s.prototype.parseConfig = function (e) {
            e = new f(e.buffer);
            return e.readUint32(), e.readCString()
        },t.XMLSubtitlein4Parser = n,t.Textin4Parser = s;
        B.prototype.setSegmentOptions = function (e, t, r) {
            var i, n = this.getTrackById(e);
            n && (this.fragmentedTracks.push(i = {}), i.id = e, i.user = t, (i.trak = n).nextSample = 0, i.segmentStream = null, i.nb_samples = 1e3, i.rapAlignement = !0, r && (r.nbSamples && (i.nb_samples = r.nbSamples), r.rapAlignement && (i.rapAlignement = r.rapAlignement)))
        }, B.prototype.unsetSegmentOptions = function (e) {
            for (var t = -1, r = 0; r < this.fragmentedTracks.length; r++) this.fragmentedTracks[r].id == e && (t = r);
            -1 < t && this.fragmentedTracks.splice(t, 1)
        }, B.prototype.setExtractionOptions = function (e, t, r) {
            var i, n = this.getTrackById(e);
            n && (this.extractedTracks.push(i = {}), i.id = e, i.user = t, (i.trak = n).nextSample = 0, i.nb_samples = 1e3, i.samples = [], r && r.nbSamples && (i.nb_samples = r.nbSamples))
        }, B.prototype.unsetExtractionOptions = function (e) {
            for (var t = -1, r = 0; r < this.extractedTracks.length; r++) this.extractedTracks[r].id == e && (t = r);
            -1 < t && this.extractedTracks.splice(t, 1)
        }, B.prototype.parse = function () {
            var e, t;
            if (!this.restoreParsePosition || this.restoreParsePosition()) for (; ;) {
                if (this.hasIncompleteMdat && this.hasIncompleteMdat()) {
                    if (this.processIncompleteMdat()) continue;
                    return
                }
                if (this.saveParsePosition && this.saveParsePosition(), (e = b.parseOneBox(this.stream, !1)).code === b.ERR_NOT_ENOUGH_DATA) {
                    if (this.processIncompleteBox) {
                        if (this.processIncompleteBox(e)) continue;
                        return
                    }
                    return
                }
                var r = "uuid" !== (t = e.box).type ? t.type : t.uuid;
                switch (this.boxes.push(t), r) {
                    case"mdat":
                        this.mdats.push(t);
                        break;
                    case"moof":
                        this.moofs.push(t);
                        break;
                    case"moov":
                        this.moovStartFound = !0, 0 === this.mdats.length && (this.isProgressive = !0);
                    default:
                        void 0 !== this[r] && u.warn("ISOFile", "Duplicate Box of type: " + r + ", overriding previous occurrence"), this[r] = t
                }
                this.updateUsedBytes && this.updateUsedBytes(t, e)
            }
        }, B.prototype.checkBuffer = function (e) {
            if (null == e) throw"Buffer must be defined and non empty";
            if (void 0 === e.fileStart) throw"Buffer must have a fileStart property";
            return 0 === e.byteLength ? (u.warn("ISOFile", "Ignoring empty buffer (fileStart: " + e.fileStart + ")"), this.stream.logBufferLevel(), !1) : (u.info("ISOFile", "Processing buffer (fileStart: " + e.fileStart + ")"), e.usedBytes = 0, this.stream.insertBuffer(e), this.stream.logBufferLevel(), !!this.stream.initialized() || (u.warn("ISOFile", "Not ready to start parsing"), !1))
        }, B.prototype.appendBuffer = function (e, t) {
            var r;
            if (this.checkBuffer(e)) return this.parse(), this.moovStartFound && !this.moovStartSent && (this.moovStartSent = !0, this.onMoovStart && this.onMoovStart()), this.moov ? (this.sampleListBuilt || (this.buildSampleLists(), this.sampleListBuilt = !0), this.updateSampleLists(), this.onReady && !this.readySent && (this.readySent = !0, this.onReady(this.getInfo())), this.processSamples(t), this.nextSeekPosition ? (r = this.nextSeekPosition, this.nextSeekPosition = void 0) : r = this.nextParsePosition, this.stream.getEndFilePositionAfter && (r = this.stream.getEndFilePositionAfter(r))) : r = this.nextParsePosition || 0, this.sidx && this.onSidx && !this.sidxSent && (this.onSidx(this.sidx), this.sidxSent = !0), this.meta && (this.flattenItemInfo && !this.itemListBuilt && (this.flattenItemInfo(), this.itemListBuilt = !0), this.processItems && this.processItems(this.onItem)), this.stream.cleanBuffers && (u.info("ISOFile", "Done processing buffer (fileStart: " + e.fileStart + ") - next buffer to fetch should have a fileStart position of " + r), this.stream.logBufferLevel(), this.stream.cleanBuffers(), this.stream.logBufferLevel(!0), u.info("ISOFile", "Sample data size in memory: " + this.getAllocatedSampleDataSize())), r
        }, B.prototype.getInfo = function () {
            var e, t, r, i, n, s, a = {}, o = new Date("1904-01-01T00:00:00Z").getTime();
            if (this.moov) for (a.hasMoov = !0, a.duration = this.moov.mvhd.duration, a.timescale = this.moov.mvhd.timescale, a.isFragmented = null != this.moov.mvex, a.isFragmented && this.moov.mvex.mehd && (a.fragment_duration = this.moov.mvex.mehd.fragment_duration), a.isProgressive = this.isProgressive, a.hasIOD = null != this.moov.iods, a.brands = [], a.brands.push(this.ftyp.major_brand), a.brands = a.brands.concat(this.ftyp.compatible_brands), a.created = new Date(o + 1e3 * this.moov.mvhd.creation_time), a.modified = new Date(o + 1e3 * this.moov.mvhd.modification_time), a.tracks = [], a.audioTracks = [], a.videoTracks = [], a.subtitleTracks = [], a.metadataTracks = [], a.hintTracks = [], a.otherTracks = [], e = 0; e < this.moov.traks.length; e++) {
                if (s = (r = this.moov.traks[e]).mdia.minf.stbl.stsd.entries[0], a.tracks.push(i = {}), i.id = r.tkhd.track_id, i.name = r.mdia.hdlr.name, i.references = [], r.tref) for (t = 0; t < r.tref.boxes.length; t++) i.references.push(n = {}), n.type = r.tref.boxes[t].type, n.track_ids = r.tref.boxes[t].track_ids;
                r.edts && (i.edits = r.edts.elst.entries), i.created = new Date(o + 1e3 * r.tkhd.creation_time), i.modified = new Date(o + 1e3 * r.tkhd.modification_time), i.movie_duration = r.tkhd.duration, i.movie_timescale = a.timescale, i.layer = r.tkhd.layer, i.alternate_group = r.tkhd.alternate_group, i.volume = r.tkhd.volume, i.matrix = r.tkhd.matrix, i.track_width = r.tkhd.width / 65536, i.track_height = r.tkhd.height / 65536, i.timescale = r.mdia.mdhd.timescale, i.cts_shift = r.mdia.minf.stbl.cslg, i.duration = r.mdia.mdhd.duration, i.samples_duration = r.samples_duration, i.codec = s.getCodec(), i.kind = r.udta && r.udta.kinds.length ? r.udta.kinds[0] : {
                    schemeURI: "",
                    value: ""
                }, i.language = r.mdia.elng ? r.mdia.elng.extended_language : r.mdia.mdhd.languageString, i.nb_samples = r.samples.length, i.size = r.samples_size, i.bitrate = 8 * i.size * i.timescale / i.samples_duration, s.isAudio() ? (i.type = "audio", a.audioTracks.push(i), i.audio = {}, i.audio.sample_rate = s.getSampleRate(), i.audio.channel_count = s.getChannelCount(), i.audio.sample_size = s.getSampleSize()) : s.isVideo() ? (i.type = "video", a.videoTracks.push(i), i.video = {}, i.video.width = s.getWidth(), i.video.height = s.getHeight()) : s.isSubtitle() ? (i.type = "subtitles", a.subtitleTracks.push(i)) : s.isHint() ? (i.type = "metadata", a.hintTracks.push(i)) : s.isMetadata() ? (i.type = "metadata", a.metadataTracks.push(i)) : (i.type = "metadata", a.otherTracks.push(i))
            } else a.hasMoov = !1;
            if (a.mime = "", a.hasMoov && a.tracks) {
                for (a.videoTracks && 0 < a.videoTracks.length ? a.mime += 'video/mp4; codecs="' : a.audioTracks && 0 < a.audioTracks.length ? a.mime += 'audio/mp4; codecs="' : a.mime += 'application/mp4; codecs="', e = 0; e < a.tracks.length; e++) 0 !== e && (a.mime += ","), a.mime += a.tracks[e].codec;
                a.mime += '"; profiles="', a.mime += this.ftyp.compatible_brands.join(), a.mime += '"'
            }
            return a
        }, B.prototype.processSamples = function (e) {
            var t;
            if (this.sampleProcessingStarted) {
                if (this.isFragmentationInitialized && null !== this.onSegment) for (t = 0; t < this.fragmentedTracks.length; t++) for (var r = this.fragmentedTracks[t], i = r.trak; i.nextSample < i.samples.length && this.sampleProcessingStarted;) {
                    u.debug("ISOFile", "Creating media fragment on track #" + r.id + " for sample " + i.nextSample);
                    var n = this.createFragment(r.id, i.nextSample, r.segmentStream);
                    if (!n) break;
                    if (r.segmentStream = n, i.nextSample++, (i.nextSample % r.nb_samples == 0 || e || i.nextSample >= i.samples.length) && (u.info("ISOFile", "Sending fragmented data on track #" + r.id + " for samples [" + Math.max(0, i.nextSample - r.nb_samples) + "," + (i.nextSample - 1) + "]"), u.info("ISOFile", "Sample data size in memory: " + this.getAllocatedSampleDataSize()), this.onSegment && this.onSegment(r.id, r.user, r.segmentStream.buffer, i.nextSample, e || i.nextSample >= i.samples.length), r.segmentStream = null, r !== this.fragmentedTracks[t])) break
                }
                if (null !== this.onSamples) for (t = 0; t < this.extractedTracks.length; t++) {
                    var s = this.extractedTracks[t];
                    for (i = s.trak; i.nextSample < i.samples.length && this.sampleProcessingStarted;) {
                        u.debug("ISOFile", "Exporting on track #" + s.id + " sample #" + i.nextSample);
                        var a = this.getSample(i, i.nextSample);
                        if (!a) break;
                        if (i.nextSample++, s.samples.push(a), (i.nextSample % s.nb_samples == 0 || i.nextSample >= i.samples.length) && (u.debug("ISOFile", "Sending samples on track #" + s.id + " for sample " + i.nextSample), this.onSamples && this.onSamples(s.id, s.user, s.samples), s.samples = [], s !== this.extractedTracks[t])) break
                    }
                }
            }
        }, B.prototype.getBox = function (e) {
            e = this.getBoxes(e, !0);
            return e.length ? e[0] : null
        }, B.prototype.getBoxes = function (e, t) {
            var r = [];
            return B._sweep.call(this, e, r, t), r
        }, B._sweep = function (e, t, r) {
            for (var i in this.type && this.type == e && t.push(this), this.boxes) {
                if (t.length && r) return;
                B._sweep.call(this.boxes[i], e, t, r)
            }
        }, B.prototype.getTrackSamplesInfo = function (e) {
            e = this.getTrackById(e);
            return e ? e.samples : void 0
        }, B.prototype.getTrackSample = function (e, t) {
            e = this.getTrackById(e);
            return this.getSample(e, t)
        }, B.prototype.releaseUsedSamples = function (e, t) {
            var r = 0, i = this.getTrackById(e);
            i.lastValidSample || (i.lastValidSample = 0);
            for (var n = i.lastValidSample; n < t; n++) r += this.releaseSample(i, n);
            u.info("ISOFile", "Track #" + e + " released samples up to " + t + " (released size: " + r + ", remaining: " + this.samplesDataSize + ")"), i.lastValidSample = t
        }, B.prototype.start = function () {
            this.sampleProcessingStarted = !0, this.processSamples(!1)
        }, B.prototype.stop = function () {
            this.sampleProcessingStarted = !1
        }, B.prototype.flush = function () {
            u.info("ISOFile", "Flushing remaining samples"), this.updateSampleLists(), this.processSamples(!0), this.stream.cleanBuffers(), this.stream.logBufferLevel(!0)
        }, B.prototype.seekTrack = function (e, t, r) {
            var i, n, s, a, o = 0, l = 0;
            if (0 === r.samples.length) return u.info("ISOFile", "No sample in track, cannot seek! Using time " + u.getDurationString(0, 1) + " and offset: 0"), {
                offset: 0,
                time: 0
            };
            for (i = 0; i < r.samples.length; i++) {
                if (n = r.samples[i], 0 === i) l = 0, a = n.timescale; else if (n.cts > e * n.timescale) {
                    l = i - 1;
                    break
                }
                t && n.is_sync && (o = i)
            }
            for (t && (l = o), e = r.samples[l].cts, r.nextSample = l; r.samples[l].alreadyRead === r.samples[l].size && r.samples[l + 1];) l++;
            return s = r.samples[l].offset + r.samples[l].alreadyRead, u.info("ISOFile", "Seeking to " + (t ? "RAP" : "") + " sample #" + r.nextSample + " on track " + r.tkhd.track_id + ", time " + u.getDurationString(e, a) + " and offset: " + s), {
                offset: s,
                time: e / a
            }
        }, B.prototype.seek = function (e, t) {
            var r, i, n = this.moov, s = {offset: 1 / 0, time: 1 / 0};
            if (this.moov) {
                for (i = 0; i < n.traks.length; i++) r = n.traks[i], (r = this.seekTrack(e, t, r)).offset < s.offset && (s.offset = r.offset), r.time < s.time && (s.time = r.time);
                return u.info("ISOFile", "Seeking at time " + u.getDurationString(s.time, 1) + " needs a buffer with a fileStart position of " + s.offset), s.offset === 1 / 0 ? s = {
                    offset: this.nextParsePosition,
                    time: 0
                } : s.offset = this.stream.getEndFilePositionAfter(s.offset), u.info("ISOFile", "Adjusted seek position (after checking data already in buffer): " + s.offset), s
            }
            throw"Cannot seek: moov not received!"
        }, B.prototype.equal = function (e) {
            for (var t = 0; t < this.boxes.length && t < e.boxes.length;) {
                var r = this.boxes[t], i = e.boxes[t];
                if (!b.boxEqual(r, i)) return !1;
                t++
            }
            return !0
        }, (t.ISOFile = B).prototype.lastBoxStartPosition = 0, B.prototype.parsingMdat = null, B.prototype.nextParsePosition = 0, B.prototype.discardMdatData = !1, B.prototype.processIncompleteBox = function (e) {
            var t;
            return "mdat" === e.type ? (t = new b[e.type + "Box"](e.size), this.parsingMdat = t, this.boxes.push(t), this.mdats.push(t), t.start = e.start, t.hdr_size = e.hdr_size, this.stream.addUsedBytes(t.hdr_size), this.lastBoxStartPosition = t.start + t.size, this.stream.seek(t.start + t.size, !1, this.discardMdatData) ? !(this.parsingMdat = null) : (this.moovStartFound ? this.nextParsePosition = this.stream.findEndContiguousBuf() : this.nextParsePosition = t.start + t.size, !1)) : ("moov" === e.type && (this.moovStartFound = !0, 0 === this.mdats.length && (this.isProgressive = !0)), this.stream.mergeNextBuffer && this.stream.mergeNextBuffer() ? (this.nextParsePosition = this.stream.getEndPosition(), !0) : (!e.type || this.moovStartFound ? this.nextParsePosition = this.stream.getEndPosition() : this.nextParsePosition = this.stream.getPosition() + e.size, !1))
        }, B.prototype.hasIncompleteMdat = function () {
            return null !== this.parsingMdat
        }, B.prototype.processIncompleteMdat = function () {
            var e = this.parsingMdat;
            return this.stream.seek(e.start + e.size, !1, this.discardMdatData) ? (u.debug("ISOFile", "Found 'mdat' end in buffered data"), !(this.parsingMdat = null)) : (this.nextParsePosition = this.stream.findEndContiguousBuf(), !1)
        }, B.prototype.restoreParsePosition = function () {
            return this.stream.seek(this.lastBoxStartPosition, !0, this.discardMdatData)
        }, B.prototype.saveParsePosition = function () {
            this.lastBoxStartPosition = this.stream.getPosition()
        }, B.prototype.updateUsedBytes = function (e, t) {
            this.stream.addUsedBytes && ("mdat" === e.type ? (this.stream.addUsedBytes(e.hdr_size), this.discardMdatData && this.stream.addUsedBytes(e.size - e.hdr_size)) : this.stream.addUsedBytes(e.size))
        }, B.prototype.add = b.Box.prototype.add, B.prototype.addBox = b.Box.prototype.addBox, B.prototype.init = function (e) {
            var e = e || {},
                t = (this.add("ftyp").set("major_brand", e.brands && e.brands[0] || "iso4").set("minor_version", 0).set("compatible_brands", e.brands || ["iso4"]), this.add("moov"));
            return t.add("mvhd").set("timescale", e.timescale || 600).set("rate", e.rate || 65536).set("creation_time", 0).set("modification_time", 0).set("duration", e.duration || 0).set("volume", e.width ? 0 : 256).set("matrix", [65536, 0, 0, 0, 65536, 0, 0, 0, 1073741824]).set("next_track_id", 1), t.add("mvex"), this
        }, B.prototype.addTrack = function (e) {
            this.moov || this.init(e);
            var t = e || {},
                e = (t.width = t.width || 320, t.height = t.height || 320, t.id = t.id || this.moov.mvhd.next_track_id, t.type = t.type || "avc1", this.moov.add("trak")),
                r = (this.moov.mvhd.next_track_id = t.id + 1, e.add("tkhd").set("flags", b.TKHD_FLAG_ENABLED | b.TKHD_FLAG_IN_MOVIE | b.TKHD_FLAG_IN_PREVIEW).set("creation_time", 0).set("modification_time", 0).set("track_id", t.id).set("duration", t.duration || 0).set("layer", t.layer || 0).set("alternate_group", 0).set("volume", 1).set("matrix", [0, 0, 0, 0, 0, 0, 0, 0, 0]).set("width", t.width << 16).set("height", t.height << 16), e.add("mdia")),
                i = (r.add("mdhd").set("creation_time", 0).set("modification_time", 0).set("timescale", t.timescale || 1).set("duration", t.media_duration || 0).set("language", t.language || "und"), r.add("hdlr").set("handler", t.hdlr || "vide").set("name", t.name || "Track created with MP4Box.js"), r.add("elng").set("extended_language", t.language || "fr-FR"), r.add("minf"));
            if (void 0 !== b[t.type + "SampleEntry"]) {
                var n, s, a, o = new b[t.type + "SampleEntry"], l = (o.data_reference_index = 1, "");
                for (n in b.sampleEntryCodes) for (var d = b.sampleEntryCodes[n], h = 0; h < d.length; h++) if (-1 < d.indexOf(t.type)) {
                    l = n;
                    break
                }
                switch (l) {
                    case"Visual":
                        i.add("vmhd").set("graphicsmode", 0).set("opcolor", [0, 0, 0]), o.set("width", t.width).set("height", t.height).set("horizresolution", 72 << 16).set("vertresolution", 72 << 16).set("frame_count", 1).set("compressorname", t.type + " Compressor").set("depth", 24), t.avcDecoderConfigRecord && (s = new b.avcCBox, a = new f(t.avcDecoderConfigRecord), s.parse(a), o.addBox(s));
                        break;
                    case"Audio":
                        i.add("smhd").set("balance", t.balance || 0), o.set("channel_count", t.channel_count || 2).set("samplesize", t.samplesize || 16).set("samplerate", t.samplerate || 65536);
                        break;
                    case"Hint":
                        i.add("hmhd");
                        break;
                    case"Subtitle":
                        i.add("sthd"), "stpp" === t.type && o.set("namespace", t.namespace || "nonamespace").set("schema_location", t.schema_location || "").set("auxiliary_mime_types", t.auxiliary_mime_types || "");
                        break;
                    default:
                        i.add("nmhd")
                }
                t.description && o.addBox(t.description), t.description_boxes && t.description_boxes.forEach(function (e) {
                    o.addBox(e)
                }), i.add("dinf").add("dref").addEntry((new b["url Box"]).set("flags", 1));
                r = i.add("stbl");
                return r.add("stsd").addEntry(o), r.add("stts").set("sample_counts", []).set("sample_deltas", []), r.add("stsc").set("first_chunk", []).set("samples_per_chunk", []).set("sample_description_index", []), r.add("stco").set("chunk_offsets", []), r.add("stsz").set("sample_sizes", []), this.moov.mvex.add("trex").set("track_id", t.id).set("default_sample_description_index", t.default_sample_description_index || 1).set("default_sample_duration", t.default_sample_duration || 0).set("default_sample_size", t.default_sample_size || 0).set("default_sample_flags", t.default_sample_flags || 0), this.buildTrakSampleLists(e), t.id
            }
        }, b.Box.prototype.computeSize = function (e) {
            e = e || new l;
            e.endianness = l.BIG_ENDIAN, this.write(e)
        }, B.prototype.addSample = function (e, t, r) {
            var r = r || {}, i = {}, e = this.getTrackById(e);
            if (null !== e) return i.number = e.samples.length, i.track_id = e.tkhd.track_id, i.timescale = e.mdia.mdhd.timescale, i.description_index = r.sample_description_index ? r.sample_description_index - 1 : 0, i.description = e.mdia.minf.stbl.stsd.entries[i.description_index], i.data = t, i.size = t.byteLength, i.alreadyRead = i.size, i.duration = r.duration || 1, i.cts = r.cts || 0, i.dts = r.dts || 0, i.is_sync = r.is_sync || !1, i.is_leading = r.is_leading || 0, i.depends_on = r.depends_on || 0, i.is_depended_on = r.is_depended_on || 0, i.has_redundancy = r.has_redundancy || 0, i.degradation_priority = r.degradation_priority || 0, i.offset = 0, i.subsamples = r.subsamples, e.samples.push(i), e.samples_size += i.size, e.samples_duration += i.duration, e.first_dts || (e.first_dts = r.dts), this.processSamples(), e = this.createSingleSampleMoof(i), this.addBox(e), e.computeSize(), e.trafs[0].truns[0].data_offset = e.size + 8, this.add("mdat").data = new Uint8Array(t), i
        }, B.prototype.createSingleSampleMoof = function (e) {
            var t = e.is_sync ? 1 << 25 : 65536, r = new b.moofBox,
                i = (r.add("mfhd").set("sequence_number", this.nextMoofNumber), this.nextMoofNumber++, r.add("traf")),
                n = this.getTrackById(e.track_id);
            return i.add("tfhd").set("track_id", e.track_id).set("flags", b.TFHD_FLAG_DEFAULT_BASE_IS_MOOF), i.add("tfdt").set("baseMediaDecodeTime", e.dts - (n.first_dts || 0)), i.add("trun").set("flags", b.TRUN_FLAGS_DATA_OFFSET | b.TRUN_FLAGS_DURATION | b.TRUN_FLAGS_SIZE | b.TRUN_FLAGS_FLAGS | b.TRUN_FLAGS_CTS_OFFSET).set("data_offset", 0).set("first_sample_flags", 0).set("sample_count", 1).set("sample_duration", [e.duration]).set("sample_size", [e.size]).set("sample_flags", [t]).set("sample_composition_time_offset", [e.cts - e.dts]), r
        }, B.prototype.lastMoofIndex = 0, B.prototype.samplesDataSize = 0, B.prototype.resetTables = function () {
            var e, t;
            for (this.initial_duration = this.moov.mvhd.duration, e = this.moov.mvhd.duration = 0; e < this.moov.traks.length; e++) {
                (t = this.moov.traks[e]).tkhd.duration = 0, t.mdia.mdhd.duration = 0, (t.mdia.minf.stbl.stco || t.mdia.minf.stbl.co64).chunk_offsets = [], (r = t.mdia.minf.stbl.stsc).first_chunk = [], r.samples_per_chunk = [], r.sample_description_index = [], (t.mdia.minf.stbl.stsz || t.mdia.minf.stbl.stz2).sample_sizes = [], (r = t.mdia.minf.stbl.stts).sample_counts = [], r.sample_deltas = [], (r = t.mdia.minf.stbl.ctts) && (r.sample_counts = [], r.sample_offsets = []);
                var r = t.mdia.minf.stbl.stss, r = t.mdia.minf.stbl.boxes.indexOf(r);
                -1 != r && (t.mdia.minf.stbl.boxes[r] = null)
            }
        }, B.initSampleGroups = function (e, t, r, i, n) {
            var s, a, o, l;

            function d(e, t, r) {
                this.grouping_type = e, this.grouping_type_parameter = t, this.sbgp = r, this.last_sample_in_run = -1, this.entry_index = -1
            }

            for (t && (t.sample_groups_info = []), e.sample_groups_info || (e.sample_groups_info = []), a = 0; a < r.length; a++) {
                for (l = r[a].grouping_type + "/" + r[a].grouping_type_parameter, o = new d(r[a].grouping_type, r[a].grouping_type_parameter, r[a]), t && (t.sample_groups_info[l] = o), e.sample_groups_info[l] || (e.sample_groups_info[l] = o), s = 0; s < i.length; s++) i[s].grouping_type === r[a].grouping_type && (o.description = i[s], o.description.used = !0);
                if (n) for (s = 0; s < n.length; s++) n[s].grouping_type === r[a].grouping_type && (o.fragment_description = n[s], o.fragment_description.used = !0, o.is_fragment = !0)
            }
            if (t) {
                if (n) for (a = 0; a < n.length; a++) !n[a].used && 2 <= n[a].version && (l = n[a].grouping_type + "/0", (o = new d(n[a].grouping_type, 0)).is_fragment = !0, t.sample_groups_info[l] || (t.sample_groups_info[l] = o))
            } else for (a = 0; a < i.length; a++) !i[a].used && 2 <= i[a].version && (l = i[a].grouping_type + "/0", o = new d(i[a].grouping_type, 0), e.sample_groups_info[l] || (e.sample_groups_info[l] = o))
        }, B.setSampleGroupProperties = function (e, t, r, i) {
            var n, s, a;
            for (n in t.sample_groups = [], i) t.sample_groups[n] = {}, t.sample_groups[n].grouping_type = i[n].grouping_type, t.sample_groups[n].grouping_type_parameter = i[n].grouping_type_parameter, r >= i[n].last_sample_in_run && (i[n].last_sample_in_run < 0 && (i[n].last_sample_in_run = 0), i[n].entry_index++, i[n].entry_index <= i[n].sbgp.entries.length - 1 && (i[n].last_sample_in_run += i[n].sbgp.entries[i[n].entry_index].sample_count)), i[n].entry_index <= i[n].sbgp.entries.length - 1 ? t.sample_groups[n].group_description_index = i[n].sbgp.entries[i[n].entry_index].group_description_index : t.sample_groups[n].group_description_index = -1, 0 !== t.sample_groups[n].group_description_index && (a = i[n].fragment_description || i[n].description, 0 < t.sample_groups[n].group_description_index ? (s = 65535 < t.sample_groups[n].group_description_index ? (t.sample_groups[n].group_description_index >> 16) - 1 : t.sample_groups[n].group_description_index - 1, a && 0 <= s && (t.sample_groups[n].description = a.entries[s])) : a && 2 <= a.version && 0 < a.default_group_description_index && (t.sample_groups[n].description = a.entries[a.default_group_description_index - 1]))
        }, B.process_sdtp = function (e, t, r) {
            t && (e ? (t.is_leading = e.is_leading[r], t.depends_on = e.sample_depends_on[r], t.is_depended_on = e.sample_is_depended_on[r], t.has_redundancy = e.sample_has_redundancy[r]) : (t.is_leading = 0, t.depends_on = 0, t.is_depended_on = 0, t.has_redundancy = 0))
        }, B.prototype.buildSampleLists = function () {
            for (var e, t = 0; t < this.moov.traks.length; t++) e = this.moov.traks[t], this.buildTrakSampleLists(e)
        }, B.prototype.buildTrakSampleLists = function (e) {
            var t, r, i, n, s, a, o, l, d, h, f, u, p, c, m, _, g, y, b, v, w, S, E, U;
            if (e.samples = [], e.samples_duration = 0, e.samples_size = 0, r = e.mdia.minf.stbl.stco || e.mdia.minf.stbl.co64, i = e.mdia.minf.stbl.stsc, n = e.mdia.minf.stbl.stsz || e.mdia.minf.stbl.stz2, s = e.mdia.minf.stbl.stts, a = e.mdia.minf.stbl.ctts, o = e.mdia.minf.stbl.stss, l = e.mdia.minf.stbl.stsd, d = e.mdia.minf.stbl.subs, u = e.mdia.minf.stbl.stdp, h = e.mdia.minf.stbl.sbgps, f = e.mdia.minf.stbl.sgpds, w = v = b = y = -1, U = E = S = 0, B.initSampleGroups(e, null, h, f), void 0 !== n) {
                for (t = 0; t < n.sample_sizes.length; t++) {
                    var x = {};
                    x.number = t, x.track_id = e.tkhd.track_id, x.timescale = e.mdia.mdhd.timescale, x.alreadyRead = 0, (e.samples[t] = x).size = n.sample_sizes[t], e.samples_size += x.size, 0 === t ? (p = 0, x.chunk_index = c = 1, x.chunk_run_index = p, g = i.samples_per_chunk[p], _ = 0, m = p + 1 < i.first_chunk.length ? i.first_chunk[p + 1] - 1 : 1 / 0) : t < g ? (x.chunk_index = c, x.chunk_run_index = p) : (c++, _ = 0, (x.chunk_index = c) <= m || (m = ++p + 1 < i.first_chunk.length ? i.first_chunk[p + 1] - 1 : 1 / 0), x.chunk_run_index = p, g += i.samples_per_chunk[p]), x.description_index = i.sample_description_index[x.chunk_run_index] - 1, x.description = l.entries[x.description_index], x.offset = r.chunk_offsets[x.chunk_index - 1] + _, _ += x.size, y < t && (b++, y < 0 && (y = 0), y += s.sample_counts[b]), 0 < t ? (e.samples[t - 1].duration = s.sample_deltas[b], e.samples_duration += e.samples[t - 1].duration, x.dts = e.samples[t - 1].dts + e.samples[t - 1].duration) : x.dts = 0, a ? (v <= t && (w++, v < 0 && (v = 0), v += a.sample_counts[w]), x.cts = e.samples[t].dts + a.sample_offsets[w]) : x.cts = x.dts, o ? (t == o.sample_numbers[S] - 1 ? (x.is_sync = !0, S++) : (x.is_sync = !1, x.degradation_priority = 0), d && d.entries[E].sample_delta + U == t + 1 && (x.subsamples = d.entries[E].subsamples, U += d.entries[E].sample_delta, E++)) : x.is_sync = !0, B.process_sdtp(e.mdia.minf.stbl.sdtp, x, x.number), x.degradation_priority = u ? u.priority[t] : 0, d && d.entries[E].sample_delta + U == t && (x.subsamples = d.entries[E].subsamples, U += d.entries[E].sample_delta), (0 < h.length || 0 < f.length) && B.setSampleGroupProperties(e, x, t, e.sample_groups_info)
                }
                0 < t && (e.samples[t - 1].duration = Math.max(e.mdia.mdhd.duration - e.samples[t - 1].dts, 0), e.samples_duration += e.samples[t - 1].duration)
            }
        }, B.prototype.updateSampleLists = function () {
            var e, t, r, i, n, s, a, o, l, d, h, f;
            if (void 0 !== this.moov) for (; this.lastMoofIndex < this.moofs.length;) if (a = this.moofs[this.lastMoofIndex], this.lastMoofIndex++, "moof" == a.type) for (o = a, e = 0; e < o.trafs.length; e++) {
                for (l = o.trafs[e], d = this.getTrackById(l.tfhd.track_id), h = this.getTrexById(l.tfhd.track_id), t = l.tfhd.flags & b.TFHD_FLAG_SAMPLE_DESC ? l.tfhd.default_sample_description_index : h ? h.default_sample_description_index : 1, r = l.tfhd.flags & b.TFHD_FLAG_SAMPLE_DUR ? l.tfhd.default_sample_duration : h ? h.default_sample_duration : 0, i = l.tfhd.flags & b.TFHD_FLAG_SAMPLE_SIZE ? l.tfhd.default_sample_size : h ? h.default_sample_size : 0, n = l.tfhd.flags & b.TFHD_FLAG_SAMPLE_FLAGS ? l.tfhd.default_sample_flags : h ? h.default_sample_flags : 0, (l.sample_number = 0) < l.sbgps.length && B.initSampleGroups(d, l, l.sbgps, d.mdia.minf.stbl.sgpds, l.sgpds), y = 0; y < l.truns.length; y++) for (var u = l.truns[y], p = 0; p < u.sample_count; p++) {
                    (f = {}).moof_number = this.lastMoofIndex, f.number_in_traf = l.sample_number, l.sample_number++, f.number = d.samples.length, l.first_sample_index = d.samples.length, d.samples.push(f), f.track_id = d.tkhd.track_id, f.timescale = d.mdia.mdhd.timescale, f.description_index = t - 1, f.description = d.mdia.minf.stbl.stsd.entries[f.description_index], f.size = i, u.flags & b.TRUN_FLAGS_SIZE && (f.size = u.sample_size[p]), d.samples_size += f.size, f.duration = r, u.flags & b.TRUN_FLAGS_DURATION && (f.duration = u.sample_duration[p]), d.samples_duration += f.duration, d.first_traf_merged || 0 < p ? f.dts = d.samples[d.samples.length - 2].dts + d.samples[d.samples.length - 2].duration : (l.tfdt ? f.dts = l.tfdt.baseMediaDecodeTime : f.dts = 0, d.first_traf_merged = !0), f.cts = f.dts, u.flags & b.TRUN_FLAGS_CTS_OFFSET && (f.cts = f.dts + u.sample_composition_time_offset[p]), c = n, u.flags & b.TRUN_FLAGS_FLAGS ? c = u.sample_flags[p] : 0 === p && u.flags & b.TRUN_FLAGS_FIRST_FLAG && (c = u.first_sample_flags), f.is_sync = !(c >> 16 & 1), f.is_leading = c >> 26 & 3, f.depends_on = c >> 24 & 3, f.is_depended_on = c >> 22 & 3, f.has_redundancy = c >> 20 & 3, f.degradation_priority = 65535 & c;
                    var c = !!(l.tfhd.flags & b.TFHD_FLAG_BASE_DATA_OFFSET),
                        m = !!(l.tfhd.flags & b.TFHD_FLAG_DEFAULT_BASE_IS_MOOF),
                        _ = !!(u.flags & b.TRUN_FLAGS_DATA_OFFSET),
                        c = c ? l.tfhd.base_data_offset : m || 0 === y ? o.start : s;
                    f.offset = 0 === y && 0 === p ? _ ? c + u.data_offset : c : s, s = f.offset + f.size, (0 < l.sbgps.length || 0 < l.sgpds.length || 0 < d.mdia.minf.stbl.sbgps.length || 0 < d.mdia.minf.stbl.sgpds.length) && B.setSampleGroupProperties(d, f, f.number_in_traf, l.sample_groups_info)
                }
                if (l.subs) {
                    d.has_fragment_subsamples = !0;
                    for (var g = l.first_sample_index, y = 0; y < l.subs.entries.length; y++) g += l.subs.entries[y].sample_delta, (f = d.samples[g - 1]).subsamples = l.subs.entries[y].subsamples
                }
            }
        }, B.prototype.getSample = function (e, t) {
            var r = e.samples[t];
            if (!this.moov) return null;
            if (r.data) {
                if (r.alreadyRead == r.size) return r
            } else r.data = new Uint8Array(r.size), r.alreadyRead = 0, this.samplesDataSize += r.size, u.debug("ISOFile", "Allocating sample #" + t + " on track #" + e.tkhd.track_id + " of size " + r.size + " (total: " + this.samplesDataSize + ")");
            for (; ;) {
                var i = this.stream.findPosition(!0, r.offset + r.alreadyRead, !1);
                if (!(-1 < i)) return null;
                var n = (i = this.stream.buffers[i]).byteLength - (r.offset + r.alreadyRead - i.fileStart);
                if (r.size - r.alreadyRead <= n) return u.debug("ISOFile", "Getting sample #" + t + " data (alreadyRead: " + r.alreadyRead + " offset: " + (r.offset + r.alreadyRead - i.fileStart) + " read size: " + (r.size - r.alreadyRead) + " full size: " + r.size + ")"), l.memcpy(r.data.buffer, r.alreadyRead, i, r.offset + r.alreadyRead - i.fileStart, r.size - r.alreadyRead), i.usedBytes += r.size - r.alreadyRead, this.stream.logBufferLevel(), r.alreadyRead = r.size, r;
                if (0 == n) return null;
                u.debug("ISOFile", "Getting sample #" + t + " partial data (alreadyRead: " + r.alreadyRead + " offset: " + (r.offset + r.alreadyRead - i.fileStart) + " read size: " + n + " full size: " + r.size + ")"), l.memcpy(r.data.buffer, r.alreadyRead, i, r.offset + r.alreadyRead - i.fileStart, n), r.alreadyRead += n, i.usedBytes += n, this.stream.logBufferLevel()
            }
        }, B.prototype.releaseSample = function (e, t) {
            e = e.samples[t];
            return e.data ? (this.samplesDataSize -= e.size, e.data = null, e.alreadyRead = 0, e.size) : 0
        }, B.prototype.getAllocatedSampleDataSize = function () {
            return this.samplesDataSize
        }, B.prototype.getCodecs = function () {
            for (var e = "", t = 0; t < this.moov.traks.length; t++) 0 < t && (e += ","), e += this.moov.traks[t].mdia.minf.stbl.stsd.entries[0].getCodec();
            return e
        }, B.prototype.getTrexById = function (e) {
            var t;
            if (!this.moov || !this.moov.mvex) return null;
            for (t = 0; t < this.moov.mvex.trexs.length; t++) {
                var r = this.moov.mvex.trexs[t];
                if (r.track_id == e) return r
            }
            return null
        }, B.prototype.getTrackById = function (e) {
            if (void 0 === this.moov) return null;
            for (var t = 0; t < this.moov.traks.length; t++) {
                var r = this.moov.traks[t];
                if (r.tkhd.track_id == e) return r
            }
            return null
        }, B.prototype.items = [], B.prototype.itemsDataSize = 0, B.prototype.flattenItemInfo = function () {
            var e = this.items, t = this.meta;
            if (null != t && void 0 !== t.hdlr && void 0 !== t.iinf) {
                for (l = 0; l < t.iinf.item_infos.length; l++) (i = {}).id = t.iinf.item_infos[l].item_ID, (e[i.id] = i).ref_to = [], i.name = t.iinf.item_infos[l].item_name, 0 < t.iinf.item_infos[l].protection_index && (i.protection = t.ipro.protections[t.iinf.item_infos[l].protection_index - 1]), t.iinf.item_infos[l].item_type ? i.type = t.iinf.item_infos[l].item_type : i.type = "mime", i.content_type = t.iinf.item_infos[l].content_type, i.content_encoding = t.iinf.item_infos[l].content_encoding;
                if (t.iloc) for (l = 0; l < t.iloc.items.length; l++) {
                    var r = t.iloc.items[l], i = e[r.item_ID];
                    switch (0 !== r.data_reference_index && (u.warn("Item storage with reference to other files: not supported"), i.source = t.dinf.boxes[r.data_reference_index - 1]), r.construction_method) {
                        case 0:
                            break;
                        case 1:
                        case 2:
                            u.warn("Item storage with construction_method : not supported")
                    }
                    for (i.extents = [], s = i.size = 0; s < r.extents.length; s++) i.extents[s] = {}, i.extents[s].offset = r.extents[s].extent_offset + r.base_offset, i.extents[s].length = r.extents[s].extent_length, i.extents[s].alreadyRead = 0, i.size += i.extents[s].length
                }
                if (t.pitm && (e[t.pitm.item_id].primary = !0), t.iref) for (l = 0; l < t.iref.references.length; l++) for (var n = t.iref.references[l], s = 0; s < n.references.length; s++) e[n.from_item_ID].ref_to.push({
                    type: n.type,
                    id: n.references[s]
                });
                if (t.iprp) for (var a = 0; a < t.iprp.ipmas.length; a++) for (var o = t.iprp.ipmas[a], l = 0; l < o.associations.length; l++) {
                    var d = o.associations[l];
                    for (void 0 === (i = e[d.id]).properties && (i.properties = {}, i.properties.boxes = []), s = 0; s < d.props.length; s++) {
                        var h = d.props[s];
                        0 < h.property_index && h.property_index - 1 < t.iprp.ipco.boxes.length && (h = t.iprp.ipco.boxes[h.property_index - 1], i.properties[h.type] = h, i.properties.boxes.push(h))
                    }
                }
            }
        }, B.prototype.getItem = function (e) {
            var t;
            if (!this.meta) return null;
            if (!(t = this.items[e]).data && t.size) t.data = new Uint8Array(t.size), t.alreadyRead = 0, this.itemsDataSize += t.size, u.debug("ISOFile", "Allocating item #" + e + " of size " + t.size + " (total: " + this.itemsDataSize + ")"); else if (t.alreadyRead === t.size) return t;
            for (var r = 0; r < t.extents.length; r++) {
                var i = t.extents[r];
                if (i.alreadyRead !== i.length) {
                    var n = this.stream.findPosition(!0, i.offset + i.alreadyRead, !1);
                    if (!(-1 < n)) return null;
                    var s = (n = this.stream.buffers[n]).byteLength - (i.offset + i.alreadyRead - n.fileStart);
                    if (!(i.length - i.alreadyRead <= s)) return u.debug("ISOFile", "Getting item #" + e + " extent #" + r + " partial data (alreadyRead: " + i.alreadyRead + " offset: " + (i.offset + i.alreadyRead - n.fileStart) + " read size: " + s + " full extent size: " + i.length + " full item size: " + t.size + ")"), l.memcpy(t.data.buffer, t.alreadyRead, n, i.offset + i.alreadyRead - n.fileStart, s), i.alreadyRead += s, t.alreadyRead += s, n.usedBytes += s, this.stream.logBufferLevel(), null;
                    u.debug("ISOFile", "Getting item #" + e + " extent #" + r + " data (alreadyRead: " + i.alreadyRead + " offset: " + (i.offset + i.alreadyRead - n.fileStart) + " read size: " + (i.length - i.alreadyRead) + " full extent size: " + i.length + " full item size: " + t.size + ")"), l.memcpy(t.data.buffer, t.alreadyRead, n, i.offset + i.alreadyRead - n.fileStart, i.length - i.alreadyRead), n.usedBytes += i.length - i.alreadyRead, this.stream.logBufferLevel(), t.alreadyRead += i.length - i.alreadyRead, i.alreadyRead = i.length
                }
            }
            return t.alreadyRead === t.size ? t : null
        }, B.prototype.releaseItem = function (e) {
            var t = this.items[e];
            if (t.data) {
                this.itemsDataSize -= t.size, t.data = null;
                for (var r = t.alreadyRead = 0; r < t.extents.length; r++) t.extents[r].alreadyRead = 0;
                return t.size
            }
            return 0
        }, B.prototype.processItems = function (e) {
            for (var t in this.items) {
                t = this.items[t];
                this.getItem(t.id), e && !t.sent && (e(t), t.sent = !0, t.data = null)
            }
        }, B.prototype.hasItem = function (e) {
            for (var t in this.items) {
                t = this.items[t];
                if (t.name === e) return t.id
            }
            return -1
        }, B.prototype.getMetaHandler = function () {
            return this.meta ? this.meta.hdlr.handler : null
        }, B.prototype.getPrimaryItem = function () {
            return this.meta && this.meta.pitm ? this.getItem(this.meta.pitm.item_id) : null
        }, B.prototype.itemToFragmentedTrackFile = function (e) {
            var e = e || {};
            if (null == (e = e.itemId ? this.getItem(e.itemId) : this.getPrimaryItem())) return null;
            var t = new B, r = (t.discardMdatData = !1, {type: e.type, description_boxes: e.properties.boxes}),
                r = (e.properties.ispe && (r.width = e.properties.ispe.image_width, r.height = e.properties.ispe.image_height), t.addTrack(r));
            return r ? (t.addSample(r, e.data), t) : null
        }, B.prototype.write = function (e) {
            for (var t = 0; t < this.boxes.length; t++) this.boxes[t].write(e)
        }, B.prototype.createFragment = function (e, t, r) {
            var e = this.getTrackById(e), i = this.getSample(e, t);
            if (null == i) return i = e.samples[t], this.nextSeekPosition ? this.nextSeekPosition = Math.min(i.offset + i.alreadyRead, this.nextSeekPosition) : this.nextSeekPosition = e.samples[t].offset + i.alreadyRead, null;
            e = r || new l, e.endianness = l.BIG_ENDIAN, t = this.createSingleSampleMoof(i), t.write(e), t.trafs[0].truns[0].data_offset = t.size + 8, u.debug("MP4Box", "Adjusting data_offset with new value " + t.trafs[0].truns[0].data_offset), e.adjustUint32(t.trafs[0].truns[0].data_offset_position, t.trafs[0].truns[0].data_offset), r = new b.mdatBox;
            return r.data = i.data, r.write(e), e
        }, B.writeInitializationSegment = function (e, t, r, i) {
            u.debug("ISOFile", "Generating initialization segment");
            var n, s = new l, a = (s.endianness = l.BIG_ENDIAN, e.write(s), t.add("mvex"));
            for (r && a.add("mehd").set("fragment_duration", r), n = 0; n < t.traks.length; n++) a.add("trex").set("track_id", t.traks[n].tkhd.track_id).set("default_sample_description_index", 1).set("default_sample_duration", i).set("default_sample_size", 0).set("default_sample_flags", 65536);
            return t.write(s), s.buffer
        }, B.prototype.save = function (e) {
            var t = new l;
            t.endianness = l.BIG_ENDIAN, this.write(t), t.save(e)
        }, B.prototype.getBuffer = function () {
            var e = new l;
            return e.endianness = l.BIG_ENDIAN, this.write(e), e.buffer
        }, B.prototype.initializeSegmentation = function () {
            var e, t, r, i;
            for (null === this.onSegment && u.warn("MP4Box", "No segmentation callback set!"), this.isFragmentationInitialized || (this.isFragmentationInitialized = !0, this.nextMoofNumber = 0, this.resetTables()), t = [], e = 0; e < this.fragmentedTracks.length; e++) {
                var n = new b.moovBox;
                n.mvhd = this.moov.mvhd, n.boxes.push(n.mvhd), r = this.getTrackById(this.fragmentedTracks[e].id), n.boxes.push(r), n.traks.push(r), (i = {}).id = r.tkhd.track_id, i.user = this.fragmentedTracks[e].user, i.buffer = B.writeInitializationSegment(this.ftyp, n, this.moov.mvex && this.moov.mvex.mehd ? this.moov.mvex.mehd.fragment_duration : void 0, 0 < this.moov.traks[e].samples.length ? this.moov.traks[e].samples[0].duration : 0), t.push(i)
            }
            return t
        }, b.Box.prototype.printHeader = function (e) {
            this.size += 8, this.size > d && (this.size += 8), "uuid" === this.type && (this.size += 16), e.log(e.indent + "size:" + this.size), e.log(e.indent + "type:" + this.type)
        }, b.FullBox.prototype.printHeader = function (e) {
            this.size += 4, b.Box.prototype.printHeader.call(this, e), e.log(e.indent + "version:" + this.version), e.log(e.indent + "flags:" + this.flags)
        }, b.Box.prototype.print = function (e) {
            this.printHeader(e)
        }, b.ContainerBox.prototype.print = function (e) {
            this.printHeader(e);
            for (var t, r = 0; r < this.boxes.length; r++) this.boxes[r] && (t = e.indent, e.indent += " ", this.boxes[r].print(e), e.indent = t)
        }, B.prototype.print = function (e) {
            e.indent = "";
            for (var t = 0; t < this.boxes.length; t++) this.boxes[t] && this.boxes[t].print(e)
        }, b.mvhdBox.prototype.print = function (e) {
            b.FullBox.prototype.printHeader.call(this, e), e.log(e.indent + "creation_time: " + this.creation_time), e.log(e.indent + "modification_time: " + this.modification_time), e.log(e.indent + "timescale: " + this.timescale), e.log(e.indent + "duration: " + this.duration), e.log(e.indent + "rate: " + this.rate), e.log(e.indent + "volume: " + (this.volume >> 8)), e.log(e.indent + "matrix: " + this.matrix.join(", ")), e.log(e.indent + "next_track_id: " + this.next_track_id)
        }, b.tkhdBox.prototype.print = function (e) {
            b.FullBox.prototype.printHeader.call(this, e), e.log(e.indent + "creation_time: " + this.creation_time), e.log(e.indent + "modification_time: " + this.modification_time), e.log(e.indent + "track_id: " + this.track_id), e.log(e.indent + "duration: " + this.duration), e.log(e.indent + "volume: " + (this.volume >> 8)), e.log(e.indent + "matrix: " + this.matrix.join(", ")), e.log(e.indent + "layer: " + this.layer), e.log(e.indent + "alternate_group: " + this.alternate_group), e.log(e.indent + "width: " + this.width), e.log(e.indent + "height: " + this.height)
        };
        var h = function (e, t) {
            e = void 0 === e || e, t = new B(t);
            return t.discardMdatData = !e, t
        };
        t.createFile = h
    });

    function Je(e) {
        return e.reduce((e, t) => 256 * e + t)
    }

    function Qe(e) {
        const t = [101, 103, 119, 99], r = e.length - 28, i = e.slice(r, r + t.length);
        return t.every((e, t) => e === i[t])
    }

    re.Log, re.MP4BoxStream, re.DataStream, re.MultiBufferStream, re.MPEG4DescriptorParser, re.BoxParser, re.XMLSubtitlein4Parser, re.Textin4Parser, re.ISOFile, re.createFile;

    class et {
        constructor() {
            this.s = null, this.a = null, this.l = 0, this.c = 0, this.u = 1 / 0, this.A = !1, this.d = !1, this.r = 4194304, this.n = new Uint8Array([30, 158, 90, 33, 244, 57, 83, 165, 2, 70, 35, 87, 215, 231, 226, 108]), this.t = this.n.slice().reverse()
        }

        destroy() {
            this.s = null, this.a = null, this.l = 0, this.c = 0, this.u = 1 / 0, this.A = !1, this.d = !1, this.r = 4194304, this.n = null, this.t = null
        }

        transport(e) {
            if (!this.s && 50 < this.l) return e;
            if (this.l++, this.d) return e;
            var t = new Uint8Array(e);
            if (this.A) {
                if (!(this.c < this.u)) return this.a && this.s ? (this.a.set(t, this.r), this.s.parse(null, this.r, t.byteLength), this.a.slice(this.r, this.r + t.byteLength)) : (console.error("video_error_2"), this.d = !0, e);
                Qe(t) && this.c++
            } else {
                var r = function (e, t) {
                    var r = function (r, i) {
                        for (let t = 0; t < r.byteLength - i.length; t++) for (let e = 0; e < i.length && r[t + e] === i[e]; e++) if (e === i.length - 1) return t;
                        return null
                    }(e, t);
                    if (r) {
                        const t = Je(e.slice(r + 16, r + 16 + 8));
                        return [t, Je(e.slice(r + 24, r + 24 + 8)), e.slice(r + 32, r + 32 + t).map(e => ~e)]
                    }
                    return null
                }(t, this.t);
                if (!r) return e;
                var i = function (e) {
                    try {
                        if ("object" != typeof WebAssembly || "function" != typeof WebAssembly.instantiate) throw null;
                        {
                            const e = new WebAssembly.Module(Uint8Array.of(0, 97, 115, 109, 1, 0, 0, 0));
                            if (!(e instanceof WebAssembly.Module && new WebAssembly.Instance(e) instanceof WebAssembly.Instance)) throw null
                        }
                    } catch (e) {
                        return new Error("video_error_4")
                    }
                    let t;
                    try {
                        t = {
                            env: {
                                __handle_stack_overflow: () => e(new Error("video_error_1")),
                                memory: new WebAssembly.Memory({initial: 256, maximum: 256})
                            }
                        }
                    } catch (e) {
                        return new Error("video_error_5")
                    }
                    return t
                }(e);
                if (i instanceof Error) return console.error(i.message), this.d = !0, e;
                this.A = !0, this.u = r[1], Qe(t) && this.c++, WebAssembly.instantiate(r[2], i).then(e => {
                    if ("function" != typeof (t = e.instance.exports).parse || "object" != typeof t.memory) return this.d = !0, void console.error("video_error_3");
                    var t;
                    this.s = e.instance.exports, this.a = new Uint8Array(this.s.memory.buffer)
                }).catch(e => {
                    this.d = !0, console.error("video_error_6")
                })
            }
            return e
        }
    }

    const U = 16,
        c = [214, 144, 233, 254, 204, 225, 61, 183, 22, 182, 20, 194, 40, 251, 44, 5, 43, 103, 154, 118, 42, 190, 4, 195, 170, 68, 19, 38, 73, 134, 6, 153, 156, 66, 80, 244, 145, 239, 152, 122, 51, 84, 11, 67, 237, 207, 172, 98, 228, 179, 28, 169, 201, 8, 232, 149, 128, 223, 148, 250, 117, 143, 63, 166, 71, 7, 167, 252, 243, 115, 23, 186, 131, 89, 60, 25, 230, 133, 79, 168, 104, 107, 129, 178, 113, 100, 218, 139, 248, 235, 15, 75, 112, 86, 157, 53, 30, 36, 14, 94, 99, 88, 209, 162, 37, 34, 124, 59, 1, 33, 120, 135, 212, 0, 70, 87, 159, 211, 39, 82, 76, 54, 2, 231, 160, 196, 200, 158, 234, 191, 138, 210, 64, 199, 56, 181, 163, 247, 242, 206, 249, 97, 21, 161, 224, 174, 93, 164, 155, 52, 26, 85, 173, 147, 50, 48, 245, 140, 177, 227, 29, 246, 226, 46, 130, 102, 202, 96, 192, 41, 35, 171, 13, 83, 78, 111, 213, 219, 55, 69, 222, 253, 142, 47, 3, 255, 106, 114, 109, 108, 91, 81, 141, 27, 175, 146, 187, 221, 188, 127, 17, 217, 92, 65, 31, 16, 90, 216, 10, 193, 49, 136, 165, 205, 123, 189, 45, 116, 208, 18, 184, 229, 180, 176, 137, 105, 151, 74, 12, 150, 119, 126, 101, 185, 241, 9, 197, 110, 198, 132, 24, 240, 125, 236, 58, 220, 77, 32, 121, 238, 95, 62, 215, 203, 57, 72],
        tt = [462357, 472066609, 943670861, 1415275113, 1886879365, 2358483617, 2830087869, 3301692121, 3773296373, 4228057617, 404694573, 876298825, 1347903077, 1819507329, 2291111581, 2762715833, 3234320085, 3705924337, 4177462797, 337322537, 808926789, 1280531041, 1752135293, 2223739545, 2695343797, 3166948049, 3638552301, 4110090761, 269950501, 741554753, 1213159005, 1684763257];

    function rt(r) {
        const i = [];
        for (let e = 0, t = r.length; e < t; e += 2) i.push(parseInt(r.substr(e, 2), 16));
        return i
    }

    function m(e, t) {
        t &= 31;
        return e << t | e >>> 32 - t
    }

    function x(e) {
        return (255 & c[e >>> 24 & 255]) << 24 | (255 & c[e >>> 16 & 255]) << 16 | (255 & c[e >>> 8 & 255]) << 8 | 255 & c[255 & e]
    }

    function it(e) {
        return e ^ m(e, 2) ^ m(e, 10) ^ m(e, 18) ^ m(e, 24)
    }

    function nt(e) {
        return e ^ m(e, 13) ^ m(e, 23)
    }

    function st(t, r, i, e) {
        let {
            padding: n = "pkcs#7",
            mode: s,
            iv: a = [],
            output: o = "string"
        } = 3 < arguments.length && void 0 !== e ? e : {};
        if ("cbc" === s && 16 !== (a = "string" == typeof a ? rt(a) : a).length) throw new Error("iv is invalid");
        if (16 !== (r = "string" == typeof r ? rt(r) : r).length) throw new Error("key is invalid");
        if (t = "string" == typeof t ? (0 !== i ? function (r) {
            const i = [];
            for (let e = 0, t = r.length; e < t; e++) {
                var n = r.codePointAt(e);
                if (n <= 127) i.push(n); else if (n <= 2047) i.push(192 | n >>> 6), i.push(128 | 63 & n); else if (n <= 55295 || 57344 <= n && n <= 65535) i.push(224 | n >>> 12), i.push(128 | n >>> 6 & 63), i.push(128 | 63 & n); else {
                    if (!(65536 <= n && n <= 1114111)) throw i.push(n), new Error("input is not supported");
                    e++, i.push(240 | n >>> 18 & 28), i.push(128 | n >>> 12 & 63), i.push(128 | n >>> 6 & 63), i.push(128 | 63 & n)
                }
            }
            return i
        } : rt)(t) : [...t], ("pkcs#5" === n || "pkcs#7" === n) && 0 !== i) {
            const r = U - t.length % U;
            for (let e = 0; e < r; e++) t.push(r)
        }
        var l = new Array(32);
        {
            var d = r, h = l;
            e = i;
            const b = new Array(4), v = new Array(4);
            for (let e = 0; e < 4; e++) v[0] = 255 & d[0 + 4 * e], v[1] = 255 & d[1 + 4 * e], v[2] = 255 & d[2 + 4 * e], v[3] = 255 & d[3 + 4 * e], b[e] = v[0] << 24 | v[1] << 16 | v[2] << 8 | v[3];
            b[0] ^= 2746333894, b[1] ^= 1453994832, b[2] ^= 1736282519, b[3] ^= 2993693404;
            for (let e, t = 0; t < 32; t += 4) e = b[1] ^ b[2] ^ b[3] ^ tt[t + 0], h[t + 0] = b[0] ^= nt(x(e)), e = b[2] ^ b[3] ^ b[0] ^ tt[t + 1], h[t + 1] = b[1] ^= nt(x(e)), e = b[3] ^ b[0] ^ b[1] ^ tt[t + 2], h[t + 2] = b[2] ^= nt(x(e)), e = b[0] ^ b[1] ^ b[2] ^ tt[t + 3], h[t + 3] = b[3] ^= nt(x(e));
            if (0 === e) for (let e, t = 0; t < 16; t++) e = h[t], h[t] = h[31 - t], h[31 - t] = e
        }
        const f = [];
        let u = a, p = t.length, c = 0;
        for (; p >= U;) {
            const r = t.slice(c, c + 16), n = new Array(16);
            if ("cbc" === s) for (let e = 0; e < U; e++) 0 !== i && (r[e] ^= u[e]);
            {
                m = void 0;
                _ = void 0;
                g = void 0;
                var m = r;
                var _ = n;
                var g = l;
                const w = new Array(4), S = new Array(4);
                for (let e = 0; e < 4; e++) S[0] = 255 & m[4 * e], S[1] = 255 & m[4 * e + 1], S[2] = 255 & m[4 * e + 2], S[3] = 255 & m[4 * e + 3], w[e] = S[0] << 24 | S[1] << 16 | S[2] << 8 | S[3];
                for (let e, t = 0; t < 32; t += 4) e = w[1] ^ w[2] ^ w[3] ^ g[t + 0], w[0] ^= it(x(e)), e = w[2] ^ w[3] ^ w[0] ^ g[t + 1], w[1] ^= it(x(e)), e = w[3] ^ w[0] ^ w[1] ^ g[t + 2], w[2] ^= it(x(e)), e = w[0] ^ w[1] ^ w[2] ^ g[t + 3], w[3] ^= it(x(e));
                for (let e = 0; e < 16; e += 4) _[e] = w[3 - e / 4] >>> 24 & 255, _[e + 1] = w[3 - e / 4] >>> 16 & 255, _[e + 2] = w[3 - e / 4] >>> 8 & 255, _[e + 3] = 255 & w[3 - e / 4]
            }
            for (let e = 0; e < U; e++) "cbc" === s && 0 === i && (n[e] ^= u[e]), f[c + e] = n[e];
            "cbc" === s && (u = 0 !== i ? n : r), p -= U, c += U
        }
        if (("pkcs#5" === n || "pkcs#7" === n) && 0 === i) {
            const t = f.length, r = f[t - 1];
            for (let e = 1; e <= r; e++) if (f[t - e] !== r) throw new Error("padding is invalid");
            f.splice(t - r, r)
        }
        {
            if ("array" === o) return f;
            if (0 !== i) return f.map(e => 1 === (e = e.toString(16)).length ? "0" + e : e).join("");
            {
                var y = f;
                const E = [];
                for (let e = 0, t = y.length; e < t; e++) 240 <= y[e] && y[e] <= 247 ? (E.push(String.fromCodePoint(((7 & y[e]) << 18) + ((63 & y[e + 1]) << 12) + ((63 & y[e + 2]) << 6) + (63 & y[e + 3]))), e += 3) : 224 <= y[e] && y[e] <= 239 ? (E.push(String.fromCodePoint(((15 & y[e]) << 12) + ((63 & y[e + 1]) << 6) + (63 & y[e + 2]))), e += 2) : 192 <= y[e] && y[e] <= 223 ? (E.push(String.fromCodePoint(((31 & y[e]) << 6) + (63 & y[e + 1]))), e++) : E.push(String.fromCodePoint(y[e]));
                return E.join("")
            }
        }
    }

    const _ = {init: 0, findFirstStartCode: 1, findSecondStartCode: 2};

    class at extends class {
        on(e, t, r) {
            const i = this.e || (this.e = {});
            return (i[e] || (i[e] = [])).push({fn: t, ctx: r}), this
        }

        once(i, n, s) {
            const a = this;

            function o() {
                a.off(i, o);
                for (var e = arguments.length, t = new Array(e), r = 0; r < e; r++) t[r] = arguments[r];
                n.apply(s, t)
            }

            return o._ = n, this.on(i, o, s)
        }

        emit(e) {
            const t = ((this.e || (this.e = {}))[e] || []).slice();
            for (var r = arguments.length, i = new Array(1 < r ? r - 1 : 0), n = 1; n < r; n++) i[n - 1] = arguments[n];
            for (let e = 0; e < t.length; e += 1) t[e].fn.apply(t[e].ctx, i);
            return this
        }

        off(e, r) {
            const t = this.e || (this.e = {});
            if (!e) return Object.keys(t).forEach(e => {
                delete t[e]
            }), void delete this.e;
            const i = t[e], n = [];
            if (i && r) for (let e = 0, t = i.length; e < t; e += 1) i[e].fn !== r && i[e].fn._ !== r && n.push(i[e]);
            return n.length ? t[e] = n : delete t[e], this
        }
    } {
        constructor(e) {
            super(), this.player = e, this.isDestroyed = !1, this.reset()
        }

        destroy() {
            this.isDestroyed = !1, this.off(), this.reset()
        }

        reset() {
            this.stats = _.init, this.tempBuffer = new Uint8Array(0), this.parsedOffset = 0, this.versionLayer = 0
        }

        dispatch(e, t) {
            let r = new Uint8Array(this.tempBuffer.length + e.length);
            for (r.set(this.tempBuffer, 0), r.set(e, this.tempBuffer.length), this.tempBuffer = r; !this.isDestroyed;) {
                if (this.state == _.Init) {
                    let e = !1;
                    for (; 2 <= this.tempBuffer.length - this.parsedOffset && !this.isDestroyed;) if (255 == this.tempBuffer[this.parsedOffset]) {
                        if (!(!1 & this.tempBuffer[this.parsedOffset + 1])) {
                            this.versionLayer = this.tempBuffer[this.parsedOffset + 1], this.state = _.findFirstStartCode, this.fisrtStartCodeOffset = this.parsedOffset, this.parsedOffset += 2, e = !0;
                            break
                        }
                        this.parsedOffset++
                    } else this.parsedOffset++;
                    if (e) continue;
                    break
                }
                if (this.state == _.findFirstStartCode) {
                    let e = !1;
                    for (; 2 <= this.tempBuffer.length - this.parsedOffset && !this.isDestroyed;) if (255 == this.tempBuffer[this.parsedOffset]) {
                        if (this.tempBuffer[this.parsedOffset + 1] == this.versionLayer) {
                            this.state = _.findSecondStartCode, this.secondStartCodeOffset = this.parsedOffset, this.parsedOffset += 2, e = !0;
                            break
                        }
                        this.parsedOffset++
                    } else this.parsedOffset++;
                    if (e) continue;
                    break
                }
                var i;
                this.state == _.findSecondStartCode && (i = this.tempBuffer.slice(this.fisrtStartCodeOffset, this.secondStartCodeOffset), this.emit("data", i, t), this.tempBuffer = this.tempBuffer.slice(this.secondStartCodeOffset), this.fisrtStartCodeOffset = 0, this.parsedOffset = 2, this.state = _.findFirstStartCode)
            }
        }
    }

    Date.now || (Date.now = function () {
        return (new Date).getTime()
    }), w.postRun = function () {
        !function (l, z) {
            function s() {
                t && (t.abort(), t = null)
            }

            let a = 1 < arguments.length && void 0 !== z && z, o = [], d = [], n = {}, t = new AbortController,
                r = null, h = null, e = null, f = null, u = null, p = null, c = !1, m = !1, _ = !!X(a), i = !1,
                g = null, y = null, b = null, v = [], w = null, S = null, E = 0, U = 0, x = null, B = null, A = 0,
                R = 0, T = !1, M = !1, N = !1, k = !1, O = () => {
                    var e = function () {
                        {
                            var r = ae;
                            let t = "";
                            if ("object" == typeof r) try {
                                t = JSON.stringify(r), t = JSON.parse(t)
                            } catch (e) {
                                t = r
                            } else t = r;
                            return t
                        }
                    }();
                    return {
                        debug: e.debug,
                        debugLevel: e.debugLevel,
                        debugUuid: e.debugUuid,
                        useOffscreen: e.useOffscreen,
                        useWCS: e.useWCS,
                        videoBuffer: e.videoBuffer,
                        videoBufferDelay: e.videoBufferDelay,
                        openWebglAlignment: e.openWebglAlignment,
                        playType: e.playType,
                        hasAudio: e.hasAudio,
                        hasVideo: e.hasVideo,
                        playbackRate: 1,
                        playbackForwardMaxRateDecodeIFrame: e.playbackForwardMaxRateDecodeIFrame,
                        playbackIsCacheBeforeDecodeForFpsRender: e.playbackConfig.isCacheBeforeDecodeForFpsRender,
                        sampleRate: 0,
                        networkDelay: e.networkDelay,
                        visibility: !0,
                        useSIMD: e.useSIMD,
                        isRecording: !1,
                        recordType: e.recordType,
                        isNakedFlow: e.isNakedFlow,
                        checkFirstIFrame: e.checkFirstIFrame,
                        audioBufferSize: 1024,
                        isCrypto: e.isCrypto,
                        cryptoKey: e.cryptoKey,
                        cryptoIV: e.cryptoIV,
                        isSm4Crypto: e.isSm4Crypto,
                        sm4CryptoKey: e.sm4CryptoKey,
                        isHls265: !1,
                        isFlv: e.isFlv,
                        isFmp4: e.isFmp4,
                        isMpeg4: e.isMpeg4,
                        isFmp4Private: e.isFmp4Private,
                        isEmitSEI: e.isEmitSEI,
                        isRecordTypeFlv: !1
                    }
                }, C = ("VideoEncoder" in self && (n = {
                    hasInit: !1,
                    isEmitInfo: !1,
                    offscreenCanvas: null,
                    offscreenCanvasCtx: null,
                    decoder: new VideoDecoder({
                        output: function (t) {
                            var e;
                            n.isEmitInfo || (I.debug.log("worker", "Webcodecs Video Decoder initSize"), postMessage({
                                cmd: oe,
                                w: t.codedWidth,
                                h: t.codedHeight
                            }), n.isEmitInfo = !0, n.offscreenCanvas = new OffscreenCanvas(t.codedWidth, t.codedHeight), n.offscreenCanvasCtx = n.offscreenCanvas.getContext("2d")), "function" == typeof t.createImageBitmap ? t.createImageBitmap().then(e => {
                                n.offscreenCanvasCtx.drawImage(e, 0, 0, t.codedWidth, t.codedHeight);
                                e = n.offscreenCanvas.transferToImageBitmap();
                                postMessage({cmd: H, buffer: e, delay: I.delay, ts: 0}, [e]), Se(t)
                            }) : (n.offscreenCanvasCtx.drawImage(t, 0, 0, t.codedWidth, t.codedHeight), e = n.offscreenCanvas.transferToImageBitmap(), postMessage({
                                cmd: H,
                                buffer: e,
                                delay: I.delay,
                                ts: 0
                            }, [e]), Se(t))
                        }, error: function (e) {
                            I.debug.error("worker", "VideoDecoder error", e)
                        }
                    }),
                    decode: function (e, t, r) {
                        var i = e[0] >> 4 == 1;
                        if (n.hasInit) {
                            const r = new EncodedVideoChunk({data: e.slice(5), timestamp: t, type: i ? "key" : "delta"});
                            n.decoder.decode(r)
                        } else if (i && 0 === e[1]) {
                            const t = 15 & e[0], r = (postMessage({cmd: de, code: t}), function (e) {
                                let r = e.subarray(1, 4), i = "avc1.";
                                for (let t = 0; t < 3; t++) {
                                    let e = r[t].toString(16);
                                    e.length < 2 && (e = "0" + e), i += e
                                }
                                return {codec: i, description: e}
                            }(e.slice(5)));
                            I._opt.recordType === G && postMessage({
                                cmd: he,
                                buffer: e,
                                codecId: t
                            }, [e.buffer]), n.decoder.configure(r), n.hasInit = !0
                        }
                    },
                    reset() {
                        n.hasInit = !1, n.isEmitInfo = !1, n.offscreenCanvas = null, n.offscreenCanvasCtx = null
                    }
                }), {
                    init() {
                        C.lastBuf = null, C.vps = null, C.sps = null, C.pps = null, C.streamType = null, C.localDts = 0, C.isSendSeqHeader = !1
                    }, destroy() {
                        C.lastBuf = null, C.vps = null, C.sps = null, C.pps = null, C.streamType = null, C.localDts = 0, C.isSendSeqHeader = !1
                    }, dispatch(e) {
                        e = new Uint8Array(e);
                        C.extractNALu$2(e)
                    }, getNaluDts() {
                        var e = C.localDts;
                        return C.localDts = C.localDts + 40, e
                    }, getNaluAudioDts() {
                        var e = I._opt.sampleRate, t = I._opt.audioBufferSize;
                        return C.localDts + parseInt(t / e * 1e3)
                    }, extractNALu(e) {
                        let t, r, i = 0, n = e.byteLength, s = 0, a = [];
                        for (; i < n;) switch (t = e[i++], s) {
                            case 0:
                                0 === t && (s = 1);
                                break;
                            case 1:
                                s = 0 === t ? 2 : 0;
                                break;
                            case 2:
                            case 3:
                                s = 0 === t ? 3 : (1 === t && i < n && (r && a.push(e.subarray(r, i - s - 1)), r = i), 0)
                        }
                        return r && a.push(e.subarray(r, n)), a
                    }, extractNALu$2(t) {
                        let s = null;
                        if (t && !(t.byteLength < 1)) {
                            C.lastBuf ? ((s = new Uint8Array(t.byteLength + C.lastBuf.length)).set(C.lastBuf), s.set(new Uint8Array(t), C.lastBuf.length)) : s = new Uint8Array(t);
                            let r = 0, i = -1, n = -2;
                            const a = new Array;
                            for (let t = 0; t < s.length; t += 2) {
                                const e = s[t], o = s[t + 1];
                                0 == i && 0 == e && 0 == o ? a.push(t - 1) : 1 == o && 0 == e && 0 == i && 0 == n && a.push(t - 2), n = e, i = o
                            }
                            if (1 < a.length) for (let t = 0; t < a.length - 1; ++t) {
                                const e = s.subarray(a[t], a[t + 1] + 1);
                                C.handleNALu(e), r = a[t + 1]
                            } else r = a[0];
                            if (0 != r && r < s.length) C.lastBuf = s.subarray(r); else {
                                C.lastBuf || (C.lastBuf = s);
                                const e = new Uint8Array(C.lastBuf.length + t.byteLength);
                                e.set(C.lastBuf), e.set(new Uint8Array(t), C.lastBuf.length), C.lastBuf = e
                            }
                        }
                    }, handleNALu(e) {
                        e.byteLength <= 4 ? I.debug.warn("worker", `handleNALu nalu byteLength is ${e.byteLength} <= 4`) : (e = e.slice(4), C.handleVideoNalu(e))
                    }, handleVideoNalu(e) {
                        if (C.streamType || (C.streamType = function (e) {
                            let t = null, r = 31 & e[0];
                            return (t = 7 !== r && 8 !== r ? t : me) || (32 !== (r = (126 & e[0]) >> 1) && 33 !== r && 34 !== r || (t = _e)), t
                        }(e)), C.streamType === me) {
                            const t = C.handleAddNaluStartCode(e), r = C.extractNALu(t);
                            if (0 === r.length) I.debug.warn("worker", "handleVideoNalu", "h264 naluList.length === 0"); else {
                                const i = [];
                                if (r.forEach(e => {
                                    var t = Q(e);
                                    8 === t || 7 === t ? C.handleVideoH264Nalu(e) : Ce(t) && i.push(e)
                                }), 1 === i.length) C.handleVideoH264Nalu(i[0]); else if (function (t) {
                                    if (0 !== t.length) {
                                        var r = Q(t[0]);
                                        for (let e = 1; e < t.length; e++) if (r !== Q(t[e])) return;
                                        return 1
                                    }
                                }(i)) {
                                    const e = Q(i[0]), n = 5 === e;
                                    C.handleVideoH264NaluList(i, n, e)
                                } else i.forEach(e => {
                                    C.handleVideoH264Nalu(e)
                                })
                            }
                        } else if (C.streamType === _e) {
                            const s = C.handleAddNaluStartCode(e), a = C.extractNALu(s);
                            if (0 === a.length) I.debug.warn("worker", "handleVideoNalu", "h265 naluList.length === 0"); else {
                                const o = [];
                                if (a.forEach(e => {
                                    var t = te(e);
                                    34 === t || 33 === t || 32 === t ? C.handleVideoH265Nalu(e) : ze(t) && o.push(e)
                                }), 1 === o.length) C.handleVideoH265Nalu(o[0]); else if (function (t) {
                                    if (0 !== t.length) {
                                        var r = te(t[0]);
                                        for (let e = 1; e < t.length; e++) if (r !== te(t[e])) return;
                                        return 1
                                    }
                                }(o)) {
                                    const e = te(o[0]), l = Re(e);
                                    C.handleVideoH265NaluList(o, l, e)
                                } else o.forEach(e => {
                                    this.handleVideoH265Nalu(e)
                                })
                            }
                        }
                    }, extractH264PPS(e) {
                        e = C.handleAddNaluStartCode(e);
                        C.extractNALu(e).forEach(e => {
                            ke(Q(e)) ? C.extractH264SEI(e) : C.handleVideoH264Nalu(e)
                        })
                    }, extractH265PPS(e) {
                        e = C.handleAddNaluStartCode(e);
                        C.extractNALu(e).forEach(e => {
                            39 === te(e) ? C.extractH265SEI(e) : C.handleVideoH265Nalu(e)
                        })
                    }, extractH264SEI(e) {
                        e = C.handleAddNaluStartCode(e);
                        C.extractNALu(e).forEach(e => {
                            C.handleVideoH264Nalu(e)
                        })
                    }, extractH265SEI(e) {
                        e = C.handleAddNaluStartCode(e);
                        C.extractNALu(e).forEach(e => {
                            C.handleVideoH265Nalu(e)
                        })
                    }, handleAddNaluStartCode(e) {
                        const t = [0, 0, 0, 1], r = new Uint8Array(e.length + t.length);
                        return r.set(t), r.set(e, t.length), r
                    }, handleVideoH264Nalu(e) {
                        const t = Q(e);
                        switch (t) {
                            case 7:
                                C.sps = e;
                                break;
                            case 8:
                                C.pps = e
                        }
                        if (C.isSendSeqHeader) {
                            if (C.sps && C.pps) {
                                const e = Ae({sps: C.sps, pps: C.pps}), t = C.getNaluDts();
                                I.decode(e, {type: 2, ts: t, isIFrame: !0, cts: 0}), C.sps = null, C.pps = null
                            }
                            var r, i, n;
                            Ce(t) ? (r = 5 === t, i = C.getNaluDts(), n = function (e, t) {
                                let r = [];
                                r[0] = t ? 23 : 39, r[1] = 1, r[2] = 0, r[3] = 0, r[4] = 0, r[5] = e.byteLength >> 24 & 255, r[6] = e.byteLength >> 16 & 255, r[7] = e.byteLength >> 8 & 255, r[8] = 255 & e.byteLength;
                                const i = new Uint8Array(r.length + e.byteLength);
                                return i.set(r, 0), i.set(e, r.length), i
                            }(e, r), C.doDecode(n, {
                                type: 2,
                                ts: i,
                                isIFrame: r,
                                cts: 0
                            })) : I.debug.warn("work", "handleVideoH264Nalu Avc Seq Head is " + t)
                        } else if (C.sps && C.pps) {
                            C.isSendSeqHeader = !0;
                            const e = Ae({sps: C.sps, pps: C.pps});
                            I.decode(e, {type: 2, ts: 0, isIFrame: !0, cts: 0}), C.sps = null, C.pps = null
                        }
                    }, handleVideoH264NaluList(e, t, r) {
                        var i, n;
                        C.isSendSeqHeader ? (i = C.getNaluDts(), n = Te(e.reduce((e, t) => {
                            const r = ee(e), i = ee(t), n = new Uint8Array(r.byteLength + i.byteLength);
                            return n.set(r, 0), n.set(i, r.byteLength), n
                        }), t), C.doDecode(n, {
                            type: 2,
                            ts: i,
                            isIFrame: t,
                            cts: 0
                        }), I.debug.log("worker", `handleVideoH264NaluList list size is ${e.length} package length is ${n.byteLength} isIFrame is ${t},nalu type is ${r}, dts is ` + i)) : I.debug.warn("worker", "handleVideoH264NaluList isSendSeqHeader is false")
                    }, handleVideoH265Nalu(e) {
                        const t = te(e);
                        switch (t) {
                            case 32:
                                C.vps = e;
                                break;
                            case 33:
                                C.sps = e;
                                break;
                            case 34:
                                C.pps = e
                        }
                        if (C.isSendSeqHeader) {
                            if (C.vps && C.sps && C.pps) {
                                const e = Pe({vps: C.vps, sps: C.sps, pps: C.pps}), t = C.getNaluDts();
                                I.decode(e, {
                                    type: 2,
                                    ts: t,
                                    isIFrame: !0,
                                    cts: 0
                                }), C.vps = null, C.sps = null, C.pps = null
                            }
                            var r, i, n;
                            ze(t) ? (r = Re(t), i = C.getNaluDts(), n = function (e, t) {
                                let r = [];
                                r[0] = t ? 28 : 44, r[1] = 1, r[2] = 0, r[3] = 0, r[4] = 0, r[5] = e.byteLength >> 24 & 255, r[6] = e.byteLength >> 16 & 255, r[7] = e.byteLength >> 8 & 255, r[8] = 255 & e.byteLength;
                                const i = new Uint8Array(r.length + e.byteLength);
                                return i.set(r, 0), i.set(e, r.length), i
                            }(e, r), C.doDecode(n, {
                                type: 2,
                                ts: i,
                                isIFrame: r,
                                cts: 0
                            })) : I.debug.warn("work", "handleVideoH265Nalu HevcSeqHead is " + t)
                        } else if (C.vps && C.sps && C.pps) {
                            C.isSendSeqHeader = !0;
                            const e = Pe({vps: C.vps, sps: C.sps, pps: C.pps});
                            I.decode(e, {type: 2, ts: 0, isIFrame: !0, cts: 0}), C.vps = null, C.sps = null, C.pps = null
                        }
                    }, handleVideoH265NaluList(e, t, r) {
                        var i, n;
                        C.isSendSeqHeader ? (i = C.getNaluDts(), n = Le(e.reduce((e, t) => {
                            const r = ee(e), i = ee(t), n = new Uint8Array(r.byteLength + i.byteLength);
                            return n.set(r, 0), n.set(i, r.byteLength), n
                        }), t), C.doDecode(n, {
                            type: 2,
                            ts: i,
                            isIFrame: t,
                            cts: 0
                        }), I.debug.log("worker", `handleVideoH265NaluList list size is ${e.length} package length is ${n.byteLength} isIFrame is ${t},nalu type is ${r}, dts is ` + i)) : I.debug.warn("worker", "handleVideoH265NaluList isSendSeqHeader is false")
                    }, doDecode(e, t) {
                        I.calcNetworkDelay(t.ts), t.isIFrame && I.calcIframeIntervalTimestamp(t.ts), I._opt.isEmitSEI && I.findSei(e, t.ts), postMessage({
                            cmd: V,
                            type: $,
                            value: e.byteLength
                        }), postMessage({cmd: V, type: j, value: t.ts}), I.decode(e, t)
                    }
                }), F = {
                    LOG_NAME: "worker fmp4Demuxer",
                    mp4Box: re.createFile(),
                    offset: 0,
                    videoTrackId: null,
                    audioTrackId: null,
                    isHevc: !1,
                    listenMp4Box() {
                        F.mp4Box.onReady = F.onReady, F.mp4Box.onError = F.onError, F.mp4Box.onSamples = F.onSamples
                    },
                    initTransportDescarmber() {
                        F.transportDescarmber = new et
                    },
                    _getSeqHeader(t) {
                        const r = F.mp4Box.getTrackById(t.id);
                        for (const t of r.mdia.minf.stbl.stsd.entries) if (t.avcC || t.hvcC) {
                            const r = new re.DataStream(void 0, 0, re.DataStream.BIG_ENDIAN);
                            let e = [];
                            e = t.avcC ? (t.avcC.write(r), [23, 0, 0, 0, 0]) : (F.isHevc = !0, t.hvcC.write(r), [28, 0, 0, 0, 0]);
                            const i = new Uint8Array(r.buffer, 8), n = new Uint8Array(e.length + i.length);
                            return n.set(e, 0), n.set(i, e.length), n
                        }
                        return null
                    },
                    onReady(e) {
                        I.debug.log(F.LOG_NAME, "onReady()", e);
                        const t = e.videoTracks[0], r = e.audioTracks[0];
                        if (t) {
                            F.videoTrackId = t.id;
                            const e = F._getSeqHeader(t);
                            e && (I.debug.log(F.LOG_NAME, "seqHeader"), I.decodeVideo(e, 0, !0, 0)), F.mp4Box.setExtractionOptions(t.id)
                        }
                        if (r) {
                            F.audioTrackId = r.id;
                            const e = r.audio || {}, t = ve.indexOf(e.sample_rate), n = r.codec.replace("mp4a.40.", "");
                            F.mp4Box.setExtractionOptions(r.id);
                            var i = function (e) {
                                var {profile: e, sampleRate: t, channel: r} = e;
                                return new Uint8Array([175, 0, e << 3 | (14 & t) >> 1, (1 & t) << 7 | r << 3])
                            }({profile: parseInt(n, 10), sampleRate: t, channel: e.channel_count});
                            I.debug.log(F.LOG_NAME, "aacADTSHeader"), I.decodeAudio(i, 0)
                        }
                        F.mp4Box.start()
                    },
                    onError(e) {
                        I.debug.error(F.LOG_NAME, "mp4Box onError", e)
                    },
                    onSamples(e, t, r) {
                        if (e === F.videoTrackId) for (const e of r) {
                            const t = e.data, r = e.is_sync, n = 1e3 * e.cts / e.timescale;
                            e.duration, e.timescale, r && I.calcIframeIntervalTimestamp(n);
                            var i = (F.isHevc ? Le : Te)(t, r);
                            I._opt.isEmitSEI && I.findSei(i, n), postMessage({
                                cmd: V,
                                type: $,
                                value: i.byteLength
                            }), postMessage({cmd: V, type: j, value: n}), I.decode(i, {type: 2, ts: n, isIFrame: r, cts: 0})
                        } else if (e === F.audioTrackId) {
                            if (I._opt.hasAudio) for (const e of r) {
                                const t = e.data, r = 1e3 * e.cts / e.timescale,
                                    s = (e.duration, e.timescale, new Uint8Array(t.byteLength + 2));
                                s.set([175, 1], 0), s.set(t, 2), postMessage({
                                    cmd: V,
                                    type: pe,
                                    value: s.byteLength
                                }), I.decode(s, {type: 1, ts: r, isIFrame: !1, cts: 0})
                            }
                        } else I.debug.warn(F.LOG_NAME, "onSamples() trackId error", e)
                    },
                    dispatch(e) {
                        let t = e;
                        "string" != typeof e ? "object" == typeof e ? ((t = F.transportDescarmber ? F.transportDescarmber.transport(t) : t).buffer.fileStart = F.offset, F.offset += t.byteLength, F.mp4Box.appendBuffer(t.buffer)) : I.debug.warn(F.LOG_NAME, "dispatch()", "data is not object", e) : I.debug.warn(F.LOG_NAME, "dispatch()", "data is string", e)
                    },
                    destroy() {
                        F.mp4Box && (F.mp4Box.flush(), F.mp4Box = null), F.transportDescarmber && (F.transportDescarmber.destroy(), F.transportDescarmber = null), F.offset = 0, F.videoTrackId = null, F.audioTrackId = null, F.isHevc = !1
                    }
                }, D = {
                    LOG_NAME: "worker mpeg4Demuxer",
                    lastBuffer: new Uint8Array(0),
                    parsedOffset: 0,
                    firstStartCodeOffset: 0,
                    secondStartCodeOffset: 0,
                    state: "init",
                    hasInitVideoCodec: !1,
                    localDts: 0,
                    dispatch(e) {
                        e = new Uint8Array(e);
                        D.extractNALu(e)
                    },
                    destroy() {
                        D.lastBuffer = new Uint8Array(0), D.parsedOffset = 0, D.firstStartCodeOffset = 0, D.secondStartCodeOffset = 0, D.state = "init", D.hasInitVideoCodec = !1, D.localDts = 0
                    },
                    extractNALu(e) {
                        if (!e || e.byteLength < 1) I.debug.warn(D.LOG_NAME, "extractNALu() buffer error", e); else {
                            const t = new Uint8Array(D.lastBuffer.length + e.length);
                            for (t.set(D.lastBuffer, 0), t.set(new Uint8Array(e), D.lastBuffer.length), D.lastBuffer = t; ;) {
                                if ("init" === D.state) {
                                    let e = !1;
                                    for (; 4 <= D.lastBuffer.length - D.parsedOffset;) if (0 === D.lastBuffer[D.parsedOffset]) if (0 === D.lastBuffer[D.parsedOffset + 1]) if (1 === D.lastBuffer[D.parsedOffset + 2]) {
                                        if (182 === D.lastBuffer[D.parsedOffset + 3]) {
                                            D.state = "findFirstStartCode", D.firstStartCodeOffset = D.parsedOffset, D.parsedOffset += 4, e = !0;
                                            break
                                        }
                                        D.parsedOffset++
                                    } else D.parsedOffset++; else D.parsedOffset++; else D.parsedOffset++;
                                    if (e) continue;
                                    break
                                }
                                if ("findFirstStartCode" === D.state) {
                                    let e = !1;
                                    for (; 4 <= D.lastBuffer.length - D.parsedOffset;) if (0 === D.lastBuffer[D.parsedOffset]) if (0 === D.lastBuffer[D.parsedOffset + 1]) if (1 === D.lastBuffer[D.parsedOffset + 2]) {
                                        if (182 === D.lastBuffer[D.parsedOffset + 3]) {
                                            D.state = "findSecondStartCode", D.secondStartCodeOffset = D.parsedOffset, D.parsedOffset += 4, e = !0;
                                            break
                                        }
                                        D.parsedOffset++
                                    } else D.parsedOffset++; else D.parsedOffset++; else D.parsedOffset++;
                                    if (e) continue;
                                    break
                                }
                                if ("findSecondStartCode" === D.state) {
                                    if (!(0 < D.lastBuffer.length - D.parsedOffset)) break;
                                    {
                                        let e, t, r = 192 & D.lastBuffer[D.parsedOffset];
                                        e = 0 == r ? D.secondStartCodeOffset - 14 : D.secondStartCodeOffset;
                                        var i = 0 == (192 & D.lastBuffer[D.firstStartCodeOffset + 4]);
                                        if (i) {
                                            if (D.firstStartCodeOffset - 14 < 0) return void I.debug.warn(D.LOG_NAME, "firstStartCodeOffset -14 is", D.firstStartCodeOffset - 14);
                                            D.hasInitVideoCodec || (D.hasInitVideoCodec = !0, I.debug.log(D.LOG_NAME, "setCodec"), L.setCodec(99, "")), t = D.lastBuffer.subarray(D.firstStartCodeOffset - 14, e)
                                        } else t = D.lastBuffer.subarray(D.firstStartCodeOffset, e);
                                        var n = D.getNaluDts();
                                        D.hasInitVideoCodec ? (postMessage({
                                            cmd: V,
                                            type: $,
                                            value: t.byteLength
                                        }), postMessage({
                                            cmd: V,
                                            type: j,
                                            value: n
                                        }), L.decode(t, i ? 1 : 0, n)) : I.debug.warn(D.LOG_NAME, "has not init video codec"), D.lastBuffer = D.lastBuffer.subarray(e), D.firstStartCodeOffset = 0 == r ? 14 : 0, D.parsedOffset = D.firstStartCodeOffset + 4, D.state = "findFirstStartCode"
                                    }
                                }
                            }
                        }
                    },
                    getNaluDts() {
                        var e = D.localDts;
                        return D.localDts = D.localDts + 40, e
                    }
                }, I = {
                    isPlayer: !0,
                    isPlayback: !1,
                    isPushDropping: !1,
                    isDestroyed: !1,
                    _opt: O(),
                    mp3Demuxer: null,
                    startStreamRateAndStatsInterval: function () {
                        I.stopStreamRateAndStatsInterval(), e = setInterval(() => {
                            h && h(0);
                            var e = JSON.stringify({
                                demuxBufferDelay: I.getVideoBufferLength(),
                                audioDemuxBufferDelay: I.getAudioBufferLength(),
                                flvBufferByteLength: I.getFlvBufferLength(),
                                netBuf: I.networkDelay || 0,
                                pushLatestDelay: I.pushLatestDelay || 0,
                                isDropping: X(I.dropping) || X(I.isPushDropping),
                                isStreamTsMoreThanLocal: i
                            });
                            postMessage({cmd: V, type: "streamStats", value: e})
                        }, 1e3)
                    },
                    stopStreamRateAndStatsInterval: function () {
                        e && (clearInterval(e), e = null)
                    },
                    useOffscreen: function () {
                        return I._opt.useOffscreen && "undefined" != typeof OffscreenCanvas
                    },
                    getDelay: function (e) {
                        return !e || I._opt.hasVideo && !_ ? -1 : (I.preDelayTimestamp && I.preDelayTimestamp > e ? 1e3 < I.preDelayTimestamp - e && I.debug.warn("worker", `getDelay() and preDelayTimestamp is ${I.preDelayTimestamp} > timestamp is ${e} more than ${I.preDelayTimestamp - e}ms`) : I.firstTimestamp ? e && (t = Date.now() - I.startTimestamp, (r = e - I.firstTimestamp) <= t ? (i = !1, I.delay = t - r) : (i = !0, I.delay = r - t)) : (I.firstTimestamp = e, I.startTimestamp = Date.now(), I.delay = -1), I.preDelayTimestamp = e, I.delay);
                        var t, r
                    },
                    getDelayNotUpdateDelay: function (t) {
                        if (!t || I._opt.hasVideo && !_) return -1;
                        if (I.preDelayTimestamp && 1e3 < I.preDelayTimestamp - t) return I.debug.warn("worker", `getDelayNotUpdateDelay and preDelayTimestamp is ${I.preDelayTimestamp} > timestamp is ${t} more than ${I.preDelayTimestamp - t}ms`), -1;
                        if (I.firstTimestamp) {
                            let e = -1;
                            var r;
                            return t && (r = Date.now() - I.startTimestamp, t = t - I.firstTimestamp, e = t <= r ? (i = !1, r - t) : (i = !0, t - r)), e
                        }
                        return -1
                    },
                    resetDelay: function () {
                        I.firstTimestamp = null, I.startTimestamp = null, I.delay = -1
                    },
                    resetAllDelay: function () {
                        I.resetDelay(), I.preDelayTimestamp = null
                    },
                    doDecode: function (e) {
                        I._opt.useWCS && I.useOffscreen() && 2 === e.type && n.decode ? n.decode(e.payload, e.ts, e.cts) : e.decoder.decode(e.payload, e.ts, e.isIFrame, e.cts)
                    },
                    decodeNext(e) {
                        if (0 !== o.length && !I.isPlayback) {
                            var t = e.ts, r = o[0], i = 2 === e.type && K(e.payload);
                            if (Ue(a)) i && (I.debug.log("worker", `decode data type is ${e.type} and
                ts is ${t} next data type is ${r.type} ts is ${r.ts}
                isVideoSqeHeader is ` + i), o.shift(), I.doDecode(r)); else {
                                const a = r.ts - t, n = 1 === r.type && 2 === e.type;
                                (a <= 20 || n || i) && (I.debug.log("worker", `decode data type is ${e.type} and
                ts is ${t} next data type is ${r.type} ts is ${r.ts}
                diff is ${a} and isVideoAndNextAudio is ${n} and isVideoSqeHeader is ` + i), o.shift(), I.doDecode(r))
                            }
                        }
                    },
                    init: function () {
                        I.debug.log("worker", "init and opt is", JSON.stringify(I._opt));
                        const t = I._opt.playType === se, r = "playbackTF" === I._opt.playType;
                        if (C.init(), I.isPlayer = t, I.isPlayback = r, I.isPlaybackCacheBeforeDecodeForFpsRender()) I.debug.log("worker", "playback and playbackIsCacheBeforeDecodeForFpsRender is true"); else {
                            const r = () => {
                                let e = null;
                                if (o.length) if (I.isPushDropping) I.debug.warn("worker", "loop() isPushDropping is true and bufferList length is " + o.length); else if (I.dropping) {
                                    for (e = o.shift(), I.debug.warn("worker", `loop() dropBuffer is dropping and isIFrame ${e.isIFrame} and delay is ${I.delay} and bufferlist is ` + o.length); !e.isIFrame && o.length;) e = o.shift();
                                    const t = I.getDelayNotUpdateDelay(e.ts);
                                    e.isIFrame && t <= I.getNotDroppingDelayTs() && (I.debug.log("worker", "loop() is dropping = false, is iFrame"), I.dropping = !1, I.doDecode(e), I.decodeNext(e))
                                } else if (e = o[0], -1 === I.getDelay(e.ts) || I.isPlayback) I.isPlayer && I.debug.log("worker", "loop() common dumex delay is -1 ,data.ts is", e.ts), o.shift(), I.doDecode(e), I.decodeNext(e); else if (I.delay > I._opt.videoBuffer + I._opt.videoBufferDelay && t) I.hasIframeInBufferList() ? (I.debug.log("worker", `delay is ${I.delay}, set dropping is true`), I.resetAllDelay(), I.dropping = !0) : (o.shift(), I.doDecode(e), I.decodeNext(e)); else for (; o.length;) {
                                    if (e = o[0], !(I.getDelay(e.ts) > I._opt.videoBuffer)) {
                                        I.delay < 0 && I.debug.warn("worker", `loop() do not decode and delay is ${I.delay}, bufferList is ` + o.length);
                                        break
                                    }
                                    o.shift(), I.doDecode(e)
                                } else -1 !== I.delay && I.debug.log("worker", "loop() bufferList is empty and reset delay"), I.resetAllDelay()
                            };
                            I.stopId = setInterval(() => {
                                var e = (new Date).getTime(), e = e - (g = g || e);
                                100 < e && I.debug.warn("worker", "loop demux diff time is " + e), r(), g = (new Date).getTime()
                            }, 20)
                        }
                        Ue(I._opt.checkFirstIFrame) && (_ = !0)
                    },
                    playbackCacheLoop: function () {
                        I.stopId && (clearInterval(I.stopId), I.stopId = null);
                        var e = () => {
                            var e;
                            o.length && (e = o.shift(), I.doDecode(e))
                        }, t = (e(), Math.ceil(1e3 / (I.streamFps * I._opt.playbackRate)));
                        I.debug.log("worker", `playbackCacheLoop fragDuration is ${t}, streamFps is ${I.streamFps}, playbackRate is ` + I._opt.playbackRate), I.stopId = setInterval(e, t)
                    },
                    close: function () {
                        if (I.debug.log("worker", "close"), I.isDestroyed = !0, I.stopStreamRateAndStatsInterval(), I.stopId && (clearInterval(I.stopId), I.stopId = null), I.mp3Demuxer && (I.mp3Demuxer.destroy(), I.mp3Demuxer = null), P) try {
                            P.clear && P.clear(), P = null
                        } catch (e) {
                            I.debug.warn("worker", "close() and audioDecoder.clear error", e)
                        }
                        if (L) try {
                            L.clear && L.clear(), L = null
                        } catch (e) {
                            I.debug.warn("worker", "close() and videoDecoder.clear error", e)
                        }
                        h = null, g = null, i = !1, n && (n.reset && n.reset(), n = null), I.firstTimestamp = null, I.startTimestamp = null, I.networkDelay = 0, I.streamFps = null, I.streamAudioFps = null, I.streamVideoFps = null, I.delay = -1, I.pushLatestDelay = -1, I.preDelayTimestamp = null, I.dropping = !1, I.isPushDropping = !1, I.isPlayer = !0, I.isPlayback = !1, I._opt = O(), I.webglObj && (I.webglObj.destroy(), I.offscreenCanvas.removeEventListener("webglcontextlost", I.onOffscreenCanvasWebglContextLost), I.offscreenCanvas.removeEventListener("webglcontextrestored", I.onOffscreenCanvasWebglContextRestored), I.offscreenCanvas = null, I.offscreenCanvasGL = null, I.offscreenCanvasCtx = null), o = [], d = [], s(), f = null, r && (r.close(1e3, "Client disconnecting"), r = null), u = null, p = null, c = !1, m = !1, _ = !1, T = !1, M = !1, N = !1, k = !1, v = [], E = 0, U = 0, y = null, b = null, x = null, B = null, A = 0, R = 0, w = null, S = null, C.destroy(), F.destroy(), D.destroy(), postMessage({cmd: "closeEnd"})
                    },
                    pushBuffer: function (e, t) {
                        if (1 === t.type && be(e)) {
                            if (I.debug.log("worker", `pushBuffer audio ts is ${t.ts}, isAacCodecPacket is true`), I._opt.isRecordTypeFlv) {
                                const t = new Uint8Array(e);
                                postMessage({cmd: "aacSequenceHeader", buffer: t}, [t.buffer])
                            }
                            I.decodeAudio(e, t.ts)
                        } else if (2 === t.type && t.isIFrame && K(e)) {
                            if (I.debug.log("worker", `pushBuffer video ts is ${t.ts}, isVideoSequenceHeader is true`), I._opt.isRecordTypeFlv) {
                                const t = new Uint8Array(e);
                                postMessage({cmd: "videoSequenceHeader", buffer: t}, [t.buffer])
                            }
                            I.decodeVideo(e, t.ts, t.isIFrame, t.cts)
                        } else {
                            if (I._opt.isRecordTypeFlv && I._opt.isRecording) {
                                const o = new Uint8Array(e);
                                postMessage({cmd: "flvBufferData", type: t.type, buffer: o, ts: t.ts}, [o.buffer])
                            }
                            if (I.isPlayer && 0 < A && 0 < B && 2 === t.type) {
                                const e = t.ts - B;
                                e > 2 * A - 5 && I.debug.warn("worker", `pushBuffer video
                    ts is ${t.ts}, preTimestamp is ${B},
                    diff is ${e} and preTimestampDuration is ${A}
                    maybe trigger black screen or flower screen
                    `)
                            }
                            if (I.isPlayer && 0 < B && 2 === t.type && t.ts < B && 36e5 < B - t.ts && (I.debug.warn("worker", `pushBuffer,
                preTimestamp is ${B}, options.ts is ${t.ts},
                diff is ${B - t.ts} more than 3600000,
                and resetAllDelay`), I.resetAllDelay()), I.isPlayer && t.ts <= B && 0 < B && 2 === t.type && I.debug.warn("worker", `pushBuffer,
                options.ts is ${t.ts} less than (or equal) preTimestamp is ${B} and
                payloadBufferSize is ${e.byteLength} and prevPayloadBufferSize is ` + R), I.isPlayer && _) {
                                const e = I._opt.videoBuffer + I._opt.videoBufferDelay, o = I.getDelayNotUpdateDelay(t.ts);
                                (I.pushLatestDelay = o) > e && I.delay < e && 0 < I.delay && I.hasIframeInBufferList() && !1 === I.isPushDropping && (I.debug.log("worker", `pushBuffer, pushLatestDelay is ${o} more than ${e} and decoder.delay is ${I.delay} and has iIframe and next decoder.dropBuffer$2()`), I.dropBuffer$2())
                            }
                            if (2 === t.type && (0 < B && (A = t.ts - B), R = e.byteLength, B = t.ts), 1 === t.type ? o.push({
                                ts: t.ts,
                                payload: e,
                                decoder: {decode: I.decodeAudio},
                                type: 1,
                                isIFrame: !1
                            }) : 2 === t.type && o.push({
                                ts: t.ts,
                                cts: t.cts,
                                payload: e,
                                decoder: {decode: I.decodeVideo},
                                type: 2,
                                isIFrame: t.isIFrame
                            }), I.isPlaybackCacheBeforeDecodeForFpsRender() && (q(I.streamVideoFps) || q(I.streamAudioFps))) {
                                let e = I.streamVideoFps, t = I.streamAudioFps;
                                q(I.streamVideoFps) && ((e = Ee(o, 2)) && (I.streamVideoFps = e, postMessage({
                                    cmd: "playbackStreamVideoFps",
                                    value: I.streamVideoFps
                                }), I.streamFps = t ? e + t : e, I.playbackCacheLoop())), q(I.streamAudioFps) && ((t = Ee(o, 1)) && (I.streamAudioFps = t, I.streamFps = e ? e + t : t, I.playbackCacheLoop())), q(I.streamVideoFps) && q(I.streamAudioFps) && I.debug.log("worker", `playbackCacheBeforeDecodeForFpsRender, calc streamAudioFps is ${t}, streamVideoFps is ${e}, bufferListLength  is ` + o.length)
                            }
                        }
                    },
                    getVideoBufferLength() {
                        let t = 0;
                        return o.forEach(e => {
                            2 === e.type && (t += 1)
                        }), t
                    },
                    hasIframeInBufferList: () => o.some(e => 2 === e.type && e.isIFrame),
                    isAllIframeInBufferList() {
                        var e = I.getVideoBufferLength();
                        let t = 0;
                        return o.forEach(e => {
                            2 === e.type && e.isIFrame && (t += 1)
                        }), e === t
                    },
                    getNotDroppingDelayTs: () => I._opt.videoBuffer + I._opt.videoBufferDelay / 2,
                    getAudioBufferLength() {
                        let t = 0;
                        return o.forEach(e => {
                            1 === e.type && (t += 1)
                        }), t
                    },
                    getFlvBufferLength() {
                        let e = 0;
                        return f && f.buffer && (e = f.buffer.byteLength), e = I._opt.isNakedFlow && C.lastBuf ? C.lastBuf.byteLength : e
                    },
                    fetchStream: function (e, n) {
                        I.debug.log("worker", "fetchStream, url is " + e, "options:", JSON.stringify(n)), n.isFlv ? I._opt.isFlv = !0 : n.isFmp4 ? I._opt.isFmp4 = !0 : n.isMpeg4 ? I._opt.isMpeg4 = !0 : n.isNakedFlow && (I._opt.isNakedFlow = !0), h = function (r) {
                            let i = 0, n = we();
                            return e => {
                                var t;
                                "[object Number]" === Object.prototype.toString.call(e) && (i += e, 1e3 <= (t = (e = we()) - n) && (r(i / t * 1e3), n = e, i = 0))
                            }
                        }(e => {
                            postMessage({cmd: V, type: "streamRate", value: e})
                        }), I.startStreamRateAndStatsInterval(), n.isFmp4 && (F.listenMp4Box(), I._opt.isFmp4Private && F.initTransportDescarmber()), 2 === n.protocol ? (f = new Z(I.demuxFlv()), fetch(e, {signal: t.signal}).then(e => {
                            if (!((t = e).ok && 200 <= t.status && t.status <= 299)) return I.debug.warn("worker", `fetch response status is ${e.status} and ok is ${e.ok} and emit error and next abort()`), s(), void postMessage({
                                cmd: V,
                                type: W,
                                value: `fetch response status is ${e.status} and ok is ` + e.ok
                            });
                            var t;
                            if (postMessage({
                                cmd: V,
                                type: ce
                            }), "undefined" != typeof WritableStream) e.body.pipeTo(new WritableStream({
                                write: e => {
                                    h(e.byteLength), n.isFlv ? f.write(e) : n.isFmp4 ? I.demuxFmp4(e) : n.isMpeg4 && I.demuxMpeg4(e)
                                }, close: () => {
                                    f = null, s(), postMessage({cmd: V, type: ue, value: ne})
                                }, abort: e => {
                                    f = null, e.name !== ye && (s(), postMessage({cmd: V, type: W, value: e.toString()}))
                                }
                            })); else {
                                const r = e.body.getReader(), i = () => {
                                    r.read().then(e => {
                                        var {done: e, value: t} = e;
                                        if (e) return f = null, s(), void postMessage({cmd: V, type: ue, value: ne});
                                        h(t.byteLength), n.isFlv ? f.write(t) : n.isFmp4 ? I.demuxFmp4(t) : n.isMpeg4 && I.demuxMpeg4(t), i()
                                    }).catch(e => {
                                        f = null, e.name !== ye && (s(), postMessage({
                                            cmd: V,
                                            type: W,
                                            value: e.toString()
                                        }))
                                    })
                                };
                                i()
                            }
                        }).catch(e => {
                            e.name !== ye && (s(), postMessage({cmd: V, type: W, value: e.toString()}), f = null)
                        })) : 1 === n.protocol && (n.isFlv && (f = new Z(I.demuxFlv())), (r = new WebSocket(e)).binaryType = "arraybuffer", r.onopen = () => {
                            I.debug.log("worker", "fetchStream, WebsocketStream  socket open"), postMessage({
                                cmd: V,
                                type: ce
                            }), postMessage({cmd: V, type: "websocketOpen"})
                        }, r.onclose = e => {
                            I.debug.log("worker", "fetchStream, WebsocketStream socket close and code is " + e.code), 1006 === e.code && I.debug.error("worker", "fetchStream, WebsocketStream socket close abnormally and code is " + e.code), f = null, postMessage({
                                cmd: V,
                                type: ue,
                                value: "websocket"
                            })
                        }, r.onerror = e => {
                            I.debug.error("worker", "fetchStream, WebsocketStream socket error", e), f = null, postMessage({
                                cmd: V,
                                type: "websocketError",
                                value: e.isTrusted ? "websocket user aborted" : "websocket error"
                            })
                        }, r.onmessage = e => {
                            h(e.data.byteLength), n.isFlv ? f.write(e.data) : n.isFmp4 ? I.demuxFmp4(e.data) : n.isMpeg4 ? I.demuxMpeg4(e.data) : I._opt.isNakedFlow ? I.demuxNakedFlow(e.data) : I.demuxM7s(e.data)
                        })
                    },
                    demuxFlv: function* () {
                        yield 9;
                        const r = new ArrayBuffer(4), e = new Uint8Array(r), i = new Uint32Array(r);
                        for (; ;) {
                            e[3] = 0;
                            const r = yield 15, a = r[4];
                            e[0] = r[7], e[1] = r[6], e[2] = r[5];
                            var t = i[0], n = (e[0] = r[10], e[1] = r[9], e[2] = r[8], e[3] = r[11], i[0]),
                                s = (yield t).slice();
                            switch (a) {
                                case 8:
                                    I.decode(s, {type: 1, ts: n});
                                    break;
                                case 9:
                                    if (0 < s.byteLength) {
                                        const r = s[0] >> 4 == 1;
                                        I.isPlayer && (I.calcNetworkDelay(n), r && I.calcIframeIntervalTimestamp(n)), i[0] = s[4], i[1] = s[3], i[2] = s[2], i[3] = 0;
                                        let e = i[0], t = s;
                                        I._opt.isCrypto ? I._opt.cryptoIV && 0 < I._opt.cryptoIV.byteLength && I._opt.cryptoKey && 0 < I._opt.cryptoKey.byteLength ? t = function (t, r, i) {
                                            r = new Uint8Array(r), i = new Uint8Array(i);
                                            const n = t.byteLength;
                                            let s = 5;
                                            for (; s < n;) {
                                                o = (o = t.slice(s, s + 4))[3] | o[2] << 8 | o[1] << 16 | o[0] << 24;
                                                if (o > n) break;
                                                var a = t[s + 4];
                                                if (1 == (a &= 31) || 5 == a) {
                                                    const n = t.slice(s + 4 + 2, s + 4 + o);
                                                    let e = new Ze.ModeOfOperation.ctr(r, new Ze.Counter(i));
                                                    a = e.decrypt(n);
                                                    e = null, t.set(a, s + 4 + 2)
                                                }
                                                s = s + 4 + o
                                            }
                                            var o;
                                            return t
                                        }(s, I._opt.cryptoKey, I._opt.cryptoIV) : I.debug.error("worker", `cryptoKey.length is ${I._opt.cryptoKey && I._opt.cryptoKey.byteLength} or cryptoIV.length is ${I._opt.cryptoIV && I._opt.cryptoIV.byteLength} null`) : I._opt.isSm4Crypto && I._opt.sm4CryptoKey && r && (t = function (e, t) {
                                            const r = e.byteLength;
                                            let i = 5;
                                            for (; i < r;) {
                                                s = (s = e.slice(i, i + 4))[3] | s[2] << 8 | s[1] << 16 | s[0] << 24;
                                                if (s > r) break;
                                                var n = e[i + 4];
                                                if (1 == (n &= 31) || 5 == n) {
                                                    const r = st(e.slice(i + 4 + 2, i + 4 + s), t, 0, {
                                                        padding: "none",
                                                        output: "array"
                                                    });
                                                    e.set(r, i + 4 + 2)
                                                }
                                                i = i + 4 + s
                                            }
                                            var s;
                                            return e
                                        }(s, I._opt.sm4CryptoKey)), I._opt.isEmitSEI && I.findSei(t, n), I.decode(t, {
                                            type: 2,
                                            ts: n,
                                            isIFrame: r,
                                            cts: e
                                        })
                                    }
                                    break;
                                case 18:
                                    postMessage({cmd: "flvScriptData", buffer: s}, [s.buffer]);
                                    break;
                                default:
                                    I.debug.log("worker", "demuxFlv() type is " + a)
                            }
                        }
                    },
                    decode: function (e, t) {
                        1 === t.type ? I._opt.hasAudio && (postMessage({
                            cmd: V,
                            type: pe,
                            value: e.byteLength
                        }), I.isPlayer ? I.pushBuffer(e, {
                            type: t.type,
                            ts: t.ts,
                            cts: t.cts
                        }) : I.isPlayback && (I.isPlaybackCacheBeforeDecodeForFpsRender() || 1 === I._opt.playbackRate ? I.pushBuffer(e, {
                            type: t.type,
                            ts: t.ts,
                            cts: t.cts
                        }) : I.decodeAudio(e, t.ts))) : 2 === t.type && I._opt.hasVideo && (postMessage({
                            cmd: V,
                            type: $,
                            value: e.byteLength
                        }), postMessage({cmd: V, type: j, value: t.ts}), I.isPlayer ? I.pushBuffer(e, {
                            type: t.type,
                            ts: t.ts,
                            isIFrame: t.isIFrame,
                            cts: t.cts
                        }) : I.isPlayback && (I.isPlaybackOnlyDecodeIFrame() ? t.isIFrame && I.pushBuffer(e, {
                            type: t.type,
                            ts: t.ts,
                            cts: t.cts,
                            isIFrame: t.isIFrame
                        }) : (I.isPlaybackCacheBeforeDecodeForFpsRender(), I.pushBuffer(e, {
                            type: t.type,
                            ts: t.ts,
                            cts: t.cts,
                            isIFrame: t.isIFrame
                        }))))
                    },
                    setCodecAudio: function (e, t) {
                        var r = e[0] >> 4;
                        if (be(e) || 7 == r || 8 == r || 2 == r) {
                            I.debug.log("worker", "setCodecAudio: init audio codec, codeId is " + r);
                            var i = 10 == r ? e.slice(2) : new Uint8Array(0);
                            P.setCodec(r, I._opt.sampleRate, i), m = !0, 10 != r && (2 == r ? (I.mp3Demuxer || (I.mp3Demuxer = new at(I), I.mp3Demuxer.on("data", (e, t) => {
                                P.decode(e, t)
                            })), I.mp3Demuxer.dispatch(e.slice(1), t)) : P.decode(e.slice(1), t));
                            {
                                const e = Number("1") || 1;
                                setTimeout(() => {
                                    I.debug.error("worker", "jessibuca pro 体验结束,请刷新页面再次体验，如需要购买商业授权，可以联系微信：bosswancheng"), I.close(), postMessage({cmd: fe})
                                }, 60 * e * 60 * 1e3)
                            }
                        } else I.debug.warn("worker", "setCodecAudio: hasInitAudioCodec is false, codecId is ", r)
                    },
                    decodeAudio: function (e, t) {
                        var r = e[0] >> 4;
                        m ? 2 == r ? I.mp3Demuxer.dispatch(e.slice(1), t) : P.decode(10 == r ? e.slice(2) : e.slice(1), t) : I.setCodecAudio(e, t)
                    },
                    setCodecVideo: function (e) {
                        var t = 15 & e[0];
                        if (K(e)) if (7 == t || 12 == t) {
                            k = 12 == t, I.debug.log("worker", "setCodecVideo: init video codec , codecId is " + t);
                            var r = e.slice(5);
                            if (7 == t && I._opt.useSIMD) {
                                const e = Be(r);
                                if (4080 < e.codecWidth || 4080 < e.codecHeight) return postMessage({cmd: "simdH264DecodeVideoWidthIsTooLarge"}), void I.debug.warn("worker", `setCodecVideo: SIMD H264 decode video width is too large, width is ${e.codecWidth}, height is ` + e.codecHeight)
                            }
                            c = !0, L.setCodec(t, r), I._opt.recordType === G && postMessage({
                                cmd: he,
                                buffer: e,
                                codecId: t
                            }, [e.buffer])
                        } else I.debug.warn("worker", `setCodecVideo: hasInitVideoCodec is false, codecId is ${t} is not H264 or H265`); else I.debug.warn("worker", `decodeVideo: hasInitVideoCodec is false, codecId is ${t} and frameType is ${e[0] >> 4} and packetType is ` + e[1])
                    },
                    decodeVideo: function (t, e, r) {
                        var i = 3 < arguments.length && void 0 !== arguments[3] ? arguments[3] : 0;
                        if (X(a)) postMessage({
                            cmd: "videoPayload",
                            payload: t,
                            isIFrame: r,
                            ts: e,
                            cts: i,
                            delay: I.delay
                        }, [t.buffer]); else if (c) if (_ = !_ && r ? !0 : _) {
                            if (r && K(t)) {
                                const a = 15 & t[0];
                                let e = {};
                                7 == a ? e = Be(t.slice(5)) : 12 == a && (e = Ie(t)), e.codecWidth && e.codecHeight && u && p && (e.codecWidth !== u || e.codecHeight !== p) && (I.debug.warn("worker", `
                            decodeVideo: video width or height is changed,
                            old width is ${u}, old height is ${p},
                            new width is ${e.codecWidth}, new height is ${e.codecHeight},
                            and emit change event`), M = !0, postMessage({cmd: "wasmWidthOrHeightChange"}))
                            }
                            if (M) I.debug.warn("worker", "decodeVideo: video width or height is changed, and return"); else if (N) I.debug.warn("worker", "decodeVideo: simd decode error, and return"); else if (K(t)) I.debug.warn("worker", "decodeVideo and payload is video sequence header so drop this frame"); else if (t.byteLength < 12) I.debug.warn("worker", "decodeVideo and payload is too small , payload length is " + t.byteLength); else {
                                const a = t.slice(5);
                                L.decode(a, r ? 1 : 0, e), I._opt.isRecording && I._opt.recordType === G && postMessage({
                                    cmd: "videoNalu",
                                    buffer: a,
                                    isIFrame: r,
                                    ts: e,
                                    cts: i
                                }, [a.buffer])
                            }
                        } else I.debug.warn("worker", "decodeVideo: first frame is not iframe"); else I.setCodecVideo(t)
                    },
                    clearBuffer: function () {
                        var e = 0 < arguments.length && void 0 !== arguments[0] && arguments[0];
                        I.debug.log("worker", `clearBuffer,bufferList length is ${o.length}, need clear is ` + e), e && (o = []), I.resetAllDelay(), I.dropping = !0
                    },
                    dropBuffer$2: function () {
                        if (0 < o.length) {
                            I.isPushDropping = !0;
                            let t = o.findIndex(e => X(e.isIFrame) && 2 === e.type);
                            if (I.isAllIframeInBufferList()) for (let e = 0; e < o.length; e++) {
                                var r = o[e], r = I.getDelayNotUpdateDelay(r.ts);
                                if (r >= I.getNotDroppingDelayTs()) {
                                    I.debug.log("worker", `dropBuffer$2() isAllIframeInBufferList() is true, and index is ${e} and tempDelay is ${r} and notDroppingDelayTs is ` + I.getNotDroppingDelayTs()), t = e;
                                    break
                                }
                            }
                            var e, i, n;
                            0 <= t ? (e = o.length, i = (o = o.slice(t)).shift(), n = I.getDelayNotUpdateDelay(i.ts), I.doDecode(i), I.isPushDropping = !1, I.debug.log("worker", `dropBuffer$2() iFrameIndex is ${t},and prev bufferList length is ${e} ,new bufferList is ${o.length} and tempDelay is ${n} ,delay is ${I.delay} `)) : I.isPushDropping = !1
                        }
                        0 === o.length && (I.isPushDropping = !1)
                    },
                    demuxM7s: function (e) {
                        const t = new DataView(e), r = t.getUint32(1, !1);
                        switch (t.getUint8(0)) {
                            case 1:
                                I.decode(new Uint8Array(e, 5), {type: 1, ts: r});
                                break;
                            case 2:
                                var i, n;
                                5 < t.byteLength && (i = new Uint8Array(e, 5), n = t.getUint8(5) >> 4 == 1, I.isPlayer && (I.calcNetworkDelay(r), n && I.calcIframeIntervalTimestamp(r)), I._opt.isEmitSEI && I.findSei(i, r), I.decode(i, {
                                    type: 2,
                                    ts: r,
                                    isIFrame: n
                                }))
                        }
                    },
                    demuxNakedFlow: function (e) {
                        C.dispatch(e)
                    },
                    demuxFmp4: function (e) {
                        e = new Uint8Array(e);
                        F.dispatch(e)
                    },
                    demuxMpeg4: function (e) {
                        D.dispatch(e)
                    },
                    findSei: function (e, r) {
                        De(e.slice(5)).forEach(e => {
                            var t = k ? e[0] >>> 1 & 63 : 31 & e[0];
                            (k && (40 == t || 39 == t) || Ue(k) && t === ge) && postMessage({
                                cmd: "videoSEI",
                                buffer: e,
                                ts: r
                            }, [e.buffer])
                        })
                    },
                    calcNetworkDelay: function (e) {
                        var t, r, i;
                        _ && 0 < e && (null === y ? (y = e, b = Y()) : e < y && (I.debug.warn("worker", `calcNetworkDelay, dts is ${e} less than bufferStartDts is ` + y), y = e, b = Y()), i = (t = e - y) < (r = Y() - b) ? r - t : 0, (I.networkDelay = i) > I._opt.networkDelay && I._opt.playType === se && (I.debug.warn("worker", `calcNetworkDelay now dts:${e}, start dts is ${y} vs start is ${t},local diff is ${r} ,delay is ` + i), postMessage({
                            cmd: V,
                            type: "networkDelayTimeout",
                            value: i
                        })))
                    },
                    calcIframeIntervalTimestamp: function (e) {
                        null === x ? x = e : x < e && (S = e - x, postMessage({cmd: "iframeIntervalTs", value: S}), x = e)
                    },
                    canVisibilityDecodeNotDrop: function () {
                        return I._opt.visibility && u * p <= 2073600
                    },
                    isPlaybackCacheBeforeDecodeForFpsRender: function () {
                        return I.isPlayback && I._opt.playbackIsCacheBeforeDecodeForFpsRender
                    },
                    isPlaybackOnlyDecodeIFrame: function () {
                        return I._opt.playbackRate >= I._opt.playbackForwardMaxRateDecodeIFrame
                    },
                    playbackUpdatePlaybackRate: function () {
                        I.clearBuffer(!0)
                    },
                    onOffscreenCanvasWebglContextLost: function (e) {
                        I.debug.error("worker", "handleOffscreenCanvasWebglContextLost and next try to create webgl"), e.preventDefault(), T = !0, I.webglObj.destroy(), I.webglObj = null, I.offscreenCanvasGL = null, setTimeout(() => {
                            I.offscreenCanvasGL = I.offscreenCanvas.getContext("webgl"), I.offscreenCanvasGL && I.offscreenCanvasGL.getContextAttributes().stencil ? (I.webglObj = ie(I.offscreenCanvasGL, I._opt.openWebglAlignment), T = !1) : I.debug.error("worker", "handleOffscreenCanvasWebglContextLost, stencil is false")
                        }, 500)
                    },
                    onOffscreenCanvasWebglContextRestored: function (e) {
                        I.debug.log("worker", "handleOffscreenCanvasWebglContextRestored"), e.preventDefault()
                    },
                    videoInfo: function (e, t, r) {
                        postMessage({cmd: de, code: e}), postMessage({
                            cmd: oe,
                            w: t,
                            h: r
                        }), u = t, p = r, I.useOffscreen() && (I.offscreenCanvas = new OffscreenCanvas(t, r), I.offscreenCanvasGL = I.offscreenCanvas.getContext("webgl"), I.webglObj = ie(I.offscreenCanvasGL, I._opt.openWebglAlignment), I.offscreenCanvas.addEventListener("webglcontextlost", I.onOffscreenCanvasWebglContextLost, !1), I.offscreenCanvas.addEventListener("webglcontextrestored", I.onOffscreenCanvasWebglContextRestored, !1))
                    },
                    audioInfo: function (e, t, r) {
                        postMessage({cmd: "audioCode", code: e}), postMessage({
                            cmd: "initAudio",
                            sampleRate: t,
                            channels: r
                        }), U = r
                    },
                    yuvData: function (e, t) {
                        if (I.isDestroyed) I.debug.log("worker", "yuvData, decoder is destroyed and return"); else {
                            var r, i = u * p * 3 / 2, e = l.HEAPU8.subarray(e, e + i), i = new Uint8Array(e);
                            if (w = null, I.useOffscreen()) try {
                                T || (I.webglObj.renderYUV(u, p, i), r = I.offscreenCanvas.transferToImageBitmap(), postMessage({
                                    cmd: H,
                                    buffer: r,
                                    delay: I.delay,
                                    ts: t
                                }, [r]))
                            } catch (e) {
                                I.debug.error("worker", "yuvData, transferToImageBitmap error is", e)
                            } else postMessage({cmd: H, output: i, delay: I.delay, ts: t}, [i.buffer])
                        }
                    },
                    pcmData: function (n, s, a) {
                        if (I.isDestroyed) I.debug.log("worker", "pcmData, decoder is destroyed and return"); else {
                            let t = s, r = [], e = 0, i = I._opt.audioBufferSize;
                            for (let e = 0; e < 2; e++) {
                                var o = l.HEAPU32[(n >> 2) + e] >> 2;
                                r[e] = l.HEAPF32.subarray(o, o + t)
                            }
                            if (E) {
                                if (!(t >= (s = i - E))) return E += t, d[0] = Float32Array.of(...d[0], ...r[0]), void (2 == U && (d[1] = Float32Array.of(...d[1], ...r[1])));
                                v[0] = Float32Array.of(...d[0], ...r[0].subarray(0, s)), 2 == U && (v[1] = Float32Array.of(...d[1], ...r[1].subarray(0, s))), postMessage({
                                    cmd: le,
                                    buffer: v,
                                    ts: a
                                }, v.map(e => e.buffer)), e = s, t -= s
                            }
                            for (E = t; E >= i; E -= i) v[0] = r[0].slice(e, e += i), 2 == U && (v[1] = r[1].slice(e - i, e)), postMessage({
                                cmd: le,
                                buffer: v,
                                ts: a
                            }, v.map(e => e.buffer));
                            E && (d[0] = r[0].slice(e), 2 == U && (d[1] = r[1].slice(e)))
                        }
                    },
                    errorInfo: function (e) {
                        null === w && (w = Y());
                        var t, r = Y(),
                            i = (i = 0 < S ? 2 * S : 5e3, n = 1e3, t = 5e3, Math.max(Math.min(i, Math.max(n, t)), Math.min(n, t))),
                            n = r - w;
                        I.debug.log("worker", "errorInfo()", "iframeIntervalTimestamp is", S, "diff is ", n, "max diff is ", i, "wasm decode error:", e.desc), i < n && (I.debug.warn("worker", "errorInfo() emit simdDecodeError and replay"), N = !0, postMessage({cmd: "simdDecodeError"}))
                    },
                    sendWebsocketMessage: function (e) {
                        r ? 1 === r.readyState ? r.send(e) : I.debug.error("worker", "socket is not open") : I.debug.error("worker", "socket is null")
                    },
                    timeEnd: function () {
                        I.debug.error("worker", "jessibuca pro 体验结束,请刷新页面再次体验，如需要购买商业授权，可以联系微信：bosswancheng"), I.close(), postMessage({cmd: fe})
                    },
                    postStreamToMain(e, t) {
                        postMessage({cmd: "tempStream", type: t, buffer: e}, [e.buffer])
                    }
                }, P = (I.debug = new xe(I), null), L = (l.AudioDecoder && (P = new l.AudioDecoder(I)), null);
            l.VideoDecoder && (L = new l.VideoDecoder(I)), postMessage({cmd: "init"}), self.onmessage = function (e) {
                var t = e.data;
                switch (t.cmd) {
                    case"init":
                        try {
                            I._opt = Object.assign(I._opt, JSON.parse(t.opt))
                        } catch (e) {
                        }
                        I.init();
                        break;
                    case"decode":
                        I.pushBuffer(t.buffer, t.options);
                        break;
                    case"audioDecode":
                        I.decodeAudio(t.buffer, t.ts);
                        break;
                    case"videoDecode":
                        I.decodeVideo(t.buffer, t.ts, t.isIFrame);
                        break;
                    case"clearBuffer":
                        I.clearBuffer(t.needClear);
                        break;
                    case"fetchStream":
                        I.fetchStream(t.url, JSON.parse(t.opt));
                        break;
                    case"close":
                        I.close();
                        break;
                    case"updateConfig":
                        I.debug.log("worker", "updateConfig", t.key, t.value), I._opt[t.key] = t.value, "playbackRate" === t.key && (I.playbackUpdatePlaybackRate(), I.isPlaybackCacheBeforeDecodeForFpsRender() && I.playbackCacheLoop());
                        break;
                    case"sendWsMessage":
                        I.sendWebsocketMessage(t.message)
                }
            }
        }(w)
    }
});
