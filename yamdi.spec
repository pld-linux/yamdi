Summary:	Yet Another MetaData Injector for FLV
Summary(pl.UTF-8):	Kolejny iniektor metadanych dla FLV
Name:		yamdi
Version:	1.4
Release:	1
License:	Other
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/yamdi/%{name}-%{version}.tar.gz
# Source0-md5:	aaca43b47a4541564ee84ef1e3a22b04
URL:		http://yamdi.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yamdi stands for Yet Another MetaData Injector and is a metadata
injector for FLV files. It adds the onMetaData event to your FLV
files.

%description -l pl.UTF-8
yamdi to rozwiniecie anglojęzycznego skrótu Yet Another MetaData
Injector czyli Kolejny Iniektor Metadanych dla formatu FLV. Program
dodaje zdarzenia onMetaData do plikow FLV.

%prep
%setup -q

%build
%{__cc} yamdi.c -o yamdi %{rpmcflags} -Wall -D_FILE_OFFSET_BITS=64

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install yamdi $RPM_BUILD_ROOT%{_bindir}/yamdi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{_bindir}/*
