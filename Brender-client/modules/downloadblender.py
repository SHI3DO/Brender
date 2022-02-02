import requests
import shutil
import os


def urldownload(url, filename):
    file = requests.get(url, stream=True)
    total_length = file.headers.get('content-length')
    dw = 0
    rw = 0
    with open(filename, 'wb') as zip:
        for chunk in file.iter_content(chunk_size=1024):
            if chunk:
                rw+=1
                dw += len(chunk)
                zip.write(chunk)
            if rw % 1000 == 0:
                f = open('./src/status.txt', 'w')
                f.write(f'Downloading Blender. {round((int(dw) / int(total_length))*100)}%')
                f.close()



def download():
    f = open('./src/status.txt', 'w')
    f.write('Downloading Blender.')
    f.close()
    urldownload("http://asphodel.kro.kr:1351/Hosting/blender-3.0.1-windows-x64.zip",
                './runtime/blender.zip')
    f = open('./src/status.txt', 'w')
    f.write('Unpacking Blender.')
    f.close()
    shutil.unpack_archive('./runtime/blender.zip', './runtime/blender', 'zip')
    os.remove('./runtime/blender.zip')
    f = open('./src/status.txt', 'w')
    f.write('Blender download completed.')
    f.close()