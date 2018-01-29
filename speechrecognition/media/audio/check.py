import os

command = "pocketsphinx_continuous -infile kendra_fine.wav>out.txt"
data = os.system(command)

with open('out.txt', 'rb') as t:
    print t.read(), 'audio to text'
