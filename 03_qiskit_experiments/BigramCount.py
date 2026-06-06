from collections import defaultdict

text="Hello World"
text=text +"."
bigram_counts = defaultdict(int)

for ch1, ch2 in zip(text, text[1:]):
    bigram_counts[(ch1,ch2)]+=1

for pair,count in bigram_counts.items():
    print(pair,"->", count)