Name:		alsa-ucm-conf
Summary:	Newer Use Case Manager configurations for ALSA
Version:	23adf5a
Release:	1
License:	BSD 3-clause
BuildArch:	noarch
Provides:   alsa-ucm
Requires:   alsa-lib
Source0:    https://github.com/alsa-project/alsa-ucm-conf/archive/23adf5a368abe9009f44547b91d60a244f735d81.tar.gz
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
