#
# Conditional build:
%bcond_with	tests	# perform "make check"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Aspell
Summary:	Text::Aspell - Perl interface to the GNU Aspell library
Summary(pl.UTF-8):	Text::Aspell - perlowy interfejs do biblioteki GNU Aspell
Name:		perl-Text-Aspell
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Aspell-%{version}.tar.gz
# Source0-md5:	67ec8b9c4769969fa714fc25c9c73832
URL:		http://search.cpan.org/dist/Text-Aspell/
BuildRequires:	aspell-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the GNU Aspell library. This
module is to meet the need of looking up many words, one at a time, in
a single session, such as spell-checking a document in memory.

%description -l pl.UTF-8
Ten moduł udostępnia perlowy interfejs do biblioteki GNU Aspell. Ma za
zadanie sprostać wyszukiwaniu wielu słów, po jednym, w pojedynczej
sesji, takiej jak sprawdzanie pisowni dokumentu w pamięci.

%prep
%setup -q -n Text-Aspell-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Text/*.pm
%dir %{perl_vendorarch}/auto/Text/Aspell
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Aspell/Aspell.so
%{_mandir}/man3/*
