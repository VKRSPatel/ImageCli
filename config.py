import os

# 192.168.29.122:5000

UPLOAD_FOLDER = 'upload/'
GARMENT_FOLDER = UPLOAD_FOLDER + 'garments/'
FACE_FOLDER = UPLOAD_FOLDER + 'faces/'
POSE_FOLDER = UPLOAD_FOLDER + 'poses/'
FINAL_FOLDER = "data/" + 'final/'

os.makedirs(GARMENT_FOLDER, exist_ok=True)
os.makedirs(FACE_FOLDER, exist_ok=True)
os.makedirs(POSE_FOLDER, exist_ok=True)
os.makedirs(FINAL_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS