import pytest
import gameofgame


def test_check_guess():
    # create test data
    guess = "Nairobi"
    wrong_guess = "Bagamoyo"
    country = "Kenya"
    countries_capitals = {"Kenya": "Nairobi", "Tanzania": "Dodoma"}

    # run function being tested and make assertions
    assert gameofgame.check_guess(guess, country, countries_capitals)
    assert not gameofgame.check_guess(wrong_guess, country, countries_capitals)



def test_get_countries_capitals():
    test_data = {"Uganda": "Kampala", "Egypt": "Cairo"}
    result = gameofgame.get_countries_capitals()

    assert isinstance(result, dict)

    assert result["Kenya"] == "Nairobi"

    #assert that the test_data is a subset of the result
    for country, capital in test_data.items():
        assert result[country] == capital
