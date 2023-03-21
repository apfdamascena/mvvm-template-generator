import os
from pathlib import Path

class Installer:

    MVVM_FOLDER = "MVVM.xctemplate"

    def __init__(self):
        self.__path = "Library/Developer/Xcode/Templates/"

    def installTemplate(self):
        home = self.__backToHomeFolder()
        templatePath = f'{home}/{self.__path}'

        if not os.path.exists(templatePath):
            os.mkdir(templatePath)
        
        mvvmFolder = os.path.join(templatePath, Installer.MVVM_FOLDER)
        os.mkdir(mvvmFolder)

    def __backToHomeFolder(self) -> str:
        current_directory = os.path.dirname(__file__)
        abs_path = Path(current_directory)
        return abs_path.home().as_posix()
    
if __name__ == "__main__":
    installer = Installer()
    installer.installTemplate()