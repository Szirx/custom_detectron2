from detectron2_repo.detectron2.config import get_cfg
import config
import os

def config_predictor():
    cfg = get_cfg()
    cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = config.SCORE_THRESH_TEST   # set the testing threshold for this model
    cfg.DATASETS.TEST = (config.DATASET_TEST)

    return cfg