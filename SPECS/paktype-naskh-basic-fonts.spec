%global priority 65-0
%global fontname paktype-naskh-basic
%global fontconf %{priority}-%{fontname}

Name:		%{fontname}-fonts
Version:	5.0
Release:	6%{?dist}
Summary:	Fonts for Arabic, Farsi, Urdu and Sindhi from PakType
License:	GPLv2 with exceptions
URL:		https://sourceforge.net/projects/paktype/
Source0:	https://sourceforge.net/projects/paktype/files/PakType-Release-2019-03-11.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:		fontpackages-filesystem

%description
The paktype-naskh-basic-fonts package contains fonts for the display of \
Arabic, Farsi, Urdu and Sindhi from PakType by Lateef Sagar.

%prep
%setup -q -c
rm -rf Code

# get rid of the white space (' ')
mv License\ files/PakType\ Naskh\ Basic\ License.txt  PakType_Naskh_Basic_License.txt
mv Features/PakType\ Naskh\ Basic\ Features.pdf PakTypeNaskhBasicFeatures.pdf

%{__sed} -i 's/\r//' PakType_Naskh_Basic_License.txt
chmod a-x PakType_Naskh_Basic_License.txt PakTypeNaskhBasicFeatures.pdf


%build
echo "Nothing to do in Build."

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakTypeNaskhBasic.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf

%_font_pkg -f %{fontconf}.conf PakTypeNaskhBasic.ttf
%ghost %attr(644, root, root) %{_fontdir}/.uuid

%doc PakType_Naskh_Basic_License.txt PakTypeNaskhBasicFeatures.pdf

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 5.0-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 5.0-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 5.0-1
- Upstream 5.0 Release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 06 2014 Pravin Satpute <psatpute@redhat.com> - 4.1-3
- Resolves bz:1062128 : Making default font for Urdu language

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Pravin Satpute <psatpute@redhat.com> - 4.1-1
- Upstream 4.1 Release

* Tue Feb 05 2013 Pravin Satpute <psatpute@redhat.com> - 4.0-2
- Upstream changed tarball

* Wed Nov 21 2012 Pravin Satpute <psatpute@redhat.com> - 4.0-1
- Upstream 4.0 release. Now no language specific ttf

* Mon Sep 03 2012 Naveen Kumar <nkumar@redhat.com> - 3.1-1
- Upstream 3.1 release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 21 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-8
- add ur-in, ur-pk & pa-pk locale-specific overrides rule in 67-paktype-naskh-basic.conf
- add ur-in, ur-pk & pa-pk locale-specific overrides rule in 67-paktype-naskh-basic-sa.conf
- resolves bug #586789

* Thu May 6 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-7
- remove binding="same" from all *.conf files

* Fri Mar 12 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-6
- Changes in summary and description

* Fri Mar 12 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-5
- changed the name of package from paktype-nashk-basic to paktype-naskh-basic

* Tue Mar 9 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-4
- removed redundant  BuildRequires from specfile
- removed unnecessary rm/rmdir's from specfile
- Sane updates in docs.

* Fri Mar 5 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-3
- removed all cd's
- changes w.r.t sed in prep section
- added .conf file for PakTypeNaskhBasic.ttf
- files section added for common
- removed space from 67-*-sindhi.conf

* Mon Feb 15 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-2
- Re-packing with updated License information.
- Changes in Spec file with new upstream source.
- Added conf files

* Mon Feb 15 2010 Naveen Kumar <nkumar@redhat.com> - 3.0-1
- Initial packaging for version-3.0


