import requests
import shutil
import os
from modules.api import call_api
import re


def urldownload(url, filename):
    file = requests.get(url, stream=True)
    print(file)
    total_length = file.headers.get("content-length")
    dw, rw = 0, 0
    with open(filename, "wb") as zip:
        for chunk in file.iter_content(chunk_size=1024):
            if chunk:
                rw += 1
                dw += len(chunk)
                zip.write(chunk)
            if rw % 1000 == 0:
                percentage = round((int(dw) / int(total_length)) * 100)
                BDS.update_status(f"Downloading {percentage}%")


class Blender_Download_Status:
    def __init__(self) -> None:
        self.status = "None"

    def update_status(self, status):
        if "Downloading" in status:
            if "%" in status:
                percentage = re.findall(r"\d+", status)[0]
                self.status = f"Downloading Blender. {percentage}%"
            else:
                self.status = "Downloading Blender."
        elif "Unpacking" in status:
            self.status = "Unpacking Blender."
        elif "Completed" in status:
            self.status = "Blender download Completed"
        else:
            self.status = "None"

        self.update_file()

    def update_file(self):
        f = open("./src/status.txt", "w")
        f.write(self.status)
        f.close()


BDS = Blender_Download_Status()


def download():
    BDS.update_status("Downloading")
    urldownload(
        call_api("GET", "blender").json()["url"],
        "./runtime/blender.zip",
    )
    BDS.update_status("Unpacking")
    shutil.unpack_archive("./runtime/blender.zip", "./runtime/blender", "zip")
    os.remove("./runtime/blender.zip")
    BDS.update_status("Completed")
