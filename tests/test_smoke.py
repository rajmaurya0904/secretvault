"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import secretvault


def test_version_is_set() -> None:
    assert secretvault.__version__
