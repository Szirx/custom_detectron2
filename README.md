# Custom Detectron with rockets
<div id="header" align="center">
  <img src="https://mai.ru/press/brand/download/Default/RU/Default.png" width="100" alt=""/>
</div>


# Методы искусственного интеллекта и предиктивная аналитика в проектах дефектоскопии
Задание: разметить собственный датасет на ресурсе Supervisely состоящий из 10-30 фотографий объекта (в данном случае ракеты) конвертировать в формат MS COCO. Зарегистрировать этот датасет и обучить готовую нейронную сеть на этом кастомном датасете.
<div align="center">
  <img src="https://github.com/Szirx/custom_detectron2/blob/main/Rockets_dataset/17.jpg" width="500" alt=""/>
</div>
Project Organization

    Custom_Detectron2/
      ├── configs/
      │   ├── config.py                 <- Values for configs
      │   ├── configPredictor.py        <- Config for Predictor
      │   └── configTrainer.py          <- Config for Trainer
      ├── datasetRockets/
      │   ├── images/                   <- directory with images rocket's
      │   └── instances.json            <- instances for dataset
      ├── notebooks/
      │   └── Custom_Detectron2.ipynb   <- notebook
      └── src/
      │   └── inference/
      │      └── predict.py             <- Predictor
      │   └── train/
      │      └── train.py               <- Trainer
      │   └── visualization/
      │      └── visualization.py       <- Functions for visualization
