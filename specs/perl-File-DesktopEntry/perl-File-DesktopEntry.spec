# $Id$
# Authority: dag
# Upstream: Jaap Karssenberg <pardus$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-DesktopEntry

Summary: Perl module that implements an object to handle .desktop files
Name: perl-File-DesktopEntry
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-DesktopEntry/

Source: http://www.cpan.org/modules/by-module/File/File-DesktopEntry-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build) >= 0.24
BuildRequires: perl(Test::More)

%description
File-DesktopEntry is a Perl module that implements an object
to handle .desktop files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/File::DesktopEntry.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/DesktopEntry/
%{perl_vendorlib}/File/DesktopEntry.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
