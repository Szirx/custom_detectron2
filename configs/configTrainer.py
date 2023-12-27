from detectron2_repo.detectron2.config import get_cfg
import config
import os

def config_trainer():
    cfg = get_cfg()
    cfg.merge_from_file(config.MERGE_FROM_FILE)
    cfg.DATASETS.TRAIN = (config.DATASET_TRAIN)
    cfg.DATALOADER.NUM_WORKERS = config.NUM_WORKERS
    cfg.MODEL.WEIGHTS = config.MODEL_WEIGHTS  # initialize from model zoo
    cfg.SOLVER.IMS_PER_BATCH = config.BATCH_SIZE
    cfg.SOLVER.BASE_LR = config.BASE_LR
    cfg.SOLVER.MAX_ITER = (config.MAX_ITER)  # 300 iterations seems good enough, but you can certainly train longer
    cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = (config.BATCH_SIZE_PER_IMAGE)  # faster, and good enough for this toy dataset
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = config.NUM_CLASSES

    os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)

    return cfg