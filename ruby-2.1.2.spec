# $Id$
# Authority: shinya wada

Summary: ruby is object oriented script language
Name: ruby
Version: 2.1.2
Release: 1 
License: GPL
BuildArch: x86_64
Group: Development
URL: http://www.ruby-lang.org/ja/

Source0: ruby-%{version}.tar.gz
#BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
ruby is object oriented script language

%prep
%setup -q -n ruby-%{version}

%build
%{__rm} -rf %{buildroot}
./configure
make 

%install
make install DESTDIR=%{buildroot}

%check

%clean
%{__rm} -rf %{buildroot}

%files 
/usr/local/ruby-%{version}

%changelog
