Name:		LuaJIT
Summary:	A Just-In-Time Compiler for Lua
Version:	2.0.0
Release:	1%{?dist}
License:	MIT
Group:		Development/Languages
URL:		http://luajit.org/
Source:		http://luajit.org/download/LuaJIT-%{version}.tar.gz

%description
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.
Lua is a powerful, dynamic and light-weight programming language. It may be
embedded or used as a general-purpose, stand-alone language.

%package devel
Summary: Library links and header files for LuaJIT app development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
LuaJIT-devel contains the library links and header files you'll
need to develop LuaJIT applications.  LuaJIT is a Just-In-Time Compiler (JIT)
for the Lua programming language.

If you want to create applications that will use LuaJIT code or
APIs, you need to install LuaJIT-devel as well as LuaJIT.
You do not need to install it if you just want to use LuaJIT,
however.

%prep
%setup -q 

%build
make PREFIX=%{_prefix}

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} \
  INSTALL_LIB=%{buildroot}%{_libdir}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{name}-%{version} ] && rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

%files
%defattr (-,root,root)
%attr(0755,root,root) %{_bindir}/luajit
%attr(0755,root,root) %{_bindir}/luajit-2.0.0
%attr(0644,root,root) %{_datarootdir}/luajit-2.0.0/jit/*.lua
%attr(0644,root,root) %{_mandir}/man1/luajit.1*

%files devel
%defattr (-,root,root)
%attr(0644,root,root) %{_includedir}/luajit-2.0/*
%attr(0644,root,root) %{_libdir}/libluajit-5.1.so*
%attr(0644,root,root) %{_libdir}/libluajit-5.1.a
%attr(0644,root,root) %{_libdir}/pkgconfig/luajit.pc

%changelog
* Tue Feb 12 2013 Hiroaki Nakamura <hnakamur@gmail.com> 2.0.0-1
- Initial version.
