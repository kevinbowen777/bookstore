"""Nox sessions."""
import nox

locations = "accounts", "books", "config", "pages", "noxfile.py"


@nox.session(python=["3.10", "3.9"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)


@nox.session(python=["3.10", "3.9"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
