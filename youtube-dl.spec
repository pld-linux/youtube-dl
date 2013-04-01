%define	ver	2013.03.29
Summary:	Video extraction utility for YouTube
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube
Name:		youtube-dl
Version:	%(echo %{ver} | tr -d .)
Release:	1
License:	Public Domain
Group:		Applications/System
Source0:	https://github.com/rg3/youtube-dl/raw/%{ver}/youtube-dl?/%{name}-%{version}
# Source0-md5:	a2a30e4b9ad06538d92968ceb2d58b3f
URL:		http://rg3.github.com/youtube-dl/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	python >= 2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
youtube-dl is a small command-line program to download videos from
YouTube.com.

%description -l pl.UTF-8
youtube-dl jest programem do ściągania plików video z YouTube.com.

%prep
%setup -c -T

%build
ver=$(%{__python} %{SOURCE0} --version | tr -d .)

if [ "$ver" != "%{version}" ]; then
	echo "Source with $ver found while expecting %{version}!" >&2
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/youtube-dl
