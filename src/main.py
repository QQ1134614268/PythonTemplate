from apply.issue.issure_shell.shell import run_3306, exec_profile

if __name__ == '__main__':
    run_3306(3306)
    run_3306(2233)
    exec_profile()

# D:\workspace\pythonSpace\PythonTemplate\venv\Scripts\pyinstaller -p D:\workspace\pythonSpace\PythonTemplate\src -D src\main.py
# D:\workspace\pythonSpace\PythonTemplate\venv\Scripts\pyinstaller -p D:\workspace\pythonSpace\PythonTemplate\src --noconfirm -D main.py
