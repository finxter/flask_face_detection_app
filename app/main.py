import cv2
import os
from werkzeug.utils import secure_filename
from flask import request, render_template
from app import app
from app.file import allowed_file
from app.capture import image_capture



UPLOAD_FOLDER = 'app/static/uploads'
CAPTURE_FOLDER = 'app/static/capture'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/capture', methods=['GET', 'POST'])
def sketch():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename =secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img = cv2.imread(UPLOAD_FOLDER+'/'+filename)
        capture_img = image_capture(img)
        capture_img_name = filename.split('.')[0]+'_capture.jpg'
        save = cv2.imwrite(CAPTURE_FOLDER+'/'+capture_img_name, capture_img)
        return render_template('home.html', org_img_name=filename, capture_img_name=capture_img_name)
    return render_template('home.html')
