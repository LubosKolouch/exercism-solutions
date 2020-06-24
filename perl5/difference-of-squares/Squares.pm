#
#===============================================================================
#
#         FILE: Squares.pm
#
#  DESCRIPTION: Difference of squares in Perl track of exercism.io
#
#        FILES: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 06/22/2020 09:08:45 PM
#     REVISION: ---
#===============================================================================
package Squares;
use strict;
use warnings;
use feature qw/say/;
use Data::Dumper;

sub new() {
  my $class = shift;
  my $self = { N => shift };
  bless $self, $class;

  return $self;
  # new inspired by https://teams.exercism.io/tracks/perl5/exercises/difference-of-squares/solutions/c08df7f7f2df40f0b4edc1363aa42d3f
}


sub sum_of_squares {
    my $self = shift;

    my $sum;
    $sum += $_**2 for (1..$self->{'N'});
    
    return $sum;
}

sub square_of_sum {
    my $self = shift;
    
    my $sum;
    $sum += $_ for (1..$self->{'N'});

    return $sum**2;
}

sub difference() {
    my $self = shift;

    return square_of_sum($self) - sum_of_squares($self);
}
1;
 

