%define	upstream_name	Text-Roman

Name:		perl-Text-Roman
Version:	3.5
Release:	1
Summary:	Allows conversion between Roman and Arabic numerals
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Group:		Development/Perl
URL:		https://metacpan.org/dist/Text-Roman
Source0:	https://cpan.metacpan.org/authors/id/S/SY/SYP/Text-Roman-3.5.tar.gz
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)

%description
Allows conversion between Roman and Arabic numerals.

%prep
%autosetup -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
find %{buildroot} -type d -empty -delete

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*
