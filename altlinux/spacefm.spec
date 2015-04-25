#
# spec file for package spacemanfm
#
%define gitrev .git869ce6c
Name: spacefm
Summary: A fast, lightweight, feature-rich, multi-panel, tabbed file manager
Summary(ru_RU.UTF-8): Легкий и быстрый файл-менеджер (форк pcmanfm 0.5)
Version: 1.0.0
Release: alt0%gitrev
License: GPL-3.0+
Group: File tools
Url: https://github.com/IgnorantGuru/spacefm
Source0: %name-%version.tar

BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: intltool
BuildRequires: pkgconfig
BuildRequires: libgtk+2-devel
BuildRequires: desktop-file-utils
BuildRequires: fdupes
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: xz
BuildRequires: libffmpegthumbnailer-devel

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libudev) >= 143
Requires:       desktop-file-utils
Requires:       shared-mime-info
# Mount without root requirement.
Requires:     udisks2
# Plugin download.
Requires:     wget
# Execution of SpaceFM and applications from root.
Requires:     xdg-utils
#if #{with gtk2}
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.18.0
#else
#BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
#endif

%description
A fast and lightweight, but extremly powerful, multi-paned, tabbed file manager originally forked from the 0.5 series pcmanfm as pcmanfm-mod.

%description -l ru_RU.UTF-8
SpaceFM — быстрый, лёгкий и расширяемый плагинами C (си) / GTK+ графический файловый менеджер (File Manager).

%prep
%setup

%build
%autoreconf
%configure --enable-pixmaps  --with-gtk2 \
  --with-preferable-sudo=%_bindir/xdg-su

%make

%install
%makeinstall_std
%find_lang %name

%files lang -f %name.lang
%dir %_datadir/%name
%dir %_datadir/%name/ui
%dir %_datadir/doc/%name
%_bindir/%name
%_bindir/spacefm-auth
%_datadir/%name/ui/*.ui
%_datadir/doc/%name/spacefm-manual-en.html
%_datadir/applications/*.desktop
%_datadir/pixmaps
%_datadir/mime/packages/spacefm-mime.xml
%_bindir/spacefm-auth

%changelog
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
