#coding:utf-8
import csv
import sys



'''def writeCSV(fileTXT,fileCSV):
    dataTXT=[]
    file_TXT=open(fileTXT,'r')

    file_CSV=open(fileCSV,'wb')
   
    write=csv.writer(file_CSV)

    for line in file_TXT:

        linestrip=line.strip('\n') 
        
        linesplit=line.split(' ')
 

        dataTXT.append(linesplit)

    file_TXT.close()

    write.writerows(dataTXT)

    file_CSV.close()
'''

def writeCSV(filename1,filename2):
    rows=[]
    with open(filename1) as f:
    
        f_csv=csv.reader(f)
        headers=next(f_csv)
        for rows1 in f_csv:
            onerow=[]
            #rows=rows.strip()
            if rows1[0]=="nonhotspot":
                onerow.append('0')
                onerow.append('nonhotspot')
            else:
                onerow.append('1')
                onerow.append('nonhotspot')
            rows.append(onerow)
    file_csv=open(filename2,'wb')
    write=csv.writer(file_csv)
    write.writerows(rows)
    file_csv.close()

def main():


    writeCSV(sys.argv[1],sys.argv[2])



if __name__=="__main__":


    main()
