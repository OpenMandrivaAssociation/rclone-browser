Summary:	Simple cross platform GUI for rclone
Name:		rclone-browser
Version:	1.8.0
Release:	1
License:	MIT
Group:		Networking/Other
URL:		https://github.com/kapitainsky/RcloneBrowser
Source0:	https://github.com/kapitainsky/RcloneBrowser/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/kapitainsky/RcloneBrowser/pull/126
Patch0:		https://github.com/kapitainsky/RcloneBrowser/pull/126/commits/ce9cf52e9c584a2cc85a5fa814b0fd7fa9cf0152.patch
# https://github.com/kapitainsky/RcloneBrowser/pull/225
Patch1:		https://github.com/kapitainsky/RcloneBrowser/pull/225/commits/a32fad90d992b9ea4ea8e20306f05fb85d2f1c37.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	pkgconfig(appstream-glib)

Requires:	rclone

%description
Simple cross platfrom GUI for rclone command line tool.

Features:
 - Allows to browse and modify any rclone remote, including encrypted ones
 - Uses same configuration file as rclone, no extra configuration required
 - Supports custom location and encryption for .rclone.conf configuration file
 - Simultaneously navigate multiple repositories in separate tabs
 - Lists files hierarchically with file name, size and modify date
 - All rclone commands are executed asynchronously, no freezing GUI
 - File hierarchy is lazily cached in memory, for faster traversal of folders
 - Allows to upload, download, create new folders, rename or delete files and
   folders
 - Allows to calculate size of folder, export list of files and copy rclone
   command to clipboard
 - Can process multiple upload or download jobs in background
 - Drag & drop support for dragging files from local file explorer for
   uploading
 - Streaming media files for playback in player like mpv or similar
 - Mount and unmount folders on macOS and GNU/Linux
 - Optionally minimizes to tray, with notifications when upload/download
   finishes
 - Supports portable mode (create .ini file next to executable with same 
   name), rclone and .rclone.conf path now can be relative to executable

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_metainfodir}/%{name}.appdata.xml

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n RcloneBrowser-%{version}

%build
%cmake \
	-GNinja
%ninja_build

%install
%ninja_install -C build

# appdata
install -dpm 0755 %{buildroot}%{_metainfodir}/ 
install -Dpm 0644 assets/rclone-browser.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml

