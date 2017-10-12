import letter_hunt


def test_random_letter_generator():
    letter = letter_hunt.random_choice() in letter_hunt.letters
    assert letter == True

def test_score_increse():
    letter_hunt.score = 0
    letter_hunt.fail = 0
    letter_hunt.letters=['a','b','c']
    letter_hunt.active_letters=['a','b']
    letter_hunt.letter_check('b')
    assert letter_hunt.score == 1
    assert letter_hunt.fail == 0
    assert letter_hunt.active_letters == ['a']

def test_score_increse_by2():
    letter_hunt.score = 0
    letter_hunt.fail = 0
    letter_hunt.letters=['a','b','c']
    letter_hunt.active_letters=['a','b']
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
    letter_hunt.letters=['a','b','c']
    letter_hunt.active_letters=['a','b']
    letter_hunt.letter_check('c')
    #assert letter_hunt.score == 0
    assert letter_hunt.fail == 1
    assert letter_hunt.active_letters == ['a','b']

def test_fail_and_score():
    letter_hunt.score = 0
    letter_hunt.fail = 0
    letter_hunt.letters=['a','b','c']
    letter_hunt.active_letters=['a','b']
    letter_hunt.letter_check('c')
    assert letter_hunt.score == 0
    assert letter_hunt.fail == 1
    assert letter_hunt.active_letters == ['a','b']
    letter_hunt.letter_check('b')
    assert letter_hunt.score == 1
    assert letter_hunt.fail == 1
    assert letter_hunt.active_letters == ['a']


def test_streak_and_sleep_time():
    letter_hunt.score = 0
    letter_hunt.strike =0
    letter_hunt.fail = 0
    letter_hunt.strike_list = []
    letter_hunt.sleep_time = 2.0
    letter_hunt.letters=['a','b','c','d','e','f','g']
    letter_hunt.active_letters=['a','b','c','d','e','f','g','a','b','c','d','e','f','g','a','b','c','d','e','f','g','a','b','c','d','e','f','g','a','b','c','d','e','f','g']
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
    assert letter_hunt.fail ==1
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
    assert letter_hunt.score ==14
    assert letter_hunt.strike == 2
    assert letter_hunt.sleep_time == 1.6
    
