Summary:	Userspace driver for the Chelsio T4 iWARP RNIC
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla kart Chelsio T4 iWARP RNIC
Name:		libibverbs-driver-cxgb4
Version:	1.0.4
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	http://www.openfabrics.org/downloads/cxgb4/libcxgb4-%{version}.tar.gz
# Source0-md5:	f89729fe33fc69cefdff8d62ae867783
URL:		http://openib.org/
BuildRequires:	libibverbs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcxgb4 is a userspace driver for the Chelsio T4 iWARP RNIC. It works
as a plug-in module for libibverbs that allows programs to use Chelsio
RNICs directly from userspace.

%description -l pl.UTF-8
libcxgb4 to sterownik przestrzeni użytkownika dla kart Chelsio T4
iWARP RNIC. Działa jako moduł ładowany przez libibverbs, pozwalający
programom na dostęp z przestrzeni użytkownika do interfejsów RNIC
Chelsio.

%package static
Summary:	Static version of cxgb4 driver
Summary(pl.UTF-8):	Statyczna wersja sterownika cxgb4
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of cxgb4 driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika cxgb4, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libcxgb4-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcxgb4.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libcxgb4-rdmav2.so
%{_sysconfdir}/libibverbs.d/cxgb4.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libcxgb4.a
