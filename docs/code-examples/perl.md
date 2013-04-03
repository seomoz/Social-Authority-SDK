---
title: Perl Example Code
layout: default
---
# Perl Example Code

Querying the Social Authority API is really quite simple. Here's an expanded example using the `HTTP::Thin::UserAgent` client from CPAN.

	#!/usr/bin/env perl
	use 5.12.1;
	use warnings;
	use HTTP::Thin::UserAgent;
	use Getopt::Long;
	use Digest::HMAC_SHA1 qw(hmac_sha1_hex);

	my $uri = 'http://api.followerwonk.com/social-authority/';

	GetOptions(
	    'uri=s' => \$uri,
	    'id=s' => \my $id,
	    'key=s' => \my $key,
	) or die;

	die "Must supply --id and --key" unless $id && $key;

	my $time = time + 500;
	my $signature = hmac_sha1_hex("$id\n$time", $key);
	my $auth = "AccessID=$id;Expires=$time;Signature=$signature";

	while ( my $names = join ',', splice @ARGV, 0,99 ) {
	    say http( 
	    	GET "$uri?screen_name=$names", 
	    	     Authorization => "MozSigned $auth" 
	    )->as_json->response->dump;
	}

Let's step through this a little bit. First we start off with a standard modern Perl preamble:

	#!/usr/bin/env perl
	use 5.12.1;
	use warnings;

We're stating that we'd like to use Perl 5.12.1. This version of Perl is the first to start with better defaults for helping us catch typos and other errors. If you're using a version before 5.12.1, we recommend replacing this line with:

	use strict;
	use feature qw(say);

Next we bring in the external libraries we would like to use. There are three:

	use HTTP::Thin::UserAgent;
	use Getopt::Long; 
	use Digest::HMAC_SHA1 qw(hmac_sha1_hex);
 

[`HTTP::Thin::UserAgent`][1] is a small HTTP client that makes doing API style requests easier. [`Getopt::Long`][2] is a standard command line argument parser, and it ships with the core Perl distribution. Finally [`Digest::HMAC_SHA1`][3] is what we'll use to sign our requests.

Continuing on:

	die "Must supply --id and --key" unless $id && $key;
 
If we don't have the information we need to sign the requests we throw an exception telling the user that they need to supply the required arguments.

Next we set up our authentication credentials:

	my $time = time + 500;
	my $signature = hmac_sha1_hex("$id\n$time", $key);
	my $auth = "AccessID=$id;Expires=$time;Signature=$signature";

Then for batches of 100 names provided on the command line, we make the API request:

	while ( my $names = join ',', splice @ARGV, 0,99 ) {
	    say http( 
	    	GET "$uri?screen_name=$names", 
	    	     Authorization => "MozSigned $auth" 
	    )->as_json->response->dump;
	}

And that's basically all there is to it.

[1]: http://metacpan.org/module/HTTP::Thin::UserAgent
[2]: http://metacpan.org/module/Getopt::Long
[3]: http://metacpan.org/module/Digest::HMAC_SHA1
