from example import add_two_numbers, get_user_input

def test_add_two_numbers():
    assert add_two_numbers(2,2) == 4

def test_get_user_input(monkeypatch):
    #simulate user input
    monkeypatch.setattr("builtins.input", lambda _: "42")

    result = get_user_input()
    print(result)

    assert result == 42