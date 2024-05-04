# from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
# import os
# from ultralytics import YOLO

# # from ultralytics import YOLO

# app = Flask(__name__)

# # before

# @app.route('/')
# def index_before():
#     return render_template('index0.html')


# # main page
# @app.route('/imageupload')
# def index():
#     return render_template('index.html')

 

# # predict page 
# @app.route('/predict', methods=['POST'])
# def get_prediction():

#     img = request.files['img']
#     filename = secure_filename(img.filename)
#     folder = '/Users/brainhj2/Desktop/final2/fp2_web/predicted'
#     img_path = os.path.join(folder, filename)
#     img.save(img_path)
    

#     model = YOLO('yolov8n-seg.pt')
#     result = model.predict(source=img_path,
#                             conf=0.25,
#                             save=True)

#     return render_template('predict.html',
#                            img_file=filename,
#                            predict_file=filename)
#     # img = request.files['img'] # HTML로부터 받아온 이미지
#     # filename = secure_filename(img.filename)
#     # folder = '/Users/brainhj2/Desktop/final2/fp2_web/predicted'
#     # img.save(os.path.join(folder, filename))
#     # # img.save('/Users/brainhj2/Desktop/final2/fp2_web/predicted' + filename) # 입력 이미지를 저장할 경로 
    
#     # model = YOLO('yolov8n-seg.pt') # 가중치 best.pt가 저장된 경로
#     # result = model.predict(source='/Users/brainhj2/Desktop/final2/fp2_web/predicted' + filename, # 입력 이미지가 저장된 경로  
#     #                         conf=0.25,
#     #                         save=True) # 예측 결과 이미지가 저장됨 
    
#     # img_file = filename # predict.html에 작성된 상위 폴더 내 입력 이미지가 저장된 경로
#     # predict_file = filename # predict.html에 작성된 상위 폴더 내 예측 결과 이미지가 저장된 경로 
		
#     # return render_template('predict.html',
#     #                        img_file=img_file,
#     #                        predict_file=predict_file)


# if __name__ == '__main__':
#     app.run(debug=True)


#-----chatgpt4
# from flask import Flask, render_template, request, send_from_directory
# from werkzeug.utils import secure_filename
# import os
# from ultralytics import YOLO

# app = Flask(__name__)

# @app.route('/')
# def index_before():
#     return render_template('index0.html')

# @app.route('/imageupload')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def get_prediction():
#     img = request.files['img']
#     filename = secure_filename(img.filename)
#     folder = '/Users/brainhj2/Desktop/final2/fp2_web/predicted'
#     img_path = os.path.join(folder, filename)
#     img.save(img_path)
    
#     model = YOLO('yolov8n-seg.pt')
#     result = model.predict(source=img_path,
#                             conf=0.25,
#                             save=True)
    
#     return render_template('predict.html',
#                            img_file=filename,
#                            predict_file=filename)

# @app.route('/predicted/<filename>')
# def send_predicted_file(filename):
#     return send_from_directory('/Users/brainhj2/Desktop/final2/fp2_web/predicted', filename)

# if __name__ == '__main__':
#     app.run(debug=True,port=5001)
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from ultralytics import YOLO

app = Flask(__name__)

@app.route('/')
def index_before():
    return render_template('index0.html')

@app.route('/imageupload')
def index():
    return render_template('index.html')
# 수정전
# @app.route('/predict', methods=['POST'])
# def get_prediction():
#     img = request.files['img']
#     filename = secure_filename(img.filename)
#     folder = '/Users/brainhj2/Desktop/final2/fp2_web/predicted'
#     img_path = os.path.join(folder, filename)
#     img.save(img_path)
    
#     model = YOLO('yolov8n-seg.pt')
#     result = model.predict(source=img_path,
#                             conf=0.25,
#                             save=True)
    
#     return render_template('predict.html',
#                            img_file=filename,
#                            predict_file=filename)


# @app.route('/predicted/<filename>')
# def send_predicted_file(filename):
#     return send_from_directory('/Users/brainhj2/Desktop/final2/fp2_web/predicted', filename)
# 수정후

@app.route('/predict', methods=['POST'])
def get_prediction():
    img = request.files['img']
    filename = secure_filename(img.filename)
    folder = '/Users/brainhj2/Desktop/final2/fp2_web/predicted'
    img_path = os.path.join(folder, filename)
    img.save(img_path)
    
    model = YOLO('yolov8n-seg.pt')
    result = model.predict(source=img_path,
                            conf=0.25,
                            save=True,
                            save_dir=folder)
    
    # 예측된 이미지의 파일 이름을 가져옵니다.
    # 예측된 이미지의 파일 이름이 원본 이미지의 파일 이름과 동일하다고 가정합니다.
    # 그렇지 않으면 예측된 이미지의 파일 이름을 확인하고 이를 사용해야합니다.
    predicted_filename = filename
    
    return render_template('predict.html',
                           img_file=filename,
                           predict_file=predicted_filename)

@app.route('/predicted/<filename>')
def send_predicted_file(filename):
    return send_from_directory('/Users/brainhj2/Desktop/final2/fp2_web/predicted', filename)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
