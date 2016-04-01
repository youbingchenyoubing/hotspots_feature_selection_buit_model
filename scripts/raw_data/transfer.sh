#!/bin/bash


sed -i  's/cla1/1/g' $1
sed -i 's/cla2/2/g'  $1
sed -i 's/cla3/3/g'  $1
sed -i 's/cla4/4/g'  $1
sed -i 's/cla5/5/g'  $1
sed -i 's/cla6/6/g'  $1
sed -i 's/helix/1/g'  $1
sed -i 's/strand/2/g' $1
sed -i 's/loop/3/g'   $1
sed -i 's/nonhotspot/0/g' $1
sed -i 's/hotspot/1/g' $1
