Summary:	Mount a Windows CE based device on your Linux file system using FUSE
Name:		synce-fur
Version:	0.4.3
Release:	0.1
License:	public domain
Group:		Applications
Source0:	http://www.infis.univ.trieste.it/~riccardo/downloads/FUR-%{version}.tar.bz2
# Source0-md5:	f52c8fa399ca1aeaad1a71f965581916
URL:		http://www.infis.univ.trieste.it/~riccardo/
#Requires:	fuse
BuildRequires:	synce-librapi2
BuildRequires:	synce-libsynce
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FUR is an application that let the user mount a Windows CE based
device as a normal Linux file system.


%prep
%setup -q -n FUR-%{version}

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
