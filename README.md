# NodictAnagram
A anagram generator (and finder/solver) with some fake words and other weird things allowed, for Python 3.

## Licenses
* Code:
  * see LICENSE
* Content:
  * hunspell en_US dictionary: custom MIT-style license (see README_en_US.txt)
  * CC0 unless otherwise specified above or in corresponding CREDITS file.

## Data formats
* census
see .header.txt files for names of columns
"cumulative frequency for a value x is the total number of scores that are less than or equal to x"
https://stattrek.com/statistics/charts/cumulative-plot.aspx

## Performance
all estimated times below were calculated using:
    Python 3.6.6
    Intel i7 4770K
    use_fake_words=True
    use_dictionary=False
    lists: 'dist.all.last', 'census-derived-all-first.txt'
    input: Jake Gustafson
see also value exists: <https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list>
fastest first:
* bloom filter
  * items cannot be removed
* cuckoo filter
ETA after 35s for my name is 8.05 days (7.67 with browser closed) <https://github.com/beaulian/cuckoofilter> via pip install cuckoofilter
  * items can be removed
  <https://stackoverflow.com/questions/867099/bloom-filter-or-cuckoo-hashing>
  "Bloom and Cuckoo filters have NO false negatives" but may have false positives.
  (which is ok for anagrams since having real words is not critical)
* frozenset:
ETA after 35s for my name is 9.9 days
  <https://stackoverflow.com/questions/38187286/find-unique-pairs-in-list-of-pairs>
`word_set = frozenset(words)`
* set:
ETA after 35s for my name is 8.8 days
```
words = []
words_set = set(words)
if word in words_set:
    print(word)
```
* bisect
ETA after 35s for my name is 8.25 days
  <https://stackoverflow.com/questions/212358/binary-search-bisection-in-python>
* list
ETA after 35s for my name is 7.61 days
`if word in words`

## Known Issues
* add checkbox for ag.allow_old_words, ag.use_fake_words (True by default), ag.use_dictionary

* add word lists from http://www.outpost 9
  .co m/fi les/W ordLists.html
* add name lists from http://mbejda.github.io/
