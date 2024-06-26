%global commit 14a33b627510414737f856994284013b8bda7f82
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _disable_source_fetch 0

Name:           sched-ext-scx-git
Version:        20240629.r%{shortcommit}
Release:        2%{?dist}
Summary:        Sched_ext Schedulers and Tools

License:        GPL=2.0
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/%{commit}/scx-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  meson >= 1.2
BuildRequires:  python
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang >= 17
BuildRequires:  llvm >= 17
BuildRequires:  lld >= 17
# BuildRequires:  bpftool
# BuildRequires:  libbpf >= 1.3
# BuildRequires:  libbpf-devel >= 1.3
BuildRequires:  elfutils-libelf
BuildRequires:  elfutils-libelf-devel
BuildRequires:  zlib
BuildRequires:  jq
BuildRequires:  jq-devel
BuildRequires:  systemd
# Requires:  libbpf
Requires:  elfutils-libelf
Requires:  zlib
Requires:  jq
Conflicts: shed-ext-scx

%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This repository contains various scheduler implementations and support utilities.

%prep
%autosetup -n scx-%{commit}

%build
%meson \
 -Dsystemd=enabled \
 -Dopenrc=disabled \
 -Dlibalpm=disabled
%meson_build


%install
%meson_install


%files
%attr(0644,root,root) %ghost %config(noreplace) %{_sysconfdir}/default/scx
%{_bindir}/*
%{_prefix}/lib/systemd/system/scx.service
%{_sysconfdir}/systemd/journald@sched-ext.conf
