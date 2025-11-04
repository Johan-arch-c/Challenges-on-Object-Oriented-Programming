class IntegerToRoman:
    def __init__(self):
        self.value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
    def convert(self, number):
        if not (0 < number < 4000):
            raise ValueError("Number must be between 1 and 3999")
        roman_numeral = ""
        for value, symbol in self.value_map:
            while number >= value:
                roman_numeral += symbol
                number -= value
        return roman_numeral
if __name__ == "__main__":
    converter = IntegerToRoman()
    print(converter.convert(1994))