# $Id$
# Authority: shinya wada

Summary: Squid is a caching proxy for the Web supporting HTTP, HTTPS, FTP, and more.
Name: squid
Version: 3.4.1
Release: 1
License: GPL
BuildArch: x86_64
Group: Web Server
URL: http://www.squid-cache.org/

Source0: http://www.squid-cache.org/Versions/v3/3.4/squid-3.4.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Squid is a caching proxy for the Web supporting HTTP, HTTPS, FTP, and more. It reduces bandwidth and improves response times by caching and reusing frequently-requested web pages. Squid has extensive access controls and makes a great server accelerator. It runs on most available operating systems, including Windows and is licensed under the GNU GPL.

%prep
%setup -q

%build
%{__rm} -rf %{buildroot}
./configure --prefix=/usr \
  --includedir=/usr/include \
  --datadir=/usr/share \
  --bindir=/usr/sbin \
  --libexecdir=/usr/lib/squid \
  --localstatedir=/var \
  --sysconfdir=/etc/squid

make

%install
make install DESTDIR=%{buildroot}

%check

%clean
%{__rm} -rf %{buildroot}

%pre
grep "^squid:" /etc/group
if [ $? -eq 1 ] then ;
  groupadd squid
fi

grep "^squid:" /etc/passwd
if [ $? -eq 1 ] then ;
  useradd squid -g squid
fi
%post

%files 
%defattr(-,root,root)
/usr/lib/squid/*
/usr/sbin/*
/usr/share/mib.txt
/usr/share/errors/*
/usr/share/icons/*
/usr/share/man/*
%attr(0664,squid,squid) /var/cache/squid
%attr(0664,squid,squid) /var/run/squid
%config /etc/squid

%changelog


