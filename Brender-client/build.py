import subprocess
import shutil
import os

if os.path.isdir('./dist'):
    shutil.rmtree('./dist')

subprocess.run('pip freeze > requirements.txt', shell=True)
subprocess.run('pyinstaller --noconfirm --onefile --windowed --icon '
               '"C:/Users/shi3do/Desktop/Github/Brender/Brender-client/src/brender-logo.ico"  '
               '"C:/Users/shi3do/Desktop/Github/Brender/Brender-client/brender.py"', shell=True)
shutil.copytree('./src', './dist/src')