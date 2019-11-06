Name:      adcli
Version:   0.8.2
Release:   6
Summary:   A helper library and tools for Active Directory client operations
Group:     Development/Libraries
License:   LGPLv2+
URL:       http://cgit.freedesktop.org/realmd/adcli
Source0:   http://www.freedesktop.org/software/realmd/releases/adcli-%{version}.tar.gz

Patch1:    0001-Remove-upper-case-only-check-when-looking-for-the-Ne.patch
Patch2:	   0002-Use-strdup-if-offset-are-used.patch
Patch3:	   0003-correct-spelling-of-adcli_tool_computer_delete-descr.patch
Patch4:	   0004-doc-explain-that-all-credential-cache-types-are-supp.patch
Patch5:	   0005-library-add-adcli_conn_is_writeable.patch
Patch6:	   0006-Handle-kvno-increment-for-RODCs.patch
Patch7:	   0007-Fix-memory-leak-in-test_check_nt_time_string_lifetim.patch
Patch8:	   0008-library-add-_adcli_bin_sid_to_str.patch
Patch9:	   0009-library-add-_adcli_call_external_program.patch
Patch10:   0010-library-add-_adcli_ldap_parse_sid.patch
Patch11:   0011-library-add-lookup_domain_sid.patch
Patch12:   0012-library-add-adcli_conn_get_domain_sid.patch
Patch13:   0013-tools-add-option-add-samba-data.patch
Patch14:   0014-tools-store-Samba-data-if-requested.patch
Patch15:   0015-make-Samba-data-tool-configurable.patch
Patch16:   0016-Add-trusted-for-delegation-option.patch
Patch17:   0017-Only-update-attributes-given-on-the-command-line.patch
Patch18:   0018-update-allow-to-add-service-names.patch
Patch19:   0019-Calculate-enctypes-in-a-separate-function.patch
Patch20:   0020-join-add-all-attributes-while-creating-computer-obje.patch
Patch21:   0021-util-add-_adcli_strv_remove_unsorted.patch
Patch22:   0022-Add-add-service-principal-and-remove-service-princip.patch
Patch23:   0023-adcli_conn_is_writeable-do-not-crash-id-domain_disco.patch
Patch24:   0024-doc-fix-typos-in-the-adcli-man-page.patch

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
