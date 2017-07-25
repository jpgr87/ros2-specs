%global gittag release-beta2
%global pkgname ament_lint
%global __python %{__python3}
%if 0%{?rhel}
%global cmake_cmd %cmake3
%else
%global cmake_cmd %cmake
%endif
%global pypkgs ament_cppcheck ament_pep8

Name:		ament-lint
Version:	0.0.0
Release:	0.2.beta2%{?dist}
Summary:	Linting tools for the ament buildsystem
BuildArch:	noarch

License:	ASL 2.0
URL:		https://ros2.org
Source0:	https://github.com/ament/%{pkgname}/archive/%{gittag}/%{pkgname}-%{gittag}.tar.gz

%if 0%{?rhel}
BuildRequires:	cmake3
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools
%else
BuildRequires:	cmake
BuildRequires:  python3-devel
%endif

%description
%{summary}.

%package -n ament-cppcheck
Summary: cppcheck support for ament
Requires:	cppcheck

%description -n ament-cppcheck
%{summary}.

%package -n ament-pep8
Summary: PEP8 checking for ament
%if 0%{?rhel}
Requires: python34-pep8
%else
Requires: python3-pep8
%endif

%description -n ament-pep8
%{summary}

%prep
%autosetup -n %{pkgname}-%{gittag}

%build
for PYPKG in %{pypkgs}
do
  pushd $PYPKG
  %{py3_build}
  popd
done

%install
for PYPKG in %{pypkgs}
do
  pushd $PYPKG
  %py3_install
  popd
done

#%check
#pushd %{subpackage}
#%{__python3} setup.py test

%files
%license LICENSE

%files -n ament-cppcheck
%{python3_sitelib}/ament_cppcheck*
%{_bindir}/ament_cppcheck

%files -n ament-pep8
%{python3_sitelib}/ament_pep8*
%{_bindir}/ament_pep8

%changelog
* Mon Jul 24 2017 Rich Mattes <richmattes@gmail.com> - 0.0.0-0.2.beta2
- Update to beta2
