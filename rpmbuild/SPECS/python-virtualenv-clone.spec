%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%endif

# Manually disable python3 support until python3-virtualenv is available
# https://bugzilla.redhat.com/show_bug.cgi?id=537246
%global with_python3 0

# A lot of inconsistency here :)
%global modname virtualenv-clone
%global undername virtualenv_clone
%global srcname clonevirtualenv

Name:             python-virtualenv-clone
Version:          0.2.4
Release:          3%{?dist}
Summary:          Script to clone virtualenvs

Group:            Development/Libraries
License:          MIT
URL:              http://pypi.python.org/pypi/virtualenv-clone
Source0:          http://pypi.python.org/packages/source/v/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:        noarch


BuildRequires:    python2-devel
BuildRequires:    python-virtualenv
Requires:         python-virtualenv

%if 0%{?with_python3}
BuildRequires:    python3-devel
BuildRequires:    python3-virtualenv
%endif

%description
A script for cloning a non-relocatable virtualenv.

Virtualenv provides a way to make virtualenv's relocatable which could then
be copied as we wanted. However making a virtualenv relocatable this way
breaks the no-site-packages isolation of the virtualenv as well as other
aspects that come with relative paths and '/usr/bin/env' shebangs that may
be undesirable.

Also, the .pth and .egg-link rewriting doesn't seem to work as intended.
This attempts to overcome these issues and provide a way to easily clone an
existing virtualenv.

%if 0%{?with_python3}
%package -n python3-virtualenv-clone
Summary:          Script to clone virtualenvs
Group:            Development/Libraries

Requires:         python3-virtualenv

%description -n python3-virtualenv-clone
virtualenv cloning script.

A script for cloning a non-relocatable virtualenv.

Virtualenv provides a way to make virtualenv's relocatable which could then
be copied as we wanted. However making a virtualenv relocatable this way
breaks the no-site-packages isolation of the virtualenv as well as other
aspects that come with relative paths and '/usr/bin/env' shebangs that may
be undesirable.

Also, the .pth and .egg-link rewriting doesn't seem to work as intended.
This attempts to overcome these issues and provide a way to easily clone an
existing virtualenv.
%endif

%prep
%setup -q -n %{modname}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
mv %{buildroot}/%{_bindir}/virtualenv-clone %{buildroot}/%{_bindir}/python3-virtualenv-clone
popd
%endif

%{__python} setup.py install -O1 --skip-build --root=%{buildroot}


%files
%doc README
%{python_sitelib}/%{srcname}.*
%{python_sitelib}/%{undername}-%{version}*
%{_bindir}/virtualenv-clone

%if 0%{?with_python3}
%files -n python3-%{modname}
%doc README
%{python3_sitelib}/%{srcname}.*
%{python3_sitelib}/%{undername}-%{version}-*
%{python3_sitelib}/__pycache__/*%{srcname}*
%{_bindir}/python3-virtualenv-clone
%endif

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.4-1
- initial package for Fedora
