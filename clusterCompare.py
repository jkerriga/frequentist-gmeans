from numpy import *
from scipy import *
from pylab import *

def clusterCompare(obs,init_labels,found_labels):
    acc = []
    clst_track = []
    for i in arange(max(init_labels)+1):
        labels_a = obs[init_labels == i,0]
        clst_acc = []
        for j in arange(max(found_labels)+1):
            x = 0
            labels_b = obs[found_labels == j,0]
            for a in arange(len(labels_a)):
                for b in arange(len(labels_b)):
                    if(labels_a[a] == labels_b[b]):
                        x += 1.0
            x = x/len(labels_a)
            clst_acc.append(x)
        
        clst_track.append(argmax(clst_acc))
        acc.append(max(clst_acc))

    return acc,clst_track
