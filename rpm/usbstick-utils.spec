Name:       usbstick-utils
Summary:    SailfishOS scripts to mount/umount external USB memorystick.
Version:    0.2
Release:    1
Group:      System/Base
License:    MIT
BuildArch:  noarch
URL:        https://github.com/kimmoli/usbstick-utils/
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  systemd
Requires:   systemd
Requires:   udisks2

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build

%install
# mounting script
# udev rules for sd[a-z][0-9]*
mkdir -p %{buildroot}%{_udevrulesdir}
cp rules/80-usbstick.rules %{buildroot}%{_udevrulesdir}

%files
%defattr(-,root,root,-)
%{_udevrulesdir}/80-usbstick.rules
