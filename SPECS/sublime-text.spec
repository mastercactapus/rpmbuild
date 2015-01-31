Name:		sublime-text
Version:	3build3065
Release:	1%{?dist}
Summary:	Sublime text editor
License:	Commercial
Group:		Development Tools/Other
URL:		http://www.sublimetext.com/3
Source0:	sublime_text_3_build_3065_x64.tar.bz2

%description


%prep
%setup -n sublime_text_3


%build


%install
mkdir -p %{buildroot}%{_datadir}/sublime_text_3 %{buildroot}%{_bindir}
cp -r . %{buildroot}%{_datadir}/sublime_text_3
ln -s %{_datadir}/sublime_text_3/sublime_text %{buildroot}%{_bindir}/sublime_text
ln -s %{_datadir}/sublime_text_3/sublime_text %{buildroot}%{_bindir}/subl


%files
%{_bindir}/*
%{_datadir}/*


%changelog

