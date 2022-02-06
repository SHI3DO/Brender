from fastapi.middleware.cors import CORSMiddleware

import os


class CustomModules:
    def __init__(self):
        self.modules = []

    def __add__(self, modules):
        self.modules.append(modules)
        return __import__(modules)

    def __modules__(self):
        return self.modules


class Utilities:
    def __init__(self):
        pass

    def cors(self, app):

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def load(self):
        self.cm = CustomModules()

        for root, dirs, files in os.walk("./cogs"):
            if not "__pycache__" in root:
                for file in files:
                    root = root.replace("\\", "/")
                    path = f"{root}/{file}"

                    module = (
                        path.removeprefix("./").replace("/", ".").removesuffix(".py")
                    )
                    self.cm.__add__(module)
                    print(f"Loaded: {module.replace('.', ' / ')}")
