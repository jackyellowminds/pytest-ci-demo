import pytest


@pytest.fixture(scope="function")
def numbers():
    print("SETUP: Preparing numbers")

    yield 10, 20

    print("TEARDOWN: Cleaning up")