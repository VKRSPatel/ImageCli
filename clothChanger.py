from gradio_client import Client, handle_file
import shutil
import os
import config
from datetime import datetime
import uuid
from flask import request

def changeCloth(garmentImage, faceImage, poseImage):
        client = Client("feishen29/IMAGDressing-v1")
        result = client.predict(
                garm_img = handle_file(garmentImage),
                face_img = handle_file(faceImage),
                pose_img = handle_file(poseImage),
                prompt="A beautiful woman",
                cloth_guidance_scale=0.85,
                caption_guidance_scale=6.5,
                face_guidance_scale=0.9,
                self_guidance_scale=0.2,
                cross_guidance_scale=0.2,
                if_ipa=False,
                if_control=False,
                denoise_steps=30,
                seed=20240508,
                api_name="/IMAGDressing-v1"
        )

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        file_extension = os.path.splitext(result)[1]
        new_file_name = f"{timestamp}_{uuid.uuid4()}{file_extension}"

        destination_file = os.path.join(config.FINAL_FOLDER, new_file_name)
        destination_path = shutil.move(result, destination_file)

        return f"{request.host}/{destination_path}"