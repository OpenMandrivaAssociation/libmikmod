%define	major	3
%define	libname	%mklibname mikmod %{major}
%define	devname	%mklibname mikmod -d

Summary:	Sound library supporting multiple module formats and digital sound files
Name:		libmikmod
Version:	3.2.0
Release:	3
License:	LGPLv2+
Group:		Sound
URL:		http://mikmod.raphnet.net/
Source0:	http://mikmod.shlomifish.org/files/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(esound)
BuildRequires:	texinfo

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
Obsoletes:	%{mklibname mikmod 2 -d} < 3.2.0-3

%description -n	%{devname}
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
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

chmod 755 %{buildroot}%{_libdir}/lib*.so.%{major}*

%multiarch_binaries %{buildroot}%{_bindir}/libmikmod-config

%files -n %{libname}
%doc AUTHORS
%{_libdir}/libmikmod.so.%{major}*

%files -n %{devname}
%doc NEWS README TODO
%{_bindir}/libmikmod-config
%{multiarch_bindir}/libmikmod-config
%{_libdir}/*.so
%{_datadir}/aclocal/*
%{_includedir}/*
%{_mandir}/man1/*
%{_infodir}/*


%changelog
* Tue Jun 26 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.2.0-1
+ Revision: 806963
- use pkgconfig() deps for buildrequires
- drop useless provides
- drop INSTALL & COPYING* files
- cleanups
- fix info-files-with-install-info-postun
- new version

* Wed May 23 2012 Andrey Bondrov <abondrov@mandriva.org> 3.2.0-0.beta4.3
+ Revision: 800232
- Enable dynamically loaded drivers feature again, try patch from upstream (alsa-dl) to see if it fixes the problem

* Wed May 23 2012 Andrey Bondrov <abondrov@mandriva.org> 3.2.0-0.beta4.2
+ Revision: 800185
- Disable dynamically loaded drivers feature (as it leads to undefined reference issues when building programs that use libmikmod)

* Sat May 12 2012 Götz Waschk <waschk@mandriva.org> 3.2.0-0.beta4.1
+ Revision: 798519
- new prerelease

* Tue Apr 10 2012 Götz Waschk <waschk@mandriva.org> 3.2.0-0.beta3.1
+ Revision: 790221
- remove libtool archives on cooker
- update build deps
- new prerelease
- drop all patches

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-0.beta2.10
+ Revision: 661497
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-0.beta2.8mdv2011.0
+ Revision: 602576
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-0.beta2.7mdv2010.1
+ Revision: 520884
- rebuilt for 2010.1

* Mon Oct 12 2009 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-0.beta2.6mdv2010.0
+ Revision: 456903
- provide a non-empty debug package

* Sun Sep 27 2009 Olivier Blin <blino@mandriva.org> 3.2.0-0.beta2.5mdv2010.0
+ Revision: 449893
- fix build of applications using libmikmod, it is using floor() but
  was never linking against libm, leading to undefined symbol
  (from Arnaud Patard)

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2.0-0.beta2.4mdv2010.0
+ Revision: 425620
- rebuild

* Thu Mar 19 2009 Frederik Himpe <fhimpe@mandriva.org> 3.2.0-0.beta2.3mdv2009.1
+ Revision: 358193
- Add two patches fixing security issues CVE-2007-6720, CVE-2009-0179

* Wed Aug 27 2008 Frederic Crozat <fcrozat@mandriva.com> 3.2.0-0.beta2.2mdv2009.0
+ Revision: 276554
- Patch9: fix aclocal warning

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 3.2.0-0.beta2.1mdv2009.0
+ Revision: 271719
- last version
- new major
- update license
- update patches 2,5
- drop patch 6

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.1.11a-11mdv2009.0
+ Revision: 222928
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 3.1.11a-10mdv2008.1
+ Revision: 178965
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Aug 31 2007 Götz Waschk <waschk@mandriva.org> 3.1.11a-8mdv2008.0
+ Revision: 76949
- fix provides and obsoletes again

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 3.1.11a-7mdv2008.0
+ Revision: 76843
- new devel naming
- reconstruct the autofoo toolchain

