import random
# 创建单词序列元组
words = ('python', 'juice', 'easy', 'answer', 'continue')

word = random.choice(words)
jumble = ''
while word :
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position]+word[(position + 1):]

print("乱序后的单词： ", jumble)