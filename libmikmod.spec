%define	major 3
%define	libname %mklibname mikmod %{major}
%define develname %mklibname mikmod -d
%define prerel beta2

Summary:	Sound library supporting multiple module formats and digital sound files
Name:		libmikmod
Version:	3.2.0
Release:	%mkrel 0.%prerel.7
License:	LGPLv2+
Group:		Sound
URL:		http://mikmod.raphnet.net/
Source0:	http://mikmod.raphnet.net/files/%{name}-%version-%prerel.tar.gz
Patch0:		libmikmod-3.1.10-dspbusy-nonblock.patch
Patch1:		libmikmod-3.1.10-lib64.patch
Patch2:		libmikmod-64bit.patch
Patch3:		libmikmod-3.1.11-rawwriter-path.patch
Patch5:		libmikmod-3.2.0-beta2-new-alsa-fix.patch
Patch7:		libmikmod-sprintf.patch
#gw dlopen libesd.so.0 instead of libesd.so
Patch8:         libmikmod-3.1.11-esd-driver.patch
# (fc) 3.2.0-0.beta2.2mdv fix aclocal warning
Patch9:		libmikmod-underquoted.patch
Patch10:	libmikmod-CVE-2007-6720.patch
Patch11:	libmikmod-CVE-2009-0179.patch
Patch12:	libmikmod_lm.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	automake1.8
BuildRequires:	esound-devel
BuildRequires:	texinfo
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Development related files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname mikmod 2 -d}

%description -n	%{develname}
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

%setup -q -n %{name}-%version-%prerel
%patch0 -p0 -b .dsp_nonblock
%patch1 -p1 -b .lib64
%patch2 -p1 -b .64bit-fixes
%patch3 -p1 -b .rawwriter_path
%patch5 -p1 -b .alsa
%patch7 -p1 -b .sprintf
%patch8 -p1 -b .esd
%patch9 -p1 -b .underquoted
%patch10 -p1 -b .CVE-2007-6720
%patch11 -p1 -b .CVE-2009-0179
%patch12 -p1 -b -lm

libtoolize --copy --force
autoreconf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall

chmod 755 %{buildroot}%{_libdir}/lib*.so.%{major}*

%multiarch_binaries %{buildroot}%{_bindir}/libmikmod-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post -n %{develname}
%_install_info mikmod.info

%preun -n %{develname}
%_remove_install_info mikmod.info

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING.LESSER COPYING.LIB
%{_libdir}/libmikmod.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc INSTALL NEWS README TODO
%{_bindir}/libmikmod-config
%multiarch %{multiarch_bindir}/libmikmod-config
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/aclocal/*
%{_includedir}/*
%{_mandir}/man1/*
%{_infodir}/*
