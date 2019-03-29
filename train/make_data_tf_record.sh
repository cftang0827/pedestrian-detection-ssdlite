python create_pascal_tf_record_only_person.py --data_dir VOCdevkit --label_map_path pascal_label_map.pbtxt --output_path person_tf_2019_03_13_train.tfrecord --year VOC2007 VOC2012 --set train

python create_pascal_tf_record_only_person.py --data_dir VOCdevkit --label_map_path pascal_label_map.pbtxt --output_path person_tf_2019_03_13_val.tfrecord --year VOC2007 VOC2012 --set val

