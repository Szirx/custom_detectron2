from detectron2_repo.detectron2.engine import DefaultPredictor
from configs.configPredictor import config_predictor

if __name__ == "__main__":

    cfg = config_predictor()
    predictor = DefaultPredictor(cfg)