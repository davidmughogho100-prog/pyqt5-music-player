import os
import shutil
import time

while True:
    if os.path.exists("__pycache__/"):
        shutil.rmtree("__pycache__/")

    time.sleep(5)
