#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	assertions
Summary:	assertions - select assertions in blocks of code
#Summary(pl.UTF-8):	
Name:		perl-assertions
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SA/SALVA/assertions-0.03.tar.gz
# Source0-md5:	d516e9c65acf3518e508778d14498d7c
URL:		http://search.cpan.org/dist/assertions/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The assertions pragma specifies the tags used to enable and disable
the execution of assertion subroutines.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{version}

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
%doc Changes
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/assertions/
%{_mandir}/man3/*
