import execjs


def get_menu_list():
    with open('test_input.js', encoding='utf-8') as f:
        doc_js = execjs.compile(f.read())
    # python.exe -X utf8 s2.py
    # 不能有 export

    # 调用函数
    # res = doc_js.call('createGuid')
    return doc_js.eval('menu_list')
