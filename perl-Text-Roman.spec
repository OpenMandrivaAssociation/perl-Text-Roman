%define upstream_name    Text-Roman
%define upstream_version 3.5

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Allows conversion between Roman and Arabic algarisms
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Roman-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This package supports both conventional Roman algarisms (which range from 1 to
3999) and Milhar Romans, a variation which uses a bar across the algarism to
indicate multiplication by 1,000. For the purposes of this module, acceptable
syntax consists of an underscore suffixed to the algarism e.g. IV_V = 4,005.
The term Milhar apparently derives from the Portuguese word for "thousands" and
the range of this notation extends the range of Roman numbers to 3999 x 1000 +
3999 = 4,002,999.

Note: the functions in this package treat Roman algarisms in a case-insensitive
manner such that "VI" == "vI" == "Vi" == "vi".

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
%{perl_vendorlib}/Text
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.300.0-1mdv2010.0
+ Revision: 405714
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.3-6mdv2009.0
+ Revision: 241990
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.3-4mdv2008.0
+ Revision: 87029
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.3-3mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.3-2mdk
- Fix SPEC according to Perl Policy
    - Source URL
- use mkrel

* Tue Aug 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.3-1mdk
- first mdk release


