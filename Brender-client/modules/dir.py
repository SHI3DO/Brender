import os


def make():
    if not os.path.isdir('./runtime'):
        os.mkdir('./runtime')
