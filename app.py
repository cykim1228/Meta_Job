from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
import os
import datetime
from faceswap import faceswap
from gfpgan_model import gfpgan_gogo

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAN_IMAGES_FOLDER'] = 'static\images'
app.config['RESULT_FOLDER'] = 'results'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/faceswap')
def faceswap_page():
    return render_template('faceswap.html')


@app.route('/faceswap', methods=['POST'])
def faceswap_route():
    man_image = request.form.get('manImage')
    face_image = request.files['faceImage']
    print("man_image : ", man_image)
    print("face_image : ", face_image)

    if man_image and face_image and allowed_file(face_image.filename):
        face_image_path = os.path.join(app.config['UPLOAD_FOLDER'], face_image.filename)
        face_image.save(face_image_path)

        man_image_path = os.path.join(app.config['MAN_IMAGES_FOLDER'], man_image)

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        result_filename = f"result_{timestamp}.jpg"
        result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)

        success, message = faceswap(man_image_path, face_image_path, result_path)
        if success:
            # GFPGAN 후처리
            gfpgan_result_filename = f"gfpgan_{result_filename}"
            gfpgan_result_path = os.path.join('results', gfpgan_result_filename)
            gfpgan_gogo(result_path, gfpgan_result_path)

            # 결과 이미지 파일 이름만 전달
            return redirect(url_for('faceswap_result', result_image=gfpgan_result_filename))
        else:
            return jsonify({'message': message}), 400
@app.route('/faceswap_result')
def faceswap_result():
    result_image = request.args.get('result_image')
    return render_template('faceswap_result.html', result_image=result_image)

@app.route('/results/<filename>')
def results(filename):
    return send_from_directory('results', filename)

if __name__ == "__main__":
    app.run('0.0.0.0', port=7777, debug=True)