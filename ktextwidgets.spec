%define major 5
%define libname %mklibname KF5TextWidgets %{major}
%define devname %mklibname KF5TextWidgets -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define _disable_lto 1

Name: ktextwidgets
Version:	5.56.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 Text Widgets library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Xml)
#(cb) causes segfaults in gwenview - no one else seems to build with this
#(bero) let's see if that's still the case, would be nice to have a11y
# If it still causes crashes, please note the version in which it did in
# the comment so we know when to test again...
BuildRequires: pkgconfig(Qt5TextToSpeech)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5SonnetUi)
BuildRequires: cmake(KF5IconThemes)
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 Text Widgets library.

%package -n %{libname}
Summary: The KDE Frameworks 5 Text Widgets library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 Text Widgets library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: cmake(KF5Sonnet)
Requires: cmake(KF5SonnetUi)

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_datadir}/kservicetypes5/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/cmake/KF5TextWidgets
