#currency.py
class Currency:

    currencies = {'CHF': 0.930023,  # Swiss Franc
                  'CAD': 1.264553,  # Canadian Dollar
                  'GBP': 0.737414,  # British Pound
                  'JPY': 111.019919,  # Japanese Yen
                  'EUR': 0.862361,  # Euro
                  'USD': 1.0}  # US Dollar

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        Transforms this Currency object from the unit "self.unit" to "new_unit".
        """
        self.value = (self.value / Currency.currencies[self.unit]) * Currency.currencies[new_unit]
        self.unit = new_unit

    def __repr__(self):
        """
        Returns the string representation of the Currency object, rounded to two digits.
        """
        return "{:.2f} {}".format(self.value, self.unit)

    def __str__(self):
        """
        Returns the string representation of the Currency object.
        """
        return repr(self)

    def __add__(self, other):
        """
        Defines the '+' operator. If 'other' is a Currency object, the currency values are added
        and the result will be in the unit of 'self'. If 'other' is an int or a float, it's treated
        as a USD value.
        """
        if isinstance(other, Currency):
            converted_other = Currency(other.value, other.unit)
            converted_other.changeTo(self.unit)
            return Currency(self.value + converted_other.value, self.unit)
        elif isinstance(other, (int, float)):
            converted_value = other / Currency.currencies['USD'] * Currency.currencies[self.unit]
            return Currency(self.value + converted_value, self.unit)
        else:
            raise TypeError("Unsupported operand type for +: '{}'".format(type(other).__name__))

    def __radd__(self, other):
      # Check if self.unit is not USD, then convert self.value to USD
      if self.unit != 'USD':
          # Convert self.value from self.unit to USD
          converted_value_to_usd = self.value / Currency.currencies[self.unit]
      else:
          # If self.unit is already USD, no conversion is needed
          converted_value_to_usd = self.value

      # Add 'other' (which is in USD) to the converted value
      total_in_usd = converted_value_to_usd + other

      # Return the result as a new Currency object in USD
      return Currency(total_in_usd, "USD")


    def __sub__(self, other):
        """
        Defines the '-' operator. Works similarly to the '+' operator but for subtraction.
        """
        if isinstance(other, Currency):
            converted_other = Currency(other.value, other.unit)
            converted_other.changeTo(self.unit)
            return Currency(self.value - converted_other.value, self.unit)
        elif isinstance(other, (int, float)):
            converted_value = other / Currency.currencies['USD'] * Currency.currencies[self.unit]
            return Currency(self.value - converted_value, self.unit)
        else:
            raise TypeError("Unsupported operand type for -: '{}'".format(type(other).__name__))

    def __rsub__(self, other):
        """
        Handles subtraction when 'Currency' object is on the right.
        """
        if isinstance(other, (int, float)):
            converted_self = self.value * Currency.currencies[self.unit] / Currency.currencies['USD']
            return Currency(other - converted_self, 'USD')
        else:
            raise TypeError("Unsupported operand type for -: '{}'".format(type(other).__name__))


v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3)  # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3)  # an int or a float is considered to be a USD value
print(30 - v2)
