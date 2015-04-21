#ok so we could move syllabizer under word, so that it would be WordSyllabizer, right? yes
#seems better
#then move this to the OLD code directory, in tact, then just set the Syllabizers to use word.syllables_set() rather
#than word.wordsyllables_set, right? yes
#ok finally, in order to make this work, I need tests...how should they look for now? like basic basic tests in test.py
#because that script is getting a little unruly too, right? yes

#how do you think I should make them look? w ell very simple, take each class, create instance, do something and check all results,
#like if word now have syllables, for word X it has 3 syllables, they are equalt to that and so on.
# right but
# something like factorialtest here ? http://pymbook.readthedocs.org/en/latest/testing.html ? just so I can get an assert function? yeah looks good
#ok cool I'll write that up in the morning. thanks a lot fo r all the help no problems

class WordSyllables(object):
  def __init__(self, **kwargs):
    self._syllables = []
    self.syllables_set(kwargs.get('syllables', []))
  def __str__(self):
    return str({
      "syllables" : self.syllables(),
    })

  def syllables(self):
    return self._syllables
  def syllables_set(self, syllables):
    self._syllables = syllables


  def as_repr(self, repr_name, **kwargs):
    join_str = kwargs.get("join_str", "-")
    return join_str.join( map(lambda c: c.as_repr(repr_name, **kwargs), self.syllables()) )
