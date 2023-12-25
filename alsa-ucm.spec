Name:		alsa-ucm
Summary:	Newer Use Case Manager configurations for ALSA
Version:	5b66bd9
Release:	2
License:	BSD 3-clause
BuildArch:	noarch
Requires:   alsa-lib
Source0:    https://github.com/Zelaf/alsa-ucm-conf/archive/5b66bd9103e9154eb3b1f0ad578ea5134867a71c.tar.gz
URL:        https://github.com/Zelaf/alsa-ucm-conf-rpm-spec
%description
Newer Use Case Manager configurations for ALSA based on the GitHub commit archives.

New releases will be made based on GitHub commits.

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/alsa
tar xvzf %{SOURCE0} -C %{buildroot}/usr/share/alsa --strip-components=1 --wildcards "*/ucm2"

%files
%{_datadir}/alsa/ucm2/*

%changelog
* Mon Dec 25 2023 Zelaf
- Edited Behringer UMC404HD to have different priorities.
