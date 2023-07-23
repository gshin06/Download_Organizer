import os
import shutil

# Folder paths
pic_folder = r"c:\Users\shing\OneDrive\Desktop\Stuff\Pictures"
doc_folder = r"c:\Users\shing\OneDrive\Desktop\Stuff\Documents"
exe_folder = r"c:\Users\shing\OneDrive\Desktop\Stuff\Executables"
sound_folder = r"c:\Users\shing\OneDrive\Desktop\Stuff\Sounds"
zip_folder = r"c:\Users\shing\OneDrive\Desktop\Stuff\Zips"
other_folder = r"c:\Users\shing\OneDrive\Desktop\Stuff\Other"
download_folder = r"c:\Users\shing\Downloads\Test"

# Main
for file in os.listdir(download_folder):
    path = os.path.join(download_folder, file)
    print(path)
    if file.endswith('.jpg') or file.endswith('.png'):
        shutil.move(path, pic_folder)
    elif file.endswith('.pdf'):
        shutil.move(path, doc_folder)
    elif file.endswith('.exe'):
        shutil.move(path, exe_folder)
    elif file.endswith('.mp3') or file.endswith('.wav'):
        shutil.move(path, sound_folder)
    elif file.endswith('.zip'):
        shutil.move(path, zip_folder)
    else:
        shutil.move(path, other_folder)