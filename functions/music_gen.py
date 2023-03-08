import random
import itertools

def noteT():
    measureT = ""
    totalbeatsT = 4
    while totalbeatsT > 0:
        a = random.choice([1, 2])
        if totalbeatsT == 0.5:
            b = 0.5
        else:
            b = random.choice([0.5, 1])
        
        if a == 1:
            x = random.randrange(65, 71)
        else:
            x = random.randrange(97, 103)
        noteTT = chr(x)
        
        if b == 0.5:
            noteTT = (f"{noteTT}/")
        
        # Get accidentals
        accidentals = random.choices(["", "^", "_"], weights=(89, 7, 4))
        # Pick the first one in the list
        accidental = accidentals[0]

        totalbeatsT -= b
        measureT = f"{measureT}{accidental}{noteTT}"
    return measureT + "|"

def noteB():
    measureB = ""
    totalbeatsB = 4
    while totalbeatsB > 0:
        c = random.choice([1, 2])
        if totalbeatsB == 2:
            d = 2
        else:
            d = random.choice([2, 4])
        if c == 1:
            y = random.randrange(65, 71)
        else:
            y = random.randrange(97, 103)
        noteBB = chr(y)
        
        if d == 2:
            noteBB = (f"{noteBB},,2")
        else:
            noteBB = (f"{noteBB},,4")

        # Get accidentals
        accidentals = random.choices(["", "^", "_"], weights=(89, 7, 4))
        # Pick the first one in the list
        accidental = accidentals[0]

        totalbeatsB -= d
        measureB = f"{measureB}{accidental}{noteBB}"
    return measureB + "|"

music_file = []

music_file.append("T: Name")
music_file.append("M: 4/4")
music_file.append("L: 1/4")
music_file.append(f"K: C") #fix for key sig.
music_file.append("V:1 clef=treble")
music_file.append(f"{''.join([ noteT() for i in range(3) ]) }")

music_file.append("V:2 clef=bass")


music_file.append(f"{''.join([ noteB() for i in range(3) ]) }")    


print( "\n".join(music_file) )

music_file_str = "\n".join(music_file) + "\n"

oo = open("output.abc", "w")

oo.writelines(music_file_str)
oo.close()

import io
f = io.StringIO(music_file_str)

from music21 import converter
# s = converter.parse("output.abc", format='ABC')
# s.id = 'test'
# s.show("midi")  # or s.write('midi', fp='output.mid')


s2 = converter.parse("output.abc", format='ABC')
s2.id = 'test2'
s2.write("musicxml", "musicxml.xml")