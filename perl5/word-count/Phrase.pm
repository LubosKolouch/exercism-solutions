#
#===============================================================================
#
#         FILE: Phrase.pm
#
#  DESCRIPTION: Module to count the words
#
#        FILES: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 05/25/2020 09:15:30 PM
#     REVISION: ---
#===============================================================================
package Phrase;
use strict;
use warnings;
use feature qw/say/;
use Data::Dumper;

sub word_count {
    my $input = shift || die "No input";

    my %output;

    for (split /([,\h\r\n\t_]+)/, $input) {
        $_ =~ s/[!@\$%^&]//g;
        next unless /\w/;
        $output{lc($_)}++;
    }

    return \%output;
}

1;
 

