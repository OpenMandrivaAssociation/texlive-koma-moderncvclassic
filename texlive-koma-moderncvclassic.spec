# revision 25025
# category Package
# catalog-ctan /macros/latex/contrib/koma-moderncvclassic
# catalog-date 2012-01-05 01:27:26 +0100
# catalog-license lppl1.3
# catalog-version v0.5
Name:		texlive-koma-moderncvclassic
Version:	v0.5
Release:	6
Summary:	An imitation of the moderncv class with the classic style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/koma-moderncvclassic
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-moderncvclassic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-moderncvclassic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an imitation of the moderncv class with
the classic style (by Xavier Danaux), to be used in conjunction
with the koma-classes. Thus it is possible to configure
pagelayout, headings etc. the way it is done in koma-classes.
Moreover, it is possible to use biblatex, while the original
moderncv-class is incompatible with biblatex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/koma-moderncvclassic/koma-moderncvclassic.sty
%doc %{_texmfdistdir}/doc/latex/koma-moderncvclassic/README
%doc %{_texmfdistdir}/doc/latex/koma-moderncvclassic/changelog
%doc %{_texmfdistdir}/doc/latex/koma-moderncvclassic/cvbasic.pdf
%doc %{_texmfdistdir}/doc/latex/koma-moderncvclassic/cvbasic.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.5-1
+ Revision: 758930
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.4-2
+ Revision: 753029
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.4-1
+ Revision: 718782
- texlive-koma-moderncvclassic
- texlive-koma-moderncvclassic
- texlive-koma-moderncvclassic
- texlive-koma-moderncvclassic

