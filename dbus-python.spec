#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v2
# autospec commit: f032afc
#
# Source0 file verified with key 0xE05AE1478F814C4F (smcv@debian.org)
#
Name     : dbus-python
Version  : 1.3.2
Release  : 39
URL      : https://dbus.freedesktop.org/releases/dbus-python/dbus-python-1.3.2.tar.gz
Source0  : https://dbus.freedesktop.org/releases/dbus-python/dbus-python-1.3.2.tar.gz
Source1  : https://dbus.freedesktop.org/releases/dbus-python/dbus-python-1.3.2.tar.gz.asc
Summary  : Python bindings for libdbus
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 MIT
Requires: dbus-python-license = %{version}-%{release}
Requires: dbus-python-python = %{version}-%{release}
Requires: dbus-python-python3 = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : glib-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Provides: pypi(dbus_python)

%description python3
python3 components for the dbus-python package.


%prep
%setup -q -n dbus-python-1.3.2
cd %{_builddir}/dbus-python-1.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697562869
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
mkdir -p %{buildroot}/usr/share/package-licenses/dbus-python
cp %{_builddir}/dbus-python-%{version}/COPYING %{buildroot}/usr/share/package-licenses/dbus-python/ddae489dc348f108458f890a9cc9c9c53ede9158 || :
cp %{_builddir}/dbus-python-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/dbus-python/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f || :
cp %{_builddir}/dbus-python-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/dbus-python/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
cp %{_builddir}/dbus-python-%{version}/subprojects/dbus-gmain/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/dbus-python/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/dbus-python-%{version}/subprojects/dbus-gmain/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/dbus-python/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
# needs to update path on python update
install -Dm0644 -t %{buildroot}/usr/lib/python3.11/dbus_python-%version.egg-info/ dbus_python.egg-info/*
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/dbus-1.0/dbus/dbus-python.h
/usr/lib64/pkgconfig/dbus-python.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dbus-python/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/dbus-python/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/dbus-python/ddae489dc348f108458f890a9cc9c9c53ede9158
/usr/share/package-licenses/dbus-python/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
