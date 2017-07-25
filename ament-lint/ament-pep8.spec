%global gittag release-beta1
%global reponame ament_lint
%global pkgname pep8
%global pkgnameu pep8
%global subpackage ament_%{pkgnameu}
%global __python %{__python3}

Name:		ament-%{pkgname}
Version:	0.0.0
Release:	0.1.beta1%{?dist}
Summary:	PEP8 checking for ament
BuildArch:	noarch

License:	ASL 2.0
URL:		https://ros2.org
Source0:	https://github.com/ament/%{reponame}/archive/%{gittag}/%{reponame}-%{version}.tar.gz

%if 0%{?rhel}
BuildRequires:	cmake3
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools
Requires:	python34-pep8
%else
BuildRequires:	cmake
BuildRequires:  python3-devel
Requires:	python3-pep8
%endif


%description
%{summary}.

%prep
%autosetup -n %{reponame}-%{gittag}

%build
pushd %{subpackage}
%{py3_build}
popd

%install
pushd %{subpackage}
%py3_install
popd

#%check
#pushd %{subpackage}/build
#%{__python3} setup.py test

%files
%license LICENSE
%{python3_sitelib}/%{subpackage}*
%{_bindir}/%{subpackage}

%changelog
* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 0.0.0-0.1.beta1
- Initial Package
