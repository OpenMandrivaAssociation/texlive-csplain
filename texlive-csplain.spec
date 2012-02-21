# revision 22650
# category Package
# catalog-ctan /macros/cstex/base/csplain.tar.gz
# catalog-date 2009-09-24 20:53:04 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-csplain
Version:	20090924
Release:	4
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
%{_texmfdistdir}/tex/csplain/base/cavantga.tex
%{_texmfdistdir}/tex/csplain/base/cbookman.tex
%{_texmfdistdir}/tex/csplain/base/chelvet.tex
%{_texmfdistdir}/tex/csplain/base/cncent.tex
%{_texmfdistdir}/tex/csplain/base/cpalatin.tex
%{_texmfdistdir}/tex/csplain/base/csenc-k.tex
%{_texmfdistdir}/tex/csplain/base/csenc-p.tex
%{_texmfdistdir}/tex/csplain/base/csenc-u.tex
%{_texmfdistdir}/tex/csplain/base/csenc-w.tex
%{_texmfdistdir}/tex/csplain/base/cseplain.ini
%{_texmfdistdir}/tex/csplain/base/csfonts.tex
%{_texmfdistdir}/tex/csplain/base/csplain-utf8.ini
%{_texmfdistdir}/tex/csplain/base/csplain.ini
%{_texmfdistdir}/tex/csplain/base/ctimes.tex
%{_texmfdistdir}/tex/csplain/base/czech.sty
%{_texmfdistdir}/tex/csplain/base/czhyphen.ex
%{_texmfdistdir}/tex/csplain/base/czhyphen.tex
%{_texmfdistdir}/tex/csplain/base/dcfonts.tex
%{_texmfdistdir}/tex/csplain/base/ecfonts.tex
%{_texmfdistdir}/tex/csplain/base/extcode.tex
%{_texmfdistdir}/tex/csplain/base/fonttabs.tex
%{_texmfdistdir}/tex/csplain/base/hyphen.ex
%{_texmfdistdir}/tex/csplain/base/hyphen.lan
%{_texmfdistdir}/tex/csplain/base/il2code.tex
%{_texmfdistdir}/tex/csplain/base/plaina4.tex
%{_texmfdistdir}/tex/csplain/base/skhyphen.ex
%{_texmfdistdir}/tex/csplain/base/skhyphen.tex
%{_texmfdistdir}/tex/csplain/base/slovak.sty
%{_texmfdistdir}/tex/csplain/base/t1code.tex
%{_texmfdistdir}/tex/csplain/base/ttimes.tex
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
csplain pdftex - -etex -translate-file=cp227.tcx csplain.ini
pdfcsplain pdftex - -etex -translate-file=cp227.tcx csplain.ini
EOF
