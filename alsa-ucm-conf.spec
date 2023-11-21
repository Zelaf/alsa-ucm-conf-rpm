Name:		alsa-ucm-conf
Summary:	Use Case Manager configuration for ALSA
Version:	23adf5a
Release:	1
License:	BSD 3-clause
BuildArch:	noarch
Source0:  https://github.com/alsa-project/alsa-ucm-conf/archive/23adf5a368abe9009f44547b91d60a244f735d81.tar.gz

%description
Use Case Manager configuration for ALSA

%prep
%autosetup -p1

%build

%install
tar xvzf *.tar.gz --strip-components=1 --wildcards "*/ucm" "*/ucm2"

%files
%{_datadir}/alsa/ucm2/*
