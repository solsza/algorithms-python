def palindrome(s):
  if len(s) == 0 or len(s) == 1:
    return True

  if s[0] != s[-1]:
    return False

  return palindrome(s[1:-1])