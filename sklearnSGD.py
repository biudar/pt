import joblib
from sklearn.linear_model import SGDClassifier

from echo import get_dataset_XY


def get_acc(predictList, trueList):
    right = 0
    total = 0
    for pre, tru in zip(predictList, trueList):
        total += 1
        if pre == tru:
            right += 1
    acc = right / 1.0 / total
    return acc


trainX, trainY, testX, testY, validX, validY = get_dataset_XY()
# print trainX[0], trainY[0]

# print len(trainX), len(trainY), len(testX), len(testY),len(validX),len(validY)


def build_model():
    clf = SGDClassifier(loss="hinge", penalty="l2", n_iter=500)
    clf.fit(trainX, trainY)
    joblib.dump(clf, 'models/sgd.model')
    predictY = clf.predict(testX)
    acc = get_acc(predictY, testY)
    print '* acc on test:', acc
    predictY = clf.predict(validX)
    acc = get_acc(predictY, validY)
    print '* acc on valid:', acc
    return 0


def main():
    build_model()
    return 0


if __name__ == '__main__':
    main()