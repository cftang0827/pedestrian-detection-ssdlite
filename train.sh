mkdir -p logs/
now=$(date +"%Y%m%d_%H%M%S")
python train.py \
    --logtostderr \
    --pipeline_config_path=ssdlite_mobilenet_v2_coco.config \
    --train_dir=train_logs 2>&1 | tee logs/train_$now.txt &

