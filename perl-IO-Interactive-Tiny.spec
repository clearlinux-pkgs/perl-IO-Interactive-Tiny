#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Interactive-Tiny
Version  : 0.2
Release  : 7
URL      : http://search.cpan.org/CPAN/authors/id/D/DM/DMUEY/IO-Interactive-Tiny-0.2.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DM/DMUEY/IO-Interactive-Tiny-0.2.tar.gz
Summary  : is_interactive() without large deps
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
IO-Interactive-Tiny version 0.2
DOCUMENTATION
See POD for documentation.
INSTALLATION

%package dev
Summary: dev components for the perl-IO-Interactive-Tiny package.
Group: Development
Provides: perl-IO-Interactive-Tiny-devel = %{version}-%{release}

%description dev
dev components for the perl-IO-Interactive-Tiny package.


%prep
%setup -q -n IO-Interactive-Tiny-0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/IO/Interactive/Tiny.pm
/usr/lib/perl5/vendor_perl/5.28.1/IO/Interactive/Tiny.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Interactive::Tiny.3
