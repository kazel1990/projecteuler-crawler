#!/usr/bin/perl

#irssi script
#required value
my $compdir = "/home/kazel1990/bots/euler/comp";
my $target = "#euler";
my $server = undef;

sub read_file {
	open(FILE, "<:encoding(UTF-8)", $compdir) or do {
		return;
	};
	while(my $row = <FILE>) {
		$server->command("MSG ${target} ${row}");
	}
}

sub event_privmsg {
	my ($server1, $data, $nick, $address) = @_;
	$server = $server1;
	Irssi::signal_remove("event privmsg", "event_privmsg");
}

if(caller) {
	require Irssi;
	Irssi::signal_add("event privmsg", "event_privmsg");
	Irssi::timeout_add(300000, "read_file", undef);
}
