import os


def make():
    if not os.path.isdir('./runtime'):
        os.mkdir('./runtime')

    if not os.path.isfile('./src/status.txt'):
        f = open('./src/status.txt', 'w')
        f.write('')
        f.close()
