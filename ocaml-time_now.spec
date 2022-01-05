#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Report the current time
Summary(pl.UTF-8):	Informacja o aktualnym czase
Name:		ocaml-time_now
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/time_now/tags
Source0:	https://github.com/janestreet/time_now/archive/v%{version}/time_now-%{version}.tar.gz
# Source0-md5:	2c72607b27ce0a25be6d6390447633bc
URL:		https://github.com/janestreet/time_now
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-jane-street-headers-devel >= 0.14
BuildRequires:	ocaml-jane-street-headers-devel < 0.15
BuildRequires:	ocaml-jst-config-devel >= 0.14
BuildRequires:	ocaml-jst-config-devel < 0.15
BuildRequires:	ocaml-ppx_base-devel >= 0.14
BuildRequires:	ocaml-ppx_base-devel < 0.15
BuildRequires:	ocaml-ppx_optcomp-devel >= 0.14
BuildRequires:	ocaml-ppx_optcomp-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a single function to report the current time in nanoseconds
since the start of the Unix epoch.

This package contains files needed to run bytecode executables using
time_now library.

%description -l pl.UTF-8
Ten moduł udostępnia jedną funkcję, zwracającą aktualny czas w
nanosekundach od początku epoki Uniksa.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki time_now.

%package devel
Summary:	Report the current time - development part
Summary(pl.UTF-8):	Informacja o aktualnym czase - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-jane-street-headers-devel >= 0.14
Requires:	ocaml-jst-config-devel >= 0.14
Requires:	ocaml-ppx_base-devel >= 0.14
Requires:	ocaml-ppx_optcomp-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
time_now library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki time_now.

%prep
%setup -q -n time_now-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/time_now/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/time_now

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%dir %{_libdir}/ocaml/time_now
%{_libdir}/ocaml/time_now/META
%{_libdir}/ocaml/time_now/runtime.js
%{_libdir}/ocaml/time_now/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/time_now/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlltime_now_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/time_now/libtime_now_stubs.a
%{_libdir}/ocaml/time_now/*.cmi
%{_libdir}/ocaml/time_now/*.cmt
%{_libdir}/ocaml/time_now/*.cmti
%{_libdir}/ocaml/time_now/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/time_now/time_now.a
%{_libdir}/ocaml/time_now/*.cmx
%{_libdir}/ocaml/time_now/*.cmxa
%endif
%{_libdir}/ocaml/time_now/dune-package
%{_libdir}/ocaml/time_now/opam
