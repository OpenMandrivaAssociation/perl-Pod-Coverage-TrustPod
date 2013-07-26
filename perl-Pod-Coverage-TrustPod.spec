%define upstream_name    Pod-Coverage-TrustPod
%define upstream_version 0.100002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.100002
Release:	1

Summary:	Allow a module's pod to contain Pod::Coverage hints
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-Coverage-TrustPod-0.100002.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl(Pod::Eventual::Simple)
BuildArch:	noarch

%description
This is a Pod::Coverage subclass (actually, a subclass of
Pod::Coverage::CountParents) that allows the POD itself to declare certain
symbol names trusted.

Here is a sample Perl module:

    package Foo::Bar;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.1-1mdv2011
+ Revision: 690307
- update to new version 0.100001

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1
+ Revision: 654181
- update to new version 0.100000

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.92.832-1mdv2011.0
+ Revision: 595985
- update to new version 0.092832

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.92.830-1mdv2011.0
+ Revision: 461347
- update to 0.092830

* Sun Aug 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.92.400-1mdv2010.0
+ Revision: 422559
- update to 0.092400

* Fri Jun 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.91.470-1mdv2010.0
+ Revision: 387283
- import perl-Pod-Coverage-TrustPod


* Fri Jun 19 2009 cpan2dist 0.091470-1mdv
- initial mdv release, generated with cpan2dist


