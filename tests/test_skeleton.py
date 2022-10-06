import pytest
from sqlalchemy import create_engine

from dbtests.skeleton import fib, main

__author__ = "djfrancesco"
__copyright__ = "djfrancesco"
__license__ = "MIT"


def test_fib():
    """API Tests"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)


def test_main(capsys):
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["7"])
    captured = capsys.readouterr()
    assert "The 7-th Fibonacci number is 13" in captured.out

def test_connection():
    username = "SA"
    password = "Admin123"
    server = "localhost"
    database = "Faker"
    port = 1433
    connect_string = f"mssql+pymssql://{username}:{password}@{server}:{port}/{database}"

    engine = create_engine(connect_string)
    conn = engine.connect()
    conn.close()
