#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kgpg
Version  : 18.12.3
Release  : 2
URL      : https://download.kde.org/stable/applications/18.12.3/src/kgpg-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/kgpg-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/kgpg-18.12.3.tar.xz.sig
Summary  : A GnuPG frontend
Group    : Development/Tools
License  : GPL-2.0
Requires: kgpg-bin = %{version}-%{release}
Requires: kgpg-data = %{version}-%{release}
Requires: kgpg-license = %{version}-%{release}
Requires: kgpg-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gpgme-dev
BuildRequires : kcontacts-dev

%description
No detailed description available

%package bin
Summary: bin components for the kgpg package.
Group: Binaries
Requires: kgpg-data = %{version}-%{release}
Requires: kgpg-license = %{version}-%{release}

%description bin
bin components for the kgpg package.


%package data
Summary: data components for the kgpg package.
Group: Data

%description data
data components for the kgpg package.


%package doc
Summary: doc components for the kgpg package.
Group: Documentation

%description doc
doc components for the kgpg package.


%package license
Summary: license components for the kgpg package.
Group: Default

%description license
license components for the kgpg package.


%package locales
Summary: locales components for the kgpg package.
Group: Default

%description locales
locales components for the kgpg package.


%prep
%setup -q -n kgpg-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555408659
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555408659
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kgpg
cp COPYING %{buildroot}/usr/share/package-licenses/kgpg/COPYING
pushd clr-build
%make_install
popd
%find_lang kgpg

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kgpg

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kgpg.desktop
/usr/share/config.kcfg/kgpg.kcfg
/usr/share/dbus-1/interfaces/org.kde.kgpg.Key.xml
/usr/share/icons/hicolor/128x128/apps/kgpg.png
/usr/share/icons/hicolor/16x16/actions/document-export-key.png
/usr/share/icons/hicolor/16x16/actions/document-import-key.png
/usr/share/icons/hicolor/16x16/actions/document-properties-key.png
/usr/share/icons/hicolor/16x16/apps/kgpg.png
/usr/share/icons/hicolor/16x16/status/key-group.png
/usr/share/icons/hicolor/16x16/status/key-orphan.png
/usr/share/icons/hicolor/16x16/status/key-pair.png
/usr/share/icons/hicolor/16x16/status/key-single.png
/usr/share/icons/hicolor/22x22/actions/document-export-key.png
/usr/share/icons/hicolor/22x22/actions/document-import-key.png
/usr/share/icons/hicolor/22x22/actions/document-properties-key.png
/usr/share/icons/hicolor/22x22/actions/key-generate-pair.png
/usr/share/icons/hicolor/22x22/actions/view-key-secret.png
/usr/share/icons/hicolor/22x22/apps/kgpg.png
/usr/share/icons/hicolor/22x22/status/key-group.png
/usr/share/icons/hicolor/22x22/status/key-pair.png
/usr/share/icons/hicolor/22x22/status/key-single.png
/usr/share/icons/hicolor/32x32/actions/document-export-key.png
/usr/share/icons/hicolor/32x32/actions/document-import-key.png
/usr/share/icons/hicolor/32x32/actions/document-properties-key.png
/usr/share/icons/hicolor/32x32/apps/kgpg.png
/usr/share/icons/hicolor/32x32/status/key-group.png
/usr/share/icons/hicolor/32x32/status/key-pair.png
/usr/share/icons/hicolor/32x32/status/key-single.png
/usr/share/icons/hicolor/48x48/actions/document-export-key.png
/usr/share/icons/hicolor/48x48/actions/document-import-key.png
/usr/share/icons/hicolor/48x48/actions/document-properties-key.png
/usr/share/icons/hicolor/48x48/apps/kgpg.png
/usr/share/icons/hicolor/48x48/status/key-group.png
/usr/share/icons/hicolor/48x48/status/key-pair.png
/usr/share/icons/hicolor/48x48/status/key-single.png
/usr/share/icons/hicolor/64x64/apps/kgpg.png
/usr/share/icons/hicolor/scalable/actions/document-export-key.svgz
/usr/share/icons/hicolor/scalable/actions/document-import-key.svgz
/usr/share/icons/hicolor/scalable/actions/document-properties-key.svgz
/usr/share/icons/hicolor/scalable/apps/kgpg.svg
/usr/share/icons/hicolor/scalable/status/key-group.svgz
/usr/share/icons/hicolor/scalable/status/key-pair.svgz
/usr/share/icons/hicolor/scalable/status/key-single.svgz
/usr/share/kgpg/tips
/usr/share/kservices5/ServiceMenus/encryptfile.desktop
/usr/share/kservices5/ServiceMenus/encryptfolder.desktop
/usr/share/kservices5/ServiceMenus/viewdecrypted.desktop
/usr/share/kxmlgui5/kgpg/keysmanager.rc
/usr/share/kxmlgui5/kgpg/kgpgeditor.rc
/usr/share/metainfo/org.kde.kgpg.appdata.xml
/usr/share/xdg/autostart/org.kde.kgpg.desktop
/usr/share/xdg/kgpg.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kgpg/index.cache.bz2
/usr/share/doc/HTML/ca/kgpg/index.docbook
/usr/share/doc/HTML/de/kgpg/editor.png
/usr/share/doc/HTML/de/kgpg/index.cache.bz2
/usr/share/doc/HTML/de/kgpg/index.docbook
/usr/share/doc/HTML/de/kgpg/keygen.png
/usr/share/doc/HTML/de/kgpg/keymanage.png
/usr/share/doc/HTML/de/kgpg/keyprop.png
/usr/share/doc/HTML/de/kgpg/keys.png
/usr/share/doc/HTML/de/kgpg/keyserver-search.png
/usr/share/doc/HTML/de/kgpg/keyserver.png
/usr/share/doc/HTML/de/kgpg/options.png
/usr/share/doc/HTML/de/kgpg/select-secret-key.png
/usr/share/doc/HTML/en/kgpg/editor.png
/usr/share/doc/HTML/en/kgpg/index.cache.bz2
/usr/share/doc/HTML/en/kgpg/index.docbook
/usr/share/doc/HTML/en/kgpg/keygen.png
/usr/share/doc/HTML/en/kgpg/keymanage.png
/usr/share/doc/HTML/en/kgpg/keyprop.png
/usr/share/doc/HTML/en/kgpg/keys.png
/usr/share/doc/HTML/en/kgpg/keyserver-search.png
/usr/share/doc/HTML/en/kgpg/keyserver.png
/usr/share/doc/HTML/en/kgpg/options.png
/usr/share/doc/HTML/en/kgpg/select-secret-key.png
/usr/share/doc/HTML/en/kgpg/systray.png
/usr/share/doc/HTML/es/kgpg/editor.png
/usr/share/doc/HTML/es/kgpg/index.cache.bz2
/usr/share/doc/HTML/es/kgpg/index.docbook
/usr/share/doc/HTML/es/kgpg/keygen.png
/usr/share/doc/HTML/es/kgpg/keymanage.png
/usr/share/doc/HTML/es/kgpg/keys.png
/usr/share/doc/HTML/es/kgpg/options.png
/usr/share/doc/HTML/et/kgpg/index.cache.bz2
/usr/share/doc/HTML/et/kgpg/index.docbook
/usr/share/doc/HTML/fr/kgpg/index.cache.bz2
/usr/share/doc/HTML/fr/kgpg/index.docbook
/usr/share/doc/HTML/gl/kgpg/index.cache.bz2
/usr/share/doc/HTML/gl/kgpg/index.docbook
/usr/share/doc/HTML/it/kgpg/editor.png
/usr/share/doc/HTML/it/kgpg/index.cache.bz2
/usr/share/doc/HTML/it/kgpg/index.docbook
/usr/share/doc/HTML/it/kgpg/keygen.png
/usr/share/doc/HTML/it/kgpg/keymanage.png
/usr/share/doc/HTML/it/kgpg/keys.png
/usr/share/doc/HTML/it/kgpg/kicker.png
/usr/share/doc/HTML/it/kgpg/options.png
/usr/share/doc/HTML/lt/kgpg/index.cache.bz2
/usr/share/doc/HTML/lt/kgpg/index.docbook
/usr/share/doc/HTML/nl/kgpg/index.cache.bz2
/usr/share/doc/HTML/nl/kgpg/index.docbook
/usr/share/doc/HTML/pt/kgpg/index.cache.bz2
/usr/share/doc/HTML/pt/kgpg/index.docbook
/usr/share/doc/HTML/pt_BR/kgpg/editor.png
/usr/share/doc/HTML/pt_BR/kgpg/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kgpg/index.docbook
/usr/share/doc/HTML/pt_BR/kgpg/keygen.png
/usr/share/doc/HTML/pt_BR/kgpg/keymanage.png
/usr/share/doc/HTML/pt_BR/kgpg/keyprop.png
/usr/share/doc/HTML/pt_BR/kgpg/keys.png
/usr/share/doc/HTML/pt_BR/kgpg/keyserver-search.png
/usr/share/doc/HTML/pt_BR/kgpg/keyserver.png
/usr/share/doc/HTML/pt_BR/kgpg/options.png
/usr/share/doc/HTML/pt_BR/kgpg/select-secret-key.png
/usr/share/doc/HTML/pt_BR/kgpg/systray.png
/usr/share/doc/HTML/sr/kgpg/index.cache.bz2
/usr/share/doc/HTML/sr/kgpg/index.docbook
/usr/share/doc/HTML/sv/kgpg/editor.png
/usr/share/doc/HTML/sv/kgpg/index.cache.bz2
/usr/share/doc/HTML/sv/kgpg/index.docbook
/usr/share/doc/HTML/sv/kgpg/keygen.png
/usr/share/doc/HTML/sv/kgpg/keymanage.png
/usr/share/doc/HTML/sv/kgpg/keys.png
/usr/share/doc/HTML/sv/kgpg/options.png
/usr/share/doc/HTML/uk/kgpg/editor.png
/usr/share/doc/HTML/uk/kgpg/index.cache.bz2
/usr/share/doc/HTML/uk/kgpg/index.docbook
/usr/share/doc/HTML/uk/kgpg/keygen.png
/usr/share/doc/HTML/uk/kgpg/keymanage.png
/usr/share/doc/HTML/uk/kgpg/keyprop.png
/usr/share/doc/HTML/uk/kgpg/keys.png
/usr/share/doc/HTML/uk/kgpg/options.png
/usr/share/doc/HTML/uk/kgpg/select-secret-key.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kgpg/COPYING

%files locales -f kgpg.lang
%defattr(-,root,root,-)

