Summary:	Jabber/XMPP package for Python
Summary(pl):	Biblioteka Jabber/XMPP dla Pythona
Name:		python-pyxmpp
Version:	0.5.20050125a
Release:	1
License:	LGPL
Group:		Libraries/Python
#Source0:	http://www.jabberstudio.org/files/pyxmpp/pyxmpp-%{version}.tar.gz
#Source0:	http://pyxmpp.jabberstudio.org/snapshots/pyxmpp-%{version}.tar.gz
Source0:	http://www.jajcus.net/files/pyxmpp-%{version}.tar.gz
# Source0-md5:	dc562adb97a85ab89ca730cf8db73985
URL:		http://pyxmpp.jabberstudio.org/
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-dns
Requires:	python-libxml2 >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Python interface to XMPP and Jabber protocols.

%description -l pl
Ten pakiet udostępnia interfejs Pythona do protokołów XMPP i Jabber.

%prep
%setup -qn pyxmpp-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO DONE ChangeLog
%dir %{py_sitedir}/pyxmpp
%attr(755,root,root) %{py_sitedir}/pyxmpp/*.so
%{py_sitedir}/pyxmpp/*.py[co]
%{py_sitedir}/pyxmpp/jabber
%{py_sitedir}/pyxmpp/jabberd
%{py_sitedir}/pyxmpp/sasl
