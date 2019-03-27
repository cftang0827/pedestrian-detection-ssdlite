# pedestrian_detection_ssdlite
Use TensorFlow object detection API and MobileNet SSDLite model to train a pedestrian detector by using VOC 2007 + 2012 dataset

## Use the api and pretrained model that I provided

Try `test.py`, and I also provided a simple interface for using model, if you don't want to know the detail, please just copy whole api directory to your project and follow the way in `test.py`, you will know how to use it.

### The model was trained by using Tensorflow object detection API, and there are tons of good tutorial, so I would not explain too much here.

### There are some useful tutorials link: 
1. https://medium.com/@WuStangDan/step-by-step-tensorflow-object-detection-api-tutorial-part-1-selecting-a-model-a02b6aabe39e
2. https://becominghuman.ai/tensorflow-object-detection-api-tutorial-training-and-evaluating-custom-object-detector-ed2594afcf73
3. https://blog.techbridge.cc/2019/02/16/ssd-hand-detection-with-tensorflow-object-detection-api/

### There are some classical scientific paper about modern object detection and the algorithm in Tensorflow Object Detection API
1. RCNN: https://arxiv.org/pdf/1311.2524.pdf
2. FastRCNN: https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf
3. FasterRCNN: https://arxiv.org/pdf/1506.01497.pdf
4. YOLO: https://pjreddie.com/media/files/papers/yolo.pdf
5. SSD: https://www.cs.unc.edu/~wliu/papers/ssd.pdf
6. MaskRCNN: https://research.fb.com/wp-content/uploads/2017/08/maskrcnn.pdf

### Training step
1. `git clone https://github.com/tensorflow/models.git`
2. Prepare VOC dataset (we took VOC 2012 + 2007 for example)
3. Edit `create_pascal_tf_record_only_person.py` and modify to the version that extract only one class, I used "person" here for example
4. Edit `pascal_label_map.pbtxt` and put one class called "person"
5. `./make_data_tf_record.sh`
6. Make training and validation dataset to tfrecord format
7. Find the proper model and detection algorithm for yourself, I took MobileNet SSDlite for example here. You can find some information in Tensorflow Object Detection API's website https://github.com/tensorflow/models/tree/master/research/object_detection
8. Download proper pretrained model from tensorflow object detection API model zoo, because we usually DO NOT train the model from scratch, instead, we will use the pretrained model from Google and do transfer learning, you can find tons of pretrained model of Tensorflow Object Detection API here: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
9. Find the proper config file for your model and algorithm, put it into directory, I used `ssdlite_mobilenet_v2_coco.config` for example. You can find the config in ```models/research/object_detection/samples/configs/```, and modify some part (training dataset path, pretrained model ckpt path) of config file to your custom dataset.
10. Use `./train.sh` and start train the model
11. After training model, you will find there are many ckpt model in `train_logs` directory, use `models/research/object_detection/export_inference_graph.py` to freeze ckpt model to pb model



>>> The tutorial is really rough, please take a look from others tutorial that I provided.
