**Object Detection**

For the object detection the Yolov5 framework was used.
Yolov5 is available at: https://github.com/ultralytics/yolov5

**Training**

For the training setup follow the tutorial at: https://wandb.ai/onlineinference/YOLO/reports/YOLOv5-Object-Detection-on-Windows-Step-By-Step-Tutorial---VmlldzoxMDQwNzk4

The labeled dataset is available at roboflow: https://app.roboflow.com/frauas/rat_detection

When downloading the data choose the Yolo v5 PyTorch option. Save the dataset in your local Yolov5 repository.

Navigate to the local Yolov5 repository.

``
python train.py --img 640 --batch 10 --epochs 200 --data path/to/dataset/.yaml --weights yolov5s.pt 
``

Here several options can be chosen:

- --img size of the pictures, as given by roboflow
- --batch and --epoch size depend on the quality of your hardware and the required training cycles
- --weights determine pretrained weights to make the training process faster
- --data the .yaml files comes with the downloaded dataset
- --weights choose a pretrained network

After the training has finished the weights file can be found at:

``
/yolov5/runs/train/expX/weights/best.pt
``

Copy this file here. These weights will be used for the object detection.