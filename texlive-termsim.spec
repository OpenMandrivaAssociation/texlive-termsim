Name:		texlive-termsim
Version:	61414
Release:	2
Summary:	Simulate Win10, Ubuntu, and Mac terminals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/termsim
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termsim.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termsim.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termsim.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX3 package provides environments terminal and
terminal*, and macros \termfile and \termfile* to simulate
Win10, Ubuntu and Mac terminals. It is based on tcolorbox,
minted and listings.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/termsim
%{_texmfdistdir}/tex/latex/termsim
%doc %{_texmfdistdir}/doc/latex/termsim

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
