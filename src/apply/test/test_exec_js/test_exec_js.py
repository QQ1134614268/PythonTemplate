from unittest import TestCase

import execjs
from execjs import runtime_names

'''r
JScript nodejs Phantomjs, js环境不一样,识别语法不一样
默认JScript, 系统环境变量path有nodejs时, 使用nodejs; idea开启时重新加载 path变量? 
'''


class TestExecjs(TestCase):

    def test0(self):
        # os.environ["EXECJS_RUNTIME"] = "Node"
        node = execjs.get(runtime_names.Node)
        with open('test_input.js', encoding='utf-8') as f:
            txt = f.read()
        ctx = node.compile(txt)
        print("当前js环境: ", ctx._runtime.name)
        data = ctx.eval('menu_list')
        print(data)
        data = ctx.call('add', 1, 2)
        print(data)
        data = ctx.eval('add(1,2)')
        print(data)

    def test1(self):
        default = execjs.get()
        print(default.eval("1 + 2"))

        jscript = execjs.get(runtime_names.JScript)
        print(jscript.eval("1 + 2"))

        node = execjs.get(runtime_names.Node)
        print(node.eval("1 + 2"))
