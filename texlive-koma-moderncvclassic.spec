Name:		texlive-koma-moderncvclassic
Version:	25025
Release:	1
Summary:	An imitation of the moderncv class with the classic style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/koma-moderncvclassic
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-moderncvclassic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-moderncvclassic.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
