
from flask import Flask, render_template, request, send_from_directory, jsonify 
from werkzeug.utils import secure_filename
import os
from ultralytics import YOLO

app = Flask(__name__)

@app.route('/')
def index_before():
    return render_template('index0.html')

@app.route('/imageupload')
def index():
    return render_template('imageupload.html')

@app.route('/gallery')
def show():
    return render_template('gallery.html')
 
# 수정후
from PIL import Image
@app.route('/predict', methods=['POST'])
def get_prediction():
    img = request.files['img']
    filename = secure_filename(img.filename)
    folder = '/Users/parkyunsu/gitfile/cvp/final_fp2_web-main/fp2_web/predicted'
    img_path = os.path.join(folder, filename)
    img.save(img_path)
    
    predicted_filename = '/Users/parkyunsu/gitfile/cvp/final_fp2_web-main/fp2_web/yolo_predicted_results'

    model = YOLO('yolov8n-seg.pt')
    predict = model.predict(source=img_path,
                            conf=0.25,
                            save=True)

    result = predict[0]
    result_image = Image.fromarray(result.plot()[:,:,::-1])
    path = os.path.join(predicted_filename, filename)

    result_image.save(path)
    
    print("@@@@@@@@@@@")
    print("@@@@@@@@@@@")
    print(predicted_filename)
    print("@@@@@@@@@@@")
    print("@@@@@@@@@@@")

    return render_template('predict.html', img_file=filename)

@app.route('/predicted/<filename>')
def send_predicted_file(filename):
    return send_from_directory('/Users/parkyunsu/gitfile/cvp/final_fp2_web-main/fp2_web/yolo_predicted_results', filename)

 
@app.route('/get-processed-img')
def get_processed_img():
    # ... determine the filename of the processed image ...
    filename = 'processed_image.jpg'  # replace this with the actual filename
    img_url = '/predicted/' + filename
    return jsonify({'img_url': img_url})



if __name__ == '__main__':
    app.run(debug=True,port=5001)