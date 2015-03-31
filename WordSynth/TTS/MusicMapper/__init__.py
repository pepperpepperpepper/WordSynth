from music21 import *
class MusicMapper():
  def __init__(self):
    pass
  def applyNote(self, syllable):
    #so should this take two arguments, a note and a syllable? or should the note
    #be an internal attribute? well what we should generate actually, and what's the input will be?
#in put will various, but at its most ...I guess packed up form, the input for word will be a text file
#and the input for notes will be a midi file. 

# but I don't need to worry about that first, the input can be more specific, I can generate a note from a test script, 
#and try to get it to work with a syllable first, and sort of build it out around that...does that make sense? well i get it, just need
#to know overview, how it all supposed to work, do we generate a note for each syllable, or ... well
#that's a great question...I don't know the answer to that, because conceivably the relationships between notes and syllables
#might not be 1 to 1, as that's not how music works. a syllable has at least 1 note, and a note has at least 1 syllable (though I guess
#you could accomplish the latter by breaking the note up into smaller notes, you know what I mean?) yeah so we have a words, and need to make
#notes which will sound like word said? here's how it works


#the note is ultimately just two things, frequency and length 440k and 100 milliseconds
#the syllable is a little bit more complex, it's a combination of consonant and vowel sounds
#the singing synthesizers work like this:
#the consonant sounds are recorded separately from the vowel sounds (as true with all tts software I think)
#anyway basically the vowel sound is pitch shifted and time stretched to match the majority of the duration of the note
#and some of the duration (usually I think just a fixed length, like 50 milliseconds) is used for the 
#consonant sound, which is not pitch shifted

#at the end, the two sounds are joined, and you have a sung syllable, do you understand? yes ok perfect

#so again, I know exactly how this works, but have poor ability to design this api in a usable way...I know
#more now though, so basically I'm thinking I start with this MusicMapper, or NoteMapper class

#what do you think it should do? so if i get it all correctly, there will be one note for each character, and syllable consist of characters,
#so first pass will be to set notes for each character, and second pass will be for example to fix syllable into proper sequence of notes given that
#we know what notes will be used there, their order, attributes etc. so if i have a base note, i first go over characters, set base note to all of them,
#add pitch to vowels, and then go over syllables to fix notes. something like that maybe?

#ahh not quite...the only thing missing is the fact that the ratio is not one note per character...
#ok so this is really the tricky part that I need help with


#lets say in a simple example the ratio between notes and syllables is 1 to 1
# I have 5 notes A B C C D 
# and I have 5 syllables
#  two three four two














n1 = note.Note('e4')
n1.duration.type = 'whole'
#so this creates a new note, and sets the "duration" on here...

#that's really all we need for an example of how to map notes to syllables, right? i guess so
