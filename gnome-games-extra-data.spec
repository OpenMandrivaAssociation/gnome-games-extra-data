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



%changelog
* Thu Mar 15 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.0-1
+ Revision: 785060
- new version 3.2.0
- cleaned up spec

* Wed Dec 07 2011 Götz Waschk <waschk@mandriva.org> 2.30.0-3
+ Revision: 738496
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-2mdv2011.0
+ Revision: 610919
- rebuild

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 529972
- new version
- update file list

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446591
- new version
- update file list

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.26.0-2mdv2010.0
+ Revision: 437766
- rebuild

* Sun Mar 15 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355388
- new version
- update file list

* Sun Aug 31 2008 Funda Wang <fwang@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 277729
- New version 2.24.0

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.22.0-3mdv2009.0
+ Revision: 246407
- rebuild

* Mon Mar 24 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 189794
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description

* Sun Feb 10 2008 Götz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 164805
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89468
- new version

* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 2.19.2-1mdv2008.0
+ Revision: 57355
- new version
- new version
- bump deps

* Wed May 02 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2008.0
+ Revision: 20385
- new version


* Tue Jan 23 2007 Götz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.0
+ Revision: 112231
- Import gnome-games-extra-data

* Tue Jan 23 2007 Götz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
- New version 2.17.90

* Fri Jul 21 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-2mdk
- Rebuild

* Sun Apr 23 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0

* Mon Feb 27 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-3mdk
- Use mkrel

* Wed Oct 19 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-2mdk
- Use correct configure macro

* Fri Oct 07 2005 Götz Waschk <waschk@mandriva.org> 2.12.0-1mdk
- New release 2.12.0

* Thu Apr 21 2005 G�tz Waschk <waschk@mandriva.org> 2.10.0-2mdk
- rebuild

* Thu Apr 21 2005 G�tz Waschk <waschk@mandriva.org> 2.10.0-1mdk
- update file list
- New release 2.10.0

* Wed Nov 10 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- initial package

