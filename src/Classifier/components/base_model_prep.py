import os
import urllib.request as request
import tensorflow as tf
import keras 
from zipfile import ZipFile
from pathlib import Path
from Classifier.entity.config_entity import ModelConfig



class Prepare_Base_Model:
    def __init__(self,config:ModelConfig):
        self.config=config
    

    def get_base_model(self):
            self.model=keras.applications.vgg16.VGG16(
            input_shape=self.config.image_size,
            weights=self.config.weights,
            include_top=self.config.include_top)
            
            self.save_model(path=self.config.model_path, model=self.model)

    @staticmethod
    def prepare_full_model(model,classes,freeze_all,freeze_till,learning_rate):
        if freeze_all:
              model.trainable=False
            
        elif (freeze_till is not None) and (freeze_till>0):
             for layers in model.layers[:-freeze_till]:
                  model.trainable=False
        

        flatten_in=keras.layers.Flatten()(model.output)
        x= keras.layers.Dense(1000,activation='relu')(flatten_in)
        predictions= keras.layers.Dense(units=classes,
                                        activation='softmax',
                                        )(x)
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=predictions
        )

        full_model.compile(
            optimizer=keras.optimizers.legacy.SGD(learning_rate=learning_rate),
            loss=keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )
        full_model.summary()
        return full_model


    def update_base_model(self):
        self.full_model = self.prepare_full_model(
            model=self.model,
            classes=self.config.classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.learning_rate
        )

        self.save_model(path=self.config.updated_model_path, model=self.full_model)

    @staticmethod
    def save_model(path:Path,model:keras.Model):
         model.save(path)