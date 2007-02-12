Summary:	OS identification program
Summary(pl.UTF-8):   Program do identyfikacji OS
Name:		queso
Version:	1.20
Release:	5
License:	GPL
Group:		Networking
Source0:	ftp://ftp.ci.uminho.pt/pub/security/apostols/%{name}-980922.tar.bz2
# Source0-md5:	9c2f3677e112a20ac7b7e2eeeec05fc9
Patch0:		%{name}-libpcap.patch.bz2
URL:		http://www.apostols.org/projectz/queso/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A program to detect remote OS.

%description -l pl.UTF-8
Program do zdalnego wykrywania Systemu Operacyjnego.

%prep
%setup -q -n %{name}-980922
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-libpcap={%_includedir}/pcap
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}}

install queso $RPM_BUILD_ROOT%{_sbindir}
install queso.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation.txt CHANGES
%attr(755,root,root) %{_sbindir}/queso
%config(noreplace) %{_sysconfdir}/queso.conf
