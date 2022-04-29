# Contributing to the Xanadu Sphinx Theme

Thank you for taking the time to contribute to the Xanadu Sphinx Theme (XST)!
:confetti_ball: :tada: :fireworks: :art:

While we will continue working on adding new and exciting features to the Xanadu
Sphinx Theme, we invite you to join us and suggest improvements or even just to
discuss how the XST fits into your workflow.

## How can I contribute?

It's up to you!

* **Test the cutting-edge XST releases** - clone our GitHub repository, and keep
  up to date with the latest features. If you run into any bugs, make a bug
  report on our
  [issue tracker](https://github.com/XanaduAI/xanadu-sphinx-theme/issues).

* **Report bugs** - even if you are not using the development branch of the XST,
  if you come across any bugs or issues, make a bug report. See the next section
  for more details on the bug reporting procedure.

* **Suggest new features and enhancements** - use the GitHub issue tracker and
  let us know what will make the XST even better for your workflow.

* **Contribute to our documentation** - if there is something you would like to
  add to our documentation or you have an idea for an improvement or change, let
  us know - or even submit a pull request directly. All authors who have
  contributed to the XST codebase will be listed alongside the latest release.

* **Build an application on top of the XST** - have an idea for an application
  where the XST is a good match? Consider making a Sphinx documentation website
  that builds upon XST as a base. Ask us if you have any questions, and send a
  link to your application to support@xanadu.ai so we can highlight it in our
  future documentation!

Appetite whetted? Keep reading below for all the nitty-gritty on reporting bugs,
contributing to the documentation, and submitting pull requests.

## Reporting bugs

We use the
[GitHub issue tracker](https://github.com/XanaduAI/xanadu-sphinx-theme/issues)
to keep track of all reported bugs and issues. If you find a bug, or have a
problem with the XST, please submit a bug report! User reports help us make the
client better on all fronts.

To submit a bug report, please work your way through the following checklist:

* **Search the issue tracker to make sure the bug wasn't previously reported**.
  If it was, you can add a comment to expand on the issue and share your
  experience.

* **Fill out the issue template**. If you cannot find an existing issue
  addressing the problem, create a new issue by filling out the
  [bug issue template](ISSUE_TEMPLATE/bug-report.yml). This template is added
  automatically to the comment box when you create a new issue. Please try and
  add as many details as possible!

* Try and make your issue as **clear, concise, and descriptive** as possible.
  Include a clear and descriptive title, and include all code snippets and
  commands required to reproduce the problem. If you're not sure what caused the
  issue, describe what you were doing when the issue occurred.

## Suggesting features, document additions, and enhancements

To suggest features and enhancements, use the
[feature request template](ISSUE_TEMPLATE/feature-request.yml). Be sure to:

* **Use a clear and descriptive title**

* **Provide a step-by-step description of the suggested feature**.

    Explain why the enhancement would be useful as well as where and how you
    would like to use it.

## Pull requests

If you would like to contribute directly to the XST codebase, simply make a
fork of the main branch and submit a
[pull request](https://help.github.com/articles/about-pull-requests). We
encourage everyone to have a go forking and modifying the XST source code;
however, we have a couple of guidelines on pull requests to ensure the main
branch conforms to existing standards and quality.

### General guidelines

* **Do not make a pull request for minor typos/cosmetic code changes** - create
  an issue instead.
* **For major features, consider making an independent package** that runs
  on top of the XST (rather than modifying the XST directly).

### Before submitting

Before submitting a pull request, please make sure the following is done:

* **All new classes, functions, and members must be clearly commented and
  documented**.
* **Ensure that the modified code is formatted correctly.**  Verify that
  `make lint` and `make format` pass.

### Submitting the pull request
* When ready, submit your fork as a
  [pull request](https://help.github.com/articles/about-pull-requests) to the
  XST repository, filling out the
  [pull request template](PULL_REQUEST_TEMPLATE.md). This template is added
  automatically to the comment box when you create a new PR.

* When describing the pull request, please include as much detail as possible
  regarding the changes made, new features, and performance improvements. If
  including any bug fixes, mention the issue numbers associated with the bugs.

* Once you have submitted the pull request, two things will automatically occur:

  - The **formatter** will automatically run on
    [GitHub Actions](https://github.com/XanaduAI/xanadu-sphinx-theme/actions) to
    ensure that all the code is properly formatted.

  Based on these results, we may ask you to make small changes to your branch
  before merging the pull request into the main branch. Alternatively, you can
  [grant us permission to make changes to your pull request branch](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/).

Thank you for contributing to the Xanadu Sphinx Theme!

\- The XST team
