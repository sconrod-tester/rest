from functools import wraps

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

