# Declare package 'Leap'
package Leap;
use strict;
use warnings;
use Exporter 'import';
our @EXPORT_OK = qw(is_leap_year);

sub is_leap_year {
  my $year = shift;

  return (($year % 4 == 0) and ( ($year % 100 != 0) or ($year % 400 ==0) ));
}

1;
