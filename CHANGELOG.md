
# Changelog

All notable changes to the AIMS-mini project will be documented in this file.

The project follows Semantic Versioning.

## [Unreleased]

### Added
- Restore Cart.discounted_total() on the development branch.
- Add regression tests for discount calculation and percentage validation.

### Fixed
- Backport the case-insensitive search fix to the development branch.

## [1.1.0] - 2026-11-07

### Added
- Add Cart.sort_by_title() to sort DVDs by title.
- Add Cart.sort_by_cost() to sort DVDs by cost.
- Add search_by_category().
- Add unit tests for cart sorting.

## [1.0.1] - 2026-11-07

### Fixed
- Make search_by_title() case-insensitive.
- Fix lowercase keyword searching in the 1.0.x release line.

## [1.0.0] - 2026-11-07

### Added
- Add Cart.print_cart() to display cart information.
- Add search_by_title() to search for DVDs.
- Add unit tests for cart capacity and discount calculation.
- Add use case documentation.
- Add pull request template.

### Fixed
- Fix cart capacity off-by-one bug (Issue #9).
- Resolve merge conflict in cart messages.
- Revert the show-added-title feature as part of Lab 03.

### Changed
- Refactor DVD and Cart modules into the aims package.
- Introduce GitHub Pull Request workflow and release branches.
