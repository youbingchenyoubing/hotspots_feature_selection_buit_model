import csv
import os





def transFerTXT2CSV(rows,filename):



    f_txt=open(filename,'r')
    row=0
    for line in f_txt:
        iteration=row+20
        row=row+1
        if row==1:
            continue

        else:
 
            newrow=[]
            line=line.split(' ') 
            file_Info=filename.split('/')[-1].split('.')[0].split('_')

            for i in xrange(1,len(file_Info)):


                newrow.append(file_Info[i])
            newrow.append(iteration)
            for i in xrange(0,len(line)):


                newrow.append(line[i])



            rows.append(newrow)

    f_txt.close()

    print "have dealed the %s file done and deal with %s rows."%(filename,str(row))
    return rows

def writeCSV(rows,result):


    file_result=open(result,'wb')
    write=csv.writer(file_result) 
    write.writerows(rows)
    file_result.close()
    print "DNOE!!!!"

def main():


    rows=[]
    rows.append(["type","choose","MRMR_feaNum","svm_feaNum","treenums","precision","recall","f1","MCC","TP","FP","TN","FN","AUC"])
    for filename in os.listdir(os.path.abspath('./')+'/result_score/'):
       
        filename=os.path.abspath('./')+'/result_score/'+filename

        print "please wait a moment,in the time of dealing with the file %s"%filename


        rows=transFerTXT2CSV(rows,filename)




    result=os.path.abspath('./')+'/all_result.csv'

    print "please wait again ,have write result"
  
    writeCSV(rows,result)



if __name__=="__main__":


   main()
