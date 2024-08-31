import config 
from datetime import datetime
import os

def uploadFile(files, file_key, folder_name):
    if file_key not in files:
        return {
            "status": 0,
            "msg": "Please Add Image"
            }
    
    clothFile = files[file_key]
    
    if clothFile.filename == '':
        return {
            "status": 0,
            "msg": "No file selected"
            }
    
    # Save the file if it is allowed
    if clothFile and config.allowed_file(clothFile.filename):
        file_extension = clothFile.filename.rsplit('.', 1)[1].lower()

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        new_filename = f"{file_key}_{timestamp}.{file_extension}"

        file_path = os.path.join(folder_name, new_filename)
        clothFile.save(file_path)

        return {
            "status": 1,
            "msg":"Success",
            "file": file_path
            }

    else:
        return {
            "status": 0,
            "msg": "File type not allowed"
            }