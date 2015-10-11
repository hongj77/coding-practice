

word = raw_input()

def isPalin(word):
  for i in range(len(word)/2):
    if word[i] != word[-1-i]:
      return False
  return True


''' how many letters do you have to add to the RIGHT side of the word
    to make it a palindrome. Find the minimum count. O(N^2). not the best'''
def palinAddition(word):
  letters = 0
  begin = 0
  end = len(word)-1

  while begin < end:
    if isPalin(word[begin:end+1]):
      break
    else:
      letters += 1
      begin += 1
  return letters
     

print palinAddition(word)
