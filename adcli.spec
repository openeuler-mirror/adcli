Name:      adcli
Version:   0.9.0
Release:   1
Summary:   A helper library and tools for Active Directory client operations
Group:     Development/Libraries
License:   LGPLv2+
URL:       http://cgit.freedesktop.org/realmd/adcli
Source0:   https://gitlab.freedesktop.org/realmd/adcli/uploads/02d8757266c24fdc10822306582287bf/adcli-%{version}.tar.gz

Patch0:    0001-man-move-note-to-the-right-section.patch
Patch1:    0002-tools-add-show-computer-command.patch
Patch2:    0003-add-description-option-to-join-and-update.patch
Patch3:    0004-Use-GSS-SPNEGO-if-available.patch
Patch4:    0005-add-option-use-ldaps.patch
Patch5:    0006-discovery-fix.patch
Patch6:    0007-delete-do-not-exit-if-keytab-cannot-be-read.patch
Patch7:    0008-tools-disable-SSSD-s-locator-plugin.patch

BuildRequires:	gcc intltool pkgconfig libtool gettext-devel krb5-devel
BuildRequires:	openldap-devel libxslt xmlto git

Requires:   cyrus-sasl-gssapi
Obsoletes:  adcli-devel < 0.5

%description
Library of routines for joining a machine to Active Directory (without samba)
and managing machine accounts there. Will probably expand to cover other
AD related tasks as well.

%package help
Summary:   Documents for %{name}
Buildarch: noarch
Requires:  man info
Provides:  %{name}-doc = %{version}-%{release}
Obsoletes: %{name}-doc < %{version}-%{release}

%description help
Man page and other related documents for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1 -Sgit

%build
autoreconf -f -i -v
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%check
make check

%pre

%preun

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%license COPYING AUTHORS
%doc ChangeLog
%{_sbindir}/adcli

%files help
%defattr(-,root,root)
%doc NEWS README
%doc %{_datadir}/*
%doc %{_mandir}/man8/*

%changelog
* Wed Aug 26 2020 wangchen <wangchen137@huawei.com> - 0.9.0-1
- update to 0.9.0

* Wed Oct 9 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.8.2-6
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: change the directory of AUTHORS

* Fri Sep 27 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.8.2-5
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:move the license

* Tue Sep 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.8.2-4
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: revise spec file with new rules

* Mon Aug 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.8.2-3
- Package init
