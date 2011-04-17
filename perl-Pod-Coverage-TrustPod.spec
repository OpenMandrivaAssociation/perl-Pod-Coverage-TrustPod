%define upstream_name    Pod-Coverage-TrustPod
%define upstream_version 0.100000

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Allow a module's pod to contain Pod::Coverage hints
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Pod::Coverage)
BuildRequires: perl(Pod::Eventual::Simple)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a Pod::Coverage subclass (actually, a subclass of
Pod::Coverage::CountParents) that allows the POD itself to declare certain
symbol names trusted.

Here is a sample Perl module:

    package Foo::Bar;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


