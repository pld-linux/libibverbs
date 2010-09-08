Summary:	Userspace driver for the Chelsio T3 iWARP RNIC
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla kart Chelsio T3 iWARP RNIC
Name:		libibverbs-driver-cxgb3
Version:	1.2.5
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	http://www.openfabrics.org/downloads/cxgb3/libcxgb3-%{version}.tar.gz
# Source0-md5:	ed2eaf99bc7cce401dd0549505febdd1
URL:		http://openib.org/
BuildRequires:	libibverbs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcxgb3 is a userspace driver for the Chelsio T3 iWARP RNIC. It works
as a plug-in module for libibverbs that allows programs to use Chelsio
RNICs directly from userspace.

%description -l pl.UTF-8
libcxgb3 to sterownik przestrzeni użytkownika dla kart Chelsio T3
iWARP RNIC. Działa jako moduł ładowany przez libibverbs, pozwalający
programom na dostęp z przestrzeni użytkownika do interfejsów RNIC
Chelsio.

%package static
Summary:	Static version of cxgb3 driver
Summary(pl.UTF-8):	Statyczna wersja sterownika cxgb3
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of cxgb3 driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika cxgb3, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libcxgb3-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcxgb3.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libcxgb3-rdmav2.so
%{_sysconfdir}/libibverbs.d/cxgb3.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libcxgb3.a
