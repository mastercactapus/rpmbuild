Name:		keepassx
Version:	2.0alpha6
Release:	1%{?dist}
Summary:	KeepassX 2 alpha release

Group:		Utilities/Other
License:	BSD and CCO and GPL-2 and GPL-3 and LGPL-2.1 and LGPL-3
URL:		http://www.keepassx.org/
Source0:	%{name}-2.0-alpha6.tar.gz

BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	qt4-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	zlib-devel
Requires:	qt4
Requires:	libgcrypt
Requires:	zlib

%description


%prep
%setup -n %{name}-2.0-alpha6


%build
%cmake


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/keepassx
%{_datadir}/*


%changelog

