import subprocess
import shutil
import os

if os.path.isdir('./dist'):
    shutil.rmtree('./dist')

if not os.path.isdir('./release'):
    os.mkdir('./release')
else:
    shutil.rmtree('./release')

subprocess.run('pip freeze > requirements.txt', shell=True)
subprocess.run('pyinstaller --noconfirm --onefile --windowed --icon '
               '"D:/Github/Brender/Brender-client/src/brender-logo.ico"  '
               '"D:/Github/Brender/Brender-client/brender.py"', shell=True)
shutil.copytree('./src', './dist/src')
shutil.make_archive('./release/Brender', 'zip', './dist')
print('done')