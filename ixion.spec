#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ixion
Version  : 0.13.0
Release  : 1
URL      : https://gitlab.com/ixion/ixion/-/archive/0.13.0/ixion-0.13.0.tar.gz
Source0  : https://gitlab.com/ixion/ixion/-/archive/0.13.0/ixion-0.13.0.tar.gz
Summary  : Generic formula computation library
Group    : Development/Tools
License  : MPL-2.0
Requires: ixion-bin
Requires: ixion-python3
Requires: ixion-lib
Requires: ixion-license
Requires: ixion-python
BuildRequires : boost-dev
BuildRequires : pkgconfig(mdds-1.2)
BuildRequires : pkgconfig(python3)

%description
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package bin
Summary: bin components for the ixion package.
Group: Binaries
Requires: ixion-license

%description bin
bin components for the ixion package.


%package dev
Summary: dev components for the ixion package.
Group: Development
Requires: ixion-lib
Requires: ixion-bin
Provides: ixion-devel

%description dev
dev components for the ixion package.


%package lib
Summary: lib components for the ixion package.
Group: Libraries
Requires: ixion-license

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
Requires: ixion-python3

%description python
python components for the ixion package.


%package python3
Summary: python3 components for the ixion package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ixion package.


%prep
%setup -q -n ixion-0.13.0

%build
## build_prepend content
bash autogen.sh
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534606019
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534606019
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ixion
cp LICENSE %{buildroot}/usr/share/doc/ixion/LICENSE
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
/usr/include/libixion-0.13/ixion/address.hpp
/usr/include/libixion-0.13/ixion/cell.hpp
/usr/include/libixion-0.13/ixion/cell_listener_tracker.hpp
/usr/include/libixion-0.13/ixion/column_store_type.hpp
/usr/include/libixion-0.13/ixion/config.hpp
/usr/include/libixion-0.13/ixion/depth_first_search.hpp
/usr/include/libixion-0.13/ixion/env.hpp
/usr/include/libixion-0.13/ixion/exceptions.hpp
/usr/include/libixion-0.13/ixion/formula.hpp
/usr/include/libixion-0.13/ixion/formula_function_opcode.hpp
/usr/include/libixion-0.13/ixion/formula_name_resolver.hpp
/usr/include/libixion-0.13/ixion/formula_opcode.hpp
/usr/include/libixion-0.13/ixion/formula_result.hpp
/usr/include/libixion-0.13/ixion/formula_tokens.hpp
/usr/include/libixion-0.13/ixion/global.hpp
/usr/include/libixion-0.13/ixion/info.hpp
/usr/include/libixion-0.13/ixion/interface/formula_model_access.hpp
/usr/include/libixion-0.13/ixion/interface/session_handler.hpp
/usr/include/libixion-0.13/ixion/interface/table_handler.hpp
/usr/include/libixion-0.13/ixion/macros.hpp
/usr/include/libixion-0.13/ixion/matrix.hpp
/usr/include/libixion-0.13/ixion/mem_str_buf.hpp
/usr/include/libixion-0.13/ixion/model_context.hpp
/usr/include/libixion-0.13/ixion/table.hpp
/usr/include/libixion-0.13/ixion/types.hpp
/usr/lib64/libixion-0.13.so
/usr/lib64/pkgconfig/libixion-0.13.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libixion-0.13.so.0
/usr/lib64/libixion-0.13.so.0.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/ixion/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
