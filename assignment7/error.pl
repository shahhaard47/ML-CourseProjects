## Assignment 7
## Balanced error perl script
## CS675-001
## Author: Usman Roshan
## Due date: Nov 5, 2018

# use Data::Dumper;

$true=shift;
open(IN,$true);
while(<IN>) {
	chomp $_;
	@s=split(/\s+/,$_);
	$truelabels{$s[1]}=$s[0];
} close IN;

# print Dumper($truelabels);

$predict=shift;
# print Dumper($predict);
open(IN,$predict);
while(<IN>) {
	chomp $_; 
	# print "line=$_\n";
	@s=split(/\s+/,$_);
	# print "splitted";
	# print Dumper($s);
	if (defined($truelabels{$s[1]})) {
		$predictedlabels{$s[1]}=$s[0];
	}
} close IN;

# print Dumper($predictedlabels);

$error=0;
foreach my $x (keys %predictedlabels) {
	if($truelabels{$x} == 0 && $predictedlabels{$x} == 0) { $a++; }
	if($truelabels{$x} == 0 && $predictedlabels{$x} == 1) { $b++; }
	if($truelabels{$x} == 1 && $predictedlabels{$x} == 0) { $c++; }
	if($truelabels{$x} == 1 && $predictedlabels{$x} == 1) { $d++; }
}
# print "a=$a b=$b c=$c d=$d\n";
$BER = 0.5*($b/($a+$b) + $c/($c+$d));
print "$BER";



































