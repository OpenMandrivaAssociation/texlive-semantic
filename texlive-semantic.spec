# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/semantic
# catalog-date 2007-01-15 20:26:34 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-semantic
Version:	2.0
Release:	1
Summary:	Help for writing programming language semantics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/semantic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Eases the typesetting of notation of semantics and compilers.
Includes T-diagrams, various derivation symbols and inference
trees.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
