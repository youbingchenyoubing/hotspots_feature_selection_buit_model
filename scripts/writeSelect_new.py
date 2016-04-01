import csv
import os
import configure
from configure import *
import numpy as np
#get selectResult
def writeResult(rows,feature_num,type):
  
    if not os.path.isdir(resultDir):
        
       os.system('mkdir '+resultDir)


    
    filename=resultFile+'_'+type+'_'+str(feature_num)+'.csv'
  
    file_feature=open(filename,'wb')

    write=csv.writer(file_feature)

    write.writerows(rows)    
    
    file_feature.close()
    print "the result have been saved in ",filename


def readSelect(result):
    colnum=[]
    print result
    for one in result:
        colnum.append(one[0])
    return colnum
def selectFeatureVariable(result,feature_num,type):
    colnum=result
    rows=[]
    with open(raw_data_all) as f_raw:

        f_raw_csv=csv.reader(f_raw)



        #headers=next(f_raw_csv)
        for onerow in f_raw_csv:
            addrow=[]
            for i in xrange(1,base):
                addrow.append(onerow[i])
            for onecol in colnum:
                addrow.append(onerow[onecol+base])
            addrow.append(onerow[0])

            rows.append(addrow)



    filename=resultFile+'_'+type+'_'+str(feature_num)+'_all.csv'

    file_select=open(filename,'w')

    write=csv.writer(file_select)
    
    write.writerows(rows)
    file_select.close()
    print "the select result have been saved in ",filename
    rows=[]
    with open(raw_data_train) as f_raw:

        f_raw_csv=csv.reader(f_raw)



        #headers=next(f_raw_csv)
        for onerow in f_raw_csv:
            addrow=[]
            for i in xrange(1,base):
                addrow.append(onerow[i])
            for onecol in colnum:
                addrow.append(onerow[onecol+base])
            addrow.append(onerow[0])
            rows.append(addrow)



    filename=resultFile+'_'+type+'_'+str(feature_num)+'_train.csv'

    file_select=open(filename,'w')

    write=csv.writer(file_select)
    
    write.writerows(rows)
    file_select.close()
    print "the select result have been saved in ",filename
    rows=[]
    with open(raw_data_test) as f_raw:

        f_raw_csv=csv.reader(f_raw)



        #headers=next(f_raw_csv)
        for onerow in f_raw_csv:
            addrow=[]
            for i in xrange(1,base):
                addrow.append(onerow[i])
            for onecol in colnum:
                addrow.append(onerow[onecol+base])
            addrow.append(onerow[0])

            rows.append(addrow)



    filename=resultFile+'_'+type+'_'+str(feature_num)+'_test.csv'

    file_select=open(filename,'w')

    write=csv.writer(file_select)
    
    write.writerows(rows)
    file_select.close()
    print "the select result have been saved in ",filename




def readFeature(filename):
    print filename
    reader=csv.reader(open(filename,'rb'),delimiter=',')
    x=list(reader)
    #data=np.recfromcsv(filename,case_sensitive=True)
    data=np.array(x)
    
    X=data[:,1:]
   
    Y=data[:,0] 


    return X,Y



