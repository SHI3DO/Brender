import inspect
import os


def print_(*arguments):
    path = inspect.stack()[1].filename
    filename = os.path.basename(path)

    print(f"[Printer] {filename}: {' | '.join(arguments)}")
