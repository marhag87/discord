Name:           discord
Version:        0.0.2
Release:        2%{?dist}
Summary:        All-in-one voice and text chat

License:        Copyright only
URL:            https://discordapp.com
Source0:        https://dl.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
AutoReqProv:    No
Obsoletes:      discord-canary

Requires:       libcxx

# Don't build debug package
%define debug_package %{nil}

%define discorddir /opt/%{name}

%description
All-in-one voice and text chat for gamers that's free,
secure, and works on both your desktop and phone.

%prep
%setup -q -n "Discord"

%build

%install
install -p -d -m 0755 %{buildroot}%{discorddir}
mv * %{buildroot}%{discorddir}/
mkdir -p %{buildroot}%{_bindir}
ln -fs %{discorddir}/Discord %{buildroot}%{_bindir}/discord

%files
%{discorddir}
%{_bindir}/discord

%changelog
* Wed Aug 23 2017 Martin Hagstrom <marhag87@gmail.com> 0.0.2-2
- Added requirement libcxx
* Wed Aug 23 2017 Martin Hagstrom <marhag87@gmail.com> 0.0.2-1
- Update to 0.0.2
* Wed Feb 01 2017 Martin Hagstrom <marhag87@gmail.com> 0.0.1-2
Discord-canary should always be obsolete, regardless of version
* Wed Jan 11 2017 Martin Hagstrom <marhag87@gmail.com> 0.0.1-1
- Initial release
