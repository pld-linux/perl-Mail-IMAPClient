#
# Conditional build:
%bcond_with	tests	# perform "make test" (currently fails?)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	IMAPClient
Summary:	Mail::IMAPClient - an IMAP Client API
Summary(pl):	Mail::IMAPClient - API klienta IMAP
Name:		perl-Mail-IMAPClient
Version:	2.2.9
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	21c1901d55a2d57f73840cad478c665d
URL:		http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.readme
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
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
yes n | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
