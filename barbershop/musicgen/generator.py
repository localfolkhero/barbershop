import random
from tempfile import NamedTemporaryFile
from music21 import converter
import io

class MusicGenerator():
    pass

class RandomMusicGenerator(MusicGenerator):
    name = None

    def noteT(self):
        measureT = ""
        totalbeatsT = 4
        while totalbeatsT > 0:
            if totalbeatsT <= 1:
                if totalbeatsT == 0.5:
                    b = 0.5
                else:
                    b = random.choices([0.5, 1], weights = (38, 62))
                    b = b[0]
            else:
                b = random.choices([0.5, 1, 1.5], weights = (34, 52, 24))
                b = b[0]

            note = random.choice(["G", "A", "B", "c", "d", "e", "f", "g", "a", "b"])

            if b == 0.5:
                note = (f"{note}/")
            elif b == 1.5:
                note = (f"{note}3/")
            elif b == 2:
                note = (f"{note}2")

            # Get accidentals
            accidentals = random.choices(["", "^", "_"], weights=(89, 7, 4))
            # Pick the first one in the list
            accidental = accidentals[0]

            totalbeatsT -= b
            measureT = f"{measureT}{accidental}{note}"
        return measureT + "|"

    def noteL(self):
        measureL = ""
        totalbeatsL = 4
        while totalbeatsL > 0:
            if totalbeatsL == 0.5:
                b = 0.5
            else:
                b = random.choice([0.5, 1])

            note = random.choice(["C", "D", "E", "F", "G", "A", "B", "c", "d", "e"])

            if b == 0.5:
                note = (f"{note}/")

            # Get accidentals
            accidentals = random.choices(["", "^", "_"], weights=(89, 7, 4))
            # Pick the first one in the list
            accidental = accidentals[0]

            totalbeatsL -= b
            measureL = f"{measureL}{accidental}{note}"
        return measureL + "|"

    def noteA(self):
        measureA = ""
        totalbeatsA = 4
        while totalbeatsA > 0:
            if totalbeatsA <= 3:
                if totalbeatsA <= 2:
                    if totalbeatsA <= 1:
                        b = 1
                    else:
                        b = random.choices([1, 2], weights = (35, 65))
                        b = b[0]
                else:
                    b = random.choices([1, 2, 3], weights = (20, 36, 44))
                    b = b[0]
            else:
                b = random.choices([1, 2, 3, 4], weights = (15, 30, 25, 50))
                b = b[0]

            note = random.choice(["D,", "E,", "F,", "G,", "A,", "B,", "C", "D", "E"])

            if b == 2:
                note = (f"{note}2")
            elif b == 3:
                note = (f"{note}3")
            elif b == 4:
                note = (f"{note}4")

            # Get accidentals
            accidentals = random.choices(["", "^", "_"], weights=(89, 7, 4))
            # Pick the first one in the list
            accidental = accidentals[0]

            totalbeatsA -= b
            measureA = f"{measureA}{accidental}{note}"
        return measureA + "|"

    def noteB(self):
        measureB = ""
        totalbeatsB = 4
        while totalbeatsB > 0:
            if totalbeatsB == 2:
                b = 2
            else:
                b = random.choice([2, 4])

            note = random.choice(["F,,", "G,,", "A,,", "B,,", "C,", "D,", "E,"])

            if b == 2:
                note = (f"{note}2")
            else:
                note = (f"{note}4")

            # Get accidentals
            accidentals = random.choices(["", "^", "_", "="], weights=(75, 9, 2, 14))
            # Pick the first one in the list
            accidental = accidentals[0]

            totalbeatsB -= b
            measureB = f"{measureB}{accidental}{note}"
        return measureB + "|"

    def key_sig(self):
        x = random.choices([1, 2], weights = (7, 5))
        y = random.choice(["A", "B", "C", "D", "E", "F", "G"])
        
        if x == 2:
            key_sig = (f"{y}#")
        else:
            key_sig = (y)
        return key_sig

    def tempo(self):
        tempo = random.randrange(80, 200, step = 10)
        return tempo

    def lowercase(self):
        n = random.randrange(97, 122)
        Real_n = chr(n)
        return Real_n
    
    def name_char(self):
        if self.name:
            return self.name
        
        how_many_to_create = random.randrange(3, 8)
        self.name = "".join([self.lowercase() for i in range(how_many_to_create) ])
        return self.name

    def generateABC(self):
        # Generate name
        self.name_char()

        music_file = []
        
        music_file.append(f"T: {self.name}")
        music_file.append("M: 4/4")
        music_file.append("L: 1/4")
        music_file.append(f"Q: {self.tempo()}")
        music_file.append(f"K: {self.key_sig()}") #fix for key sig.
        music_file.append("%%score V:1 V:2 (V:3 V:4)")
        music_file.append("V:1 clef=treble")
        music_file.append(f"{''.join([ self.noteT() for i in range(4) ]) }")

        music_file.append("V:2 clef=treble")
        music_file.append(f"{''.join([ self.noteL() for i in range(4) ]) }")

        music_file.append("V:3 clef=bass+8")
        music_file.append(f"{''.join([ self.noteA() for i in range(4) ]) }")

        music_file.append("V:4 clef=bass+8")
        music_file.append(f"{''.join([ self.noteB() for i in range(4) ]) }")
        
        # print( "\n".join(music_file) )

        music_file_str = "\n".join(music_file) + "\n"

        return music_file_str
    
class ABCtoMusicConverter():
    def generateMusicXML(self, music_file_str):
        f = io.StringIO(music_file_str)
        s2 = converter.parse(f.read(), format='ABC')
        q = s2.write("musicxml")
        output = q.read_text()
        return output


    def generateMusicMIDIbytes(self, music_file_str):
        f = io.StringIO(music_file_str)
        s2 = converter.parse(f.read(), format='ABC')
        q = s2.write('midi')
        output = q.read_bytes()
        return output        
