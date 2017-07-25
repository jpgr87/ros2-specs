%global gittag release-beta1
%global reponame ament_lint
%global pkgname lint-common
%global pkgnameu lint_common
%global subpackage ament_%{pkgnameu}
%global __python %{__python3}

Name:		ament-%{pkgname}
Version:	0.0.0
Release:	0.1.beta1%{?dist}
Summary:	Commonly use linters in ament
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

Requires:	ament-cmake-test
Requires:	ament-cmake-copyright
Requires:	ament-cmake-cppcheck
Requires:	ament-cmake-cpplint
Requires:	ament-cmake-lint-cmake
Requires:	ament-cmake-pep257
Requires:	ament-lint-uncrustify

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