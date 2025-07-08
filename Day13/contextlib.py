from contextlib import contextmanager

@contextmanager
def custom_context():
    print("Enter")
    yield
    print("Exit")

with custom_context():
    print("Inside block")
