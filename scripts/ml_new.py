#!/usr/bin/python
#coding=UTF-8

#from writeSelect import resultResult
import sys
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.io.ObjectOutputStream as ObjectOutputStream
import java.io.ObjectInputStream as ObjectInputStream
import java.io.FileOutputStream as FileOutputStream
import java.io.FileInputStream as FileInputStream
import java.io.FileReader as FileReader
import java.io.File as File
import weka.core.Instances as Instances
import weka.classifiers.Evaluation as Evaluation
import weka.core.converters.CSVLoader as CSVLoader
import weka.classifiers.trees.RandomForest as RF 
 #训练数据格式为CSV文件
import weka.core.Range as Range
import weka.core.Utils.splitOptions as splitOptions
#from weka.classifiers import Classifier,SingleClassifierEnhancer, MultipleClassifiersCombiner, FilteredClassifier,PredictionOutput
#import weka.core.classes 
#from weka.core.classes import Random
import weka.classifiers.evaluation.output.prediction.PlainText as PlainText
import configure
from configure import *
#import csv 
import java.util.Random as Random 
def readFeature(num_features,type,select_feature,numtrees):
    #filename1=resultFileTest
    #filename2=resultFileTest2
    filename1=resultFile+'_'+type+'_'+num_features+'_'+select_feature+'_train.csv'
    filename2=resultFile+'_'+type+'_'+num_features+'_'+select_feature+'_test.csv'
    #print filename1
    loader=CSVLoader()
    loader.setSource(File(filename1))
    data=loader.getDataSet()
    #print data.numAttributes()    
    
    data.setClassIndex(data.numAttributes()-1)

    rf=RF()
    rf.setNumTrees(numtrees)
    
    rf.buildClassifier(data)
   
    #print rf
    loader.setSource(File(filename2))
    

    test_data=Instances(loader.getDataSet())
    
    test_data.setClassIndex(test_data.numAttributes()-1)

    
    ''' num=test_data.numInstances()

    
    print num
   
    for i in xrange(num):

        r1=rf.distributionForInstance(test_data.instance(i))
  
        r2=rf.classifyInstance(test_data.instance(i))

        ptrixrint r1 
          
           print r2'''
    buffer = StringBuffer()  # buffer for the predictions
    output=PlainText()
    output.setHeader(test_data)
    output.setBuffer(buffer)
    
    attRange = Range()  # attributes to output
    outputDistribution = Boolean(True)
    evaluator=Evaluation(data)
    evaluator.evaluateModel(rf,test_data,[output,attRange,outputDistribution])
    #print evaluator.evaluateModel(RF(),['-t',filename1,'-T',filename2,'-I',str(numtrees)])
    #evaluator1=Evaluation(test_data)
    print evaluator.toSummaryString()
    print evaluator.toClassDetailsString()
    print evaluator.toMatrixString()
    return [evaluator.precision(1),evaluator.recall(1),evaluator.fMeasure(1),evaluator.matthewsCorrelationCoefficient(1),evaluator.numTruePositives(1),evaluator.numFalsePositives(1),evaluator.numTrueNegatives(1),evaluator.numFalseNegatives(1),evaluator.areaUnderROC(1)]
    
def readCross(num,type,select_feature,numtrees):

    filename=resultFile+'_'+type+'_'+num+'_'+select_feature+'_all.csv'
    loader=CSVLoader()
    loader.setSource(File(filename))
    data=loader.getDataSet()
    #print data.numAttributes()    
    
    data.setClassIndex(data.numAttributes()-1)

    rf=RF()
    rf.setNumTrees(numtrees)
    #pred_output = PredictionOutput( classname="weka.classifiers.evaluation.output.prediction.PlainText", options=["-distribution"]) 
    buffer = StringBuffer()  # buffer for the predictions
    output=PlainText()
    output.setHeader(data)
    output.setBuffer(buffer)
    output.setOutputDistribution(True) 
    attRange = Range()  # attributes to output
    outputDistributions = Boolean(True)
    evaluator=Evaluation(data) 
    
    evaluator.crossValidateModel(rf,data,10, Random(1),[output,attRange,outputDistributions])
    

    print evaluator.toSummaryString()
    print evaluator.toClassDetailsString()
    print evaluator.toMatrixString()
    return [evaluator.precision(1),evaluator.recall(1),evaluator.fMeasure(1),evaluator.matthewsCorrelationCoefficient(1),evaluator.numTruePositives(1),evaluator.numFalsePositives(1),evaluator.numTrueNegatives(1),evaluator.numFalseNegatives(1),evaluator.areaUnderROC(1)]
def writeResult(rows,filename):


    file_csv=open(filename,'w')

    for onerow in rows:
        for word in onerow:
            file_csv.write(str(word)+' ')
        file_csv.write('\n')
    file_csv.close()
    print "the score has ben saved in ",filename 
    
if __name__=="__main__":
   
    num=sys.argv[1]
    type=sys.argv[2]
    feature_se=sys.argv[3]
    rows=[]
    rows.append(['precision','recall','f1','MCC','TP','FP','FN','FP','AUC'])
    for i in xrange(10,120):
        newrow=readFeature(num,type,feature_se,i)
        #newrow=[str(i)+'numtrees',str(pre),str(recall),str(f1)]
        rows.append(newrow)

    filename=result+'_'+type+'_'+num+'_'+feature_se+'.txt'
    writeResult(rows,filename)
    #num=sys.argv[1]
    #type=sys.argv[2]
    '''rows=[]
    rows.append(['precision','recall','f1','MCC','TP','FP','FN','FP','AUC'])
    for i in xrange(10,120):
        newrow=readCross(num,type,feature_se,i)
        rows.append(newrow)

    filename=result1+'_'+type+'_'+num+'_'+feature_se+'.txt'
    writeResult(rows,filename)
    #exit(0)'''
