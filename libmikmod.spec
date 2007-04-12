%define	name	libmikmod
%define	version	3.1.11a
%define	release	%mkrel 6

%define	major	2
%define	libname	%mklibname mikmod %{major}

Summary:	Sound library supporting multiple module formats and digital sound files
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://mikmod.raphnet.net/files/%{name}-3.1.11.tar.bz2
Patch0:		libmikmod-3.1.10-dspbusy-nonblock.patch
Patch1:		libmikmod-3.1.10-lib64.patch
Patch2:		libmikmod-3.1.11-a-64bit-fixes.patch
Patch3:		libmikmod-3.1.11-rawwriter-path.patch
Patch5:		libmikmod-3.1.11-new-alsa-fix.patch
Patch6:		libmikmod-3.1.11-a.patch
Patch7:		libmikmod-sprintf.patch
#gw dlopen libesd.so.0 instead of libesd.so
Patch8:         libmikmod-3.1.11-esd-driver.patch
License:	LGPL
Group:		Sound
URL:		http://mikmod.raphnet.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	esound-devel alsa-lib-devel
BuildRequires:	automake1.8 texinfo


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
Obsoletes:	%{name}
Provides:	%{name} = %{version}-%{release}

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

%package -n	%{libname}-devel
Summary:	Development related files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
Libmikmod is a portable sound library, capable of playing samples as
well as module files, originally written by Jean-Paul Mikkers (MikMak)
for DOS. It has subsequently been hacked by many hands and now runs on
many Unix flavours.  

It uses the OSS /dev/dsp driver including in all recent kernels for
output, as well as ALSA and EsounD, and will also write wav files.

Supported file formats include 669, AMF, APUN, DSM, FAR, GDM, IT, IMF,MOD,
MED, MTM, OKT, S3M, STM, STX, ULT, UNI and XM.
Full source included, use of this library for music/sound effects in
your own programs is encouraged!

Install the limikmod-devel package if you want to develop applications that
will use the limikmod library.

%prep
%setup -q -n %{name}-3.1.11
%patch6 -p1 -b .3_1_11a
%patch0 -p0 -b .dsp_nonblock
%patch1 -p1 -b .lib64
%patch2 -p1 -b .64bit-fixes
%patch3 -p1 -b .rawwriter_path
%patch5 -p1 -b .alsa
%patch7 -p1 -b .sprintf
%patch8 -p1 -b .esd
rm -f configure
aclocal-1.8
autoconf
automake-1.8 -a -c

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/libmikmod-config

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname}-devel
#{__install_info} %{_infodir}/mikmod.info.bz2 %{_infodir}/dir --entry="* MikMod: (mikmod).            MikMod Sound Library."
%_install_info mikmod.info

%preun -n %{libname}-devel
#if [ "$1" = 0 ]; then
#{__install_info} --delete %{_infodir}/mikmod.info.bz2 %{_infodir}/dir --entry="* MikMod: (mikmod).            MikMod Sound Library."
#fi
%_remove_install_info mikmod.info

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING.LESSER COPYING.LIB
%{_libdir}/libmikmod.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc INSTALL NEWS README TODO
%{_bindir}/libmikmod-config
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/aclocal/*
%{_includedir}/*
%{_mandir}/man1/*
%{_infodir}/*

%multiarch %{multiarch_bindir}/libmikmod-config


