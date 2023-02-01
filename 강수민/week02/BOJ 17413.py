w = list(input())
tag = False
word = ''
result = ''

for i in w:
  # tag가 아닌 것
  if tag == False:
    if i == '<':
      tag = True
      word = word + i
    # 공백을 기준으로 단어 정리
    elif i==' ':
      word = word + i
      result = result + word
      word = ''
    else:
      word = i + word

  # tag인 것
  elif tag == True:
    word = word + i
    if i == '>':
      tag = False
      result = result + word
      word = ''

print(result + word)
