Name:		timebot
Version:	0.1
Release:	1%{?dist}
Summary:	This is a web time bot

License:	GNU GPL 2
Source0:	timebot.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	grep,sed,initscripts,chkconfig,java-1.8.0-openjdk

%description
This is a web time bot to get host localtime

%prep
%setup -c 

%install
rm -rf %{buildroot}
mkdir %{buildroot}
cp -R * %{buildroot}

%check
../../test.sh $(pwd)/usr/lib/timebot/timebot.jar

%clean
rm -rf %{buildroot}


%files
%defattr(640,timebot,timebot,750)
/usr/lib/timebot
%attr(440,-,-) /usr/lib/timebot/timebot.jar
%attr(0750,-,-) %{_initrddir}/timebot
%doc

# 1 - install
# 2 - upgrade
%pre
if [ "$1" -eq 1 ]; then
	id timebot &>/dev/null || useradd timebot || exit 1
	if ! grep 8080 /etc/sysconfig/iptables | grep "-j ACCEPT" &>/dev/null; then
		chainName=$(grep -hE "^\-A.*INPUT" /etc/sysconfig/iptables | grep lo | head -1 | cut -d' ' -f2)
		{ [ -n "$chainName" ] && \
			sed "/-A \(.*\) .*-i lo.*-j ACCEPT/{s/$/\n-A $chainName -m state --state NEW -m tcp -p tcp --dport 8080 -j ACCEPT/}" \
			-i /etc/sysconfig/iptables && cat /etc/sysconfig/iptables | iptables-restore; } \
			|| echo "Port 8080 to firewall exaption" # may be no iptable
		logfile=/var/log/timebot.log
		touch $logfile && chown timebot:timebot $logfile && chmod 640 $logfile
	fi
fi

# 1 - install
# 2 - upgrade
%post
chkconfig --add timebot


# 0 - uninstall
# 1 - upgrade
%preun
[ "$1" -eq 0 ] && /sbin/service timebot stop &>/dev/null || :


# 0 - uninstall
# 1 - upgrade
%postun
[ "$1" -ge 1 ] && /sbin/service timebot condrestart &>/dev/null
if [ "$1" -eq 0 ]; then
	userdel timebot
	{ sed '/--dport 8080/d' -i /etc/sysconfig/iptables && cat /etc/sysconfig/iptables | iptables-restore; \
		} || echo "Please, delete port 8080 from filewall"
	rm -f /var/log/timebot.log*
fi


%changelog

