# $Id$
# Authority: shinya wada

Summary: ruby is object oriented script language
Name: ruby
Version: 2.0.0
Release: p0
License: GPL
BuildArch: x86_64
Group: Development
URL: http://www.ruby-lang.org/ja/

Source0: http://ftp.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ruby is object oriented script language

%prep
%setup -q -n ruby-%{version}-%{release}

%build
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/ruby-%{version}-%{release}
./configure --prefix=/usr/local/ruby-%{version}-%{release}
make 

%install
make install DESTDIR=%{buildroot}

%check

%clean
%{__rm} -rf %{buildroot}


%post
cd /usr/local/
ln -s ruby-%{version}-%{release} ruby

%files 
/usr/local/ruby-%{version}-%{release}

%changelog
