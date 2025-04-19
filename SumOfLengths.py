def sum_of_lengths(strings):
  if(len(strings) == 0): return 0
  length = calculate_lengths(strings[0])
  return length + sum_of_lengths(strings[1:])


def calculate_lengths(string):
  return len(string)
