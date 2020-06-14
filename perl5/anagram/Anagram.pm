#
#===============================================================================
#
#         FILE: Anagram.pm
#
#  DESCRIPTION: Excercism module to solve the Anagram task
#
#        FILES: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 06/14/2020 12:19:20 PM
#     REVISION: ---
#===============================================================================
package Anagram;
use strict;
use warnings;
use Data::Dumper;
use feature qw/say/;

sub match {
    my ($word, @list) = @_;

    # sort the word alphabetically for easier comparison
    my $sorted_word =  join('', sort(split(//, lc($word))));

    my @result;

    for my $w_test (@list) {
        # same word obviously is not anagram
        next if $w_test eq $word;
        my $sorted_test =  join('', sort(split(//, lc($w_test))));

        # add to result if it contains the same letters
        push @result, $w_test if $sorted_word eq $sorted_test;
    }

    return \@result;
}

1;

