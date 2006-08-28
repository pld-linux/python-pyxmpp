Summary:	Jabber/XMPP package for Python
Summary(pl):	Biblioteka Jabber/XMPP dla Pythona
Name:		python-pyxmpp
Version:	1.0.0
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://files.jabberstudio.org/pyxmpp/pyxmpp-%{version}.tar.gz
# Source0-md5:	02700da5a2f36b57916e9da200d2c14f
URL:		http://pyxmpp.jabberstudio.org/
BuildRequires:	libxml2-devel >= 2.6.19
BuildRequires:	python-devel >= 1:2.3.0
%pyrequires_eq	python-modules
Requires:	python-dns
Requires:	python-libxml2 >= 2.6.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Python interface to XMPP and Jabber protocols.

%description -l pl
Ten pakiet udostêpnia interfejs Pythona do protoko³ów XMPP i Jabber.

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
%doc CHANGES README TODO ChangeLog doc/www/*
%dir %{py_sitedir}/pyxmpp
%attr(755,root,root) %{py_sitedir}/pyxmpp/*.so
%{py_sitedir}/pyxmpp/*.py[co]
%{py_sitedir}/pyxmpp/jabber
%{py_sitedir}/pyxmpp/jabberd
%{py_sitedir}/pyxmpp/sasl
