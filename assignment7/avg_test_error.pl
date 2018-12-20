## Assignment 7
## Average test error perl script
## CS675-001
## Author: Usman Roshan
## Due date: Nov 5, 2018

# use strict;
$mean = 0;
$data = shift;
# $dir=$data."_std";
$dir="../datasets/".$data;
$tmpdir="tmp";
mkdir $tmpdir unless -d $tmpdir;
$n=1;
#$dir=$data;
print "-----------------------Dataset: $data-----------------------\n";

for(my $i=0; $i<$n; $i++){
  system("python assignment7.py $dir/$data.data $dir/$data.trainlabels.$i > $tmpdir/nm_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels $tmpdir/nm_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
}
$mean /= $n;
$sd = 0;
for(my $i=0; $i<$n; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= $n;
$sd = sqrt($sd);
print "Stump error = $mean ($sd)\n";

q^
for(my $i=0; $i<$n; $i++){
  system("python least_squares_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i > $tmpdir/nm_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels $tmpdir/nm_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
}
$mean /= $n;
$sd = 0;
for(my $i=0; $i<$n; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= $n;
$sd = sqrt($sd);
print "Least squares error = $mean ($sd)\n";
^if 0;

q^
$mean = 0;
for(my $i=0; $i<$n; $i++){
  system("python hinge_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i > $tmpdir/nb_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels $tmpdir/nb_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
}
$mean /= $n;
$sd = 0;
for(my $i=0; $i<$n; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= $n;
$sd = sqrt($sd);
print "Hinge error = $mean ($sd)\n";
^if 0;

q^
$mean = 0;
for(my $i=0; $i<$n; $i++){
  system("python3 perceptron.py $dir/$data.data $dir/$data.trainlabels.$i $eta $stop > p_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels p_out.$data`;
  print $err[$i];
  chomp $err[$i];
  $mean += $err[$i];
}
$mean /= $n;
$sd = 0;
for(my $i=0; $i<$n; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= $n;
$sd = sqrt($sd);
print "Perceptron (eta=$eta) error = $mean ($sd)\n";
^if 0;

q^
$mean = 0;
for(my $i=0; $i<$n; $i++){
  system("python3 hinge.py $dir/$data.data $dir/$data.trainlabels.$i $eta $stop > p_out");
  $err[$i] = `perl error.pl $dir/$data.labels p_out`;
  print $err[$i];
  chomp $err[$i];
  $mean += $err[$i];
}
$mean /= $n;
$sd = 0;
for(my $i=0; $i<$n; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= $n;
$sd = sqrt($sd);
print "Hinge (eta=$eta) error = $mean ($sd)\n";
^if 0;

q^
$mean = 0;
for(my $i=0; $i<$n; $i++){
  ##Create the training data and labels for SVM

  ##Obtain the cross-validated value of C
  $C = `perl cv-svm.pl data_cv labels_cv`;

  ##Predict with that value of C
  system("perl run_svm_light.pl $data.data $data.trainlabels.$i $C");
  $err[$i] = `perl error.pl $data.labels svmpredictions`;
  chomp $err[$i];
  $mean += $err[$i];
}
$mean /= $n;
$sd = 0;
for(my $i=0; $i<$n; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= $n;
$sd = sqrt($sd);
print "SVM error = $mean ($sd)\n";
^if 0;
