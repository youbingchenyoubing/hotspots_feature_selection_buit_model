#!/bin/bash



i=25
b=60
while(true)

do
 echo "select feature ,featurenum=$i"
 if [ $i -lt $b ]
 then 
 # python mrmr -n $i mrmr.csv
 python mrmr -n $i  mrmr.csv 
  i=$(($i+1))
 else 
 break
fi
done
