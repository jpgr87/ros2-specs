%global commit0 2b545fc75cb8beb6d49c26509fd07acc6a746545
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:		Fast-RTPS
Version:	1.4.0
Release:	2%{?dist}
Summary:	C++ Implementation of the RTPS (Real Time Publish Subscribe) Protocol

License:	ASL2.0
URL:		http://www.eprosima.com/index.php/products-all/eprosima-fast-rtps
Source0:  https://github.com/eProsima/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Patch0: fastrtps-1.4.0-fedora.patch
Patch1: fastrtps-1.4.0-asio.patch
Patch2: fastrtps-1.4.0-el7.patch

BuildRequires:  asio-devel
BuildRequires:	cmake
BuildRequires:  Fast-CDR-devel
BuildRequires:  tinyxml2-devel

%description
eprosima Fast RTPS is a C++ implementation of the RTPS (Real Time Publish
Subscribe) protocol, which provides publisher-subscriber communications over
unreliable transports such as UDP, as defined and maintained by the Object
Management Group (OMG) consortium. RTPS is also the wire interoperability
protocol defined for the Data Distribution Service (DDS) standard, again by
the OMG. eProsima Fast RTPS holds the benefit of being standalone and
up-to-date, as most vendor solutions either implement RTPS as a tool to
implement DDS or use past versions of the specification.

%package devel
Summary: Development files and libraries for Fast-RTPS
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%summary.

%prep
%setup -q -n %{name}-%{commit0}
%patch0 -p0 -b .fedora
%patch1 -p0 -b .asio
%patch2 -p0 -b .el7

%build
mkdir build; pushd build;
%cmake ..
popd
make %{?_smp_mflags} -C build


%install
%make_install -C build
mv %{buildroot}/usr/examples %{buildroot}%{_datadir}/fastrtps

%files
%license LICENSE
%{_libdir}/*.so
%dir %{_datadir}/fastrtps
%{_datadir}/fastrtps/LICENSE

%files devel
%{_includedir}/fastrtps
%{_libdir}/fastrtps
%{_datadir}/fastrtps/examples

%changelog
* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 1.4.0-2
- Fix CMake issue on el7
- Add dependencies on asio-devel and tinyxml2-devel

* Fri Jun 09 2017 Rich Mattes <richmattes@gmail.com> - 1.4.0-1
- Initial pakage
