#!/usr/bin/perl

use HTTP::Request;
use LWP::UserAgent;

#irssi script
#required value
my $compdir = "";
my $target = "";
my $server = undef;

sub read_file {
	open(FILE, "<:encoding(UTF-8)", $compdir) or do {
		return;
	};
	while(my $row = <FILE>) {
		$server->command("MSG ${target} ${row}");
	}
}

sub get_num_solved {
	my $text = shift;

	my $request = HTTP::Request->new(GET => "http://projecteuler.net/profile/${text}.txt");

	my $ua = LWP::UserAgent->new;
	$ua->agent("Mozilla/5.0");

	my $response = $ua->request($request);
	return "fail" unless($response->is_success);

	my $response_string = $response->decoded_content;
	if ($response_string =~ m/Solved (\d+\+?)\,/) {
		return "${text} solved ".$1." problems";
	}
	return "fail";
}

sub event_privmsg {
	my ($server1, $data, $nick, $address) = @_;
	my ($target1, $text) = split(/ :/, $data, 2);
	if($server == undef) {
		$server = $server1;
	}
	if ($text =~ /count\?\s*(.+)/) {
		$server->command("MSG ${target} [count]".get_num_solved($+));
	}
}

if(caller) {
	require Irssi;
	Irssi::signal_add("event privmsg", "event_privmsg");
	Irssi::timeout_add(300000, "read_file", undef);
}

