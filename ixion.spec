#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v2
# autospec commit: f032afc
#
Name     : ixion
Version  : 0.18.1
Release  : 31
URL      : https://gitlab.com/ixion/ixion/-/archive/0.18.1/ixion-0.18.1.tar.gz
Source0  : https://gitlab.com/ixion/ixion/-/archive/0.18.1/ixion-0.18.1.tar.gz
Summary  : Generic formula computation library
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: ixion-bin = %{version}-%{release}
Requires: ixion-lib = %{version}-%{release}
Requires: ixion-license = %{version}-%{release}
Requires: ixion-python = %{version}-%{release}
Requires: ixion-python3 = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : pkgconfig(mdds-2.1)
BuildRequires : pkgconfig(python3)
BuildRequires : pkgconfig(vulkan)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Ixion is a general purpose formula parser, interpreter, formula cell dependency
tracker and spreadsheet document model backend all in one package.

%package bin
Summary: bin components for the ixion package.
Group: Binaries
Requires: ixion-license = %{version}-%{release}

%description bin
bin components for the ixion package.


%package dev
Summary: dev components for the ixion package.
Group: Development
Requires: ixion-lib = %{version}-%{release}
Requires: ixion-bin = %{version}-%{release}
Provides: ixion-devel = %{version}-%{release}
Requires: ixion = %{version}-%{release}

%description dev
dev components for the ixion package.


%package lib
Summary: lib components for the ixion package.
Group: Libraries
Requires: ixion-license = %{version}-%{release}

%description lib
lib components for the ixion package.


%package license
Summary: license components for the ixion package.
Group: Default

%description license
license components for the ixion package.


%package python
Summary: python components for the ixion package.
Group: Default
Requires: ixion-python3 = %{version}-%{release}

%description python
python components for the ixion package.


%package python3
Summary: python3 components for the ixion package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ixion package.


%prep
%setup -q -n ixion-0.18.1
cd %{_builddir}/ixion-0.18.1

%build
## build_prepend content
bash autogen.sh
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697584722
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697584722
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ixion
cp %{_builddir}/ixion-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/ixion/d22157abc0fc0b4ae96380c09528e23cf77290a9 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ixion-formula-tokenizer
/usr/bin/ixion-parser
/usr/bin/ixion-sorter

%files dev
%defattr(-,root,root,-)
/usr/include/libixion-0.18/ixion/address.hpp
/usr/include/libixion-0.18/ixion/address_iterator.hpp
/usr/include/libixion-0.18/ixion/cell.hpp
/usr/include/libixion-0.18/ixion/cell_access.hpp
/usr/include/libixion-0.18/ixion/compute_engine.hpp
/usr/include/libixion-0.18/ixion/config.hpp
/usr/include/libixion-0.18/ixion/dirty_cell_tracker.hpp
/usr/include/libixion-0.18/ixion/document.hpp
/usr/include/libixion-0.18/ixion/env.hpp
/usr/include/libixion-0.18/ixion/exceptions.hpp
/usr/include/libixion-0.18/ixion/formula.hpp
/usr/include/libixion-0.18/ixion/formula_function_opcode.hpp
/usr/include/libixion-0.18/ixion/formula_name_resolver.hpp
/usr/include/libixion-0.18/ixion/formula_opcode.hpp
/usr/include/libixion-0.18/ixion/formula_result.hpp
/usr/include/libixion-0.18/ixion/formula_tokens.hpp
/usr/include/libixion-0.18/ixion/formula_tokens_fwd.hpp
/usr/include/libixion-0.18/ixion/global.hpp
/usr/include/libixion-0.18/ixion/info.hpp
/usr/include/libixion-0.18/ixion/interface/session_handler.hpp
/usr/include/libixion-0.18/ixion/interface/table_handler.hpp
/usr/include/libixion-0.18/ixion/macros.hpp
/usr/include/libixion-0.18/ixion/matrix.hpp
/usr/include/libixion-0.18/ixion/model_context.hpp
/usr/include/libixion-0.18/ixion/model_iterator.hpp
/usr/include/libixion-0.18/ixion/module.hpp
/usr/include/libixion-0.18/ixion/named_expressions_iterator.hpp
/usr/include/libixion-0.18/ixion/table.hpp
/usr/include/libixion-0.18/ixion/types.hpp
/usr/lib64/libixion-0.18.so
/usr/lib64/pkgconfig/libixion-0.18.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libixion-0.18.so.0
/usr/lib64/libixion-0.18.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ixion/d22157abc0fc0b4ae96380c09528e23cf77290a9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
