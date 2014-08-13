# $Id$
# Authority: shinya wada

Summary: ruby is object oriented script language
Name: ruby
Version: 2.1.1
Release: 1 
License: GPL
BuildArch: x86_64
Group: Development
URL: http://www.ruby-lang.org/ja/

Source0: ruby-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
ruby is object oriented script language

%prep
%setup -q -n ruby-%{version}

%build
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/ruby-%{version}
./configure --prefix=/usr/local/ruby-%{version}
make 

%install
make install DESTDIR=%{buildroot}

%check

%clean
%{__rm} -rf %{buildroot}


%post
cd /usr/local/
ln -s ruby-%{version} ruby

%files 
/usr/local/bin/ruby
/usr/local/bin/erb
/usr/local/bin/irb
/usr/local/bin/gem
/usr/local/bin/rdoc
/usr/local/bin/rake
/usr/local/bin/testrb
/usr/local/bin/ri
/usr/local/lib/ruby/gems/2.1.0
/usr/local/lib/ruby/2.1.0
/usr/local/lib/libruby-static.a
/usr/local/lib/pkgconfig/ruby-2.1.pc
/usr/local/share/doc/ruby
/usr/local/share/ri/2.1.0
/usr/local/share/man/man1/ruby.1
/usr/local/share/man/man1/rake.1
/usr/local/share/man/man1/ri.1
/usr/local/share/man/man1/irb.1
/usr/local/share/man/man1/erb.1
/usr/local/include/ruby-2.1.0
%changelog
