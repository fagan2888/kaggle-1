import scipy as sp
import math

################################
### classification functions ###
################################
def log_loss(predicted, target):
    if len(predicted) != len(target):
        error = 'lengths not equal! Number of predictions: ', len(predictions), ' and number of targets: ', len(target)
        raise Exception(error)
    target = [float(x) for x in target] # make sure all float values
    predicted = [min([max([x,1e-15]),1-1e-15]) for x in predicted] # within (0,1) interval
    return -(1.0/len(target))*sum([target[i]*math.log(predicted[i]) + (1.0-target[i])*math.log(1.0-predicted[i]) for i in xrange(len(target))])

def classification_accuracy(preds, targets, debug=False):
    if len(predicted) != len(target):
        error = 'lengths not equal! Number of predictions: ', len(predictions), ' and number of targets: ', len(target)
        raise Exception(error)
    correct = 0.
    total = len(preds)
    for i,p in enumerate(preds):
        t = targets[i]
        if t == p:
            correct += 1.
            if debug: print "right",t,p
        else:
            if debug: print "wrong",t,p
    return correct/total



############################
### regression functions ###
############################

# root mean square logarithmic error
def rmsle(preds, targets):
    if len(preds) != len(targets):
        error = 'lengths not equal! Number of predictions: ', len(predictions), ' and number of targets: ', len(target)
        raise Exception(error)
    total = 0.
    for i,p in enumerate(preds):
        t = targets[i]
        total += (math.log(p[0] + 1) - math.log(t + 1)) ** 2
    avg = total/len(preds)
    return math.sqrt(avg)
