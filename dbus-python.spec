#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE05AE1478F814C4F (smcv@debian.org)
#
Name     : dbus-python
Version  : 1.2.18
Release  : 28
URL      : https://files.pythonhosted.org/packages/b1/5c/ccfc167485806c1936f7d3ba97db6c448d0089c5746ba105b6eb22dba60e/dbus-python-1.2.18.tar.gz
Source0  : https://files.pythonhosted.org/packages/b1/5c/ccfc167485806c1936f7d3ba97db6c448d0089c5746ba105b6eb22dba60e/dbus-python-1.2.18.tar.gz
Source1  : https://files.pythonhosted.org/packages/b1/5c/ccfc167485806c1936f7d3ba97db6c448d0089c5746ba105b6eb22dba60e/dbus-python-1.2.18.tar.gz.asc
Summary  : Python bindings for libdbus
Group    : Development/Tools
License  : AFL-2.1 GPL-2.0 MIT
Requires: dbus-python-license = %{version}-%{release}
Requires: dbus-python-python = %{version}-%{release}
Requires: dbus-python-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)

%description
=======================================
dbus-python_: Python bindings for D-Bus
=======================================

%package dev
Summary: dev components for the dbus-python package.
Group: Development
Provides: dbus-python-devel = %{version}-%{release}
Requires: dbus-python = %{version}-%{release}

%description dev
dev components for the dbus-python package.


%package license
Summary: license components for the dbus-python package.
Group: Default

%description license
license components for the dbus-python package.


%package python
Summary: python components for the dbus-python package.
Group: Default
Requires: dbus-python-python3 = %{version}-%{release}

%description python
python components for the dbus-python package.


%package python3
Summary: python3 components for the dbus-python package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dbus-python package.


%prep
%setup -q -n dbus-python-1.2.18
cd %{_builddir}/dbus-python-1.2.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634309231
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1634309231
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dbus-python
cp %{_builddir}/dbus-python-1.2.18/COPYING %{buildroot}/usr/share/package-licenses/dbus-python/fc42db3361510bdd81175b50483588737b66115a
cp %{_builddir}/dbus-python-1.2.18/dbus-gmain/COPYING %{buildroot}/usr/share/package-licenses/dbus-python/b79a4d61264303b3341005eef4ce4015f178b1b8
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/dbus-1.0/dbus/dbus-python.h
/usr/lib64/pkgconfig/dbus-python.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dbus-python/b79a4d61264303b3341005eef4ce4015f178b1b8
/usr/share/package-licenses/dbus-python/fc42db3361510bdd81175b50483588737b66115a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
