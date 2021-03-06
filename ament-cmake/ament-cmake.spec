%global gittag release-beta2
%global reponame ament_cmake
%global subpackage ament_cmake
%global __python %{__python3}

Name:		ament-cmake
Version:	0.0.0
Release:	0.1.beta1%{?dist}
Summary:	@DESC@
BuildArch:	noarch

License:	ASL 2.0
URL:		https://ros2.org
Source0:	https://github.com/ament/%{reponame}/archive/%{gittag}/%{reponame}-%{version}.tar.gz

%if 0%{?rhel}
BuildRequires:	cmake3
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools
%else
BuildRequires:	cmake
BuildRequires:  python3-devel
%endif

BuildRequires:	ament-cmake-core
BuildRequires:	ament-cmake-export-dependencies

%if 0%{?rhel}
Requires:	cmake3
%else
Requires:	cmake
%endif
Requires:	ament-cmake-core
Requires:	ament-cmake-export-definitions
Requires:	ament-cmake-export-dependencies
Requires:	ament-cmake-export-include-directories
Requires:	ament-cmake-export-interfaces
Requires:	ament-cmake-export-libraries
Requires:	ament-cmake-export-link-flags
Requires:	ament-cmake-libraries
Requires:	ament-cmake-python
Requires:	ament-cmake-target-dependencies
Requires:	ament-cmake-test


%description
%{summary}.

%prep
%autosetup -n %{reponame}-%{gittag}

%build
mkdir %{subpackage}/build
pushd %{subpackage}/build
%if 0%{?rhel}
%cmake3 ..
%else
%cmake ..
%endif
popd

%install
%make_install -C %{subpackage}/build

#%check
#pushd %{subpackage}/build
#make check

%files
%license LICENSE
%{_datadir}/%{subpackage}
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{subpackage}
%{_datadir}/ament_index/resource_index/packages/%{subpackage}
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{subpackage}


%changelog
* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 0.0.0-0.1.beta1
- Initial Package
