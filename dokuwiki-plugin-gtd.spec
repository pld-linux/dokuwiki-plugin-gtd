%define		plugin		gtd
Summary:	DokuWiki GTD (Getting Things Done) Plugin
Summary(pl.UTF-8):	Wtyczka gtd dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20090521
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://cloud.github.com/downloads/chimeric/dokuwiki-plugin-gtd/plugin-gtd.tgz
# Source0-md5:	05017b5fa8678054ad8c42772b4b0e47
URL:		http://www.dokuwiki.org/plugin:gtd
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20090214
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This plugin implements a nice formatted easy to use todo list following the principles of GTD.

%prep
%setup -qc
mv %{plugin}/* .

version=$(cat VERSION)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force js/css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/images
