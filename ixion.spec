#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ixion
Version  : 0.15.0
Release  : 19
URL      : https://gitlab.com/ixion/ixion/-/archive/0.15.0/ixion-0.15.0.tar.gz
Source0  : https://gitlab.com/ixion/ixion/-/archive/0.15.0/ixion-0.15.0.tar.gz
Summary  : Generic formula computation library
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: ixion-bin = %{version}-%{release}
Requires: ixion-lib = %{version}-%{release}
Requires: ixion-license = %{version}-%{release}
Requires: ixion-python = %{version}-%{release}
Requires: ixion-python3 = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(mdds-1.5)
BuildRequires : pkgconfig(python3)
BuildRequires : pkgconfig(spdlog)

%description
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

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
%setup -q -n ixion-0.15.0
cd %{_builddir}/ixion-0.15.0

%build
## build_prepend content
bash autogen.sh
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592456554
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1592456554
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ixion
cp %{_builddir}/ixion-0.15.0/LICENSE %{buildroot}/usr/share/package-licenses/ixion/d22157abc0fc0b4ae96380c09528e23cf77290a9
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
/usr/include/libixion-0.15/ixion/address.hpp
/usr/include/libixion-0.15/ixion/address_iterator.hpp
/usr/include/libixion-0.15/ixion/cell.hpp
/usr/include/libixion-0.15/ixion/column_store_type.hpp
/usr/include/libixion-0.15/ixion/compute_engine.hpp
/usr/include/libixion-0.15/ixion/config.hpp
/usr/include/libixion-0.15/ixion/dirty_cell_tracker.hpp
/usr/include/libixion-0.15/ixion/env.hpp
/usr/include/libixion-0.15/ixion/exceptions.hpp
/usr/include/libixion-0.15/ixion/formula.hpp
/usr/include/libixion-0.15/ixion/formula_function_opcode.hpp
/usr/include/libixion-0.15/ixion/formula_name_resolver.hpp
/usr/include/libixion-0.15/ixion/formula_opcode.hpp
/usr/include/libixion-0.15/ixion/formula_result.hpp
/usr/include/libixion-0.15/ixion/formula_tokens.hpp
/usr/include/libixion-0.15/ixion/formula_tokens_fwd.hpp
/usr/include/libixion-0.15/ixion/global.hpp
/usr/include/libixion-0.15/ixion/info.hpp
/usr/include/libixion-0.15/ixion/interface/formula_model_access.hpp
/usr/include/libixion-0.15/ixion/interface/session_handler.hpp
/usr/include/libixion-0.15/ixion/interface/table_handler.hpp
/usr/include/libixion-0.15/ixion/macros.hpp
/usr/include/libixion-0.15/ixion/matrix.hpp
/usr/include/libixion-0.15/ixion/mem_str_buf.hpp
/usr/include/libixion-0.15/ixion/model_context.hpp
/usr/include/libixion-0.15/ixion/model_iterator.hpp
/usr/include/libixion-0.15/ixion/module.hpp
/usr/include/libixion-0.15/ixion/table.hpp
/usr/include/libixion-0.15/ixion/types.hpp
/usr/lib64/libixion-0.15.so
/usr/lib64/pkgconfig/libixion-0.15.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libixion-0.15.so.0
/usr/lib64/libixion-0.15.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ixion/d22157abc0fc0b4ae96380c09528e23cf77290a9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
