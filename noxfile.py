"""Nox sessions."""
import nox

nox.options.sessions = "lint", "tests"
locations = "accounts", "books", "config", "pages", "noxfile.py"


@nox.session(python=["3.10", "3.9"])
def black(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.10", "3.9"])
def lint(session):
    """Lint using flake8."""
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python=["3.10", "3.9"])
def tests(session):
    """Run the test suite."""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
