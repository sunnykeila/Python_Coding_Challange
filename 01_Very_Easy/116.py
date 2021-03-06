"""
Tallest Birthday Cake Candles
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Examples
birthday_cake_candles([4, 4, 1, 3]) ➞ 2
# The maximum height candles are four units high.
# There are two of them, so you return 2.

birthday_cake_candles([3, 2, 1, 3]) ➞ 2

birthday_cake_candles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25]) ➞ 4
Notes
N/A
"""
def birthday_cake_candles(candles):
    return candles.count(max(candles))


def birthday_cake_candles(candles):
    m = max(candles)
    count = candles.count(m)
    return count
