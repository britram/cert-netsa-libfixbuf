%define name libfixbuf
%define version 2.2.0
%define release 1

Summary: Fixbuf IPFIX implementation library
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Group: Applications/System
License: LGPLv3
Source: http://tools.netsa.cert.org/releases/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
Vendor: http://tools.netsa.cert.org/
URL: http://tools.netsa.cert.org/fixbuf/

Requires: glib2 >= 2.18
%if "x" == "x1"
Requires: libsctp
%endif
%if "x1" == "x1"
Requires: libspread
%endif
%if "x" == "x1"
Requires: openssl
%endif
BuildRequires: glib2-devel >= 2.18
BuildRequires: pkgconfig >= 0.8
%if "x" == "x1"
BuildRequires: libsctp-devel
%endif
%if "x1" == "x1"
BuildRequires: libspread-devel
%endif
%if "x" == "x1"
BuildRequires: openssl-devel
%endif

%description
libfixbuf aims to be a compliant implementation of the IPFIX Protocol
and message format, from which IPFIX Collecting Processes and
IPFIX Exporting Processes may be built.

%package devel
Summary: Static libraries and C header files for libfixbuf
Group: Applications/System
Provides: libfixbuf-devel
Requires: %{name} = %{version}
Requires: pkgconfig >= 0.8

%description devel
Static libraries and C header files for libfixbuf.

%prep
%setup -q -n %{name}-%{version}

%build
./configure  --with-spread=/Users/netsa
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%makeinstall

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS LICENSE.txt NEWS README
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so*

%files devel
%defattr(-,root,root)
%doc doc/html
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
