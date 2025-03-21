#
# Conditional build:
%bcond_without	python2	# CPython 2.x module

# full version number as seen on youtube-dl website
%define	verlong	2021.12.17

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
Release:	6
Epoch:		2
License:	Public Domain
Group:		Applications/System
Source0:	https://youtube-dl.org/downloads/%{verlong}/%{name}-%{verlong}.tar.gz
# Source0-md5:	64b373c39c30c314cda9396c6a3f731f
Source1:	%{name}.conf
# should be downloaded from:
# https://github.com/rg3/youtube-dl/pull/10291.diff
# but the author removed his repository, so the url is 404
# git log -p --reverse pr/10291~3..pr/10291
Patch0:		10291.diff
Patch1:		extract-uploader.patch
URL:		http://youtube-dl.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.720
Requires:	python3-setuptools
Requires:	python3-%{name} = %{epoch}:%{version}-%{release}
Suggests:	ffmpeg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package -n python-%{name}
Summary:	Python 2 video extraction utility for YouTube
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube dla Pythona 2
Group:		Libraries/Python
Requires:	python-pyxattr >= 0.5.0

%description -n python-%{name}
Python 2 video extraction utility for YouTube.

%description -n python-%{name} -l pl.UTF-8
Narzędzie do wydobywania filmów z YouTube dla Pythona 2.

%package -n python3-%{name}
Summary:	Python 3 video extraction utility for YouTube
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube dla Pythona 3
Group:		Libraries/Python
Requires:	python3-pyxattr >= 0.5.0

%description -n python3-%{name}
Python 3 video extraction utility for YouTube.

%description -n python3-%{name} -l pl.UTF-8
Narzędzie do wydobywania filmów z YouTube dla Pythona 3.

%package -n zsh-completion-%{name}
Summary:	Zsh completion for youtube-dl command
Summary(pl.UTF-8):	Dopełnianie parametrów w zsh dla polecenia youtube-dl
Group:		Applications/Shells
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zsh

%description -n zsh-completion-%{name}
Zsh completion for youtube-dl command.

%description -n zsh-completion-%{name} -l pl.UTF-8
Dopełnianie parametrów w zsh dla polecenia youtube-dl.

%prep
%setup -qc
%{__mv} %{name} .tmp; %{__mv} .tmp/* .
%patch -P 0 -p1
%patch -P 1 -p0

%build
%if %{with python2}
%py_build
%endif

%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%py3_install

install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

install -d $RPM_BUILD_ROOT{%{bash_compdir},%{fish_compdir},%{zsh_compdir}}
%{__mv} $RPM_BUILD_ROOT%{_prefix}/etc/bash_completion.d/youtube-dl.bash-completion \
	$RPM_BUILD_ROOT%{bash_compdir}/%{name}
%{__mv} $RPM_BUILD_ROOT%{_prefix}/etc/fish/completions/youtube-dl.fish \
	$RPM_BUILD_ROOT%{fish_compdir}/%{name}.fish
cp -p youtube-dl.zsh $RPM_BUILD_ROOT%{zsh_compdir}/_youtube-dl
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/youtube_dl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/youtube-dl.conf
%attr(755,root,root) %{_bindir}/youtube-dl
%{_mandir}/man1/youtube-dl.1*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/%{name}

%files -n fish-completion-%{name}
%defattr(644,root,root,755)
%{fish_compdir}/%{name}.fish

%if %{with python2}
%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/youtube_dl
%{py_sitescriptdir}/youtube_dl-*-py*.egg-info
%endif

%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/youtube_dl
%{py3_sitescriptdir}/youtube_dl-*-py*.egg-info

%files -n zsh-completion-%{name}
%defattr(644,root,root,755)
%{zsh_compdir}/_youtube-dl
