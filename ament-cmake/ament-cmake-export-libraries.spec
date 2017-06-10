%global gittag release-beta1
%global reponame ament_cmake
%global pkgname export-libraries
%global pkgnameu export_libraries
%global subpackage ament_cmake_%{pkgnameu}
%global __python %{__python3}

Name:		ament-cmake-%{pkgname}
Version:	0.0.0
Release:	0.1.beta1%{?dist}
Summary:	Export libraries to downstream packages in the ament buildsystem in CMake
BuildArch:	noarch

License:	ASL 2.0
URL:		https://ros2.org
Source0:	https://github.com/ament/%{reponame}/archive/%{gittag}/%{reponame}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ament-cmake-core
BuildRequires:	python3

Requires:	ament-cmake-core

%description
%{summary}.

%prep
%autosetup -n %{reponame}-%{gittag}

%build
mkdir %{subpackage}/build
pushd %{subpackage}/build
%cmake ..
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
