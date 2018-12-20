# CS675-001 Course Project
- Author: Haard Shah
- Contact: Hks32@njit.edu

Main file: `courseProjectMain.py`

to run course project on test data:
```bash
$ python courseProjectMain.py train_data/snps.data train_data/snps.labels testdata
```

Other files:
- `featureSelection.py` - performs chi squared feature selection
- `read_files.py` - read data and labels from file
- `create_splits.py` - create splits for cross-validation


### Program outline
1. read data using `read_files.py`
2. select features using `featureSelection.py`
3. perform svm using Sklearn.svm module
4. output predictions for test file

