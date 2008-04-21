%define name stormbaancoureur
%define version	2.1.4
%define release %mkrel 1

Summary: Simulated obstacle course for automobiles
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://bram.creative4vision.nl/sturmbahnfahrer/download/%{name}-%{version}.tar.gz
Source1: %{name}-16.png
Source2: %{name}-32.png
Source3: %{name}-48.png
Patch0: %{name}-1.5.2-use-shared-ode.patch
Group: Games/Arcade
License: GPL
URL: http://www.sturmbahnfahrer.com/
BuildRoot: %_tmppath/%{name}-build
BuildRequires: ode-devel >= 0.6
BuildRequires: plib-devel
BuildRequires: ImageMagick
BuildRequires: mesaglut-devel
BuildRequires: alsa-lib-devel
Obsoletes: sturmbahnfahrer

%description
Stormbaan Coureur is the Linux game that was formerly known as 
Sturmbahnfahrer.

It is back with a larger track, more challenges, many improvements in a 
PC (Politically Correct) edition.

In this game, it is all about the car Physics.

If you want to master it, try to have the laws of physics work with you, not
against you.

Enabling technologies behind Stormbaan Coureur include ODE, the Open Dynamics 
Engine and the portable game library known as PLIB.

Stormbaan Coureur is a game by Bram Stolk.

%prep

%setup -q -n %{name}-%{version}/src-%{name}
%patch -p0
# x86_64
perl -pi -e "s#LIBDIRNAME=lib#LIBDIRNAME=%{_lib}#g" Makefile

%build
%make

%install
rm -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}

#icons
install -d -m 755 %{buildroot}/%{_miconsdir}
install -m 644 %{SOURCE1} %{buildroot}/%{_miconsdir}/%{name}.png
install -d -m 755 %{buildroot}/%{_iconsdir}
install -m 644 %{SOURCE2} %{buildroot}/%{_iconsdir}/%{name}.png
install -d -m 755 %{buildroot}/%{_liconsdir}
install -m 644 %{SOURCE3} %{buildroot}/%{_liconsdir}/%{name}.png

#xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Stormbaancoureur
Comment=Simulated obstacle course for automobiles
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc JOYSTICKS README TODO *.keys.example
%attr(0755,root,games) %{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

%clean
rm -rf %{buildroot}
