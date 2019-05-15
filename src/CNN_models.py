
#Create NN model
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten,Conv2D,MaxPooling2D, Reshape
from keras.callbacks import ModelCheckpoint, EarlyStopping, History
from sklearn.utils import shuffle
import numpy as np

#Train NN model fit settings
def fit_model(model,Xtrainsubset,ytrainsubset,output,seed=7):
    #shuffle trainset
    Xtrainsubset,ytrainsubset = shuffle(Xtrainsubset,ytrainsubset,random_state=seed)
    #save after each epoch in output
    checkpoint=ModelCheckpoint(output)
    opt='adam'
    model.compile(loss='categorical_crossentropy',optimizer=opt)
    if len(ytrainsubset)>32:
        batch_size=32
    elif len(ytrainsubset)>4:
        batch_size=int(len(ytrainsubset)/4)
    else:
        batch_size=1
    model.fit(x=Xtrainsubset,y=ytrainsubset, batch_size=batch_size, epochs=5,callbacks=[checkpoint])

def load(name):
    return load_model(name)


def CNN_BoterKaasEieren(Nlabels,input_shape):
    model = Sequential()
    model.add(Conv2D(10,input_shape=input_shape, kernel_size=(2,2),strides=(1,1), activation='relu')) # 2X2x10
    model.add(Conv2D(20,kernel_size=(2,2),strides=(1,1), activation='relu')) # 1X1x20
    model.add(Reshape((20,))) # 20
    model.add(Dense(20, activation='relu'))# 20
    model.add(Dense(15, activation='relu'))# 15
    model.add(Dense(Nlabels,  activation='softmax'))# Nlabels
    print(model.summary())
    return model

#main fuctie waarin mogelijke type CNN kan worden aangeroepen
def baseline_model(input_shape,Nlabels,type):

    if type == "CNN_BoterKaasEieren":
        return CNN_BoterKaasEieren(style,tmax,Nlabels,input_shape)
    exit("Error, Model type for Neural Network must be: CNN_BoterKaasEieren. type given is: "+type)
