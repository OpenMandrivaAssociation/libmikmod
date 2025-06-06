%define major 3
%define libname %mklibname mikmod %{major}
%define devname %mklibname mikmod -d

Summary:	Sound library supporting multiple module formats and digital sound files
Name:		libmikmod
Version:	3.3.13
Release:	1
License:	LGPLv2+
Group:		Sound
Url:		https://mikmod.raphnet.net/
Source0:	http://sourceforge.net/projects/mikmod/files/libmikmod/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(alsa)

%description
Libmikmod is a portable sound library, capable of playing samples as
well as module files, originally written by Jean-Paul Mikkers (MikMak)
for DOS. It has subsequently been hacked by many hands and now runs on
many Unix flavours.

It uses the OSS /dev/dsp driver including in all recent kernels for
output, as well as ALSA and EsounD, and will also write wav files.

Supported file formats include 669, AMF, APUN, DSM, FAR, GDM, IT, IMF,MOD,
MED, MTM, OKT, S3M, STM, STX, ULT, UNI and XM.
Full source included, use of this library for music/sound effects in
your own programs is encouraged !

%package -n	%{libname}
Summary:	Sound library supporting multiple module formats and digital sound files
Group:		Sound

%description -n %{libname}
Libmikmod is a portable sound library, capable of playing samples as
well as module files, originally written by Jean-Paul Mikkers (MikMak)
for DOS. It has subsequently been hacked by many hands and now runs on
many Unix flavours.

It uses the OSS /dev/dsp driver including in all recent kernels for
output, as well as ALSA and EsounD, and will also write wav files.

Supported file formats include 669, AMF, APUN, DSM, FAR, GDM, IT, IMF,MOD,
MED, MTM, OKT, S3M, STM, STX, ULT, UNI and XM.
Full source included, use of this library for music/sound effects in
your own programs is encouraged !

%package -n	%{devname}
Summary:	Development related files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Install the limikmod-devel package if you want to develop applications that
will use the limikmod library.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--disable-altivec \
	--enable-alsa

%make_build

%install
%make_install

chmod 755 %{buildroot}%{_libdir}/lib*.so.%{major}*

%files -n %{libname}
%doc AUTHORS
%{_libdir}/libmikmod.so.%{major}*

%files -n %{devname}
%doc NEWS README TODO
%{_bindir}/libmikmod-config
%{_libdir}/pkgconfig/libmikmod.pc
%{_libdir}/*.so
%{_datadir}/aclocal/*
%{_includedir}/*
%{_mandir}/man1/*
%{_infodir}/*
