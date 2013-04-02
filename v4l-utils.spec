%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Utilities for video4linux and DVB devices
Name            : v4l-utils
Version         : 0.9.3
Release         : 0
License         : GPLv2+ and GPLv2
Vendor          : Freescale
Packager        : Andre Silva
Group           : System Environment/Libraries
URL             : http://linuxtv.org/downloads/v4l-utils/
Source          : %{name}-%{version}.tar.bz2
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --disable-silent-rules DESTDIR=$TOP/rpm/BUILD/%{name}-%{version}/build
make 


%Install
rm -rf $RPM_BUILD_ROOT
rm -rf $TOP/rpm/BUILD/%{name}-%{version}/install

mkdir $TOP/rpm/BUILD/%{name}-%{version}/install
cd $TOP/rpm/BUILD/%{name}-%{version}/install
mkdir usr
mkdir usr/lib
mkdir usr/lib/libv4l1
mkdir usr/include


cp ../lib/libdvbv5/.libs/libdvbv5.so.0.0.0 usr/lib/
cd  usr/lib
ln -s libdvbv5.so.0.0.0 libdvbv5.so
ln -s libdvbv5.so.0.0.0 libdvbv5.so.0
cd ../../

cp ../lib/libv4l1/.libs/libv4l1.so.0.0.0 usr/lib/
cd  usr/lib
ln -s libv4l1.so.0.0.0 libv4l1.so
ln -s libv4l1.so.0.0.0 libv4l1.so.0
cd ../../

cp ../lib/libv4l2/.libs/libv4l2.so.0.0.0 usr/lib/
cd  usr/lib
ln -s libv4l2.so.0.0.0 libv4l2.so
ln -s libv4l2.so.0.0.0 libv4l2.so.0
cd ../../

cp ../lib/libv4l2rds/.libs/libv4l2rds.so.0.0.0 usr/lib/
cd  usr/lib
ln -s libv4l2rds.so.0.0.0 libv4l2rds.so
ln -s libv4l2rds.so.0.0.0 libv4l2rds.so.0
cd ../../

cp ../lib/libv4lconvert/.libs/libv4lconvert.so.0.0.0 usr/lib/
cd  usr/lib
ln -s libv4lconvert.so.0.0.0 libv4lconvert.so
ln -s libv4lconvert.so.0.0.0 libv4lconvert.so.0
cd ../../

cp ../lib/libv4l1/.libs/v4l1compat.so usr/lib/libv4l1
cp ../lib/libv4l2/.libs/v4l2convert.so usr/lib/libv4l1
cp ../lib/libv4lconvert/ov511-decomp usr/lib/libv4l1
cp ../lib/libv4lconvert/ov518-decomp usr/lib/libv4l1

cd  usr/lib
ln -s libv4l1/v4l1compat.so v4l1compat.so
ln -s libv4l1/v4l2convert.so v4l2convert.so
cd ../../

cp ../lib/include/*.h usr/include/
rm usr/include/descriptors.h

mkdir $RPM_BUILD_ROOT/
mkdir $RPM_BUILD_ROOT/opt
mkdir $RPM_BUILD_ROOT/opt/freescale
mkdir $RPM_BUILD_ROOT/opt/freescale/rootfs
mkdir $RPM_BUILD_ROOT%{pfx}

cp -rf $TOP/rpm/BUILD/%{name}-%{version}/install/* $RPM_BUILD_ROOT%{pfx}



%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
