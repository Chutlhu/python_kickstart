from sklearn import svm

def train(data, target, C, gamma):
    clf = svm.SVC(C, 'rbf', gamma=gamma)
    clf.fit(data[:90],
            target[:90])
    return clf
