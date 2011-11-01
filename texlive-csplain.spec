Name:		texlive-csplain
Version:	20090924
Release:	1
Summary:	Plain TeX support for Czech/Slovak typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/cstex/base/csplain.tar.gz
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csplain.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-tex
Requires:	texlive-csplain.bin
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-tetex

%description
TeXLive csplain package.

%pre
    %_texmf_fmtutil_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_fmtutil_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_post
	%_texmf_mktexlsr_post
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
csplain pdftex - -etex -translate-file=cp227.tcx csplain.ini
pdfcsplain pdftex - -etex -translate-file=cp227.tcx csplain.ini
EOF
