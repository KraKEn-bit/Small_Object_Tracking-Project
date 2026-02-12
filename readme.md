# **YOLOv11 Object Tracking 🎯 (Video + Webcam):**

A small project that performs **object detection + tracking** using **Ultralytics YOLOv11**.  
It can track objects from a **video file** or in **real-time via webcam**, and shows tracked results with bounding boxes (and IDs when available).

---

#**Features:**
-  Object tracking using **YOLOv11 (Ultralytics)**
-  Track objects in a **video file** (`object_tracker.py`)
-  Track objects in **real-time webcam feed** (`stream.py`)
-  Persistent tracking across frames (`persist=True`)
-  Save output results to `runs/` (when `save=True`)
-  Visualized predictions (annotated frames)

---

## 🖼️ Demo / Output

![Tracking Prediction](https://github.com/KraKEn-bit/Small_Object_Tracking-Project/blob/main/YOLO11%20Tracking%202_12_2026%207_35_24%20PM.png)


---

## 📁 Project Structure
```bash
Object-tracking/
│── object_tracker.py        # Track objects in a video file
│── stream.py                # Track objects using webcam
│── yolo11n.pt               # YOLOv11 weights file
