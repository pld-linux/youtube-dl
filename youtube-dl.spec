Summary:	Video extraction utility for YouTube
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube
Name:		youtube-dl
Version:	20120927
Release:	1
License:	Public Domain
Group:		Applications/System
Source0:	https://github.com/rg3/youtube-dl/raw/2012.09.27/youtube-dl
# Source0-md5:	b581c339555f66df4e213ececce37a11
URL:		http://rg3.github.com/youtube-dl/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	python >= 2.5
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
