#
# spec file for package spacemanfm
#

Name: spacefm
Version: 1.0.4
Release: alt0.1

Summary: A fast, lightweight, feature-rich, multi-panel, tabbed file manager
Summary(ru_RU.UTF-8): Легкий и быстрый файл-менеджер (форк pcmanfm 0.5)
License: GPL-3.0+
Group: File tools
Url: https://github.com/IgnorantGuru/spacefm

Source0: %name-%version.tar.xz

Requires: desktop-file-utils gksu shared-mime-info wget xterm

# Automatically added by buildreq on Sat Apr 25 2015
BuildRequires: intltool libffmpegthumbnailer-devel libgtk+2-devel libstartup-notification-devel libudev-devel

%description
A fast and lightweight, but extremly powerful, multi-paned, tabbed file manager originally forked from the 0.5 series pcmanfm as pcmanfm-mod.

%description -l ru_RU.UTF-8
SpaceFM — быстрый, лёгкий и расширяемый плагинами C (си) / GTK+ графический файловый менеджер (File Manager).

%prep
%setup

%build
%autoreconf
%configure --with-gtk2 \
           --enable-pixmaps \
           --with-preferable-sudo=%_bindir/gksu

%make

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%dir %_datadir/%name
%dir %_datadir/%name/ui
%dir %_datadir/doc/%name
%_bindir/*
%_datadir/%name/ui/*.ui
%_datadir/doc/%name/spacefm-manual-en.html
%_datadir/applications/*.desktop
%_datadir/pixmaps/*
%_datadir/mime/packages/spacefm-mime.xml

%changelog
* Sun Oct 18 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.0.4-alt0.1
- 1.0.4

* Sun Apr 26 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.0.0-alt0.M70T.1
- draft build for AltLinux

* Tue Mar 19 2013 mournblade@gmx.us
- 0.8.7 Upstream Release
* Tue Mar 12 2013 mournblade@gmx.us
- 0.8.6 Upstream Release
* Fri Sep 14 2012 mournblade@gmx.us
- 0.7.11 Upstream Release
* Mon Aug 13 2012 mournblade@gmx.us
- 0.7.10 Upstream Release
* Sat Apr 14 2012 mournblade@gmx.us
- 0.7.5 Upstream Release
* Tue Apr  3 2012 mournblade@gmx.us
- 0.7.4 Upstream Release
* Mon Mar 26 2012 mournblade@gmx.us
- Initial Package Release
