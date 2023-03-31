Name:		texlive-pinoutikz
Version:	55966
Release:	2
Summary:	Draw chip pinouts with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pinoutikz
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pinoutikz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pinoutikz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of macros for typesetting electronic
chip pinouts. It is designed as a tool that is easy to use,
with a lean syntax, native to LaTeX, and directly supporting
PDF output format. It has therefore been based on the very
impressive TikZ package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pinoutikz
%doc %{_texmfdistdir}/doc/latex/pinoutikz

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
