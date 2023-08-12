"""
STRATEGY
Multiple ways of handling data
* a class behaviour or algorithm can be changed at run time
* Objects contain algorithm logic
* Context object that can handle algorithm objects
+ Useful when we want to be able to add functionality without changing program structure
"""


class Printer:
    def __init__(self, format_strategy):
        self.format_strategy = format_strategy

    def print_string(self, message: str):
        print(self.format_strategy(message))


def lowercase_formatter(msg):
    return msg.lower()


def uppercase_formatter(msg):
    return msg.upper()


if __name__ == '__main__':
    input_string = "LOREM ipsum dolor SIT amet"
    lower_printer = Printer(lowercase_formatter)
    lower_printer.print_string(input_string)

    upper_printer = Printer(uppercase_formatter)
    upper_printer.print_string(input_string)

