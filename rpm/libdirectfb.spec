Name:          libdirectfb
Summary:       Direct framebuffer is a small scale graphics library
Version:       1.7.4
Release:       1
Group:         Development/Libraries
License:       LGPLv2.1
URL:           http://directfb.org/
Source0:       %{name}-%{version}.tar.gz
Source1:       directfbrc
Patch0:        0001-fbdev-use-configured-pixel-format-if-possible.patch
BuildRequires: fluxcomp


%description
%{summary}

%package -n directfb-tools
Summary:    Tools for testing and configuring Direct FB libraries
Group:      Development/Tools
Requires:   libdirectfb

%description -n directfb-tools
%{summary}

%package devel
Summary:    Direct framebuffer development headers
Group:      Development/Libraries
Requires:   libdirectfb

%description devel
%{summary}

%package -n directfb-doc
Summary:    Direct framebuffer man pages
Group:      Development/Libraries

%description -n directfb-doc
%{summary}

%prep
%setup -q -n %{name}-%{version}

pushd %{name}
# 0001-fbdev-use-configured-pixel-format-if-possible.patch
%patch0 -p1

popd

%build
pushd %{name}
%autogen CFLAGS=-Os --disable-static --disable-divine \
	--enable-zlib --disable-x11 --disable-vnc --disable-osx \
	--disable-multi --enable-idirectfbgl-egl \
	--enable-fbdev --enable-egl --with-gfxdrivers=gles2 \
	--disable-x11vdpau --disable-mesa --disable-multi-kernel \
	--with-timidity=no --disable-fusionsound \
	--enable-pvr2d=no --enable-wayland=no --enable-webp=no \
	--enable-jpeg=no --enable-zlib=no --enable-png=yes \
	--enable-gif=no --enable-tiff=no  --enable-pnm=no \
	--enable-mpeg2=no --enable-bmp=no --enable-jpeg2000=no \
	--enable-video4linux=no \
	--with-timidity=no --with-vorbis=no \
	--disable-egl --disable-egl-united  \
	--with-gfxdrivers=gles2 \
	--with-inputdrivers=linuxinput \
	--enable-freetype=no --with-mad=no --with-cdda=no --with-smooth-scaling=no
#./sailfish-configure.sh
make %{?jobs:-j%jobs}
popd

%install
rm -rf %{buildroot}

install -D -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/directfbrc

pushd %{name}
%make_install
popd

%post -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/lib*
%{_libdir}/directfb*
%{_datadir}/directfb*
%{_sysconfdir}/directfbrc

%files -n directfb-tools
%defattr(-,root,root,-)
%{_bindir}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*


%files -n directfb-doc
%defattr(-,root,root,-)
%{_datadir}/man/man1/*
%{_datadir}/man/man5/*



