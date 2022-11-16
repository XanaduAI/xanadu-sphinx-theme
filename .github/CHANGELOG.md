## Release 0.3.4

### Improvements

* Added the option to customize the href fragment of the details directive
  [#26](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/26)

### Contributors

This release contains contributions from (in alphabetical order):

[David Wierichs](https://github.com/dwierichs).

## Release 0.3.3

### Bug fixes

* Fixed an issue where footnote references were being rendered without brackets.
  [#25](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/25)

### Contributors

This release contains contributions from (in alphabetical order):

[Josh Izaac](https://github.com/josh146).

## Release 0.3.2

### Bug fixes

* Added missing variables: `github_repo` and `gallery_dirs` to address the View on GitHub link not working for demos.
  [#24](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/24)

* Fixed a bug where author bio photos would appear squished. [#25](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/25)

### Contributors

This release contains contributions from (in alphabetical order):

[Lucas Silbernagel](https://github.com/LucasSilbernagel)
[Josh Izaac](https://github.com/josh146).

## Release 0.3.1

### Improvements

* Added support for images in navbar links. [#21](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/21)

### Bug fixes

* Fixed a bug where the navbar would incorrectly display a drop shadow
  with small screen widths when the global TOC was active.
  [#20](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/20)

* Fixed a bug where gallery card margins would not reduce on smaller
  width displays. [#22](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/22)

### Contributors

This release contains contributions from (in alphabetical order):

[Josh Izaac](https://github.com/josh146).

## Release 0.3.0

### Improvements

* Added documentation. [#13](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/13)

* Add a new `.. bio::` directive, which supports inserting author bios. [#14](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/14)

* Add support for Sphinx Gallery. [#14](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/14)

* Add a new option `toc_global` which allows the left-hand global ToC sidebar
  to be disabled. [#14](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/14)

* Update heading and navbar font to Quicksand. [#15](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/15)

* Add new options to customize the footer: [#16](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/16)

  - `footer_about` set the 'About' section of the footer
  - `footer_links` to create columns of links
  - `footer_social` to customize social media icons
  - `footer_tagline` to set the tagline

* Included autosummary templates within the Xanadu Sphinx Theme.
  The provided templates directory is available via
  `xanadu_sphinx_theme.templates_dir()` and can be added to the
  `templates_path` list variable in `conf.py`.
  [#18](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/18)

### Bug fixes

* Fixed a bug where the HTML sidebars were not properly configured. [#17](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/17)

### Contributors

This release contains contributions from (in alphabetical order):

[Mikhail Andrenkov](https://github.com/Mandrenkov),
[Josh Izaac](https://github.com/josh146).

## Release 0.2.1

### Improvements

* [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) is now imported
  using `@import` instead of `@font-face` for stability reasons.
  [#9](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/9)

### Contributors

This release contains contributions from (in alphabetical order):

[Mikhail Andrenkov](https://github.com/Mandrenkov)

## Release 0.2.0

### New features since last release

* Adds the `toc_overview` option, which allows the table of contents to
  optionally display the project title and a link to the documentation
  homepage. [#7](https://github.com/XanaduAI/xanadu-sphinx-theme/pull/7)

### Contributors

This release contains contributions from (in alphabetical order):

[Mikhail Andrenkov](https://github.com/Mandrenkov),
[Josh Izaac](https://github.com/josh146).

## Release 0.1.0

### New features since last release

* This is the initial public release.

### Contributors

This release contains contributions from (in alphabetical order):

[Mikhail Andrenkov](https://github.com/Mandrenkov),
[Tom Bromley](https://github.com/trbromley),
[Josh Izaac](https://github.com/josh146).
