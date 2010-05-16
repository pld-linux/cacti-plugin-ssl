%define		plugin	ssl
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - forcing SSL access
Summary(pl.UTF-8):	Wtyczka do Cacti wymuszająca dostęp przez SSL
Name:		cacti-plugin-ssl
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{plugin}-%{version}.zip
# Source0-md5:	72eda21392828e9433a7b89674ddb468
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
BuildRequires:	unzip
Requires:	cacti
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{plugindir}
