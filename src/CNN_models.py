
#Create NN model
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten,Conv1D,MaxPooling1D, Reshape
from keras.callbacks import ModelCheckpoint, EarlyStopping, History
from sklearn.utils import shuffle
from keras.optimizers import SGD
from tensorflow.python.client import device_lib

print (device_lib.list_local_devices())
exit()

#Train NN model fit settings 
def fit_model(style,regressor,Xtrainsubset,ytrainsubset,Xval,yval,Xvalweights,output,seed):
    Xtrainsubset,ytrainsubset = shuffle(Xtrainsubset,ytrainsubset,random_state=seed)
    checkpoint=ModelCheckpoint(output)
    Earlystop=EarlyStopping(monitor='abs(val_acc-acc)',patience=5,mode='min')
    history=History()
    opt='adam'
    regressor.compile(loss='mean_squared_error',optimizer=opt, metrics=['accuracy'])#'categorical_crossentropy'

    if not style=='regression' and not style=='classification':
        exit("Error, fit_model style must be either 'regression' or  'classification'.")
    if style=='regression':
        regressor.fit(x=Xtrainsubset,y=ytrainsubset.reshape(-1,1), validation_data=(Xval,yval.reshape(-1,1),Xvalweights), batch_size=1000, epochs=150,callbacks=[checkpoint,history,Earlystop])
    if style=='classification':
        regressor.fit(x=Xtrainsubset,y=ytrainsubset, validation_data=(Xval,yval,Xvalweights), batch_size=1000, epochs=150,callbacks=[checkpoint,history,Earlystop])

def baseline_model_Large(style,tmax,Nlabels,input_shape):
    if not style=='regression' and not style=='classification':
        exit("Error, fit_model style must be either 'regression' or  'classification'.")
    model = Sequential()
    model.add(Conv1D(filters=200,input_shape=input_shape, kernel_size=(1), strides=(1), activation='relu'))#200 x 40
    model.add(MaxPooling1D(pool_size=2)) #200 x 20
    model.add(Conv1D(filters=180, kernel_size=(3), strides=(1), activation='relu'))#180 x 18
    model.add(Conv1D(filters=140, kernel_size=(3), strides=(1), activation='relu'))#140 x 16
    model.add(MaxPooling1D(pool_size=2)) #140 x 8
    model.add(Conv1D(filters=120, kernel_size=(3), strides=(1), activation='relu'))#120 x 6
    model.add(MaxPooling1D(pool_size=2))#120 x 3
    model.add(Conv1D(filters=120, kernel_size=(3), strides=(1), activation='relu'))#120 x 1
    model.add(Reshape((120,)))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(80, activation='relu'))
    model.add(Dense(60, activation='relu'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(20, activation='relu'))
    if style=='classification':
        model.add(Dense(Nlabels,  activation='softmax'))
    if style=='regression':
        model.add(Dense(1,activation='relu'))
    print model.summary()
    return model


def baseline_model_Medium(style,tmax,Nlabels,input_shape):
    if not style=='regression' and not style=='classification':
        exit("Error, fit_model style must be either 'regression' or  'classification'.")
    model = Sequential()
    model.add(Conv1D(filters=40,input_shape=input_shape, kernel_size=(1), strides=(1), activation='relu'))#40 x 40
    model.add(MaxPooling1D(pool_size=2))#40x20
    model.add(Conv1D(filters=80, kernel_size=(3), strides=(1), activation='relu'))#80 x 18
    model.add(Conv1D(filters=80, kernel_size=(3), strides=(1), activation='relu'))#80 x 16
    model.add(MaxPooling1D(pool_size=2))#80 x 8
    model.add(Conv1D(filters=120, kernel_size=(8), strides=(1), activation='relu'))#120 x 1
    model.add(Reshape((120,)))
    model.add(Dense(80, activation='relu'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(20, activation='relu'))
    if style=='classification':
        model.add(Dense(Nlabels,  activation='softmax'))
    if style=='regression':
        model.add(Dense(1,activation='relu'))
    print model.summary()
    return model


def baseline_model_small(style,tmax,Nlabels,input_shape):
    if not style=='regression' and not style=='classification':
        exit("Error, fit_model style must be either 'regression' or  'classification'.")
    model = Sequential()
    model.add(Conv1D(filters=10,input_shape=input_shape, kernel_size=(1), strides=(1), activation='relu'))#10 x 40
    model.add(MaxPooling1D(pool_size=2))#10 x 20
    model.add(Conv1D(filters=20, kernel_size=(5), strides=(1), activation='relu'))#20 x 16
    model.add(MaxPooling1D(pool_size=2))#20 x 8
    model.add(Conv1D(filters=40, kernel_size=(8), strides=(1), activation='relu'))#40x1
    model.add(Reshape((40,)))
    if style=='classification':
        model.add(Dense(Nlabels,  activation='softmax'))
    if style=='regression':
        model.add(Dense(1,activation='relu'))
    print model.summary()
    return model

def baseline_model_MostlyDense(style,tmax,Nlabels,input_shape):
    if not style=='regression' and not style=='classification':
        exit("Error, fit_model style must be either 'regression' or  'classification'.")
    model = Sequential()
    model.add(Conv1D(filters=120,input_shape=input_shape, kernel_size=(input_shape[0]), strides=(1), activation='relu'))#120 x 1
    model.add(Reshape((120,)))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(80, activation='relu'))
    model.add(Dense(60, activation='relu'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(20, activation='relu'))
    if style=='classification':
        model.add(Dense(Nlabels,  activation='softmax'))
    if style=='regression':
        model.add(Dense(1,activation='relu'))
    print model.summary()
    return model

def baseline_model_OnlyDense(style,tmax,Nlabels,input_shape):
    if not style=='regression' and not style=='classification':
        exit("Error, fit_model style must be either 'regression' or  'classification'.")
    model = Sequential()
    model.add(Dense(120,input_shape=input_shape, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(80, activation='relu'))
    model.add(Dense(60, activation='relu'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(20, activation='relu'))
    if style=='classification':
        model.add(Dense(Nlabels,  activation='softmax'))
    if style=='regression':
        model.add(Dense(1,activation='relu'))
    print model.summary()
    return model

#main fuctie waarin mogelijke type CNN kan worden aangeroepen
def baseline_model(style,tmax,Nlabels,type,expand_to_track):
    if expand_to_track:
        input_shape=(tmax,3)
    else:
        input_shape=(6,)
    if type == "MostlyDense":
        return baseline_model_MostlyDense(style,tmax,Nlabels,input_shape)
    if type == "OnlyDense":
        return baseline_model_OnlyDense(style,tmax,Nlabels,input_shape)
    if type == "CNNsmall":
        return baseline_model_small(style,tmax,Nlabels,input_shape)
    if type == "CNNmedium":
        return baseline_model_Medium(style,tmax,Nlabels,input_shape)
    if type == "CNNlarge":
        return baseline_model_Large(style,tmax,Nlabels,input_shape)
    exit("Error, Model type for Neural Network must be: OnlyDense,MostlyDenses,CNNsmall,CNNmedium or CNNlarge. type given is: "+type)
