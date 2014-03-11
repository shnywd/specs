# $Id$
# Authority: shinya wada

Summary: package management system for ruby
Name: rubygems
Version: 1.8.25
Release: 1
License: GPL
BuildArch: %{_arch}
Group: Development/Libraries
URL: http://rubyforge.org/frs/?group_id=126

Source0: http://rubyforge.org/frs/download.php/76729/rubygems-1.8.25.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
rubygems is package management system for ruby.

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/var/lib/gems/1.8/
export GEM_HOME=%{buildroot}/var/lib/gems/1.8
ruby setup.rb --prefix=%{buildroot}/var/lib/gems/1.8

%check


%clean
%{__rm} -rf %{buildroot}


%post

%files 
/var/lib/gems/1.8

%changelog
