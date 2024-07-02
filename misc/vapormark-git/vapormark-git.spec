%define _disable_source_fetch 0
%global commit bf5e50e8400753eaa66175e25f88abc7b665db79
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vapormark-git
Version:        20240522.r%{shortcommit}
Release:        1%{?dist}
Summary:        Benchmark framework for measuring performance metrics while running a program on Linux

License:        GPL=2.0
URL:            https://github.com/Igalia/vapormark
Source0:        %{URL}/archive/%{commit}/vapormark-%{commit}.tar.gz
Source1:        https://git.kernel.org/pub/scm/linux/kernel/git/mason/schbench.git/snapshot/schbench-1.0.tar.gz

BuildRequires: make
BuildRequires: git
BuildRequires: gcc

Requires: mangohud
Requires: python
Requires: pandoc

%description
Vapormark is a benchmark framework developed for measuring various performance metrics (e.g., throughput, latency, and tail latency) and the process states (e.g., backend stall, energy consumption) while running a program on Linux.

%prep
%autosetup -n vapormark-%{commit}
tar -xzf %{SOURCE1} -C %{_builddir}

%build
# Build vapormark first
cd %{_builddir}/vapormark-%{commit}
make

# Build schbench
cd %{_builddir}/schbench-1.0
make

%install
cd %{_builddir}/vapormark-%{commit}
install -Dm755 bin/* -t %{buildroot}/%{_bindir}/
install -Dm644 LICENSE -t %{buildroot}/usr/share/licenses/vapormark-git/

cd %{_builddir}/schbench-1.0
install -Dm755 schbench %{buildroot}/%{_bindir}/

%files
%{_bindir}/*
/usr/share/licenses/vapormark-git/LICENSE


