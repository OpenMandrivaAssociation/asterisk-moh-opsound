%undefine __find_provides
%undefine __find_requires

Summary:	Free music files for the Asterisk PBX and telephony application and toolkit
Name:		asterisk-moh-opsound
Version:	20091226
Release:	3
License:	GPL
Group:		System/Servers
URL:		http://www.asterisk.org/
#for I in alaw g722 g729 gsm siren7 siren14 sln16 ulaw wav ; do wget -c http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-$I.tar.gz -P SOURCES ; done
Source0:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-alaw.tar.gz
Source1:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-g722.tar.gz
Source2:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-g729.tar.gz
Source3:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-gsm.tar.gz
Source4:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-siren7.tar.gz
Source5:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-siren14.tar.gz
Source6:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-sln16.tar.gz
Source7:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-ulaw.tar.gz
Source8:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-wav.tar.gz
Requires:	asterisk
Provides:	asterisk-moh-freeplay
Provides:	asterisk-moh
Obsoletes:	asterisk-moh-freeplay
BuildArch:	noarch

%description
Asterisk is an Open Source PBX and telephony development platform that can both
replace a conventional PBX and act as a platform for developing custom
telephony applications for delivering dynamic content over a telephone
similarly to how one can deliver dynamic content through a web browser using
CGI and a web server.
 
Asterisk talks to a variety of telephony hardware including BRI, PRI, POTS, and
IP telephony clients using the Inter-Asterisk eXchange protocol (e.g. gnophone
or miniphone).

This package contains freely usable music sounds that were meant to be used
with Asterisk in the following formats: a-Law, G.722, G.729, GSM, Siren7, 
Siren14, sln16, mu-Law, WAV

%prep

%setup -q -c -T -n %{name} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8

# fix dir perms
find . -type d | xargs chmod 755
    
# fix file perms
find . -type f | xargs chmod 644

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build

mv CHANGES-asterisk-moh-opsound-wav CHANGES
mv CREDITS-asterisk-moh-opsound-wav CREDITS
mv LICENSE-asterisk-moh-opsound-wav LICENSE

%install
rm -rf %{buildroot}

install -d %{buildroot}/var/lib/asterisk/moh
cp -aRf * %{buildroot}/var/lib/asterisk/moh/

# cleanup
rm -f %{buildroot}/var/lib/asterisk/moh/{CHANGES,CREDITS,LICENSE}*

# make a file list
find %{buildroot}/var/lib/asterisk/moh -type f | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(0644,root,root) /' >> %{name}.filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.filelist
%defattr(-,root, root)
%doc CHANGES CREDITS LICENSE


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 20091226-2mdv2011.0
+ Revision: 610000
- rebuild

* Wed Jan 06 2010 Lonyai Gergely <aleph@mandriva.org> 20091226-1mdv2010.1
+ Revision: 486659
- Date: 20091226
  Version: 2.03

* Wed Aug 19 2009 Lonyai Gergely <aleph@mandriva.org> 20090818-1mdv2010.0
+ Revision: 417941
- initial package
- create asterisk-moh-opsound

