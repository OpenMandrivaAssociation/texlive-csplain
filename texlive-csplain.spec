%global tl_name csplain
%global tl_revision 79618
%global tl_bin_links csplain:pdftex luacsplain:luatex pdfcsplain:pdftex

Name:		texlive-%{tl_name}
Epoch:		1
Version:	Mar.2022
Release:	%{tl_revision}.1
Summary:	Plain TeX multilanguage support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/cstex/base/csplain.tar.gz
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csplain.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cm)
Requires:	texlive(cs)
Requires:	texlive(csplain.bin)
Requires:	texlive(enctex)
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(luatex)
Requires:	texlive(luatex85)
Requires:	texlive(pdftex)
Requires:	texlive(plain)
Requires:	texlive(tex)
Requires:	texlive(tex-ini-files)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
CSplain is a small extension of basic Plain TeX macros, the formats
csplain and pdfcsplain can be generated. It supports: hyphenation of
words for 50+ languages, simple and powerful font loading system
(various sizes of fonts), TeX, pdfTeX, XeTeX and LuaTeX engines, math
fonts simply loaded with full amstex-like features, three internal
encodings (IL2 for Czech/Slovak languages, T1 for many languages with
latin alphabet and Unicode in new TeX engines), natural UTF-8 input in
pdfTeX using encTeX without any active characters, Czech and Slovak
special typesetting features. An important part of the package is OPmac,
which implements most of LaTeX's features (sectioning, font selection,
color, hyper reference and urls, bibliography, index, toc, tables,etc.)
by Plain TeX macros. The OPmac macros can generate and bibliography
without any external program.

