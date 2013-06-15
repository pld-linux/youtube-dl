# TODO
# - bash-completions subpackage
%define	ver	2013.05.23
Summary:	Video extraction utility for YouTube
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube
Name:		youtube-dl
Version:	%(echo %{ver} | tr -d .)
Release:	1
License:	Public Domain
Group:		Applications/System
Source0:	http://youtube-dl.org/downloads/%{ver}/%{name}-%{ver}.tar.gz
# Source0-md5:	6cb4ee904456d102d4f3edb68272ca50
URL:		http://youtube-dl.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
youtube-dl is a small command-line program to download videos from
YouTube.com.

%description -l pl.UTF-8
youtube-dl jest programem do ściągania plików video z YouTube.com.

%prep
%setup -qc
mv %{name} .tmp; mv .tmp/* .

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/youtube_dl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.md LICENSE
%attr(755,root,root) %{_bindir}/youtube-dl
%{_mandir}/man1/youtube-dl.1*
%{py_sitescriptdir}/youtube_dl
%{py_sitescriptdir}/youtube_dl-%{ver}-py*.egg-info
