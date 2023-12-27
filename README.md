# Custom Detectron with rockets
Project Organization
------------

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