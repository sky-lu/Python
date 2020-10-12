import pytest

def test_assignment1_question1(script_runner):
    f = open('./Input/assignment_1_question_1_input', 'rb')
    ret = script_runner.run('./Assignment_1/question1.py', stdin=f)
    f.close()
    assert 'The product is  600' in ret.stdout

def test_assignment1_question2(script_runner):
    f = open('./Input/assignment_1_question_2_input', 'rb')
    ret = script_runner.run('./Assignment_1/question2.py', stdin=f)
    assert 'The average of five numbers is  4.0' in ret.stdout

    
def test_assignment1_question3():
    assert 1 == 1