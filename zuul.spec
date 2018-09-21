%global install_dir /opt/gdc/zuul

Name:             zuul
Summary:          GoodData customized Zuul gatekeeper
Epoch:            1
Version:          2.5.1
Release:          %{?gdcversion}%{?dist}.gdc

Vendor:           GoodData
Group:            GoodData/Tools

License:          Apache
URL:              https://github.com/gooddata/zuul
Source0:          sources.tar
BuildArch:        x86_64
BuildRoot:        %{_tmppath}/%{name}-%{version}-root

Requires:         python-virtualenv
BuildRequires:    git
BuildRequires:    libffi-devel
BuildRequires:    libjpeg-devel
BuildRequires:    openssl-devel
BuildRequires:    python-pip
BuildRequires:    python-virtualenv

%prep
%setup -q -c

%build
export PBR_VERSION="%{version}.%{release}"
make build

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT%{install_dir} install
cp -r tools %{buildroot}%{install_dir}/

%check
export PBR_VERSION="%{version}.%{release}"
make check

%clean
rm -rf $RPM_BUILD_ROOT

%description
GoodData customized Zuul gatekeeper

%files
%attr(0755, root, root) %dir %{install_dir}
%attr(0755, root, root) %{install_dir}/bin
%attr(0755, root, root) %{install_dir}/include
%attr(0755, root, root) %{install_dir}/lib
%attr(0755, root, root) %{install_dir}/lib64
%attr(0755, root, root) %{install_dir}/status
%attr(0755, root, root) %{install_dir}/tools

%changelog
* Fri Sep 21 2018 Tomáš Čech <tomas.cech@gooddata.com> 2.5.1-%{?gdcversion}%{?dist}.gdc
- drop RPM changelog
- for changelog see GIT log of gooddata/zuul

