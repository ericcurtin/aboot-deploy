Name:           aboot-deploy
Version:        0.1
Release:        2%{?dist}
Summary:        Deploy aboot

License:        GPLv2+
Source0:        aboot-deploy

BuildArch:      noarch

%description

Aboot-deploy is a tool that given a aboot (Android) image, writes it to the
relevant bootloader partition.

%prep

%build

%install
install -Dm755 %{SOURCE0} %{buildroot}%{_bindir}/aboot-deploy

%files
%{_bindir}/aboot-deploy

%changelog
* Wed Jan 11 2023 Eric Curtin <ecurtin@redhat.com>
- Changed to take ab partitioning into account

* Wed Jan 11 2023 Eric Curtin <ecurtin@redhat.com>
- Added noarch, it's a shell script

* Wed Oct 12 2022 Eric Curtin <ecurtin@redhat.com>
- Initial version
