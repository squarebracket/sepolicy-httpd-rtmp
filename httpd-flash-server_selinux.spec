# vim: sw=4:ts=4:et

%define selinux_policyver 0.0.0

Name:   nginx-module-rtmp-selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module that allows httpd_t to bind/communicate on flash_port_t

Group:	System Environment/Base		
License:	GPLv2+	
# This is an example. You will need to change it.
URL:		http://HOSTNAME
Source0:	httpd-flash-server.pp
Source1:	httpd-flash-server.if



Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
BuildArch: noarch

%description
This package installs and sets up the SELinux policy security module that allows
services running in the httpd_t domain to bind and communicate on the rtmp/flash
port (1935). In particular, it installs a boolean `httpd_enable_flash_server`
that, when enabled, allows httpd_t to do what it needs to do.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}%{_mandir}/man8/

install -d %{buildroot}/etc/selinux/targeted/contexts/users/


%post
semodule -n -i %{_datadir}/selinux/packages/httpd-flash-server.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    

fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r httpd-flash-server
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/httpd-flash-server.pp
%{_datadir}/selinux/devel/include/contrib/httpd-flash-server.if



%changelog
* Wed May 13 2020 YOUR NAME <YOUR@EMAILADDRESS> 1.0-1
- Initial version

