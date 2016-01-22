from functools import wraps

def identity(x):
    'Pure, higher-order, identity function'
    return x

registry = set()

def register_set(func):
    'Higher-order, identity function, that registers as a side-effect'
    registry.add(func.__name__)    
    return func

dispatcher = {}      # map a name to a function

def register(func):
    'Higher-order, identity function, that registers as a side-effect'
    dispatcher[func.__name__] = func
    return func

def add_logging(func):
    @wraps(func)
    def inner(x):
        print 'The', func.__name__, 'function was called with', x
        answer = func(x)
        print 'The answer is', answer
        return answer
    return inner

def cache(func):
    answers = {}
    @wraps(func)
    def inner(x):
        if x in answers:
            return answers[x]
        answer = func(x)
        answers[x] = answer
        return answer
    return inner

if __name__ == '__main__':

    ## Sample data for higher order functions #######################

    import time

    @cache
    @register
    @register_set
    @identity                   # square = identity(square)
    @add_logging
    def square(x):
        'Return a value times itself'
        return x * x

    @cache
    @add_logging
    def collatz(x):
        if x % 2 == 0:
            return x // 2
        return 3 * x + 1

    @cache
    def big_calc(x):
        'Simulate a slow operation'
        print 'Doing hard work!'
        time.sleep(1)
        return x + 1


    
