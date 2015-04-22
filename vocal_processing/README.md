<html>
<pre>
PROCESSING (using the voice synthesizer)
start with
  -the music object, containing notes and syllables, their respective durations
  -default ratio between consonant length and vowel length to send to the voice synthesizer
  -too many syllables per number of seconds ratio (to test data with)

  iterate through the notes of the music object, generating audio samples on the fly (this is something that could potentially be divided
  up for parallel processing, so it's important to keep this as sort of it's own separate api section)
  is it silence?
  yes
     process silence with sox using the expected duration
     next
  is it not silence?
  yes
     1 note and 1 syllable?
     yes
        break syllable up into phonemes
        process using the ratio between consonant length and vowel length (result must be a little shorter, not longer,
        than the expected length)
        NOT YET IMPLEMENTED add vibrato with sox
        pad with silence with sox
        name file by idx
        next
     &lt;1 note and 1 syllable?
     yes
        number of notes == m
        break syllable up into phonemes
        divide total length of clip into m parts
        group consonant phonemes with vowels, evenly distribute vowels
        pad with silence with sox
        name file by idx
        next
     1 note and &lt;1 syllable?
     yes
        are there too many syllables per num of seconds?
        yes
          ERROR
        create longer TUNE format string to account for multiple syllables
        pad with silence with sox
        name file by idx
        next

  join file with sox


on to effects and mixing!

</pre>
</html>
