# Chapter3

## Install libraries

```
$ pip install -r requirements.txt
```

## Generate blogdata.txt from feeds in feedlist.txt

```
$ pyton generatefeedvector.py
```

## Create hierarchical cluster from blogdata.txt

```
$ python
>> import clusters
>> blognames, words, data = clusters.readfile('blogdata.txt')
>> clust = clusters.hcluster(data) # create hierarchical cluster
>> clusters.printclust(clust, labels = blognames) # print hierarchical cluster
```
