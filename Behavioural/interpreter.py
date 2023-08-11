"""
INTERPRETER
System that can understand or process a language
* Recursively evaluate grammar and expressions
* Parsing, processing engines, etc.
* Two components
    - Terminal expressions
    - Non terminal expressions
"""

class AbstractExpression:
    """Abstract Expression class"""
    @staticmethod
    def interpret():
        """Static interpret method"""
        pass


# Terminal expression
class Number(AbstractExpression):
    """Number class"""
    def __init__(self, value):
        self.value = float(value)

    def interpret(self):
        """Interpret method"""
        return self.value


# Non-terminal expression
class AlgebraExpression(AbstractExpression):
    """Algebra Expression class"""
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(AlgebraExpression):
    """Add Expression class"""
    def interpret(self):
        """Interpret method"""
        return self.left.interpret() + self.right.interpret()


class Subtract(AlgebraExpression):
    """Subtract Expression class"""
    def interpret(self):
        """Interpret method"""
        return self.left.interpret() - self.right.interpret()


class Multiply(AlgebraExpression):
    """Multiply Expression class"""
    def interpret(self):
        """Interpret method"""
        return self.left.interpret() * self.right.interpret()


class Divide(AlgebraExpression):
    """Divide Expression class"""
    def interpret(self):
        """Interpret method"""
        return self.left.interpret() / self.right.interpret()


if __name__ == '__main__':
    # Interpreter
    target_exp = "3 + 5 - 2 * 7 / 5 + 11"

    tokens = target_exp.split(" ")
    expressions = []

    for i in range(len(tokens)):
        if i == 0:
            expressions.append(Number(tokens[i]))
        elif tokens[i] == "+":
            expressions.append(Add(expressions.pop(), Number(tokens[i+1])))
        elif tokens[i] == "-":
            expressions.append(Subtract(expressions.pop(), Number(tokens[i + 1])))
        elif tokens[i] == "*":
            expressions.append(Multiply(expressions.pop(), Number(tokens[i+1])))
        elif tokens[i] == "/":
            expressions.append(Divide(expressions.pop(), Number(tokens[i + 1])))

    result = expressions.pop().interpret()
    print(result)



