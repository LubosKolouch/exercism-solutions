# Declare package 'Bob'
package Bob;
use strict;
use warnings;
use Exporter 'import';
our @EXPORT_OK = qw(hey);

sub hey {
    my $msg = shift or return 'Fine. Be that way!';

    return 'Fine. Be that way!' if $msg =~ /^\n*\r*\h+$/sx;

    if ( ( lc($msg) =~ /[a-z]/sx ) and ( $msg eq uc($msg) ) ) {
        return 'Calm down, I know what I\'m doing!' if $msg =~ /\?$/sx;
        return 'Whoa, chill out!';
    }

    return 'Sure.' if $msg =~ /\?\h*$/sx;

    return 'Whatever.';
}

1;
