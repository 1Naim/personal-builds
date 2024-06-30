%global commit 6801ed049d40436c4c6416a4226fd7236d0e91da
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _disable_source_fetch 0

Name:           ananicy-cpp-rules
Version:        20240629.r%{shortcommit}
Release:        1%{?dist}
Summary:        List of rules used to assign specific nice values to specific processes

License:        GPL=3.0
URL:            https://github.com/CachyOS/ananicy-rules
Source0:        %{URL}/archive/%{commit}/ananicy-rules-%{commit}.tar.gz

Requires: ananicy-cpp

%description
List of rules used to assign specific nice values to specific processes

%prep
%autosetup -n ananicy-rules-%{commit}

%install
install -d %{buildroot}/etc/ananicy.d
cp %{_builddir}/ananicy-rules-%{commit}/00-default %{buildroot}/etc/ananicy.d/ -r
cp %{_builddir}/ananicy-rules-%{commit}/00-cgroups.cgroups %{buildroot}/etc/ananicy.d/ -r
cp %{_builddir}/ananicy-rules-%{commit}/00-types.types %{buildroot}/etc/ananicy.d/ -r
cp %{_builddir}/ananicy-rules-%{commit}/ananicy.conf %{buildroot}/etc/ananicy.d/ -r

%files rules
%defattr(-,root,root,-)
/etc/ananicy.d/*

%changelog
%autochangelog
