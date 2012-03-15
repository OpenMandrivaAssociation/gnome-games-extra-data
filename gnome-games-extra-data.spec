Summary: Extra data files for the GNOME games
Name: gnome-games-extra-data
Version: 3.2.0
Release: 1
License: GPL
Group: Games/Other
Url: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildArch: noarch

Requires: gnome-games >= %{version}

%description
This contains extra data files such as more artwork for the GNOME games.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-games/glines/pixmaps/*
%{_datadir}/gnome-games/gnobots2/themes/*.png
%{_datadir}/gnome-games/iagno/pixmaps/*
%{_datadir}/gnome-games/mahjongg/pixmaps/*

