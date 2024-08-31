from flask import Flask, jsonify, request, send_from_directory
import os
from gradio_client import Client, handle_file
from datetime import datetime
import config 
import clothChanger 
import uploadFile

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

@app.route('/data/final/<filename>')
def serve_file(filename):
    return send_from_directory('data/final', filename)


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 0,
        'message': "Data not available!!!"
    }), 400

# Route to get all items
@app.route('/api/change_cloth', methods=['POST'])
def change_cloth():

    clothResponse = uploadFile.uploadFile(request.files, "garmentImage", config.GARMENT_FOLDER)
    if clothResponse['status'] == 0 :
        return jsonify({
            "status": 0,
            "message": clothResponse.get('error', 'Invalid Garment Image')
            }), 400
        
    faceResponse = uploadFile.uploadFile(request.files, "faceImage", config.FACE_FOLDER)
    if faceResponse['status'] == 0 :
        return jsonify({
            "status": 0,
            "message": faceResponse.get('error', 'Invalid Face Image')
            }), 400
    
    poseResponse = uploadFile.uploadFile(request.files, "poseImage", config.POSE_FOLDER)
    if poseResponse['status'] == 0 :
        return jsonify({
            "status": 0,
            "message": poseResponse.get('error', 'Invalid Pose Image')
            }), 400
    
    data = clothChanger.changeCloth(clothResponse['file'], faceResponse['file'], poseResponse['file'])
    return jsonify({
            "status": 1,
            "message" :"Success",
            "data": data
            }), 200

if __name__ == '__main__':
    app.run(debug=False)
    # app.run(host='0.0.0.0', port=5000)
