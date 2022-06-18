Name:		alsa-ucm-conf
Summary:	Use Case Manager configuration for ALSA
Version:	1.2.7.1
Release:	1
License:	BSD 3-clause
Source0:	https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-%{version}.tar.bz2
BuildArch:	noarch

%description
Use Case Manager configuration for ALSA

%prep
%autosetup -p1

%build

%install
find ucm2 -type f -iname "*.conf" -exec install -vDm 644 {} "%{buildroot}%{_datadir}/alsa/"{} \;
find ucm2 -type l -iname "*.conf" -exec cp -dv {} "%{buildroot}%{_datadir}/alsa/"{} \;

%files
%{_datadir}/alsa/ucm2/*
