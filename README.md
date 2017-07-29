autor:chen youbing
contact Email:youbingchenyoubing@163.com

lab:Xiamen university


Description

=============

> this a program for feature selection. the main idea is using minimum Redundancy Maximum Relevance and SVM-forward method to features selection.
> then, we used features selected by previous method to bulid a classification based on random forest.Finally we used an exhausive search the best model we built in different condition. more deatails see our paper:Predicting Hot Spots in protein interfaces based on feature selection using mRMR combining with SVM Forward


How to use it 
=============
DEPENDENCIES
============
this program depends on the following:


+ weka-3.7
+ jpython
+ scikit-learn
+ sckit-feature

Usage
=============

+ prepare your features file (csv format) ./scripts/mrmr.csv (for feature selection ) ./scripts/raw_data/all_data.csv (for cross validation) ./scripts/raw_data/train_data.csv ./scripts/raw_data/test_data.csv (for independent validation)




+ cd ./scripts/


+ <p><code> ./myrun.sh</code>　</p>


+ wait for a little time you can find the result files in ./scripts/result_score

+ to analyze the all results use the following command:

+ <p><code> python transferTXT2CSV2.py</code></p>

ATTENTION
============
>Build model with final features you can find in following directory

+<p><code>cd ./scripts/check/feature_select</code> </p>

Reference
====
[Predicting Hot Spots in Protein Interfaces Based on Feature Selection
using Mrmr Combining with SVM Forward](http://www.tjfeonline.com/admin/archive/215.06.20161465990363.pdf)
