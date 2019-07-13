#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE05AE1478F814C4F (smcv@debian.org)
#
Name     : dbus-python
Version  : 1.2.8
Release  : 5
URL      : https://files.pythonhosted.org/packages/3f/e7/4edb582d1ffd5ac3c84188deea32e960b5c8c0fe1da56ce70224f85ce542/dbus-python-1.2.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/3f/e7/4edb582d1ffd5ac3c84188deea32e960b5c8c0fe1da56ce70224f85ce542/dbus-python-1.2.8.tar.gz
Source99 : https://files.pythonhosted.org/packages/3f/e7/4edb582d1ffd5ac3c84188deea32e960b5c8c0fe1da56ce70224f85ce542/dbus-python-1.2.8.tar.gz.asc
Summary  : Python bindings for libdbus
Group    : Development/Tools
License  : GPL-2.0
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
%setup -q -n dbus-python-1.2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546556807
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1546556807
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dbus-python
cp dbus-gmain/COPYING %{buildroot}/usr/share/package-licenses/dbus-python/dbus-gmain_COPYING
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/dbus-1.0/dbus/dbus-python.h
/usr/lib64/pkgconfig/dbus-python.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dbus-python/dbus-gmain_COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
