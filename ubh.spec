%include	/usr/lib/rpm/macros.perl
Summary:	The Usenet Binary Harvester
Summary(pl.UTF-8):   Usenetowy żniwiarz binariów
Name:		ubh
Version:	2.5
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://ubh.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	3e16a79b92da43318924587df4e0dc3b
URL:		http://ubh.sourceforge.net/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ubh - the Usenet Binary Harvester - is a GPL'ed Perl console
application which automatically discovers, downloads, and decodes
single-part and multi-part Usenet binaries. Automatically assembles
multi-part binaries. Provides searching via Perl regular expression
syntax. Also provides a pre-selection capability whereby the user can
interactively choose which binaries to download. Uses a standard
.newsrc file to control which groups to process, and uses the .newsrc
to keep track of articles already processed. Handles uuencoded
binaries and MIME attachments.

%description -l pl.UTF-8
ubh - usenetowy żniwiarz binarek jest perlową aplikacją działającą na
konsoli która automatycznie rozpoznaje, ściąga i dekoduje pojedyncze i
wieloczęściowe binaria zamieszczone w usenecie. Wieloczęściowe
przesyłki są automatycznie łączone. Obsługuje wyszukiwanie przez
perlową składnię wyrażeń regularnych. Pozwala także na wstępny wybór
możliwości gdzie użytkownik może sam wybrać binaria do ściągnięcia.
Wykorzystuje standardowy plik .newsrc to kontrolowania używanych grup
i śledzenia które artykuły zostały już przetworzone. Obsługuje
uuencodowane binaria i załączniki MIME.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ubh contrib/mydecode contrib/newshark $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO examples doc/*
%attr(755,root,root) %{_bindir}/*
