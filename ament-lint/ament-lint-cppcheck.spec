%global gittag release-beta1
%global reponame ament_lint
%global __python %{__python3}

Name:		ament-lint-cppcheck
Version:	0.0.0
Release:	0.1.beta1%{?dist}
Summary:	cppcheck support for ament
BuildArch:	noarch

License:	ASL 2.0
URL:		https://ros2.org
Source0:	https://github.com/ament/%{reponame}/archive/%{gittag}/%{reponame}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ament-package
BuildRequires:	python3

%description
The CMake API for ament_cppcheck to perform static code analysis on C/C++
code using Cppcheck.

%prep
%autosetup -n %{reponame}-%{gittag}

%build
mkdir ament_cmake_core/build
pushd ament_cmake_core/build
%cmake ..
popd

%install
%make_install -C ament_cmake_core/build

#%check
#pushd ament_cmake_core/build
#make test

%files
%license LICENSE
%{_datadir}/ament_cmake_core
%{_datadir}/ament_index

%changelog
* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 0.0.0-0.1.beta1
- Initial Package
