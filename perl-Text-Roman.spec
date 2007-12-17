%define module  Text-Roman
%define name    perl-%{module}
%define version 3.3
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Allows conversion between Roman and Arabic algarisms
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{perl_vendorlib}/Text
%{_mandir}/*/*

