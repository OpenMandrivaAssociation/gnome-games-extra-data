%define name gnome-games-extra-data
%define version 2.26.0
%define release %mkrel 2

Summary: Extra data files for the GNOME games
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPL
Group: Games/Other
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: gnome-games >= 2.19.1
BuildArch: noarch

%description
This contains extra data files such as more artwork for the GNOME games.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%_datadir/gnome-games/glines/pixmaps/*
%_datadir/gnome-games/gnobots2/pixmaps/*
%_datadir/gnome-games/gnometris/pixmaps/*
%_datadir/gnome-games/iagno/pixmaps/*
%_datadir/gnome-games/mahjongg/pixmaps/*
%_datadir/gnome-games-common/cards/*
%_datadir/gnome-games/same-gnome/themes/2.10/*

