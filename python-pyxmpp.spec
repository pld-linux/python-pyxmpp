Summary:	Jabber/XMPP package for Python
Summary(pl.UTF-8):	Biblioteka Jabber/XMPP dla Pythona
Name:		python-pyxmpp
%define	snap	20070831
Version:	1.0.0
Release:	4.%{snap}.1
License:	LGPL
Group:		Libraries/Python
Source0:	http://pyxmpp.jajcus.net/downloads/snapshots/pyxmpp-%{version}.s%{snap}.tar.gz
# Source0-md5:	0aa7cda25d7dea8f38683afc78ea69e7
URL:		http://pyxmpp.jajcus.net/
BuildRequires:	libxml2-devel >= 2.6.19
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-modules
Requires:	python-dns
Requires:	python-libxml2 >= 2.6.19
Conflicts:	python-M2Crypto < 0.17-0.beta1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Python interface to XMPP and Jabber protocols.

%description -l pl.UTF-8
Ten pakiet udostępnia interfejs Pythona do protokołów XMPP i Jabber.

%prep
%setup -qn pyxmpp-%{version}.s%{snap}

%build
export CFLAGS="%{rpmcflags}"
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" | xargs rm

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
%{py_sitedir}/pyxmpp-*.egg-info
