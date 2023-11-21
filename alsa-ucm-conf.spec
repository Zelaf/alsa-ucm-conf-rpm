Name:		alsa-ucm-conf
Summary:	Use Case Manager configuration for ALSA
Version:	23adf5a
Release:	1
Source0: https://github.com/alsa-project/alsa-ucm-conf/archive/23adf5a368abe9009f44547b91d60a244f735d81.tar.gz
License:	BSD 3-clause
BuildArch:	noarch

%description
Use Case Manager configuration for ALSA

%prep
%autosetup -p1
mv 23adf5a368abe9009f44547b91d60a244f735d81.tar.gz alsa-ucm-conf.tar.gz

%build

%install
find ucm2 -type f -iname "*.conf" -exec install -vDm 644 {} "%{buildroot}%{_datadir}/alsa/"{} \;
find ucm2 -type l -iname "*.conf" -exec cp -dv {} "%{buildroot}%{_datadir}/alsa/"{} \;

%files
%{_datadir}/alsa/ucm2/*
