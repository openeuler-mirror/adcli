Name:      adcli
Version:   0.9.1
Release:   2
Summary:   A helper library and tools for Active Directory client operations
Group:     Development/Libraries
License:   LGPLv2+
URL:       https://gitlab.freedesktop.org/realmd/adcli
Source0:   https://gitlab.freedesktop.org/sbose/adcli/uploads/30880d967e79cee789194435e70fbf30/adcli-%{version}.tar.gz

Patch0: backport-configure-check-for-ns_get16-and-ns_get32-as-well.patch

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
* Tue Aug 10 2021 yixiangzhike <zhangxingliang3@huawei.com> - 0.9.1-2
- fix the compilation failure with new version glibc

* Tue Jul 27 2021 fuanan <fuanan3@huawei.com> - 0.9.1-1
- update to 0.9.1

* Thu Jul 23 2020 Liquor <lirui130@huawei.com> - 0.9.0-1
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
