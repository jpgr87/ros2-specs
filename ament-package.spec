%global gittag release-beta2
%global reponame ament_package
Name:		ament-package
Version:	0.0.0
Release:	0.2.beta2%{?dist}
Summary:	The parser for the manifest files in the ament buildsystem
BuildArch:	noarch

License:	ASL 2.0
URL:		https://ros2.org
Source0:	https://github.com/ament/%{reponame}/archive/%{gittag}/%{name}-%{version}-%{gittag}.tar.gz

%if 0%{?rhel}
BuildRequires:	python34-devel
BuildRequires:	python34-mock
BuildRequires:	python34-setuptools
%else
BuildRequires:	python3-devel
BuildRequires:  python3-mock
%endif

%description
%{summary}

%prep
%autosetup -n %{reponame}-%{gittag}

%build
%py3_build

#%check
#%{__python3} setup.py test

%install
%py3_install

%files
%license LICENSE
%doc CONTRIBUTING.md
%{python3_sitelib}/%{reponame}
%{python3_sitelib}/%{reponame}-*


%changelog
* Mon Jul 24 2017 Rich Mattes <richmattes@gmail.com> - 0.0.0-0.2.beta2
- Update to beta2

* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 0.0.0-0.1.beta1
- Initial Package
