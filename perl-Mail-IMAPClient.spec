%include	/usr/lib/rpm/macros.perl
Summary:	Mail::IMAPClient perl module
Summary(pl):	Modu³ perla Mail::IMAPClient
Name:		perl-Mail-IMAPClient
Version:	2.2.8
Release:	1
License:	Artistic License or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/Mail-IMAPClient-%{version}.tar.gz
# Source0-md5:	d8a02891cf82901a7c96e2b50ccc23bb
URL:		http://www.cpan.org/modules/by-module/Mail/Mail-IMAPClient-%{version}.readme
BuildRequires:	rpm-perlprov
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides perl routines that simplify a sockets connection
to and an IMAP conversation with an IMAP server.

%prep
%setup -q -n Mail-IMAPClient-%{version}

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
