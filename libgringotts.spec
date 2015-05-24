Summary:	Small library to encapsulate data in an encrypted structure
Summary(pl.UTF-8):	Mała biblioteka do hermetyzacji danych w zaszyfrowanej strukturze
Name:		libgringotts
Version:	1.2.1
Release:	6
License:	GPL
Group:		Libraries
Source0:	http://prdownload.berlios.de/gringotts/%{name}-%{version}.tar.bz2
# Source0-md5:	ccea1078679d79c924842fad40de4102
URL:		http://gringotts.berlios.de/
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

%description -l pl.UTF-8
libGringotts jest biblioteką C nadającą się do użytku w programach
wielowątkowych, która pozwala na zapisywanie danych w konkretnych
formatach plików. Dane są kompresowane, szyfrowane silnym algorytmem
i zapisywane na dysku w bezpieczny sposób. Biblioteka ta daje kontrolę
nad każdym użytym algorytmem i udostępnia dodatkowe, bezpieczne
funkcje użytkowe.

%package devel
Summary:	Headers for libgringotts
Summary(pl.UTF-8):	Pliki nagłówkowe libgringotts
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Files needed to develop applications with libGringotts.

%description devel -l pl.UTF-8
Pliki potrzebne do tworzenia aplikacji używających libGringotts.

%package static
Summary:	Static version of libgringotts
Summary(pl.UTF-8):	Statyczna wersja libgringotts
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	bzip2-devel
Requires:	libmcrypt-devel
Requires:	mhash-devel
Requires:	zlib-devel

%description static
Static version of libgringotts.

%description static -l pl.UTF-8
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

# docdir was not empty
rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO docs/manual.htm
%attr(755,root,root) %{_libdir}/libgringotts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgringotts.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
