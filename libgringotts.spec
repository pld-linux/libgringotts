Summary:	Small library to encapsulate data in an encrypted structure
Summary(pl):	Ma³a biblioteka do hermetyzacji danych w zaszyfrowanej strukturze
Name:		libgringotts
Version:	1.2.1
Release:	4
License:	GPL
Group:		Libraries
Source0:	http://devel.pluto.linux.it/projects/libGringotts/current/%{name}-%{version}.tar.bz2
# Source0-md5:	ccea1078679d79c924842fad40de4102
URL:		http://devel.pluto.linux.it/projects/libGringotts/index.php
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libmcrypt-devel
BuildRequires:	mhash-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libGringotts is a thread-safe C library that allows the programmer to
save data in a particular file format. The data are compressed and
encrypted with a strong encryption algorithm, and saved to the disk in
a secure way. The library gives control over every algorithm involved
in the process, and provides additional security-related utility
functions.

%description -l pl
libGringotts jest bibliotek± C nadaj±c± siê do u¿ytku w programach
wielow±tkowych, która pozwala na zapisywanie danych w konkretnych
formatach plików. Dane s± kompresowane, szyfrowane silnym algorytmem
i zapisywane na dysku w bezpieczny sposób. Biblioteka ta daje kontrolê
nad ka¿dym u¿ytym algorytmem i udostêpnia dodatkowe, bezpieczne
funkcje u¿ytkowe.

%package devel
Summary:	Headers for libgringotts
Summary(pl):	Pliki nag³ówkowe libgringotts
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Files needed to develop applications with libGringotts.

%description devel -l pl
Pliki potrzebne do tworzenia aplikacji u¿ywaj±cych libGringotts.

%package static
Summary:	Static version of libgringotts
Summary(pl):	Statyczna wersja libgringotts
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	bzip2-devel
Requires:	libmcrypt-devel
Requires:	mhash-devel
Requires:	zlib-devel

%description static
Static version of libgringotts.

%description static -l pl
Statyczna wersja libgringotts.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf libgringotts.so.2.0.7 \
	$RPM_BUILD_ROOT%{_libdir}/libgringotts.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/libgringotts.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
