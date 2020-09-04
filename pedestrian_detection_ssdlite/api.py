import numpy as np
import tensorflow.compat.v1 as tf
import cv2 as cv
import os

tf.disable_v2_behavior()
# Read the graph.
with tf.gfile.FastGFile(
    os.path.join(os.path.dirname(__file__), "frozen_inference_graph.pb"), "rb"
) as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

sess = tf.Session()
# Restore session
sess.graph.as_default()
tf.import_graph_def(graph_def, name="")


def get_person_bbox(img, thr):

    bound_box_list = []
    # Read and preprocess an image.
    rows = img.shape[0]
    cols = img.shape[1]
    inp = cv.resize(img, (300, 300))
    inp = inp[:, :, [2, 1, 0]]  # BGR2RGB

    # Run the model
    out = sess.run(
        [
            sess.graph.get_tensor_by_name("num_detections:0"),
            sess.graph.get_tensor_by_name("detection_scores:0"),
            sess.graph.get_tensor_by_name("detection_boxes:0"),
            sess.graph.get_tensor_by_name("detection_classes:0"),
        ],
        feed_dict={"image_tensor:0": inp.reshape(1, inp.shape[0], inp.shape[1], 3)},
    )

    # Visualize detected bounding boxes.
    num_detections = int(out[0][0])
    for i in range(num_detections):
        classId = int(out[3][0][i])
        score = float(out[1][0][i])
        bbox = [float(v) for v in out[2][0][i]]
        if score > thr:
            x = bbox[1] * cols
            y = bbox[0] * rows
            right = bbox[3] * cols
            bottom = bbox[2] * rows
            bound_box_list.append([(int(x), int(y)), (int(right), int(bottom))])

    return bound_box_list
