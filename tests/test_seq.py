#pylint: disable = no-value-for-parameter
from euler_math import Seq, seq


def test_seq_init():
    squares = Seq.init(5, lambda x: x*x)
    assert list(squares) == [0,1,4,9,16]


def test_seq_unfold_unpacked():
    fib = Seq.unfold(lambda a, b: (b, (b, a+b)), (0,1))
    assert next(fib) == 1
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3


def test_seq_unfold_packed():
    fib = Seq.unfold(lambda p: (p[1], (p[1], p[1]+p[0])), (0,1))
    assert next(fib) == 1
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3
    

def test_seq_unfold_finite():
    def next_n(n):
        if n > 0:
            return (n, n-1)
        else:
            return None
    result = Seq.unfold(next_n, 4)
    assert list(result) == [4,3,2,1]
    

def test_seq_unfold_single_parameter():
    squares = Seq.unfold(lambda x: (x*x, x+1), 1)
    assert next(squares) == 1
    assert next(squares) == 4
    assert next(squares) == 9
    assert next(squares) == 16
    

def test_seq_initInfinite():
    squares = Seq.initInfinite(lambda x: (x*x))
    assert next(squares) == 0
    assert next(squares) == 1
    assert next(squares) == 4
    assert next(squares) == 9


def test_seq_sum():
    sequence = [1,2,3,4,5]
    result = sequence >> Seq.sum()
    assert result == 15


def test_seq_sum_inline():
    sequence = [1,2,3,4,5]
    result = Seq.sum(sequence)()
    assert result == 15
    

def test_seq_sumBy():
    sequence = [1,2,3,4,5]
    result = sequence >> Seq.sumBy(lambda x: x*x)
    assert result == 55


def test_seq_scan():
    sequence = [1,2,3]
    result = sequence >> Seq.scan(lambda a,b: a+b, 0)
    assert next(result) == 0
    assert next(result) == 1
    assert next(result) == 3
    assert next(result) == 6


def test_seq_scani():
    sequence = [1,2,3]
    result = sequence >> Seq.scani(lambda a,b: a+b, 0)
    assert next(result) == (0,0)
    assert next(result) == (1,1)
    assert next(result) == (2,3)
    assert next(result) == (3,6)


def test_seq_filter():
    sequence = range(7)
    result = sequence >> Seq.filter(lambda x: x%2 == 1)
    assert next(result) == 1
    assert next(result) == 3
    assert next(result) == 5


def test_seq_takeWhile():
    sequence = range(7) >> Seq.takeWhile(lambda x: x<3)
    result = list(sequence)
    assert result == [0,1,2]


def test_seq_skipWhile():
    sequence = range(7) >> Seq.skipWhile(lambda x: x<3)
    result = list(sequence)
    assert result == [3,4,5,6]


def test_seq_skip():
    sequence = range(7) >> Seq.skip(3)
    result = list(sequence)
    assert result == [3,4,5,6]


def test_seq_nth():
    result = range(7) >> Seq.nth(4)
    assert result == 4

def test_seq_map():
    sequence = [1,2,3,4,5] >> Seq.map(lambda x: x*x)
    result = list(sequence)
    assert result == [1,4,9,16,25]


def test_seq_mapi_unpacked():
    result = [1,2,3,4,5] >> Seq.mapi(lambda i,x: (i,x*x))
    assert next(result) == (0,1)
    assert next(result) == (1,4)
    assert next(result) == (2,9)
    assert next(result) == (3,16)
    assert next(result) == (4,25)

    
def test_seq_mapi_packed():
    result = [1,2,3,4,5] >> Seq.mapi(lambda x: (x[0],x[1]*x[1]))
    assert next(result) == (0,1)
    assert next(result) == (1,4)
    assert next(result) == (2,9)
    assert next(result) == (3,16)
    assert next(result) == (4,25)


def test_seq_toList():
    result = range(5) >> Seq.toList()
    assert result == [0,1,2,3,4]


def test_seq_toSet():
    result = range(5) >> Seq.toSet()
    assert result == {0,1,2,3,4}


def test_seq_append():
    result = range(3,6) >> Seq.append(range(3))
    assert list(result) == [0,1,2,3,4,5]


def test_seq_take():
    sequence = [1,2,3,4,5,6,7,8]
    result = sequence >> Seq.take(3)
    assert list(result) == [1,2,3]


def test_seq_max():
    sequence = range(5)
    result = sequence >> Seq.max()
    assert result == 4
    
def test_seq_min():
    sequence = range(5)
    result = sequence >> Seq.min()
    assert result == 0
    

def test_seq_reduce():
    result = [1,2,3,4,5] >> Seq.reduce(lambda a,b: a+b)
    assert result == 15
    
        
def test_seq_window():
    sequence = range(5) >> Seq.window(2)
    assert next(sequence) == (0,1)
    assert next(sequence) == (1,2)
    assert next(sequence) == (2,3)


def test_seq_product():
    sequence = [1,2,3,4]
    result = sequence >> Seq.product()
    assert result == 24


def test_seq_head():
    sequence = range(5)
    result = sequence >> Seq.head()
    assert result == 0


def test_seq_find():
    sequence = range(1,10)
    result = sequence >> Seq.find(lambda x: x%5 == 0)
    assert result == 5


def test_seq_findIndex():
    sequence = range(1,10)
    result = sequence >> Seq.findIndex(lambda x: x%5 == 0)
    assert result == 4


def test_seq_rev():
    sequence = range(3)
    result = sequence >> Seq.rev()
    assert list(result) == [2,1,0]


def test_seq_zip():
    a = range(5)
    b = range(1,6)
    result = b >> Seq.zip(a)
    assert list(result) == [(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)]
    
    
def test_seq_flatten():
    sequence = [[1], [2,2], [3,3,3]]
    result = sequence >> Seq.flatten()
    assert list(result) == [1, 2, 2, 3, 3, 3]
    

def test_seq_length():
    sequence = range(4)
    result = sequence >> Seq.length()
    assert result == 4
    

def test_seq_exists():
    sequence = range(4)
    result = sequence >> Seq.exists(lambda x: x%2==0)
    assert result


def test_seq_collect():
    sequence = [1,2,3]
    result = sequence >> Seq.collect(lambda x: [x]*x)
    assert list(result) == [1, 2, 2, 3, 3, 3]


def test_seq_distinct():
    sequence = [1, 2, 2, 3, 3, 3]
    result = sequence >> Seq.distinct()
    assert list(result) == [1,2,3]
    

def test_seq_forall_true():
    sequence = [5, 10, 15]
    result = sequence >> Seq.forall(lambda x: x%5 == 0)
    assert result
    

def test_seq_forall_false():
    sequence = [5, 10, 15, 18]
    result = sequence >> Seq.forall(lambda x: x%5 == 0)
    assert not result
    

def test_seq_maxBy():
    sequence = [5, 15, -10, -17]
    result = sequence >> Seq.maxBy(abs)
    assert result == -17
    

def test_seq_sort():
    sequence = [5, 15, -10, -17]
    result = sequence >> Seq.sort()
    assert list(result) == [-17, -10, 5, 15]
    

def test_seq_sortBy():
    sequence = [5, 15, -10, -17]
    result = sequence >> Seq.sortBy(abs)
    assert list(result) == [5, -10, 15, -17]
