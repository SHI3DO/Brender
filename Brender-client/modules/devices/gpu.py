import GPUtil


def getname():
    gpu_list = GPUtil.getGPUs()

    namelist = []
    for gpu_ in gpu_list:
        namelist.append(gpu_.name)

    return namelist
