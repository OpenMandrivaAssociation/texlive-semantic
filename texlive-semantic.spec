%global tl_name semantic
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Help for writing programming language semantics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/semantic
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Eases the typesetting of notation of semantics and compilers. Includes
T-diagrams, various derivation symbols and inference trees.

