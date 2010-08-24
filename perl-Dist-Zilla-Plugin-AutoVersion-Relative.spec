%define upstream_name    Dist-Zilla-Plugin-AutoVersion-Relative
%define upstream_version 0.01037118

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Time-Relative versioning
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DateTime)
BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(MooseX::StrictConstructor)
BuildRequires: perl(MooseX::Types::DateTime)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(Readonly)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


