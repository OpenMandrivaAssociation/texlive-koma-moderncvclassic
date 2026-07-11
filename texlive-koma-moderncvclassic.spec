%global tl_name koma-moderncvclassic
%global tl_revision 78632

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Makes the style and command of moderncv (style classic) available for KOMA-cl...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/koma-moderncvclassic
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-moderncvclassic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-moderncvclassic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an imitation of the moderncv class with the
classic style (by Xavier Danaux), to be used in conjunction with the
KOMA-classes. Thus it is possible to configure pagelayout, headings etc.
the way it is done in KOMA-classes. Moreover, it is possible to use
BibLaTeX, while the original moderncv-class is incompatible with
BibLaTeX.

