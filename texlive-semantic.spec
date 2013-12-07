# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/semantic
# catalog-date 2007-01-15 20:26:34 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-semantic
Version:	2.0
Release:	5
Summary:	Help for writing programming language semantics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/semantic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 755904
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719502
- texlive-semantic
- texlive-semantic
- texlive-semantic
- texlive-semantic

