from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n-seg.pt')

# Run inference on 'bus.jpg' with arguments
model.predict('/Users/brainhj2/Desktop/final2/fp2_web/T004343_001_0120_B_D_F_0.jpg', save=True, imgsz=320, conf=0.5)