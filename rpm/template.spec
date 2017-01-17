Name:           ros-indigo-nerian-sp1
Version:        1.5.0
Release:        1%{?dist}
Summary:        ROS nerian_sp1 package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/nerian_sp1
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL-devel
Requires:       boost-devel
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  SDL-devel
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
Node for the SP1 Stereo Vision System by Nerian Vision Technologies

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jan 17 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.5.0-1
- Autogenerated by Bloom

* Tue Jan 17 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.5.0-0
- Autogenerated by Bloom

* Tue May 17 2016 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.3.3-0
- Autogenerated by Bloom

* Thu May 05 2016 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.3.1-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.3.0-0
- Autogenerated by Bloom

* Fri Feb 12 2016 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.2.2-0
- Autogenerated by Bloom

* Tue Jan 12 2016 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.2.1-0
- Autogenerated by Bloom

* Mon Nov 23 2015 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.2.0-0
- Autogenerated by Bloom

* Mon Oct 05 2015 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.1.2-0
- Autogenerated by Bloom

* Tue Sep 15 2015 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.1.1-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.1.0-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.0.2-1
- Autogenerated by Bloom

* Tue Aug 25 2015 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.0.2-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.0.1-0
- Autogenerated by Bloom

* Mon Aug 24 2015 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.0.0-0
- Autogenerated by Bloom

