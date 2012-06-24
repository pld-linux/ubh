%include        /usr/lib/rpm/macros.perl
Summary:	The Usenet Binary Harvester
Summary(pl):	Usenetowy �niwiarz
Name:		ubh
Version:	2.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://ubh.sourceforge.net/download/%{name}-%{version}.tar.gz
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

%description -l pl
ubh - Usenetowy �niwiarz Binarek jest perlow� aplikacj� dzia�aj�c� na
konsoli kt�ra automatycznie rozpoznaje, �ci�ga i dekoduje pojedy�cze i
wielocz�ciowe binaria zamieszczone w usenecie. Wielocz�ciowe
przesy�ki s� automatycznie ��czone. Obs�uguje wyszukiwanie przez
perlow� sk�adni� wyra�e� regularnych. Pozwala tak�e na wst�pny wyb�r
mo�liwo�ci gdzie u�ytkownik mo�e sam wybra� binaria do �ci�gni�cia.
Wykorzystuje standardowy plik .newsrc to kontrolowania u�ywanych grup
i �ledzenia kt�re artyku�y zosta�y ju� przetworzone. Obs�uguje
uuencodowane binaria i za��czniki MIME.

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
