Summary:	Mount a Windows CE based device on your Linux file system using FUSE
Summary(pl.UTF-8):	Montowanie urządzeń z Windows CE w linuksowym systemie plików
Name:		synce-fur
Version:	0.6
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/synce/fur-%{version}.tar.gz
# Source0-md5:	02c91b8052309c335bbcb95b0e5bfbd8
URL:		http://www.synce.org/
BuildRequires:	libfuse-devel
BuildRequires:	pkgconfig
BuildRequires:	synce-core-lib-devel >= 0.17
Requires:	synce-core-lib >= 0.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FUR is an application that let the user mount a Windows CE based
device as a normal Linux file system.

%description -l pl.UTF-8
FUR to aplikacja pozwalająca użytkownikowi montować urządzenia oparte
na Windows CE jako normalne linuksowe systemy plików.

%prep
%setup -q -n fur-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README.txt docs
%attr(755,root,root) %{_bindir}/Fur
