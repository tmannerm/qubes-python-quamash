%define mod_name Quamash

Name:           python-%{mod_name}
Version:        0.6.1
Release:        1%{?dist}
Url:            http://github.com/harvimt/quamash
Summary:        PEP 3156 event-loop (asyncio) api using the Qt Event-Loop
License:        BSD
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/01/1e/cf6f3c38cee61ed04fea58667f673adc67d6412eba0b3327dbb5732c1177/%{mod_name}-%{version}.tar.gz
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{mod_name}}
# import fails without at least one pyqt implementation installed
BuildRequires:  python%{python3_pkgversion}-PyQt4
BuildArch:      noarch

%description
PEP 3156 event-loop (asyncio) api using the Qt Event-Loop

%package -n python%{python3_pkgversion}-%{mod_name}
Summary:        PEP 3156 event-loop (asyncio) api using the Qt Event-Loop

%description -n python%{python3_pkgversion}-%{mod_name}
PEP 3156 event-loop (asyncio) api using the Qt Event-Loop

%prep
%setup -q -n %{mod_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{mod_name}
%doc README.rst
%{python3_sitelib}/%{mod_name}*
%{python3_sitelib}/quamash

%changelog
