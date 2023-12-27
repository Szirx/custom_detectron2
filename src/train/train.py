from detectron2_repo.detectron2.engine import DefaultTrainer
from configs.configTrainer import config_trainer

if __name__ == '__name__':
    
    cfg = config_trainer()
    trainer = DefaultTrainer(cfg)
    trainer.resume_or_load(resume=False)
    trainer.train()