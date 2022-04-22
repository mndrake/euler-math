#pylint: disable = no-value-for-parameter
from euler_math import List


def test_list_sum():
    lst = [1,2,3,4,5]
    result = lst >> List.sum()
    assert result == 15


def test_list_sumBy():
    lst = [1,2,3,4,5]
    result = lst >> List.sumBy(lambda x: x*x)
    assert result == 55


def test_list_filter():
    lst = [0,1,2,3,4,5,6]
    result = lst >> List.filter(lambda x: x%2 == 1)
    assert result == [1,3,5]


def test_list_map():
    lst = [1,2,3,4,5] >> List.map(lambda x: x*x)
    result = list(lst)
    assert result == [1,4,9,16,25]


def test_list_max():
    lst = range(5)
    result = lst >> List.max()
    assert result == 4


def test_list_reduce():
    result = [1,2,3,4,5] >> List.reduce(lambda a,b: a+b)
    assert result == 15


def test_list_collect():
    lst = [1,2,3]
    result = lst >> List.collect(lambda x: [x]*x)
    assert result == [1, 2, 2, 3, 3, 3]
