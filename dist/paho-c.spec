Summary:            MQTT C Client
Name:               paho-c
Version:            1.2.0
Release:            9%{?dist}
License:            BSD and EPL
Source:             https://github.com/eclipse/paho.mqtt.c/archive/v%{version}.tar.gz
URL:                https://eclipse.org/paho/clients/c/
BuildRequires:      cmake
BuildRequires:      gcc
BuildRequires:      graphviz
BuildRequires:      doxygen
BuildRequires:      openssl-devel


%description
The Paho MQTT C Client is a fully fledged MQTT client written in C.


%package devel
Summary:            MQTT C Client development kit
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and samples for the the Paho MQTT C Client.


%package devel-doc
Summary:            MQTT C Client development kit documentation
BuildArch:          noarch

%description devel-doc
Development documentation files for the the Paho MQTT C Client.

%prep
%autosetup -n paho-c-%{version}

%build
mkdir build.paho && cd build.paho
%cmake -DPAHO_WITH_SSL=TRUE -DPAHO_BUILD_DOCUMENTATION=TRUE -DPAHO_BUILD_SAMPLES=TRUE ..
%make_build

%install
cd build.paho
%make_install

%files
%license edl-v10 epl-v10
%{_bindir}/paho*
%{_libdir}/*.so.*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%{_bindir}/MQTT*
%{_includedir}/*
%{_libdir}/*.so

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

%files devel-doc
%license edl-v10 epl-v10
%{_defaultdocdir}/*

%changelog
* Thu Oct 19 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-9
- Reduce description size to less than 80 characters
- Install the Paho client/servers tools in the binary package
- Install the binary examples in the development package only

* Sat Aug 12 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-8
- Added missing ldconfig on the postun section

* Sat Aug 12 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-7
- Replaced build and install commands with respective macros
- Added license to the devel docs packages
- Removed explicit require on OpenSSL
- Move the shared library symlinks to the devel package

* Mon Jul 31 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-6
- Fixed short description of the project license

* Sun Jul 30 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-5
- Renamed the documentation package to -doc

* Sun Jul 30 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-4
- Removed Group tag as required by packaging guidelines
- Prevent the devel package from being used with incompatible versions
- Replaced the doc tag with the license tag

* Thu Jul 27 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-4
- Enabled generation of debuginfo package

* Thu Jul 27 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-3
- Fixed changelog issues pointed by rpmlint

* Thu Jul 27 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-2
- Updated changelog to comply with Fedora packaging guidelines

* Wed Jul 26 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-1
- Fixed rpmlint warnings: replaced cmake call with builtin macro
- Fixed rpmlint warnings: removed buildroot reference from build section

* Fri Jun 30 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0
- Updated package to version 1.2.0

* Sat Dec 31 2016 Otavio R. Piske <opiske@redhat.com> - 1.1.0
- Initial packaging
