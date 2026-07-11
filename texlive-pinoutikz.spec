%global tl_name pinoutikz
%global tl_revision 55966

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	Draw chip pinouts with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pinoutikz
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pinoutikz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pinoutikz.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a set of macros for typesetting electronic chip
pinouts. It is designed as a tool that is easy to use, with a lean
syntax, native to LaTeX, and directly supporting PDF output format. It
has therefore been based on the very impressive TikZ package.

