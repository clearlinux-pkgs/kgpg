#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kgpg
Version  : 24.12.3
Release  : 37
URL      : https://download.kde.org/stable/release-service/24.12.3/src/kgpg-24.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.3/src/kgpg-24.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.3/src/kgpg-24.12.3.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: kgpg-bin = %{version}-%{release}
Requires: kgpg-data = %{version}-%{release}
Requires: kgpg-license = %{version}-%{release}
Requires: kgpg-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : grantleetheme-dev
BuildRequires : kcontacts-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kmbox-dev
BuildRequires : knotifications-dev
BuildRequires : kservice-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : libkdepim-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gpgme)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kgpg-24.12.3
cd %{_builddir}/kgpg-24.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742540925
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742540925
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kgpg
cp %{_builddir}/kgpg-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kgpg/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kgpg-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kgpg/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kgpg-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kgpg/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/kgpg-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kgpg/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kgpg-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kgpg/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
GOAMD64=v2
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
/usr/share/kio/servicemenus/kgpg_encryptfile.desktop
/usr/share/kio/servicemenus/kgpg_encryptfolder.desktop
/usr/share/kio/servicemenus/kgpg_viewdecrypted.desktop
/usr/share/metainfo/org.kde.kgpg.appdata.xml
/usr/share/qlogging-categories6/kgpg.categories
/usr/share/xdg/autostart/org.kde.kgpg.desktop

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
/usr/share/doc/HTML/es/kgpg/index.cache.bz2
/usr/share/doc/HTML/es/kgpg/index.docbook
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
/usr/share/doc/HTML/it/kgpg/keyprop.png
/usr/share/doc/HTML/it/kgpg/keys.png
/usr/share/doc/HTML/it/kgpg/keyserver-search.png
/usr/share/doc/HTML/it/kgpg/keyserver.png
/usr/share/doc/HTML/it/kgpg/kicker.png
/usr/share/doc/HTML/it/kgpg/options.png
/usr/share/doc/HTML/it/kgpg/select-secret-key.png
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
/usr/share/doc/HTML/ru/kgpg/index.cache.bz2
/usr/share/doc/HTML/ru/kgpg/index.docbook
/usr/share/doc/HTML/sl/kgpg/index.cache.bz2
/usr/share/doc/HTML/sl/kgpg/index.docbook
/usr/share/doc/HTML/sr/kgpg/index.cache.bz2
/usr/share/doc/HTML/sr/kgpg/index.docbook
/usr/share/doc/HTML/sr@latin/kgpg/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kgpg/index.docbook
/usr/share/doc/HTML/sv/kgpg/editor.png
/usr/share/doc/HTML/sv/kgpg/index.cache.bz2
/usr/share/doc/HTML/sv/kgpg/index.docbook
/usr/share/doc/HTML/sv/kgpg/keygen.png
/usr/share/doc/HTML/sv/kgpg/keymanage.png
/usr/share/doc/HTML/sv/kgpg/keys.png
/usr/share/doc/HTML/sv/kgpg/options.png
/usr/share/doc/HTML/tr/kgpg/index.cache.bz2
/usr/share/doc/HTML/tr/kgpg/index.docbook
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
/usr/share/package-licenses/kgpg/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/kgpg/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kgpg/7d9831e05094ce723947d729c2a46a09d6e90275

%files locales -f kgpg.lang
%defattr(-,root,root,-)

