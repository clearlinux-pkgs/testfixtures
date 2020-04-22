#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : testfixtures
Version  : 6.14.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/27/87/c7e7e4cb6e776e74513227c595b29816d2c905553c611e2ae9cfb57d85e1/testfixtures-6.14.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/27/87/c7e7e4cb6e776e74513227c595b29816d2c905553c611e2ae9cfb57d85e1/testfixtures-6.14.1.tar.gz
Summary  : A collection of helpers and mock objects for unit tests and doc tests.
Group    : Development/Tools
License  : MIT
Requires: testfixtures-python = %{version}-%{release}
Requires: testfixtures-python3 = %{version}-%{release}
Requires: twine
Requires: wheel
BuildRequires : buildreq-distutils3
BuildRequires : twine
BuildRequires : wheel

%description
Testfixtures
============
|CircleCI|_ |Docs|_
.. |CircleCI| image:: https://circleci.com/gh/Simplistix/testfixtures/tree/master.svg?style=shield
.. _CircleCI: https://circleci.com/gh/Simplistix/testfixtures/tree/master

%package python
Summary: python components for the testfixtures package.
Group: Default
Requires: testfixtures-python3 = %{version}-%{release}

%description python
python components for the testfixtures package.


%package python3
Summary: python3 components for the testfixtures package.
Group: Default
Requires: python3-core
Provides: pypi(testfixtures)

%description python3
python3 components for the testfixtures package.


%prep
%setup -q -n testfixtures-6.14.1
cd %{_builddir}/testfixtures-6.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587562204
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
