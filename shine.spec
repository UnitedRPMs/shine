%global commit0 97f188efc3dc90315b79a2af1f477c0c18d85e82
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           shine
Version:        3.1.1
Release:    	1%{?gver}%{dist}
Summary:        Super fast fixed-point MP3 encoder

Group:          System Environment/Libraries
License:        GPLv2
URL:            https://github.com/savonet/shine
Source:         https://github.com/toots/shine/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake 
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}

%description
shine is a blazing fast mp3 encoding library implemented in fixed-point 
arithmetic. The library can thus be used to performe super fast mp3 encoding 
on architectures without a FPU, such as armel, etc.

%package libs
Summary: shine library
Group: Development/Libraries

%description libs
This package contains the shared library file.

%package devel
Summary: shine development
Group: Development/Libraries
Requires:  %{name} = %{version}-%{release}

%description devel
This package contains the development files.

%prep
%autosetup -n %{name}-%{commit0}


%build
./bootstrap
%configure
make 

%install
%make_install

rm -f %{buildroot}/%{_libdir}/libshine.a
rm -f %{buildroot}/%{_libdir}/libshine.la

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/shineenc

%files libs
%{_libdir}/libshine.so
%{_libdir}/libshine.so.3
%{_libdir}/libshine.so.3.0.1

%files devel
%{_includedir}/%{name}/layer3.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog

* Wed Oct 25 2017 David Vasquez <davidva at tutanota dot com> 3.1.1-1.git97f188e
- Initial build rpm
