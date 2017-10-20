import letter_hunt


def test_random_letter_generator():
    letter = letter_hunt.random_choice() in letter_hunt.letters
    assert letter


def test_score_increse():
    letter_hunt.score = 0
    letter_hunt.fail = 0
    letter_hunt.letters = ['a', 'b', 'c']
    letter_hunt.active_letters = ['a', 'b']
    letter_hunt.letter_check('b')
    assert letter_hunt.score == 1
    assert letter_hunt.fail == 0
    assert letter_hunt.active_letters == ['a']


def test_score_increse_by2():
    letter_hunt.score = 0
    letter_hunt.fail = 0
    letter_hunt.letters = ['a', 'b', 'c']
    letter_hunt.active_letters = ['a', 'b']
    letter_hunt.letter_check('b')
    assert letter_hunt.score == 1
    assert letter_hunt.fail == 0
    assert letter_hunt.active_letters == ['a']
    letter_hunt.letter_check('a')
    assert letter_hunt.score == 2
    assert letter_hunt.fail == 0
    assert letter_hunt.active_letters == []


def test_fail_increse():
    letter_hunt.score = 0
    letter_hunt.fail = 0
    letter_hunt.letters = ['a', 'b', 'c']
    letter_hunt.active_letters = ['a', 'b']
    letter_hunt.letter_check('c')
    #assert letter_hunt.score == 0
    assert letter_hunt.fail == 1
    assert letter_hunt.active_letters == ['a', 'b']


def test_fail_and_score():
    letter_hunt.score = 0
    letter_hunt.fail = 0
    letter_hunt.letters = ['a', 'b', 'c']
    letter_hunt.active_letters = ['a', 'b']
    letter_hunt.letter_check('c')
    assert letter_hunt.score == 0
    assert letter_hunt.fail == 1
    assert letter_hunt.active_letters == ['a', 'b']
    letter_hunt.letter_check('b')
    assert letter_hunt.score == 1
    assert letter_hunt.fail == 1
    assert letter_hunt.active_letters == ['a']


def test_streak_and_sleep_time():
    letter_hunt.score = 0
    letter_hunt.strike = 0
    letter_hunt.fail = 0
    letter_hunt.strike_list = []
    letter_hunt.sleep_time = 2.0
    letter_hunt.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letter_hunt.active_letters = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g']
    letter_hunt.letter_check('a')
    assert letter_hunt.score == 1
    assert letter_hunt.strike == 0
    letter_hunt.letter_check('a')
    letter_hunt.letter_check('a')
    letter_hunt.letter_check('a')
    assert letter_hunt.score == 4
    assert letter_hunt.strike == 0
    assert letter_hunt.sleep_time == 2.0
    letter_hunt.letter_check('a')
    assert letter_hunt.score == 5
    assert letter_hunt.strike == 1
    assert letter_hunt.sleep_time == 1.8
    letter_hunt.letter_check('a')
    assert letter_hunt.score == 5
    assert letter_hunt.fail == 1
    assert letter_hunt.strike == 1
    letter_hunt.letter_check('b')
    letter_hunt.letter_check('b')
    letter_hunt.letter_check('b')
    letter_hunt.letter_check('b')
    letter_hunt.letter_check('v')
    assert letter_hunt.score == 9
    assert letter_hunt.fail == 2
    assert letter_hunt.strike == 1
    letter_hunt.letter_check('b')
    assert letter_hunt.score == 10
    assert letter_hunt.fail == 2
    assert letter_hunt.strike == 1
    assert letter_hunt.sleep_time == 1.8
    letter_hunt.letter_check('c')
    letter_hunt.letter_check('c')
    letter_hunt.letter_check('c')
    letter_hunt.letter_check('c')
    assert letter_hunt.score == 14
    assert letter_hunt.strike == 2
    assert letter_hunt.sleep_time == 1.6


def test_letter_mappping():
    letter_hunt.initial_size=5
    letter_hunt.letters=["a","b","c","d","e","f"]
    letter_hunt.active_add_letters()
    letter_hunt.active_letters=["a","b","c","d","e"]
    letter_hunt.letter_position()
    assert letter_hunt.letter_mapping() == {1:'a',2:'b',3:'c',4:'d',5:'e'}
    letter_hunt.active_letters=["a","b","f","d","e"]
    letter_hunt.letter_position()
    assert letter_hunt.letter_mapping() == {1:'a',2:'b',3:'f',4:'d',5:'e'}


def test_show_letter():
    letter_hunt.letters=["a","b","c","d","e","f"]
    letter_hunt.active_letters=["a","b","c","d","e"]
    letter_hunt.letter_position()
    letter_hunt.letter_mapping()
    assert letter_hunt.show_letter() in letter_hunt.active_letters

def test_letter_mapping2():
    letter_hunt.initial_size=5
    letter_hunt.active_add_letters()
    letter_hunt.active_letters=["a","b","c","d","e"]
    letter_hunt.letter_position()
    assert letter_hunt.letter_mapping() == {1:'a',2:'b',3:'c',4:'d',5:'e'}
    letter_hunt.letter_check("c")
    letter_hunt.letters = ["x"]
    letter_hunt.active_add_letters()   
    assert letter_hunt.active_letters == ["a","b","d","e","x"]
    letter_hunt.letter_position()
    assert letter_hunt.letter_mapping() == {1:'a',2:'b',3:'d',4:'e',5:'x'}

def test_life_true():
    life_remains=2
  #  a=True
    letter_hunt.life(True)
    assert life_remains == 1
    assert letter_hunt.life(a) == False
 #   b=False
    letter_hunt.life(False)
    assert life_remains == 1
    assert letter_hunt.life(a) == False
#    c=False
    letter_hunt.life(True)
    assert life_remains == 0
    assert letter_hunt.life(a) == True
    
    
