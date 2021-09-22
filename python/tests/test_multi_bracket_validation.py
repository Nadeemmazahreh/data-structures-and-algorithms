import re

def multi_bracket_validation(input):
    x=False
    if input.count('{')==input.count('}') and input.count('(')==input.count(')') and input.count('[')==input.count(']'):
        x=True
    try :
       if re.search("\(.?}", input) or re.search("\[.?}", input) or re.search("\[.?)", input) or re.search("\(.?]", input) or re.search("\{.?)", input) or re.search("\{.?]", input):
            x=False
    except:
        return x

    return x


def test_happypath():
    assert multi_bracket_validation('{}') == True
    assert multi_bracket_validation('{}(){}') == True
    assert multi_bracket_validation('()[[Extra Characters]]') == True
    assert multi_bracket_validation('(){}[[]]') == True


def test_Expected_failure():
    assert multi_bracket_validation('{}{Code}[Fellows](())') != False
    assert multi_bracket_validation('[({}]') != True


def test_Edge_Case():
    assert multi_bracket_validation('(](') == False
    assert multi_bracket_validation('{(})') == False
    assert multi_bracket_validation('{') == False
    assert multi_bracket_validation(')') == False
    assert multi_bracket_validation('[}') == False
