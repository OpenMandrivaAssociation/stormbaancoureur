Name:			stormbaancoureur
Version:		2.1.6
Release:		%mkrel 2

Summary:	Simulated obstacle course for automobiles
License:	GPLv3
Group:		Games/Arcade
URL:		https://www.stolk.org/stormbaancoureur/
Source0:	http://www.stolk.org/stormbaancoureur/download/%{name}-%{version}.tar.gz
Source1:	stormbaancoureur-16.png
Source2:	stormbaancoureur-32.png
Source3:	stormbaancoureur-48.png
Patch0:		stormbaancoureur-1.5.2-use-shared-ode.patch

BuildRequires:	ode-devel >= 0.6
BuildRequires:	plib-devel
BuildRequires:	imagemagick
BuildRequires:	mesaglut-devel
BuildRequires:	alsa-lib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

Obsoletes:	sturmbahnfahrer

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
%patch0 -p0
# x86_64
sed -i -e "s#LIBDIRNAME=lib#LIBDIRNAME=%{_lib}#g" -e "s#CXXFLAGS=#CXXFLAGS+=#" -e "s#LFLAGS=#LFLAGS+=#" Makefile
%build
LFLAGS="%{ldflags}" CXXFLAGS="%{optflags}" %make


%install
rm -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}

#icons
install -d -m 755 %{buildroot}/%{_miconsdir}
install -m 644 %{_sourcedir}/stormbaancoureur-16.png %{buildroot}/%{_miconsdir}/stormbaancoureur.png
install -d -m 755 %{buildroot}/%{_iconsdir}
install -m 644 %{_sourcedir}/stormbaancoureur-32.png %{buildroot}/%{_iconsdir}/stormbaancoureur.png
install -d -m 755 %{buildroot}/%{_liconsdir}
install -m 644 %{_sourcedir}/stormbaancoureur-48.png %{buildroot}/%{_liconsdir}/stormbaancoureur.png

#xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-stormbaancoureur.desktop << EOF
[Desktop Entry]
Name=Stormbaancoureur
Comment=Simulated obstacle course for automobiles
Exec=%{_gamesbindir}/stormbaancoureur
Icon=stormbaancoureur
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc JOYSTICKS README TODO *.keys.example
%attr(0755,root,games) %{_gamesbindir}/*
%{_gamesdatadir}/stormbaancoureur
%{_miconsdir}/stormbaancoureur.png
%{_iconsdir}/stormbaancoureur.png
%{_liconsdir}/stormbaancoureur.png
%{_datadir}/applications/mandriva-stormbaancoureur.desktop

%clean
rm -rf %{buildroot}
