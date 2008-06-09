Summary:	Video extraction utility for YouTube
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube
Name:		youtube-dl
Version:	20080630
Release:	1
License:	MIT
Group:		Applications/System
Source0:	http://www.arrakis.es/~rggi3/%{name}/youtube-dl
# Source0-md5:	f79194714ad3d4913fc01417f4c71195
URL:		http://www.arrakis.es/~rggi3/youtube-dl/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	python >= 2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
youtube-dl is a small command-line program to download videos from
YouTube.com.

%description -l pl.UTF-8
youtube-dl jest programem do ściągania plików video z YouTube.com.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/youtube-dl
