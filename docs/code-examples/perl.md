# Perl Example Code

This example uses the `HTTP::Thin::UserAgent` client from CPAN.

	#!/usr/bin/env perl
	use 5.12.1;
	use warnings;
	use HTTP::Thin::UserAgent;
	use Getopt::Long;
	use Digest::HMAC_SHA1 qw(hmac_sha1_hex);

	my $uri = 'https://api.followerwonk.com/social-authority/';

	GetOptions(
	    'uri=s' => \$uri,
	    'id=s' => \my $id,
	    'key=s' => \my $key,
	) or die;

	die "Must supply --id and --key" unless $id && $key;

	my $time = time + 500;
	my $signature = hmac_sha1_hex("$id\n$time", $key);
	my $auth = "AccessID=$id;Timestamp=$time;Signature=$signature";

	while ( my $names = join ',', splice @ARGV, 0,99 ) {
	    say http( 
	    	GET "$uri?screen_name=$names", 
	    	     Authorization => "MozSigned $auth" 
	    )->as_json->response->dump;
	}

Begin with a standard Perl preamble:

	#!/usr/bin/env perl
	use 5.12.1;
	use warnings;

The preamble states that we'd like to use Perl 5.12.1, the first version to start with better defaults for catching typos and other errors. If you're using a version prior to 5.12.1, we recommend replacing:

	use 5.12.1;

with:

	use strict;
	use feature qw(say);

Next we import three external libraries:

	use HTTP::Thin::UserAgent;
	use Getopt::Long; 
	use Digest::HMAC_SHA1 qw(hmac_sha1_hex);
 
[`HTTP::Thin::UserAgent`][1] is a small HTTP client that makes API-style requests easier. [`Getopt::Long`][2] is a standard command line argument parser that ships with the core Perl distribution. Finally, [`Digest::HMAC_SHA1`][3] is for signing requests.

Continuing on:

	die "Must supply --id and --key" unless $id && $key;
 
If the information needed to sign requests isn't included, we throw an exception telling the user to supply the required arguments.

Next we set up our authentication credentials:

	my $time = time + 500;
	my $signature = hmac_sha1_hex("$id\n$time", $key);
	my $auth = "AccessID=$id;Timestamp=$time;Signature=$signature";

Then for batches of 100 names provided on the command line, we make the API request:

	while ( my $names = join ',', splice @ARGV, 0,99 ) {
	    say http( 
	    	GET "$uri?screen_name=$names", 
	    	     Authorization => "MozSigned $auth" 
	    )->as_json->response->dump;
	}

That's all there is to it!

[1]: http://metacpan.org/module/HTTP::Thin::UserAgent
[2]: http://metacpan.org/module/Getopt::Long
[3]: http://metacpan.org/module/Digest::HMAC_SHA1
