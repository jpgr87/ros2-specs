%global gittag release-beta1
%global reponame ament_cmake
%global pkgname core
%global pkgnameu core
%global subpackage ament_cmake_%{pkgnameu}
%global __python %{__python3}

Name:		ament-cmake-%{pkgname}
Version:	0.0.0
Release:	0.1.beta1%{?dist}
Summary:	The core of the ament buildsystem in CMake
BuildArch:	noarch

License:	ASL 2.0
URL:		https://ros2.org
Source0:	https://github.com/ament/%{reponame}/archive/%{gittag}/%{reponame}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ament-package
BuildRequires:	python3

Requires:	ament-package

%description
The core of the ament buildsystem in CMake.

Several subcomponents provide specific funtionalities:
    * environment: provide prefix-level setup files
    * environment_hooks: provide package-level setup files and environment hooks
    * index: store information in an index and retrieve them without crawling
    * package_templates: templates from the ament_package Python package
    * symlink_install: use symlinks for CMake install commands

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
#pushd ament_cmake_core/build
#make test

%files
%license LICENSE
%{_datadir}/%{subpackage}
# This package owns ament_index; other packages drop their files there
%{_datadir}/ament_index

%changelog
* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 0.0.0-0.1.beta1
- Initial Package
