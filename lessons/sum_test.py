"""unit tests for sum function"""

from lessons.sum import sum

def test_empty() -> None:
    assert sum([]) == 0.0