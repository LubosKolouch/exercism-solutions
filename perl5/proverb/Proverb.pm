#
#===============================================================================
#
#         FILE: Proverb.pm
#
#  DESCRIPTION: Proverb module for Perl track of exercism.io
#
#        FILES: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 07/04/2020 01:32:17 PM
#     REVISION: ---
#===============================================================================

package Proverb;
use strict;
use warnings;
use feature qw/say/;

sub proverb() {
    my ($input, $qualifier) = @_;

    $qualifier = " $qualifier" if $qualifier;

    my $output;

    for (0..scalar @$input -2) {
        $output .= "For want of a @$input[$_] the @$input[$_+1] was lost.\n";
    }

    $output .= "And all for the want of a$qualifier @$input[0].";

    return $output;
}


1;
 

