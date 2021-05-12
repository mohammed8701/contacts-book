import pytest
import menus

mock_contact_name = "anthony pettis"
def test_new_contact_first_name(monkeypatch):   
    monkeypatch.setattr('builtins.input',mock_contact_name)
    actual = menus.new_contact_first_name()
    expected = "Anthony Pettis"
    assert actual == expected 
    
    
mock_number = "074154655"
def test_new_contact_number(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_number)
    actual = menus.new_contact_number()
    expected = "74154655"
    assert actual == expected

mock_email = "test_email@mail.com"
def test_new_contact_email(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_email)
    actual = menus.new_contact_email()
    expected = "test_email@mail.com"
    assert actual == expected
