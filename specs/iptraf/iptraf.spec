# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Gerard Paul Java <riker@seul.org>
# Upstream: <iptraf-users@seul.org>

Summary: Console-based network monitoring utility
Name: iptraf
Version: 2.7.0
Release: 1
License: GPL
Group: Applications/System
URL: http://iptraf.seul.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.cebu.mozcom.com/pub/linux/net/iptraf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
IPTraf is a console-based network monitoring utility.  IPTraf gathers
data like TCP connection packet and byte counts, interface statistics
and activity indicators, TCP/UDP traffic breakdowns, and LAN station
packet and byte counts.

IPTraf features include an IP traffic monitor which shows TCP flag
information, packet and byte counts, ICMP details, OSPF packet types,
and oversized IP packet warnings; interface statistics showing IP, TCP,
UDP, ICMP, non-IP and other IP packet counts, IP checksum errors,
interface activity and packet size counts; a TCP and UDP service monitor
showing counts of incoming and outgoing packets for common TCP and UDP
application ports, a LAN statistics module that discovers active hosts
and displays statistics about their activity; TCP, UDP and other protocol
display filters so you can view just the traffic you want; logging;
support for Ethernet, FDDI, ISDN, SLIP, PPP, and loopback interfaces;
and utilization of the built-in raw socket interface of the Linux kernel,
so it can be used on a wide variety of supported network cards.

%prep
%setup

### remove prebuilt cruft included in the tarball so that sparc and alpha can
### build properly
%{__rm} -f src/{cfconv,iptraf,rvnamed}

%{__perl} -pi.orig -e '
		s|^(TARGET)\w*=.+$|$1=\$(bindir)|;
		s|^(WORKDIR)\w*=.+$|$1=\$(localstatedir)/run/iptraf|;
		s|^(LOCKDIR)\w*=.+$|$1=\$(localstatedir)/lock/iptraf|;
		s|^(LOGDIR)\w*=.+$|$1=\$(localstatedir)/log/iptraf|;
	' src/Makefile

%build
%{__make} -C src \
	CFLAGS="%{optflags}" \
	bindir="%{_bindir}" \
	localstatedir="%{_localstatedir}"

%install
%{__rm} -rf %{buildroot}
#makeinstall -C src

%{__install} -D -m0755 src/iptraf %{buildroot}%{_bindir}/iptraf
%{__install} -D -m0755 src/rvnamed %{buildroot}%{_bindir}/rvnamed

%{__install} -D -m644 Documentation/iptraf.8 %{buildroot}%{_mandir}/man8/iptraf.8
%{__install} -D -m644 Documentation/rvnamed.8 %{buildroot}%{_mandir}/man8/rvnamed.8

%{__install} -d -m0700 %{buildroot}%{_localstatedir}/{lock,log,run}/iptraf/
touch %{buildroot}%{_localstatedir}/log/iptraf/rvnamed.log \
	%{buildroot}%{_localstatedir}/run/iptraf/iptraf.cfg \
	%{buildroot}%{_localstatedir}/run/iptraf/iptraf-promisclist.tmp \
	%{buildroot}%{_localstatedir}/run/iptraf/iptraf-processcount.dat \
	%{buildroot}%{_localstatedir}/run/iptraf/iptraf-itrafmoncount.dat

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES FAQ LICENSE INSTALL README* RELEASE-NOTES Documentation/
%doc %{_mandir}/man?/*
%{_bindir}/*

%defattr(-, root, root, 0700)
%config(missingok) %{_localstatedir}/run/iptraf/
%config(missingok) %{_localstatedir}/log/iptraf/
%{_localstatedir}/lock/iptraf/

%changelog
* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 2.7.0-1
- Initial package. (using DAR)
