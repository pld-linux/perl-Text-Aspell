#
# Conditional build:
%bcond_with	tests
#
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Aspell perl module
Summary(pl.UTF-8):	Moduł perla Text::Aspell
Name:		perl-Text-Aspell
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Aspell-%{version}.tar.gz
# Source0-md5:	9be39d6eaa222c10780396188c3567d0
BuildRequires:	aspell-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Aspell - Perl interface to the GNU Aspell library

%description -l pl.UTF-8
Text::Aspell - Perl interface to the GNU Aspell library

%prep
%setup -q -n Text-Aspell-%{version}

%build
%{__perl} Makefile.PL \
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
%doc Changes README
%{perl_vendorarch}/Text/*.pm
%dir %{perl_vendorarch}/auto/Text/Aspell
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Aspell/Aspell.so
%{_mandir}/man3/*
