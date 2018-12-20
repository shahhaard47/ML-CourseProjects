##################################
##  Extra credit Assignment 9
##  Random Hyperplanes
##  Author: Haard Shah
##  CS675
##################################

#### Main File: `assignment9.py`
execute it as follows:
```bash
python assignment9.py ../datasets/ionosphere/ionosphere.data ../datasets/ionosphere/ionosphere.trainlabels.0 1000
```

#### Calculating Error: `error.py`
execute it as follows:
```bash
python error.py ionosphere
```
OR
```bash
python error.py all
```

#### Results of running on first split of all six datasets with all values of k:
```bash
hks32_afs/afs/cad/courses/ccs/f18/cs/675/001/hks32/extra_credit$ python error.py all
----------------------------------------------
ionosphere split 0
Original data: LinearSVC best C = 100 , test error = 9.866220735785953 %
Random hyperplanes data:
For k= 10
LinearSVC best C = 1 , test error = 32.274247491638796 %
----------------------------------------------
breast_cancer split 0
Original data: LinearSVC best C = 0.001 , test error = 50.0 %
Random hyperplanes data:
For k= 10
LinearSVC best C = 1 , test error = 15.530303030303031 %
----------------------------------------------
qsar split 0
Original data: LinearSVC best C = 10 , test error = 10.515873015873016 %
Random hyperplanes data:
For k= 10
LinearSVC best C = 0.001 , test error = 50.0 %
----------------------------------------------
climate split 0
Original data: LinearSVC best C = 10 , test error = 10.0 %
Random hyperplanes data:
For k= 10
LinearSVC best C = 0.001 , test error = 50.0 %
----------------------------------------------
micromass split 0
Original data: LinearSVC best C = 0.001 , test error = 50.0 %
Random hyperplanes data:
For k= 10
LinearSVC best C = 100 , test error = 48.85057471264368 %
----------------------------------------------
hill_valley split 0
Original data: LinearSVC best C = 0.1 , test error = 46.774193548387096 %
Random hyperplanes data:
For k= 10
LinearSVC best C = 0.001 , test error = 50.0 %
++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------
ionosphere split 0
Original data: LinearSVC best C = 100 , test error = 9.866220735785953 %
Random hyperplanes data:
For k= 100
LinearSVC best C = 100 , test error = 7.6923076923076925 %
----------------------------------------------
breast_cancer split 0
Original data: LinearSVC best C = 0.001 , test error = 50.0 %
Random hyperplanes data:
For k= 100
LinearSVC best C = 10 , test error = 14.646464646464647 %
----------------------------------------------
qsar split 0
Original data: LinearSVC best C = 10 , test error = 10.515873015873016 %
Random hyperplanes data:
For k= 100
LinearSVC best C = 100 , test error = 23.055555555555557 %
----------------------------------------------
climate split 0
Original data: LinearSVC best C = 10 , test error = 10.0 %
Random hyperplanes data:
For k= 100
LinearSVC best C = 0.001 , test error = 50.0 %
----------------------------------------------
micromass split 0
Original data: LinearSVC best C = 0.001 , test error = 50.0 %
Random hyperplanes data:
For k= 100
LinearSVC best C = 10 , test error = 20.593869731800766 %
----------------------------------------------
hill_valley split 0
Original data: LinearSVC best C = 0.1 , test error = 46.774193548387096 %
Random hyperplanes data:
For k= 100
LinearSVC best C = 10 , test error = 40.32258064516129 %
++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------
ionosphere split 0
Original data: LinearSVC best C = 100 , test error = 9.866220735785953 %
Random hyperplanes data:
For k= 1000
LinearSVC best C = 10 , test error = 7.6923076923076925 %
----------------------------------------------
breast_cancer split 0
Original data: LinearSVC best C = 0.001 , test error = 50.0 %
Random hyperplanes data:
For k= 1000
LinearSVC best C = 100 , test error = 8.207070707070708 %
----------------------------------------------
qsar split 0
Original data: LinearSVC best C = 10 , test error = 10.515873015873016 %
Random hyperplanes data:
For k= 1000
LinearSVC best C = 10 , test error = 12.619047619047619 %
----------------------------------------------
climate split 0
Original data: LinearSVC best C = 10 , test error = 10.0 %
Random hyperplanes data:
For k= 1000
LinearSVC best C = 10 , test error = 20.0 %
----------------------------------------------
micromass split 0
Original data: LinearSVC best C = 0.001 , test error = 50.0 %
Random hyperplanes data:
For k= 1000
LinearSVC best C = 100 , test error = 8.28544061302682 %
----------------------------------------------
hill_valley split 0
Original data: LinearSVC best C = 0.1 , test error = 46.774193548387096 %
Random hyperplanes data:
For k= 1000
LinearSVC best C = 0.001 , test error = 50.0 %
++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------
ionosphere split 0
Original data: LinearSVC best C = 100 , test error = 9.866220735785953 %
Random hyperplanes data:
For k= 10000
LinearSVC best C = 10 , test error = 7.6923076923076925 %
----------------------------------------------
breast_cancer split 0
Original data: LinearSVC best C = 0.001 , test error = 50.0 %
Random hyperplanes data:
For k= 10000
LinearSVC best C = 100 , test error = 8.207070707070708 %
----------------------------------------------
qsar split 0
Original data: LinearSVC best C = 10 , test error = 10.515873015873016 %
Random hyperplanes data:
For k= 10000
LinearSVC best C = 100 , test error = 12.579365079365079 %
----------------------------------------------
climate split 0
Original data: LinearSVC best C = 10 , test error = 10.0 %
Random hyperplanes data:
For k= 10000
LinearSVC best C = 100 , test error = 20.0 %

```




