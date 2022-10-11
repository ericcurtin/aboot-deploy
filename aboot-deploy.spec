Name:           aboot-deploy
Version:        0.1
Release:        1%{?dist}
Summary:        Deploy aboot

License:        GPLv2+
Source0:        aboot-deploy

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
* Wed Oct 12 2022 Eric Curtin <ecurtin@redhat.com>
- Initial version
