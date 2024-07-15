# get Windows lock screen pics and add .jpg to all files and store them in a folder in the current directory:

import os
import shutil

USERNAME = os.getlogin()
FROM_DIR = f"C:/Users/{USERNAME}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
FOLDER_NAME = "pics"

for filename in os.listdir(FROM_DIR):
    if not filename.endswith(".jpg") and not filename.endswith(".py"):
        if not os.path.exists(FOLDER_NAME):
            os.makedirs(FOLDER_NAME)
        shutil.copyfile(os.path.join(FROM_DIR, filename),
                        os.path.join(FOLDER_NAME, filename+".jpg"))
