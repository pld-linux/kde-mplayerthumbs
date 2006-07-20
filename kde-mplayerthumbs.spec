Summary:	MPlayerThumbs - a thumbnail generator for video files on Konqueror
Summary(pl):	MPlayerThumbs - program generuj±cy miniatury dla plików video w Konquerorze
Name:		kde-mplayerthumbs
Version:	0.5b
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://xoomer.virgilio.it/rockman81/mplayerthumbs-%{version}.tar.bz2
# Source0-md5:	df8aadc2ef9484da8e819e9ddec2e020
URL:		http://www.kde-look.org/content/show.php?content=41180
BuildRequires:	kdebase-devel
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MPlayerThumbs is a thumbnail generator for video files on Konqueror.
Unlike the original konqueror plugin (in my gentoo box is
artsplugin-xine), it DOESN'T depend neither on xine nor arts, instead
it uses only mplayer. You can take advantage of this on x86_64
systems, where you can use a 32bit mplayer to load win32codecs. To
configure the location of your mplayer binary launch
mplayerthumbsconfig. Also it's faster than the xine plugin, since it
can seek and play only a limited number of frames. It catches a random
frame from 15% to 70%, checking also how contrasted is the image, and
dropping bad frames.

%description -l pl
MPlayerThumbs jest programem generuj±cym miniatury dla plików video w
Konquerorze. W przeciwieñstwie do oryginalnej wtyczki, zamiast xine i
arts u¿ywa tylko mplayera. Mo¿na poczuæ korzy¶æ u¿ywaj±c tego na
systemach x86_64, na których mo¿na u¿ywaæ 32-bitowego mplayera wraz z
win32codecs. Aby skonfigurowaæ po³o¿enie mplayera wystarczy za³adowaæ
program mplayerthumbsconfig. Program ten jest tak¿e szybszy ni¿
wtyczka xine, poniewa¿ przeszukiwanie i odgrywanie odbywa siê na
ograniczonej liczbie ramek. MPlayerThumbs pobiera losow± klatkê z 15%
do 70% pliku video, sprawdzaj±c kontrast obrazka i pozbywaj±c siê
niepoprawnych klatek.

%prep
%setup -q -n mplayerthumbs-%{version}

%build
%configure \
	--disable-rpath \
	--with-mplayer=%{_bindir}/mplayer \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang videopreview --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f videopreview.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/mplayerthumbsconfig
%attr(755,root,root) %{_libdir}/kde3/videopreview.so
%{_libdir}/kde3/videopreview.la
%{_datadir}/apps/videothumbnail
%{_datadir}/services/videopreview.desktop
%{_datadir}/config.kcfg/mplayerthumbs.kcfg
