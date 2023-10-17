import pytest
from flatten_list import flatten_list

def test_flatten_list():
    input1 = [1, 2, [3], [4, 5]]
    expected_output1 = [1,2,3,4,5]
    assert flatten_list(input1) == expected_output1

    input2 = [1,2,[9,[9,2,3],10],2,3]
    expected_output2 =[1,2,9,9,2,3,10,2,3]
    assert flatten_list(input) == expected_output1