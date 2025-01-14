Name:		texlive-semantic
Version:	15878
Release:	2
Summary:	Help for writing programming language semantics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/semantic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Eases the typesetting of notation of semantics and compilers.
Includes T-diagrams, various derivation symbols and inference
trees.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/semantic/infernce.sty
%{_texmfdistdir}/tex/latex/semantic/ligature.sty
%{_texmfdistdir}/tex/latex/semantic/reserved.sty
%{_texmfdistdir}/tex/latex/semantic/semantic.sty
%{_texmfdistdir}/tex/latex/semantic/shrthand.sty
%{_texmfdistdir}/tex/latex/semantic/tdiagram.sty
%doc %{_texmfdistdir}/doc/latex/semantic/semantic.pdf
#- source
%doc %{_texmfdistdir}/source/latex/semantic/semantic.dtx
%doc %{_texmfdistdir}/source/latex/semantic/semantic.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
