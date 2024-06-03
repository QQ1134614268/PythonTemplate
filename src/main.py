from apply.issue.issue_shell.shell import run_3306, exec_profile

if __name__ == '__main__':
    run_3306(3306)
    run_3306(2233)
    exec_profile()

# D:\workspace\PythonTemplate\venv\Scripts\pyinstaller -p D:\workspace\PythonTemplate\src -D src\main.py
# D:\workspace\PythonTemplate\venv\Scripts\pyinstaller -p D:\workspace\PythonTemplate\src --noconfirm -D main.py
