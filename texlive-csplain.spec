Name:		texlive-csplain
Version:	20180328
Release:	1
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
%{_texmfdistdir}/tex/csplain
%{_texmf_fmtutil_d}/csplain

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
