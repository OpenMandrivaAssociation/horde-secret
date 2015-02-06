%define prj    Horde_Secret

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-secret
Version:       0.0.2
Release:       16
Summary:       Secret Encryption API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-framework
Requires:      horde-cipher
Requires:      horde-util
Requires:      php-mcrypt
Requires:      php-pear-channel-horde
Requires:      php-pear
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
The Secret:: class provides an API for encrypting and decrypting small
pieces of data with the use of a shared key.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%{peardir}/Horde/Secret.php


%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-15mdv2011.0
+ Revision: 564081
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-14mdv2010.1
+ Revision: 523034
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Sat Mar 06 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-13mdv2010.1
+ Revision: 514882
- replaced requires php-pear5 with php-pear

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-12mdv2010.1
+ Revision: 509366
- removed Buildrequires: horder-framework
- replace PreReq with Requires(pre)
- Initial import


