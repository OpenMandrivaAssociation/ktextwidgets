%define major 5
%define libname %mklibname KF5TextWidgets %{major}
%define devname %mklibname KF5TextWidgets -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: ktextwidgets
Version:	5.81.0
Release:	2
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
BuildRequires: cmake(Qt5UiPlugin)
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
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant.

%package designer
Summary: Qt Designer plugin for handling %{name} widgets
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description designer
Qt Designer plugin for handling %{name} widgets

%files designer
%{_libdir}/qt5/plugins/designer/*.so

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}

%files -f %{name}%{major}.lang

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/cmake/KF5TextWidgets

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
