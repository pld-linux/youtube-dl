# full version number as seen on youtube-dl website
%define	verlong	2015.11.10

# transform version so we don't have to bump epoch after four digit upgrades:
# 2013.01.17.1 becomes 20130117_1
# 2013.01.28   becomes 20130128
# $ rpmvercmp 20130117_1 20130128
# 20130117_1 < 20130128
%define	ver	%(echo %{verlong} | awk -F. 'NF == 3 {printf("%s%s%s", $1, $2, $3)} NF == 4 {printf("%s%s%s_%s", $1, $2, $3, $4)}')
Summary:	Video extraction utility for YouTube
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube
Name:		youtube-dl
Version:	%{ver}
Release:	1
Epoch:		2
License:	Public Domain
Group:		Applications/System
Source0:	http://youtube-dl.org/downloads/%{verlong}/%{name}-%{verlong}.tar.gz
# Source0-md5:	b4fa9e4a08d21b25733f36f140180228
Source1:	%{name}.conf
URL:		http://youtube-dl.org/
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-pyxattr >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		bash_compdir	%{_datadir}/bash-completion/completions
%define		fish_compdir	%{_datadir}/fish/completions

%description
youtube-dl is a small command-line program to download videos from
YouTube.com.

%description -l pl.UTF-8
youtube-dl jest programem do ściągania plików video z YouTube.com.

%package -n bash-completion-%{name}
Summary:	Bash completion for youtube-dl command
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów polecenia youtube-dl
Group:		Applications/Shells
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-%{name}
Bash completion for youtube-dl command.

%description -n bash-completion-%{name} -l pl.UTF-8
Bashowe dopełnianie parametrów polecenia youtube-dl.

%package -n fish-completion-%{name}
Summary:	Fish completion for youtube-dl command
Summary(pl.UTF-8):	Dopełnianie parametrów w fish dla polecenia youtube-dl
Group:		Applications/Shells
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	fish

%description -n fish-completion-%{name}
Fish completion for youtube-dl command.

%description -n fish-completion-%{name} -l pl.UTF-8
Dopełnianie parametrów w fish dla polecenia youtube-dl.

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

install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

install -d $RPM_BUILD_ROOT{%{bash_compdir},%{fish_compdir}}
%{__mv} $RPM_BUILD_ROOT%{_prefix}/etc/bash_completion.d/youtube-dl.bash-completion \
	$RPM_BUILD_ROOT%{bash_compdir}/%{name}
%{__mv} $RPM_BUILD_ROOT%{_prefix}/etc/fish/completions/youtube-dl.fish \
	$RPM_BUILD_ROOT%{fish_compdir}/%{name}.fish
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/youtube_dl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/youtube-dl.conf
%attr(755,root,root) %{_bindir}/youtube-dl
%{_mandir}/man1/youtube-dl.1*
%{py_sitescriptdir}/youtube_dl
%{py_sitescriptdir}/youtube_dl-*-py*.egg-info

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/%{name}

%files -n fish-completion-%{name}
%defattr(644,root,root,755)
%{fish_compdir}/%{name}.fish
