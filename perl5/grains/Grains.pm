package Grains;
use strict;
use warnings;
use Exporter 'import';
our @EXPORT_OK = qw(grains_on_square total_grains);
use bigint;

sub grains_on_square {
  my ($square) = @_;
  die 'square must be between 1 and 64' unless ($square > 0) and ($square <= 64);
  return 2**($square-1);
}

sub total_grains {
  my $total;

  for (0..63) {
      $total += 2**$_;
  }
  return $total;
}

1;
