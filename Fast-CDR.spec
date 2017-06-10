Name:		Fast-CDR
Version:	1.0.6
Release:	2%{?dist}
Summary:	Fast CDR Serialization Library

License:	ASLv2.0
URL:		http://www.eprosima.com
Source0:	https://github.com/eProsima/Fast-CDR/archive/v%{version}.tar.gz

Patch0:		fastcdr-1.0.6-endian.patch

BuildRequires:	cmake

%description
eProsima FastCDR is a C++ library that provides two serialization mechanisms.
One is the standard CDR serialization mechanism, while the other is a faster
implementation that modifies the standard.

%package devel
Summary:	Development files and libraries for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and libraries for %{name}

%prep
%setup -q
%patch0 -p0 -b .endian

%build
%cmake
make %{?_smp_mflags}


%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/*.so
%{_datadir}/fastcdr

%files devel
%{_includedir}/fastcdr
%{_libdir}/fastcdr

%changelog
* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-2
- Rename endian define to avoid conflicts

* Fri Jun 9 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-1
- Initial package
