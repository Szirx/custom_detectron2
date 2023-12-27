import random
from detectron2_repo.detectron2.utils.visualizer import Visualizer
import cv2
from google.colab.patches import cv2_imshow
from detectron2_repo.detectron2.utils.visualizer import ColorMode

def show_masks(dataset_dicts, dataset_train_metadata):

    for d in random.sample(dataset_dicts, 3):
        img = cv2.imread(d["file_name"])
        visualizer = Visualizer(img[:, :, ::-1], metadata=dataset_train_metadata, scale=0.5)
        vis = visualizer.draw_dataset_dict(d)
        cv2_imshow(vis.get_image()[:, :, ::-1])

def show_predicted_masks(dataset_dicts, dataset_train_metadata, predictor):
    for d in random.sample(dataset_dicts, 3):    
        im = cv2.imread(d["file_name"])
        outputs = predictor(im)
        v = Visualizer(im[:, :, ::-1],
                    metadata=dataset_train_metadata, 
                    scale=0.8, 
                    instance_mode=ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels
        )
        v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        cv2_imshow(v.get_image()[:, :, ::-1])