%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : The libffi library provides a portable, high level programming interface to various calling conventions. 
Name            : libffi
Version         : 3.0.12
Release         : 0
License         : BSD
Vendor          : Freescale
Packager        : Andre Silva
Group           : System Environment/Libraries
URL             : http://www.linuxfromscratch.org/blfs/view/svn/general/libffi.html
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build
patch -Np1 -i /opt/freescale/pkgs/libffi-3.0.12-includedir-1.patch && ./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --disable-static
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*.la" | xargs rm -f

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
