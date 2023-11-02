# Sample session 1.1 from Composing Programs 
# URL: http://www.composingprograms.com/pages/11-getting-started.html

2 + 2

from urllib.request import urlopen

shakespeare = urlopen('https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt')
words = set(shakespeare.read().decode().split())
print({w for w in words if len(w) == 6 and w[::-1] in words})

