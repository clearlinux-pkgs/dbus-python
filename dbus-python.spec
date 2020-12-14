#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE05AE1478F814C4F (smcv@debian.org)
#
Name     : dbus-python
Version  : 1.2.16
Release  : 17
URL      : https://files.pythonhosted.org/packages/62/7e/d4fb56a1695fa65da0c8d3071855fa5408447b913c58c01933c2f81a269a/dbus-python-1.2.16.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/7e/d4fb56a1695fa65da0c8d3071855fa5408447b913c58c01933c2f81a269a/dbus-python-1.2.16.tar.gz
Source1  : https://files.pythonhosted.org/packages/62/7e/d4fb56a1695fa65da0c8d3071855fa5408447b913c58c01933c2f81a269a/dbus-python-1.2.16.tar.gz.asc
Summary  : Python bindings for libdbus
Group    : Development/Tools
License  : MIT
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
%setup -q -n dbus-python-1.2.16
cd %{_builddir}/dbus-python-1.2.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582915962
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1582915962
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dbus-python
cp %{_builddir}/dbus-python-1.2.16/COPYING %{buildroot}/usr/share/package-licenses/dbus-python/fc42db3361510bdd81175b50483588737b66115a
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/dbus-1.0/dbus/dbus-python.h
/usr/lib64/pkgconfig/dbus-python.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dbus-python/fc42db3361510bdd81175b50483588737b66115a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
