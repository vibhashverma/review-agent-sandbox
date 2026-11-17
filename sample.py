def get_odds(numbers):
    result = []
    for n in numbers:
        if n % 2 == 1:
            result.append(n)
    return result

