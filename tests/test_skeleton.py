import pytest
from sqlalchemy import create_engine

from dbtests.skeleton import fib, main

__author__ = "François Pacull"
__copyright__ = "Architecture & Performance"
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


# def test_tests():
#     assert False

# def test_connection():
#     """Test connection and write permissions with SQL Server."""
#     username = "SA"
#     password = "Admin123"
#     server = "localhost"
#     database = "Faker"
#     port = 1433
#     connect_string = f"mssql+pymssql://{username}:{password}@{server}:{port}/{database}"

#     engine = create_engine(connect_string)
#     conn = engine.connect()

#     query_1 = """
#         CREATE TABLE recipes (
#           recipe_id INT NOT NULL,
#           recipe_name VARCHAR(30) NOT NULL,
#           PRIMARY KEY (recipe_id),
#           UNIQUE (recipe_name)
#         );"""
#     _ = conn.execute(query_1)

#     query_2 = """
#         INSERT INTO recipes 
#             (recipe_id, recipe_name) 
#         VALUES 
#             (1, 'Tacos'),
#             (2, 'Tomato Soup'),
#             (3, 'Grilled Cheese');"""
#     _ = conn.execute(query_2)

#     query_3 = """
#         SELECT COUNT(*) FROM recipes"""
#     result = conn.execute(query_3).fetchone()[0]

#     conn.close()

#     assert result == 2
