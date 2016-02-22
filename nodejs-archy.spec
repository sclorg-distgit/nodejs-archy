%{?scl:%scl_package nodejs-archy}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}


Name:       %{?scl_prefix}nodejs-archy
Version:    1.0.0
Release:    1%{?dist}
Summary:    Renders nested hierarchies with unicode pipes
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/substack/node-archy
Source0:    http://registry.npmjs.org/archy/-/archy-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Render nested hierarchies with unicode pipes, `npm ls` style.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/archy
cp -p index.js package.json %{buildroot}%{nodejs_sitelib}/archy

%nodejs_symlink_deps

# tests disabled until tap is packaged
#%%check
#%%tap test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/archy
%doc readme.markdown examples/*

%changelog
* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- New upstream release

* Thu Oct 17 2013 Tomas Hrcka thrcka@redhat.com - 0.0.2-8
- replace provides and requires with macro

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.2-7
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-5
- fix URL

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-4
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-3
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-2
- fix BuildRequires not present on <F17

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-1
- initial package
