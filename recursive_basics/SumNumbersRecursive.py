def sum_numbers_recursive(numbers):
    if len(numbers) == 0: return 0
    return sum_numbers(numbers, 0)


def sum_numbers(numbers, pointer):
    current_value = numbers[pointer]
    if pointer == len(numbers) - 1 : return current_value
    return sum_numbers(numbers, pointer + 1) + current_value