DATASET_TRAIN = 'rockets_new'
DATASET_TEST = 'rockets_new'
NUM_WORKERS = 2
MODEL_WEIGHTS = "detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl"
BATCH_SIZE = 2
BASE_LR = 0.02
MAX_ITER = 300
BATCH_SIZE_PER_IMAGE = 128
NUM_CLASSES = 2
MERGE_FROM_FILE = "./detectron2_repo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
SCORE_THRESH_TEST = 0.5
