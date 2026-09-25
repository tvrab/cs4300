from src.task1 import hello_world

# Function to test that the hello_world function works
def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"