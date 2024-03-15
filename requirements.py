import subprocess
import time

#run this to install everything 

command = ["sudo", "apt", "install", "steghide", "tesseract-ocr"]
pip3_install = ["pip3", "install", "colorama", "Pillow", "pytesseract"]
subprocess.run(command)
time.sleep(1)
subprocess.run(pip3_install)