package ETL;

use strict;
use warnings;
use Exporter 'import';
our @EXPORT_OK = qw(transform);

sub transform {

    my $hash_ref = shift;
    
    my %return_hash;

    while (my ($k, $v) = each %$hash_ref) {
        for my $item (@$v) {
            $return_hash{lc($item)} = $k;
        }
    }

    return \%return_hash;
}

1;
