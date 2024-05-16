import numpy as np
import json
import tensorflow as tf
def loadData(dataset = 'database.json', tensor = True):
    with open(dataset, "r") as datafile:
        data = json.load(datafile)
        items = []
        labels = []
        rejects = []
        for item in data:
            if item[1] and not type(item[1]) is str:
                items.append(item[0])
                labels.append(item[1])
            else:
                rejects.append(item)
        # Segment Data
        p = np.random.permutation(len(items))
        items = np.array(items)[p]
        labels = np.array(labels)[p]
        xTrainInputs = items[0: int(len(items) * .8)]
        yTrainInputs = labels[0: int(len(items) * .8)]
        xTestInputs = items[int(len(items) * .8):]
        yTestInputs = labels[int(len(items) * .8):]
        if tensor:
            outInputs = tf.convert_to_tensor(xTrainInputs.astype('float32'))
            outLabels = tf.convert_to_tensor(yTrainInputs.astype('float32'))
            Testinputs = tf.convert_to_tensor(xTestInputs.astype('float32'))
            Testlabels = tf.convert_to_tensor(yTestInputs.astype('float32'))
            return outInputs, outLabels, Testinputs, Testlabels
        else:
            return xTrainInputs, yTrainInputs, xTestInputs, yTestInputs
loadData()
