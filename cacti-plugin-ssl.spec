%define		plugin	ssl
%define		php_min_version 5.0.0
Summary:	Plugin for Cacti - forcing SSL access
Summary(pl.UTF-8):	Wtyczka do Cacti wymuszająca dostęp przez SSL
Name:		cacti-plugin-%{plugin}
Version:	0.1
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{plugin}-%{version}.tar.gz
# Source0-md5:	dd762734fe19d73c4285c23245932c28
URL:		http://forums.cacti.net/viewtopic.php?f=14&t=24236
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
This Cacti plugin forces your Cacti users to use SSL to access Cacti.
No page or graph will be viewable through regular HTTP. Make sure you
are running SSL support on your web server before enabling.

%description -l pl.UTF-8
Wtyczka do Cacti wymuszająca stosowanie SSL (szyfrowania) przy
dostępie WWW do Cacti. Żadna strona ani wykres nie będzie dostępny po
nieszyfrowanym HTTP. Przed zainstalowaniem wtyczki należy upewnić się,
że serwer WWW obsługuje SSL.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{plugindir}
