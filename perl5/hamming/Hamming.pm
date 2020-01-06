package Hamming;
use strict;
use warnings;
use Exporter 'import';
our @EXPORT_OK = qw(hamming_distance);

sub hamming_distance {
  my ( $strand1, $strand2 ) = @_;

  die 'left and right strands must be of equal length' unless length($strand1) == length($strand2);

  my $count = 0;
  for (0..length($strand1)-1) {
    $count++ if substr($strand1,$_,1) ne substr($strand2,$_,1);
  }

  return $count;
}

1;
