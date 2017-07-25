%global gittag release-beta2
%global pkgname ament_cmake
%global subpkglist core test libraries export_definitions export_dependencies export_include_directories export_interfaces export_link_flags export_libraries gmock gtest include_directories nose python target_dependencies
%if 0%{?rhel}
%global cmake_cmd %cmake3
%else
%global cmake_cmd %cmake
%endif
%global __python %{__python3}

Name:           ament-cmake
Version:        0.0.0
Release:        0.2.beta2%{?dist}
Summary:        CMake support for ament
BuildArch:      noarch

License:        ASL 2.0
URL:            https://github.com/ament/ament_cmake
Source0:        https://github.com/ament/%{pkgname}/archive/%{gittag}/%{name}-%{gittag}.tar.gz

%if 0%{?rhel}
BuildRequires:  cmake3
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools
%else
BuildRequires:  cmake
BuildRequires:  python3-devel
%endif

%if 0%{?rhel}
Requires:       cmake3
%else
Requires:       cmake
%endif
Requires:       ament-cmake-core
Requires:       ament-cmake-export-definitions
Requires:       ament-cmake-export-dependencies
Requires:       ament-cmake-export-include-directories
Requires:       ament-cmake-export-interfaces
Requires:       ament-cmake-export-libraries
Requires:       ament-cmake-export-link-flags
Requires:       ament-cmake-libraries
Requires:       ament-cmake-python
Requires:       ament-cmake-target-dependencies
Requires:       ament-cmake-test

%description
The entry point package for the ament buildsystem in CMake.

%package -n %{name}-core
Summary: The core of the ament buildsystem in CMake

BuildRequires:  ament-package
Requires:       ament-package

%package -n %{name}-auto
Summary: Auto-magic functions for ease to use of the ament buildsystem in CMake
Requires: %{name}

%description -n %{name}-auto
%{summary}.


%description -n %{name}-core
The core of the ament buildsystem in CMake.

Several subcomponents provide specific funtionalities:
    * environment: provide prefix-level setup files
    * environment_hooks: provide package-level setup files and environment hooks
    * index: store information in an index and retrieve them without crawling
    * package_templates: templates from the ament_package Python package
    * symlink_install: use symlinks for CMake install commands

%package -n %{name}-export-definitions
Summary: Export definitions to downstream packages in the ament buildsystem
Requires: %{name}-core

%description -n %{name}-export-definitions
%{summary}.

%package -n %{name}-export-dependencies
Summary:  Export dependencies to downstream packages in the ament buildsystem in CMake
Requires: %{name}-core
Requires: %{name}-libraries

%description -n %{name}-export-dependencies
%{summary}.

%package -n %{name}-export-include-directories
Summary:  Export include directories to downstream packages in the ament buildsystem in CMake
Requires: %{name}-core

%description -n %{name}-export-include-directories
%{summary}.

%package -n %{name}-export-interfaces
Summary:  Export interfaces to downstream packages in the ament buildsystem in CMake
Requires: %{name}-core

%description -n %{name}-export-interfaces
%{summary}.

%package -n %{name}-export-libraries
Summary:  Export libraries to downstream packages in the ament buildsystem in CMake
Requires: %{name}-core

%description -n %{name}-export-libraries
%{summary}.

%package -n %{name}-export-link-flags
Summary:  Export link flags to downstream packages in the ament buildsystem in CMake
Requires: %{name}-core

%description -n %{name}-export-link-flags
%{summary}.

%package -n %{name}-gmock
Summary:  Add Google mock-based tests in the ament buildsystem in CMake
Requires: %{name}-core
Requires: gmock-devel

%description -n %{name}-gmock
%{summary}.

%package -n %{name}-gtest
Summary:  Add Google test-based tests in the ament buildsystem in CMake
Requires: %{name}-core
Requires: gtest-devel

%description -n %{name}-gtest
%{summary}.

%package -n %{name}-include-directories
Summary: Order include directories according to a chain of prefixes in the ament buildsystem in CMake
Requires: %{name}-core

%description -n %{name}-include-directories
%{summary}.

%package -n %{name}-libraries
Summary: Deduplicate libraries in the ament buildsystem in CMake
Requires: %{name}-core

%description -n %{name}-libraries
%{summary}.

%package -n %{name}-nose
Summary: Add nose-based tests in the ament buildsystem in CMake
Requires: %{name}-core
Requires:       ament-cmake-test
%if 0%{?rhel}
Requires:       python34-nose
%else
Requires:       python3-nose
%endif

%description -n %{name}-nose
%{summary}.

%package -n %{name}-python
Summary: Add the ability to use Python in the ament buildsystem in CMake
Requires: %{name}-core

%description -n %{name}-python
%{summary}.

%package -n %{name}-target-dependencies
Summary: Add definitions, include directories and libraries of a package to a target in the ament buildsystem
Requires: %{name}-core

%description -n %{name}-target-dependencies
%{summary}.

%package -n %{name}-test
Summary: Add tests in ament
Requires: %{name}-core

%description -n %{name}-test
This package provides the ability to add tests in the ament buildsystem in CMake

%prep
%autosetup -n %{pkgname}-%{gittag}

%build
for SUBPKG in %{subpkglist}
do
  mkdir %{pkgname}_$SUBPKG/build
  pushd %{pkgname}_$SUBPKG/build
  %cmake_cmd .. -DCMAKE_PREFIX_PATH=%{buildroot}/%{_datadir}
  %make_install
  popd
done

mkdir %{pkgname}/build
pushd %{pkgname}/build
%cmake_cmd .. -DCMAKE_PREFIX_PATH=%{buildroot}/%{_datadir}
%make_install
popd

mkdir %{pkgname}_auto/build
pushd %{pkgname}_auto/build
%cmake_cmd .. -DCMAKE_PREFIX_PATH=%{buildroot}/%{_datadir}
%make_install
popd

%install
for SUBPKG in %{subpkglist}
do
  %make_install -C %{pkgname}_$SUBPKG/build
done
%make_install -C %{pkgname}/build
%make_install -C %{pkgname}_auto/build

%files
%license LICENSE
%{_datadir}/%{pkgname}
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}
%{_datadir}/ament_index/resource_index/packages/%{pkgname}
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}

%files -n %{name}-auto
%license LICENSE
%{_datadir}/%{pkgname}_auto
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_auto
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_auto
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_auto

%files -n %{name}-core
%license LICENSE
%{_datadir}/%{pkgname}_core
%dir %{_datadir}/ament_index
%dir %{_datadir}/ament_index/resource_index
%dir %{_datadir}/ament_index/resource_index/package_run_dependencies
%dir %{_datadir}/ament_index/resource_index/packages
%dir %{_datadir}/ament_index/resource_index/parent_prefix_path
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_core
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_core
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_core

%files -n %{name}-export-definitions
%license LICENSE
%{_datadir}/%{pkgname}_export_definitions
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_export_definitions
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_export_definitions
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_export_definitions

%files -n %{name}-export-dependencies
%license LICENSE
%{_datadir}/%{pkgname}_export_dependencies
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_export_dependencies
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_export_dependencies
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_export_dependencies

%files -n %{name}-export-include-directories
%license LICENSE
%{_datadir}/%{pkgname}_export_include_directories
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_export_include_directories
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_export_include_directories
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_export_include_directories

%files -n %{name}-export-interfaces
%license LICENSE
%{_datadir}/%{pkgname}_export_interfaces
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_export_interfaces
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_export_interfaces
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_export_interfaces

%files -n %{name}-export-libraries
%license LICENSE
%{_datadir}/%{pkgname}_export_libraries
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_export_libraries
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_export_libraries
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_export_libraries

%files -n %{name}-export-link-flags
%license LICENSE
%{_datadir}/%{pkgname}_export_link_flags
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_export_link_flags
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_export_link_flags
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_export_link_flags

%files -n %{name}-gmock
%license LICENSE
%{_datadir}/%{pkgname}_gmock
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_gmock
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_gmock
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_gmock

%files -n %{name}-gtest
%license LICENSE
%{_datadir}/%{pkgname}_gtest
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_gtest
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_gtest
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_gtest

%files -n %{name}-include-directories
%license LICENSE
%{_datadir}/%{pkgname}_include_directories
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_include_directories
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_include_directories
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_include_directories

%files -n %{name}-libraries
%license LICENSE
%{_datadir}/%{pkgname}_libraries
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_libraries
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_libraries
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_libraries

%files -n %{name}-nose
%license LICENSE
%{_datadir}/%{pkgname}_nose
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_nose
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_nose
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_nose

%files -n %{name}-python
%license LICENSE
%{_datadir}/%{pkgname}_python
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_python
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_python
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_python

%files -n %{name}-target-dependencies
%license LICENSE
%{_datadir}/%{pkgname}_target_dependencies
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_target_dependencies
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_target_dependencies
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_target_dependencies

%files -n %{name}-test
%license LICENSE
%{_datadir}/%{pkgname}_test
%{_datadir}/ament_index/resource_index/package_run_dependencies/%{pkgname}_test
%{_datadir}/ament_index/resource_index/packages/%{pkgname}_test
%{_datadir}/ament_index/resource_index/parent_prefix_path/%{pkgname}_test 

%changelog
* Mon Jul 24 2017 Rich Mattes <richmattes@gmail.com> - 0.0.0-0.2.beta2
- Update to beta2
