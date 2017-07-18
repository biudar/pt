import numpy
import os
from baseZhang import  if_no_create_it
from time import time
from keras.callbacks import EarlyStopping
from keras.layers import Dense, Dropout
from keras.models import Sequential, model_from_json
from sklearn.preprocessing import LabelEncoder
from echo import get_dataset_XY
from sklearnBayes import get_acc

trainX, trainY, testX, testY, validX, validY = get_dataset_XY()

seed = 1007
numpy.random.seed(seed)

encoder = LabelEncoder()
encoder.fit(trainY)
trainY = encoder.transform(trainY)
testY = encoder.transform(testY)
validY = encoder.transform(validY)

def create_baseline():
    model = Sequential()
    model.add(Dense(600, input_dim=12,init='normal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(500,  init='normal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(400,  init='normal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(300,  init='normal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(200,  init='normal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(100,  init='normal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(50, init='normal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def main():
    model_path = 'kerasModel/dnn.model'

    if_no_create_it(model_path)
    retrain = 1
    if retrain != 1 and os.path.isfile(model_path):
        # load json and create model
        json_file = open(model_path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights(model_path.replace('.model', '.weights'))
        print("Loaded model from disk")
    else:
        model = create_baseline()
        print model.summary()
        callbacks = [EarlyStopping(monitor='val_loss', patience=2, verbose=0)]
        model.fit(trainX, trainY, batch_size=100, nb_epoch=10, validation_data=(validX, validY), callbacks=callbacks,
                  verbose=1)
        if retrain == 1 or not os.path.isfile(model_path):
            # serialize model to JSON
            model_json = model.to_json()
            with open(model_path, "w") as json_file:
                json_file.write(model_json)
            # serialize weights to HDF5
            model.save_weights(model_path.replace('.model', '.weights'))
            print("Saved model to disk")

    pre_testY = model.predict_classes(testX)
    print '\n acc: ', get_acc(pre_testY, testY)

    return 0


if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print 'It takes:%.2f s'%(end-start)