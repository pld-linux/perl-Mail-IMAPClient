%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	IMAPClient
Summary:	Mail::IMAPClient - an IMAP Client API
Summary(pl):	Mail::IMAPClient - API klienta IMAP
Name:		perl-Mail-IMAPClient
Version:	2.2.8
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8a02891cf82901a7c96e2b50ccc23bb
URL:		http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.readme
BuildRequires:	rpm-perlprov
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl routines that simplify a sockets connection
to and an IMAP conversation with an IMAP server.

%description
Modu³ ten udostêpnia funkcje Perla upraszczaj±ce po³±czenia z serwerem
IMAP za pomoc± gniazd oraz konwersacjê z nim w protokole IMAP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
yes n | %{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%{perl_sitelib}/Mail/IMAPClient
%{perl_sitelib}/Mail/IMAPClient.pm
%{_mandir}/man3/*
