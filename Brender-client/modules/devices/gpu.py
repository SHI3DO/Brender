import GPUtil


def getname():
    gpus = GPUtil.getGPUs()

    namelist = []
    for i in range(0, len(gpus)):
        namelist.append(gpus[i].name)

    return namelist
