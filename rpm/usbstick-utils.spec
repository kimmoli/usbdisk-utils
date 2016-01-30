Name:       usbstick-utils
Summary:    SailfishOS scripts to mount/umount external USB memorystick.
Version:    0.1
Release:    1
Group:      System/Base
License:    MIT
BuildArch:  noarch
URL:        https://github.com/kimmoli/usbstick-utils/
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  systemd
Requires:   systemd
Requires:   tracker

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build

%install
# mounting script
mkdir -p %{buildroot}%{_sbindir}
cp scripts/mount-usbstick.sh %{buildroot}%{_sbindir}
# systemd service install
mkdir -p %{buildroot}%{_unitdir}
cp scripts/mount-usbstick@.service %{buildroot}%{_unitdir}
# udev rules for sd[a-z][0-9]*
mkdir -p %{buildroot}%{_udevrulesdir}
cp rules/90-mount-usbstick.rules %{buildroot}%{_udevrulesdir}

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_sbindir}/mount-usbstick.sh
%{_unitdir}/mount-usbstick@.service
%{_udevrulesdir}/90-mount-usbstick.rules
