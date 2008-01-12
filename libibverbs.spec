Summary:	A library for direct userspace use of InfiniBand hardware
Summary(pl.UTF-8):	Biblioteka bezpośredniego dostępu do sprzętu InfiniBand z przestrzeni użytkownika
Name:		libibverbs
Version:	1.1.1
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	http://openib.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	2bf5c8f089a97a5e70701edc22066137
URL:		http://openib.org/
BuildRequires:	rpmbuild(macros) >= 1.402
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libibverbs is a library that allows userspace processes to use
InfiniBand "verbs" as described in the InfiniBand Architecture
Specification. This includes direct hardware access for fast path
operations.

For this library to be useful, a device-specific plug-in module should
also be installed.

%description -l pl.UTF-8
libibverbs to biblioteka pozwalająca procesom przestrzeni użytkownika
używać metod "verbs" InfiniBand opisanej w specyfikacji architektury
InfiniBand. Obejmuje to bezpośredni dostęp do sprzętu dla operacji po
szybkiej ścieżce.

Aby ta biblioteka była użyteczna powinien być zainstalowany także
odpowiedni moduł dla używanego sprzętu.

%package devel
Summary:	Development files for libibverbs library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libibverbs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libibverbs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libibverbs.

%package static
Summary:	Static libibverbs library
Summary(pl.UTF-8):	Statyczna biblioteka libibverbs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libibverbs-devel-static

%description static
Static libibverbs library.

%description static -l pl.UTF-8
Statyczna biblioteka libibverbs.

%package utils
Summary:	Examples for the libibverbs library
Summary(pl.UTF-8):	Przykładowe programy do biblioteki libibverbs
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description utils
Useful libibverbs example programs such as ibv_devinfo, which
displays information about InfiniBand devices.

%description utils -l pl.UTF-8
Przydatne programy przykładowe do biblioteki libibverbs, takie jak
ibv_devinfo wyświetlający informacje o urządzeniach InfiniBand.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libibverbs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibverbs.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibverbs.so
%{_libdir}/libibverbs.la
%{_includedir}/infiniband
%{_mandir}/man3/ibv_*.3*
%{_mandir}/man3/mult_to_ibv_rate.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libibverbs.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ibv_*
%{_mandir}/man1/ibv_*.1*
