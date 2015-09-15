Name:           ros-jade-nerian-sp1
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS nerian_sp1 package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/nerian_sp1
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL-devel
Requires:       boost-devel
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
BuildRequires:  SDL-devel
BuildRequires:  boost-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs

%description
Node for the SP1 Stereo Vision System by Nerian Vision Technologies

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
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

