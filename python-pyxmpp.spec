Summary:	Jabber/XMPP package for Python
Summary(pl.UTF-8):	Biblioteka Jabber/XMPP dla Pythona
Name:		python-pyxmpp
Version:	1.1.1
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://pyxmpp.jajcus.net/downloads/pyxmpp-%{version}.tar.gz
# Source0-md5:	5f1f5472c3e2360fa49552cc49861bd4
URL:		http://pyxmpp.jajcus.net/
BuildRequires:	libxml2-devel >= 2.6.19
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-dns
Requires:	python-libxml2 >= 2.6.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Python interface to XMPP and Jabber protocols.

%description -l pl.UTF-8
Ten pakiet udostępnia interfejs Pythona do protokołów XMPP i Jabber.

%prep
%setup -qn pyxmpp-%{version}

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
