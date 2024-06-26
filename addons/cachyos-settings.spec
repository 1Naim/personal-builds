%define _disable_source_fetch 0

Name:           cachyos-settings
Release:        9%{?dist}
Version:        1.0.0
Summary:        CachyOS-Settings ported to Fedora
License:        GPLv3
URL:            https://github.com/CachyOS/CachyOS-Settings
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

Requires:       zram-generator

Provides:       zram-generator-defaults
Provides:       kerver
Obsoletes:      zram-generator-defaults
Obsoletes:      bore-sysctl
Obsoletes:      kerver

%description
CachyOS-Settings for Fedora based systems

%prep
%autosetup -n CachyOS-Settings-%{version}

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_prefix}/lib
cp %{_builddir}/CachyOS-Settings-%{version}/usr/{bin,lib} %{buildroot}/%{_prefix} -r
mv %{buildroot}/%{_prefix}/lib/modprobe.d/nvidia.conf %{buildroot}/%{_prefix}/lib/modprobe.d/nvidia_cachyos.conf
rm %{buildroot}/%{_bindir}/tunecfs*
chmod +x %{buildroot}/%{_bindir}/*

%files
%{_bindir}/*
%{_prefix}/lib/*

%changelog
%autochangelog





