
```
>>> import treepredict
>>> tree = treepredict.buildtree(treepredict.my_data)
>>> treepredict.printtree(tree)
0:slashdot? 
T->{'None': 3}
F->0:(direct)? 
 T->1:New Zealand? 
  T->{'None': 1}
  F->{'Basic': 1}
 F->1:New Zealand? 
  T->{'Basic': 1}
  F->0:digg? 
   T->2:yes? 
    T->{'Basic': 1}
    F->{'None': 1}
   F->1:USA? 
    T->{'Premium': 1}
    F->3:23? 
     T->0:google? 
      T->{'Premium': 1}
      F->{'Basic': 1}
     F->1:France? 
      T->{'Basic': 1}
      F->0:kiwitobes? 
       T->{'None': 1}
       F->2:yes? 
        T->{'Basic': 1}
        F->3:21? 
         T->{'Premium': 1}
         F->{'None': 1}
>>> treepredict.classify(['(direct)', 'USA', 'yes', 5], tree)
{'Basic': 1}
```
