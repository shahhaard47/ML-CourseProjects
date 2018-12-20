
First Run
```bash
hks32_afs/afs/cad/courses/ccs/f18/cs/675/001/hks32/course_project$ python courseProject.py
Reading data: current iter - 1000
Reading data: current iter - 2000
Reading data: current iter - 3000
Reading data: current iter - 4000
Reading data: current iter - 5000
Reading data: current iter - 6000
Reading data: current iter - 7000
Reading data: current iter - 8000
----------Num features: 5 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.613125
Adaptive hinge loss training...
Accuracy: 0.513125
Adaptive least squares training...
Accuracy: 0.53625
----------Num features: 5 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.615
Adaptive hinge loss training...
Accuracy: 0.48
Adaptive least squares training...
Accuracy: 0.48
----------Num features: 5 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.62625
```
<ended it>

```bash
hks32_afs/afs/cad/courses/ccs/f18/cs/675/001/hks32/course_project$ python courseProject.py 
Reading data: current iter - 1000
Reading data: current iter - 2000
Reading data: current iter - 3000
Reading data: current iter - 4000
Reading data: current iter - 5000
Reading data: current iter - 6000
Reading data: current iter - 7000
Reading data: current iter - 8000
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.661875
Adaptive hinge loss training...
Accuracy: 0.51375
Adaptive least squares training...
Accuracy: 0.5175
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.67375
Adaptive hinge loss training...
Accuracy: 0.484375
Adaptive least squares training...
Accuracy: 0.489375
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.648125
Adaptive hinge loss training...
Accuracy: 0.4975
Adaptive least squares training...
Accuracy: 0.503125
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.68875
Adaptive hinge loss training...
Accuracy: 0.51375
Adaptive least squares training...
Accuracy: 0.52
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.675625
Adaptive hinge loss training...
Accuracy: 0.484375
```

more got rid of hinge and least squares 
* Added gaussian naive bayes from scikit learn

```bash
hks32_afs/afs/cad/courses/ccs/f18/cs/675/001/hks32/course_project$ python courseProject.py 
Reading data: current iter - 1000
Reading data: current iter - 2000
Reading data: current iter - 3000
Reading data: current iter - 4000
Reading data: current iter - 5000
Reading data: current iter - 6000
Reading data: current iter - 7000
Reading data: current iter - 8000
----------Num features: 5 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.613125
Scikit learn gaussian naive bayes training...
Accuracy: 0.623125
----------Num features: 5 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.615
Scikit learn gaussian naive bayes training...
Accuracy: 0.61
----------Num features: 5 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.62625
Scikit learn gaussian naive bayes training...
Accuracy: 0.6325
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.661875
Scikit learn gaussian naive bayes training...
Accuracy: 0.64125
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.67375
Scikit learn gaussian naive bayes training...
Accuracy: 0.634375
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.648125
Scikit learn gaussian naive bayes training...
Accuracy: 0.643125
```

Added balanced error (running again continuing at 30)
```bash
hks32_afs/afs/cad/courses/ccs/f18/cs/675/001/hks32/course_project$ python courseProject.py 
Reading data: current iter - 1000
Reading data: current iter - 2000
Reading data: current iter - 3000
Reading data: current iter - 4000
Reading data: current iter - 5000
Reading data: current iter - 6000
Reading data: current iter - 7000
Reading data: current iter - 8000
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.68875
Balanced accuracy: 0.6892368603756591
Scikit learn gaussian naive bayes training...
Accuracy: 0.645
Balanced accuracy: 0.6453849473664459
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.675625
Balanced accuracy: 0.6761876832844576
Scikit learn gaussian naive bayes training...
Accuracy: 0.658125
Balanced accuracy: 0.6585141739980449
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.665625
Balanced accuracy: 0.6655947648691217
Scikit learn gaussian naive bayes training...
Accuracy: 0.63375
Balanced accuracy: 0.6338220955523888
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.690625
Balanced accuracy: 0.6907176677362254
Scikit learn gaussian naive bayes training...
Accuracy: 0.64
Balanced accuracy: 0.6401059551285659
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.665
Balanced accuracy: 0.6658455522971652
Scikit learn gaussian naive bayes training...
Accuracy: 0.64875
Balanced accuracy: 0.6494232649071359
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training...
Accuracy: 0.655625
Balanced accuracy: 0.6556820170504263
Scikit learn gaussian naive bayes training...
Accuracy: 0.635
Balanced accuracy: 0.6350221255531389
```
continuing at 100 (only calculating balanced accuracy because its more stable)

```bash
hks32_afs/afs/cad/courses/ccs/f18/cs/675/001/hks32/course_project$ python courseProject.py 
Reading data: current iter - 1000
Reading data: current iter - 2000
Reading data: current iter - 3000
Reading data: current iter - 4000
Reading data: current iter - 5000
Reading data: current iter - 6000
Reading data: current iter - 7000
Reading data: current iter - 8000
----------Num features: 100 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training...
Balanced accuracy: 0.6879171123161891
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6383733948798779
----------Num features: 100 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training...
Balanced accuracy: 0.6711045943304008
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.64
----------Num features: 100 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training...
Balanced accuracy: 0.658766469161729
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6426473161829046
----------Num features: 500 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training...
Balanced accuracy: 0.6223972504206305
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6275855490714853
----------Num features: 500 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training...
Balanced accuracy: 0.6341348973607038
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6303812316715542
----------Num features: 500 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training...
Balanced accuracy: 0.6288094702367559
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6170435510887772
```
FINAL
```bash
hks32_afs/afs/cad/courses/ccs/f18/cs/675/001/hks32/course_project$ python courseProject.py 
Reading data: current iter - 1000
Reading data: current iter - 2000
Reading data: current iter - 3000
Reading data: current iter - 4000
Reading data: current iter - 5000
Reading data: current iter - 6000
Reading data: current iter - 7000
Reading data: current iter - 8000
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6622555182356658
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6622555182356658
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6622555182356658
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6411848960776587
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6737829912023461
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6737829912023461
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6737829912023461
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6344281524926686
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6481005775144378
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6481005775144378
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6481005775144378
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6432442061051526
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.3 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6531127392386551
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6531127392386551
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6531127392386551
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6487557011807831
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.4 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6555446868886374
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6555446868886374
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6555446868886374
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.628869748923377
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.5 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6528701496619905
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6528701496619905
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6528701496619905
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6399163768512368
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.6 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6615318382842159
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6615318382842159
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6615318382842159
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6473758365621698
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.7 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6712573203582523
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6712573203582523
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6712573203582523
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.650072812955081
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.8 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6549298305651526
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6549298305651526
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6549298305651526
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6343962272111459
----------Num features: 15 ----- Labels: train_data/snps.trainlabels.9 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6650041251031276
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6650041251031276
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6650041251031276
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6437660941523538
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6892368603756591
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6892368603756591
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6892368603756591
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6453849473664459
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6761876832844576
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6761876832844576
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6761876832844576
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6585141739980449
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6655947648691217
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6655947648691217
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6655947648691217
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6338220955523888
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.3 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6687354198990936
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6687354198990936
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6687354198990936
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6506267978543716
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.4 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6606012213186991
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6606012213186991
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6606012213186991
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6332028051577901
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.5 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6653745457387363
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6653745457387363
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6653745457387363
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6443749755773515
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.6 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6569057962506359
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6569057962506359
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6569057962506359
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6567962114985715
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.7 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6856745979662373
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6856745979662373
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6856745979662373
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6506868792929956
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.8 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6737359579092774
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6737359579092774
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6737359579092774
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6412990994623026
----------Num features: 30 ----- Labels: train_data/snps.trainlabels.9 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6681510787769694
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6681510787769694
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6681510787769694
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6481505787644691
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.0 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6907176677362254
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6907176677362254
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6907176677362254
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6401059551285659
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.1 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6658455522971652
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6658455522971652
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6658455522971652
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6494232649071359
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.2 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6556820170504263
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6556820170504263
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6556820170504263
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6350221255531389
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.3 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6656252587894669
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6656252587894669
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6656252587894669
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6431299111404861
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.4 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6674906713502634
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6674906713502634
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6674906713502634
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6358060765918083
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.5 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6587433081942871
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6587433081942871
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6587433081942871
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6195771951076551
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.6 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6607177801260224
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6607177801260224
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6607177801260224
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.639536613048413
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.7 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6769589184932405
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6769589184932405
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6769589184932405
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6419961999762498
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.8 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6850962026780175
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6850962026780175
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6850962026780175
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.644386054557302
----------Num features: 50 ----- Labels: train_data/snps.trainlabels.9 ----------
Selecting features...
Scikit learn svm training... C : 0.001
Balanced accuracy: 0.6674979374484362
Scikit learn svm training... C : 1.0
Balanced accuracy: 0.6674979374484362
Scikit learn svm training... C : 1000
Balanced accuracy: 0.6674979374484362
Scikit learn gaussian naive bayes training...
Balanced accuracy: 0.6499599989999749
```

