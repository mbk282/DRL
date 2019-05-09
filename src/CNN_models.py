
#Create NN model
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten,Conv2D,MaxPooling2D, Reshape
from keras.callbacks import ModelCheckpoint, EarlyStopping, History
from sklearn.utils import shuffle

#Train NN model fit settings
def fit_model(model,Xtrainsubset,ytrainsubset,output,seed):
    #shuffle trainset
    Xtrainsubset,ytrainsubset = shuffle(Xtrainsubset,ytrainsubset,random_state=seed)
    #save after each epoch in output
    checkpoint=ModelCheckpoint(output)
    opt='adam'
    model.compile(loss='categorical_crossentropy',optimizer=opt, metrics=['accuracy'])
    model.fit(x=Xtrainsubset,y=ytrainsubset, batch_size=len(ytrainsubset), epochs=1,callbacks=[checkpoint])



def CNN_BoterKaasEieren(Nlabels,input_shape):
    model = Sequential()
    model.add(Conv2D(10,input_shape=input_shape, kernel_size=(2,2),stride=1, activation='relu')) # 2X2x10
    model.add(Conv2D(20,kernel_size=(2,2),stride=1, activation='relu')) # 1X1x20
    model.add(Reshape((20))) # 20
    model.add(Dense(20, activation='relu'))# 20
    model.add(Dense(15, activation='relu'))# 15
    model.add(Dense(Nlabels,  activation='softmax'))# Nlabels
    print(model.summary())
    return model

#main fuctie waarin mogelijke type CNN kan worden aangeroepen
def baseline_model(input_shape,Nlabels,type):

    if type == "CNN_BoterKaasEieren":
        return CNN_BoterKaasEieren(style,tmax,Nlabels,input_shape)
    exit("Error, Model type for Neural Network must be: OnlyDense,MostlyDenses,CNNsmall,CNNmedium or CNNlarge. type given is: "+type)
