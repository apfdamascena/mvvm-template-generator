import os
from pathlib import Path
import shutil
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

        if not os.path.exists(mvvmFolder):
            os.mkdir(mvvmFolder)

        self.__removeFilesFromTemplateFolder(mvvmFolder)
        self.__addMVVMFilesTo(mvvmFolder)

    def __backToHomeFolder(self) -> str:
        current_directory = os.path.dirname(__file__)
        abs_path = Path(current_directory)
        return abs_path.home().as_posix()

    def __removeFilesFromTemplateFolder(self, mvvmFolder: str):
        mvvmFolderFiles = os.listdir(mvvmFolder)
        for filename in mvvmFolderFiles:
            file = os.path.join(mvvmFolder, filename)
            os.remove(file)
    
    def __addMVVMFilesTo(self, mvvmFolder: str):
        files = os.listdir(Installer.MVVM_FOLDER)
        for filename in files:
            file = os.path.join(Installer.MVVM_FOLDER, filename)
            shutil.copy2(file, mvvmFolder)

        

    
if __name__ == "__main__":
    installer = Installer()
    installer.installTemplate()