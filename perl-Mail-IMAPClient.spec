#
# Conditional build:
%bcond_with	tests	# perform "make test" (currently fails?)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	IMAPClient
Summary:	Mail::IMAPClient - an IMAP Client API
Summary(pl.UTF-8):	Mail::IMAPClient - API klienta IMAP
Name:		perl-Mail-IMAPClient
Version:	3.25
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://search.cpan.org/CPAN/authors/id/P/PL/PLOBBES/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1035ad9328fef03f72a65d7afed6fa26
URL:		http://search.cpan.org/dist/Mail-IMAPClient/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Suggests:	perl(Authen::NTLM)
Suggests:	perl(Authen::SASL)
Suggests:	perl(Digest::HMAC_MD5)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl routines that simplify a sockets connection
to and an IMAP conversation with an IMAP server.

%description -l pl.UTF-8
Moduł ten udostępnia funkcje Perla upraszczające połączenia z serwerem
IMAP za pomocą gniazd oraz konwersację z nim w protokole IMAP.

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
%doc Changes README TODO
%{perl_vendorlib}/Mail/IMAPClient
%{perl_vendorlib}/Mail/IMAPClient.pm
%{_mandir}/man3/*
