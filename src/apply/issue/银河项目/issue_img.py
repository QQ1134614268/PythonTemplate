import os

from 银河项目.cache_util import to_file


@to_file("o.html")
def get_html():
    name_list = os.listdir("./img")

    print(name_list)
    l = sorted(filter(lambda x: x.endswith(".png"), name_list))
    arr = []
    for i in l:
        path = f"img: {i}"
        name = i
        fmt = f"""  <div style="display: flex;">
        <button class="btn" onclick="copy(this)" data-clipboard-text="{path}" style="height: 24px">{name}</button>
        <img src="{name}" width="400px" onmousemove="toBig(this)" onmouseleave="toSmall(this)">
    </div>"""

        arr.append(fmt)

    cont = "\n".join(arr)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="https://cdn.bootcdn.net/ajax/libs/clipboard.js/2.0.10/clipboard.min.js"></script>
</head>
<body>
{cont}
</body>
<script>
    function copy(element) {{
        new ClipboardJS('.btn')
        element.style.textDecoration = 'line-through'
        element.parentElement.style.display= 'none'
    }}

    function toBig(element) {{
        element.style.width = '600px'
    }}

    function toSmall(element) {{
        element.style.width = '400px'
    }}
</script>
</html>"""


if __name__ == '__main__':
    get_html()
