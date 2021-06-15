import operator


class Operators:
    def __init__(self):
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '<': operator.lt,
            '>': operator.gt,
            '<=': operator.le,
            '>=': operator.ge,
            '!': operator.not_,
            '==': operator.eq,
            '!==': operator.ne
        }

    def logic(self, op, a, b) -> bool:
        return self.ops[op](str(a), str(b))

    def arithmetic(self, op, a, b) -> int:
        return int(self.ops[op](int(a), int(b)))
