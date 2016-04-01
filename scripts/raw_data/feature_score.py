import sys
import os
import numpy as np
from skfeature.function.statistical_based import chi_square
from skfeature.function.statistical_based import f_score
from skfeature.function.statistical_based import t_score
from skfeature.function.statistical_based import gini_index
from sknn.mlp import Classifier,Layer
import pdb


def readCSV(filename):


    fh=open(filename,'r')

    lines=[l.strip() for l in fh]

    length=len(lines)

    names=lines[0].split(',')[1:]

    features=[[x for x in l.split(',')]for l in lines[1:]if l!='']

    m=np.array(features)


    targets=m[:,0]

    variables=m[:,1:]

    fh.close()
    return targets,variables



def  get_X_Y(filetrain,filetest):


    y_train,x_train=readCSV(filetrain)
    y_test,x_test=readCSV(filetest)

   # print f_score.f_score(X,Y)

    #print t_score.t_score(X,Y)
    nn=Classifier(layers=[Layer("Rectifier",units=100),Layer("Softmax")],learning_rate=0.02,n_iter=10)
    #pdb.set_trace()
    nn.fit(x_train,y_train)

    score=nn.score(x_test,y_test)
def main():



    file_train=sys.argv[1]
    file_test=sys.argv[2]

    get_X_Y(file_train,file_test)


if __name__=="__main__":


     main()
