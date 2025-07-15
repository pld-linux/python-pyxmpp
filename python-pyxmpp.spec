Summary:	Jabber/XMPP package for Python
Summary(pl.UTF-8):	Biblioteka Jabber/XMPP dla Pythona
Name:		python-pyxmpp
Version:	1.1.2
Release:	7
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pyxmpp/pyxmpp-%{version}.tar.gz
# Source0-md5:	a38abf032aca0408b6055cd94296eb75
Patch0:		%{name}-openfire_bug.patch
Patch1:		%{name}-xep-0203.patch
Patch2:		tls.patch
URL:		https://pypi.org/project/pyxmpp/
BuildRequires:	libxml2-devel >= 2.6.19
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-dns >= 1.6.0
Requires:	python-libxml2 >= 2.6.19
Requires:	python-modules >= 1:2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Python interface to XMPP and Jabber protocols.

%description -l pl.UTF-8
Ten pakiet udostępnia interfejs Pythona do protokołów XMPP i Jabber.

%prep
%setup -qn pyxmpp-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO ChangeLog doc/www/*
%dir %{py_sitedir}/pyxmpp
%attr(755,root,root) %{py_sitedir}/pyxmpp/*.so
%{py_sitedir}/pyxmpp/*.py[co]
%{py_sitedir}/pyxmpp/jabber
%{py_sitedir}/pyxmpp/jabberd
%{py_sitedir}/pyxmpp/sasl
%{py_sitedir}/pyxmpp-%{version}-py*.egg-info
