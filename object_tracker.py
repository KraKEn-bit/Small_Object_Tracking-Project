from ultralytics import YOLO

# Configuring the tracking parameters and run the tracker
model = YOLO("yolo11n.pt")
#results = model.track(source="", conf=0.3, iou=0.5, show=True, save=True)
results = model.track(source="ult_lrNqIsgc.mp4", conf=0.3, iou=0.5, show=True, save=True)
print(results)