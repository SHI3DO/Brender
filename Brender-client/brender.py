import shutil
import sys
from modules.devices import gpu
from modules import dir
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import os
import platform
from modules import downloadblender


def BrenderBox():
    groupbox = QGroupBox("Brender")
    brenderpix = QPixmap("./src/brender_banner.png")

    pix_label = QLabel()
    pix_label.setPixmap(brenderpix)
    pix_label.setAlignment(Qt.AlignCenter)

    vbox = QVBoxLayout()
    vbox.addWidget(pix_label)
    groupbox.setLayout(vbox)

    return groupbox


def StatsBox():
    groupbox = QGroupBox("Global Stats")

    radio1 = QRadioButton("Radio1")
    radio2 = QRadioButton("Radio2")
    radio3 = QRadioButton("Radio3")
    radio1.setChecked(True)
    checkbox = QCheckBox("Independent Checkbox")
    checkbox.setChecked(True)

    vbox = QVBoxLayout()
    vbox.addWidget(radio1)
    vbox.addWidget(radio2)
    vbox.addWidget(radio3)
    vbox.addWidget(checkbox)
    groupbox.setLayout(vbox)

    return groupbox


def SessionBox():
    groupbox = QGroupBox("Session info")

    radio1 = QRadioButton("Radio1")
    radio2 = QRadioButton("Radio2")
    radio3 = QRadioButton("Radio3")
    radio1.setChecked(True)

    vbox = QVBoxLayout()
    vbox.addWidget(radio1)
    vbox.addWidget(radio2)
    vbox.addWidget(radio3)
    groupbox.setLayout(vbox)

    return groupbox


def WorkingBox():
    groupbox = QGroupBox("Session info")

    radio1 = QRadioButton("Radio1")
    radio2 = QRadioButton("Radio2")
    radio3 = QRadioButton("Radio3")
    radio1.setChecked(True)

    vbox = QVBoxLayout()
    vbox.addWidget(radio1)
    vbox.addWidget(radio2)
    vbox.addWidget(radio3)
    groupbox.setLayout(vbox)

    return groupbox


def SettingsBtn_clicked():
    gui.setCurrentIndex(gui.currentIndex() + 1)


def ExitBtn_clicked():
    QCoreApplication.quit()


def SettingsBackBtn_clicked():
    gui.setCurrentIndex(gui.currentIndex() - 1)


class DownloadBlenderthread(QThread):
    def __init__(self, parent):
        super(DownloadBlenderthread, self).__init__()
        self.parent = parent

    def run(self):
        downloadblender.download()


class BrenderGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(lambda: self.timeout())
        self.StatusLabel = QLabel("")
        self.initUI()

    def initUI(self):
        if not os.path.isdir("./runtime/blender"):
            downloadthread = DownloadBlenderthread(self)
            downloadthread.start()
        # /////////////////////////////////////////////////////////////////////////////

        pjgroupbox = QGroupBox("Project")
        self.StatusLabel.setAlignment(Qt.AlignCenter)
        NameLabel = QLabel("Name")
        NameLabel.setAlignment(Qt.AlignCenter)
        RendertimeLabel = QLabel("Rendering  for")
        RendertimeLabel.setAlignment(Qt.AlignCenter)
        RemainingtimeLabel = QLabel("Remaining")
        RemainingtimeLabel.setAlignment(Qt.AlignCenter)
        MethodLabel = QLabel("Compute Method")
        MethodLabel.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.StatusLabel)
        vbox.addWidget(NameLabel)
        vbox.addWidget(RendertimeLabel)
        vbox.addWidget(RemainingtimeLabel)
        vbox.addWidget(MethodLabel)
        pjgroupbox.setLayout(vbox)
        # /////////////////////////////////////////////////////////////////////////////
        groupbox = QGroupBox("Menu")
        SettingsBtn = QPushButton("Settings")
        PauseBtn = QPushButton("Pause")
        PassBtn = QPushButton("Pass this project")
        ExitBtn = QPushButton("Exit")
        vbox = QGridLayout()
        vbox.addWidget(SettingsBtn, 0, 0)
        vbox.addWidget(PauseBtn, 0, 1)
        vbox.addWidget(PassBtn, 1, 0)
        vbox.addWidget(ExitBtn, 1, 1)
        groupbox.setLayout(vbox)

        SettingsBtn.clicked.connect(lambda: SettingsBtn_clicked())
        ExitBtn.clicked.connect(lambda: ExitBtn_clicked())

        grid = QGridLayout()
        grid.addWidget(BrenderBox(), 0, 0)
        grid.addWidget(pjgroupbox, 1, 0)
        grid.addWidget(StatsBox(), 2, 0)
        grid.addWidget(SessionBox(), 3, 0)
        grid.addWidget(WorkingBox(), 4, 0)
        grid.addWidget(groupbox, 5, 0)
        self.setLayout(grid)

    def timeout(self):
        f = open("./src/status.txt", "r")
        statustext = f.read()
        f.close()
        try:
            self.StatusLabel.setText(f"Status: {statustext}")
        except Exception as e:
            print(e)


class BrenderSettingsGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.SettingsUI()

    def SettingsUI(self):
        # /////////////////////////////////////////////////////////////////////////////
        groupbox = QGroupBox("Menu")
        BackBtn = QPushButton("Back")
        SaveBtn = QPushButton("Save")
        vbox = QGridLayout()
        vbox.addWidget(BackBtn, 0, 0)
        vbox.addWidget(SaveBtn, 0, 1)
        groupbox.setLayout(vbox)
        # /////////////////////////////////////////////////////////////////////////////
        authgroupbox = QGroupBox("Authentication")
        usernameLabel = QLabel("Username:")
        passwordLabel = QLabel("Password:")
        if os.path.isfile("./src/config.txt"):
            f = open("./src/config.txt", "r")
            content = f.readlines()
            f.close()
            usernameLine = QLineEdit(f"{content[0].strip()}")
            passwordLine = QLineEdit(f"{content[1].strip()}")
        else:
            usernameLine = QLineEdit()
            passwordLine = QLineEdit()
        passwordLine.setEchoMode(QLineEdit.Password)
        auhbox1 = QHBoxLayout()
        auhbox1.addWidget(usernameLabel)
        auhbox1.addWidget(usernameLine)
        auhbox2 = QHBoxLayout()
        auhbox2.addWidget(passwordLabel)
        auhbox2.addWidget(passwordLine)
        auvbox = QVBoxLayout()
        auvbox.addLayout(auhbox1)
        auvbox.addLayout(auhbox2)
        authgroupbox.setLayout(auvbox)
        # /////////////////////////////////////////////////////////////////////////////
        computegroupbox = QGroupBox("Compute devices")
        cvbox = QVBoxLayout()
        gpu_list = gpu.getname()
        checkbox = QCheckBox("CPU")
        cvhbox = QHBoxLayout()
        cvhbox.addWidget(checkbox)
        checkbox.setChecked(1)
        cvbox.addLayout(cvhbox)
        for gpu_ in gpu_list:
            checkbox = QCheckBox(gpu_)
            checkbox.setChecked(1)
            hbox = QHBoxLayout()
            hbox.addWidget(checkbox)
            cvbox.addLayout(hbox)
        computegroupbox.setLayout(cvbox)
        # /////////////////////////////////////////////////////////////////////////////
        opgroupbox = QGroupBox("Advanced options")
        cpnameLabel = QLabel("Computer name:")
        if os.path.isfile("./src/config.txt"):
            f = open("./src/config.txt", "r")
            content = f.readlines()
            f.close()
            cpnameLine = QLineEdit(f"{content[2].strip()}")
        else:
            cpnameLine = QLineEdit()
        ophbox1 = QHBoxLayout()
        ophbox1.addWidget(cpnameLabel)
        ophbox1.addWidget(cpnameLine)
        ophbox2 = QHBoxLayout()
        checkbox1 = QCheckBox("Auto sign in")
        ophbox2.addWidget(checkbox1)
        opvbox = QVBoxLayout()
        opvbox.addLayout(ophbox1)
        opvbox.addLayout(ophbox2)
        opgroupbox.setLayout(opvbox)
        # /////////////////////////////////////////////////////////////////////////////
        BackBtn.clicked.connect(lambda: SettingsBackBtn_clicked())
        SaveBtn.clicked.connect(
            lambda: self.SettingsSaveBtn_clicked(usernameLine, passwordLine, cpnameLine)
        )

        for cv in computegroupbox.findChildren(QCheckBox):
            print(cv.isChecked())

        grid = QGridLayout()
        grid.addWidget(BrenderBox(), 0, 0)
        grid.addWidget(authgroupbox, 1, 0)
        grid.addWidget(computegroupbox, 2, 0)
        grid.addWidget(opgroupbox, 3, 0)
        grid.addWidget(groupbox, 4, 0)
        self.setLayout(grid)

    def SettingsSaveBtn_clicked(self, usernameLine, passwordLine, cpnameLine):
        username = usernameLine.text().strip()
        password = passwordLine.text().strip()
        pcname = cpnameLine.text().strip()
        if username == "":
            username = "brender"
        if password == "":
            password = "brender"
        if pcname == "":
            pcname = str(platform.node())
        f = open("./src/config.txt", "w")
        f.write(f"{username}\n{password}\n{pcname}")
        f.close()


if __name__ == "__main__":
    dir.make()
    app = QApplication(sys.argv)
    gui = QStackedWidget()
    main = BrenderGUI()
    settings = BrenderSettingsGUI()
    gui.addWidget(main)
    gui.addWidget(settings)
    gui.setWindowTitle("Brender")
    gui.resize(600, 1000)
    gui.setWindowIcon(QIcon("./src/brender-logo.png"))
    gui.show()
    app.exec_()
