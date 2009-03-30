Summary:	Mount a Windows CE based device on your Linux file system using FUSE
Summary(pl.UTF-8):	Montowanie urządzeń z Windows CE w linuksowym systemie plików
Name:		synce-fur
Version:	0.4.5
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.infis.univ.trieste.it/~riccardo/downloads/FUR-%{version}.tar.bz2
# Source0-md5:	582b8a327efa9965771762305b3d26bf
URL:		http://www.infis.univ.trieste.it/~riccardo/
BuildRequires:	libfuse-devel
BuildRequires:	pkgconfig
BuildRequires:	synce-librapi2-devel > 0.9.1
BuildRequires:	synce-libsynce-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FUR is an application that let the user mount a Windows CE based
device as a normal Linux file system.

%description -l pl.UTF-8
FUR to aplikacja pozwalająca użytkownikowi montować urządzenia oparte
na Windows CE jako normalne linuksowe systemy plików.

%prep
%setup -q -n FUR-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install Fur $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README.txt docs
%attr(755,root,root) %{_bindir}/*
