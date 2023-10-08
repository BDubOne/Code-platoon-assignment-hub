import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_bigadd():
    assert calculator.calculate(546, 454, "add") == 1000
   # Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    calculator.main()
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "8", "2", "divide"])
    assert calculator.calculate(8, 2, "divide") == 4.0