# revision 34304
# category Package
# catalog-ctan /macros/cstex/base/csplain.tar.gz
# catalog-date 2012-11-24 09:12:36 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-csplain
Version:	20121124
Release:	9
Summary:	Plain TeX support for Czech/Slovak typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/cstex/base/csplain.tar.gz
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csplain.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires(post):	texlive-cs
Requires:	texlive-tex
Requires:	texlive-csplain.bin

%description
TeXLive csplain package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/csplain/base/csenc-k.tex
%{_texmfdistdir}/tex/csplain/base/csenc-p.tex
%{_texmfdistdir}/tex/csplain/base/csenc-u.tex
%{_texmfdistdir}/tex/csplain/base/csenc-w.tex
%{_texmfdistdir}/tex/csplain/base/cseplain.ini
%{_texmfdistdir}/tex/csplain/base/csfonts.tex
%{_texmfdistdir}/tex/csplain/base/csfontsm.tex
%{_texmfdistdir}/tex/csplain/base/csplain-utf8.ini
%{_texmfdistdir}/tex/csplain/base/csplain.ini
%{_texmfdistdir}/tex/csplain/base/czhyphen.ex
%{_texmfdistdir}/tex/csplain/base/czhyphen.tex
%{_texmfdistdir}/tex/csplain/base/extcode.tex
%{_texmfdistdir}/tex/csplain/base/fonttabs.tex
%{_texmfdistdir}/tex/csplain/base/hyphen.ex
%{_texmfdistdir}/tex/csplain/base/hyphen.lan
%{_texmfdistdir}/tex/csplain/base/il2code.tex
%{_texmfdistdir}/tex/csplain/base/luaplain.ini
%{_texmfdistdir}/tex/csplain/base/plaina4.tex
%{_texmfdistdir}/tex/csplain/base/skhyphen.ex
%{_texmfdistdir}/tex/csplain/base/skhyphen.tex
%{_texmfdistdir}/tex/csplain/base/t1code.tex
%{_texmfdistdir}/tex/csplain/base/t1enc-u.tex
%{_texmfdistdir}/tex/csplain/base/ucode.tex
%{_texmfdistdir}/tex/csplain/base/xeplain.ini
%{_texmfdistdir}/tex/csplain/fonts/ams-math.tex
%{_texmfdistdir}/tex/csplain/fonts/cavantga.tex
%{_texmfdistdir}/tex/csplain/fonts/cbookman.tex
%{_texmfdistdir}/tex/csplain/fonts/chars-8z.tex
%{_texmfdistdir}/tex/csplain/fonts/chelvet.tex
%{_texmfdistdir}/tex/csplain/fonts/cncent.tex
%{_texmfdistdir}/tex/csplain/fonts/cpalatin.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-adventor.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-all.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-antt.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-arev.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-bera.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-bonum.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-charter.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-cursor.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-heros.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-pagella.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-polta.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-schola.tex
%{_texmfdistdir}/tex/csplain/fonts/cs-termes.tex
%{_texmfdistdir}/tex/csplain/fonts/ctimes.tex
%{_texmfdistdir}/tex/csplain/fonts/cyrchars.tex
%{_texmfdistdir}/tex/csplain/fonts/dcfonts.tex
%{_texmfdistdir}/tex/csplain/fonts/ecfonts.tex
%{_texmfdistdir}/tex/csplain/fonts/exchars.tex
%{_texmfdistdir}/tex/csplain/fonts/lmfonts.tex
%{_texmfdistdir}/tex/csplain/fonts/luafonts.tex
%{_texmfdistdir}/tex/csplain/fonts/tx-math.tex
%{_texmfdistdir}/tex/csplain/fonts/unifam.tex
%{_texmfdistdir}/tex/csplain/opmac/opmac-bib-iso690.tex
%{_texmfdistdir}/tex/csplain/opmac/opmac-bib-simple.tex
%{_texmfdistdir}/tex/csplain/opmac/opmac-bib.tex
%{_texmfdistdir}/tex/csplain/opmac/opmac-xetex.tex
%{_texmfdistdir}/tex/csplain/opmac/opmac.tex
%{_texmfdistdir}/tex/csplain/opmac/pdfuni.tex
%_texmf_fmtutil_d/csplain

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/csplain <<EOF
#
# from csplain:
csplain pdftex - -etex -enc csplain-utf8.ini
pdfcsplain pdftex - -etex -enc csplain-utf8.ini
pdfcsplain xetex - -etex csplain.ini
pdfcsplain luatex - -etex csplain.ini
EOF
