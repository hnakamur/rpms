# $Id$
# Authority: matthias

Summary: Library of Optimized Inner Loops, CPU optimized functions
Name: liboil
Version: 0.3.9
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://liboil.freedesktop.org/
Source: http://liboil.freedesktop.org/download/liboil-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glib2-devel, gcc-c++

%description
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-poing numbers or multiplying
and summing an array of N numbers. Clearly such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).


%package devel
Summary: Development files and static library for liboil
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-poing numbers or multiplying
and summing an array of N numbers. Clearly such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc ChangeLog
%{_bindir}/oil-bugreport
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/html/liboil/


%changelog
* Wed Sep 20 2006 Matthias Saou <http://freshrpms.net/> 0.3.9-1
- Update to 0.3.9.
- Remove no longer gcc opt patch.
- Enable _smp_mflags as they work again.

* Fri Feb  3 2006 Matthias Saou <http://freshrpms.net/> 0.3.7-1
- Update to 0.3.7.

* Wed Dec 14 2005 Matthias Saou <http://freshrpms.net/> 0.3.6-1
- Update to 0.3.6.

* Mon Nov 14 2005 Matthias Saou <http://freshrpms.net/> 0.3.5-3
- Sync spec files across branches.
- Parallel make seems to have worked for 0.3.5 on devel, but just in case...

* Sat Nov 12 2005 Thomas Vander Stichele <thomas at apestaart dot org> 0.3.5-2
- Trigger rebuild.

* Sat Nov 12 2005 Thomas Vander Stichele <thomas at apestaart dot org> 0.3.5-1
- Update to 0.3.5.

* Wed Oct 12 2005 Matthias Saou <http://freshrpms.net/> 0.3.3-3
- Add patch to disable unrecognized "-fasm-blocks" gcc option on PPC.

* Tue Oct  4 2005 Matthias Saou <http://freshrpms.net/> 0.3.3-2
- Update to 0.3.3.
- Update liboil-0.3.3-gccoptfixes.patch.

* Thu Jun 16 2005 Thomas Vander Stichele <thomas at apestaart dot org> 0.3.2-2
- Disable parallel make

* Wed May 25 2005 Matthias Saou <http://freshrpms.net/> 0.3.2-1
- Update to 0.3.2.
- Change ldconfig calls to be the program.
- Include new gtk-doc files in the devel package.
- add dist macro.

* Tue May 24 2005 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.0-4
- fix compilation error in FC-4 (bz #158641)
- use buildtime exported CFLAGS instead of making up its own

* Sat Apr  2 2005 Matthias Saou <http://freshrpms.net/> 0.3.1-1
- Update to 0.3.1.
- Include gtk-doc files.

* Fri Jan 28 2005 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Update to 0.3.0.

* Wed Nov 24 2004 Matthias Saou <http://freshrpms.net/> 0.2.2-1
- Update to 0.2.2.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.2.0-1
- Initial RPM release.

