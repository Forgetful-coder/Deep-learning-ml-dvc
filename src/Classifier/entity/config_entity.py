from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url:str
    local_file_data:Path
    unzip_file_path:Path

@dataclass(frozen=True)
class ModelConfig:
    root_dir:Path
    model_path:Path
    updated_model_path:Path
    learning_rate: float
    image_size:list
    include_top:bool
    weights:str
    classes:int


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list