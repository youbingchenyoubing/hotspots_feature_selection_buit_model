import sys
import os
import numpy as np
from skfeature.function.statistical_based import chi_square
from skfeature.function.statistical_based import f_score
from skfeature.function.statistical_based import t_score
from skfeature.function.statistical_based import gini_index
from skfeature.function.wrapper import svm_forward
from skfeature.function.wrapper import svm_backward
from skfeature.function.wrapper import decision_tree_forward
from sknn.mlp import Classifier,Layer
import pdb
import writeSelect_new

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



def  get_X_Y(filetrain,type,numbers):

    Y,X=readCSV(filetrain)
    #y_train,x_train=readCSV(filetrain)
    #y_test,x_test=readCSV(filetest)

    #print f_score.f_score(X,Y)

    #print chi_square.chi_square(X,Y)i
    for i in xrange(20,len(X[0])):
        print "begin svm select" 
        #Feature=svm_forward.svm_forward(X,Y,i)
        Feature=svm_forward.svm_forward(X,Y,i)
        writeSelect_new.selectFeatureVariable(Feature,i,type+'_'+str(numbers))
        os.system('./os_new.sh'+' '+str(numbers)+' '+type+' '+str(i))
    #nn=Classifier(layers=[Layer("Rectifier",units=100),Layer("Softmax")],learning_rate=0.02,n_iter=10)
    #pdb.set_trace()
    #nn.fit(x_train,y_train)
    #print svm_forward.svm_forward(X,Y,12)
    #score=nn.score(x_test,y_test)
    #print score
def main():



    file_train=sys.argv[1]
    #file_test=sys.argv[2]
    type=sys.argv[2]
    numbers=sys.argv[3]
    get_X_Y(file_train,type,numbers)


if __name__=="__main__":


     main()
