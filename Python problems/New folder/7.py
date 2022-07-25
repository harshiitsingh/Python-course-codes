words = ['ab', 'aba', 'abaa', 'baba']

cnt = 0

for word in words:
    if len(word) >= 3 and word[0] == word[-1]:
        cnt += 1

print(cnt)