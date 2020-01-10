Name: hunspell-tn
Summary: Tswana hunspell dictionaries
%define upstreamid 20091101
Version: 0.%{upstreamid}
Release: 6%{?dist}
Source: http://releases.mozilla.org/pub/mozilla.org/addons/46617/tswana__south_africa__dictionary-%{upstreamid}-fx+tb.xpi
Group: Applications/Text
URL: http://www.translate.org.za/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Tswana hunspell dictionaries.

%prep
%setup -q -c -n hunspell-tn

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/tn-ZA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/tn_ZA.aff
cp -p dictionaries/tn-ZA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/tn_ZA.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
tn_ZA_aliases="tn_BW"
for lang in $tn_ZA_aliases; do
        ln -s tn_ZA.aff $lang.aff
        ln -s tn_ZA.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README-tn-ZA.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20091101-6
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 Caolán McNamara <caolanm@redhat.com> - 0.20091101-1
- latest version

* Wed Jan 06 2010 Caolán McNamara <caolanm@redhat.com> - 0.20060123-5
- README says was derived from GPL work -> GPL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060123-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060123-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 30 2008 Caolán McNamara <caolanm@redhat.com> - 0.20060123-2
- add Botswana alias

* Tue Sep 09 2008 Caolán McNamara <caolanm@redhat.com> - 0.20060123-1
- initial version
