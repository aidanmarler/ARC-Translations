import pathlib
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--translations-path",
        action="store",
        required=True,
        help="Path to the ARCH<version> folder, e.g. ARCH1.4.1",
    )


def pytest_generate_tests(metafunc):
    if "arc_path" in metafunc.fixturenames:
        base = pathlib.Path(metafunc.config.getoption("--translations-path"))
        language_csvs = sorted(base.glob("*/ARCH.csv"))

        if not language_csvs:
            raise FileNotFoundError(f"No language CSVs found under {base}")

        metafunc.parametrize(
            "arc_path",
            language_csvs,
            ids=[p.parent.name for p in language_csvs],  # shows language in test name
        )