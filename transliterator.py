import sys

table = {}

table ['а'] = 'a'
table ['б'] = 'b'
table ['в'] = 'v'
table ['г'] = 'h'
table ['ґ'] = 'g'
table ['д'] = 'd'
table ['е'] = 'e'
table ['є'] = 'je'
table ['ё'] = 'jo'
table ['ж'] = 'ž'
table ['з'] = 'z'
table ['i'] = 'i'
table ['ї'] = 'ji'
table ['и'] = 'y'
table ['ы'] = 'y'
table ['й'] = 'j'
table ['к'] = 'k'
table ['л'] = 'l'
table ['м'] = 'm'
table ['н'] = 'n'
table ['о'] = 'o'
table ['п'] = 'p'
table ['р'] = 'r'
table ['с'] = 's'
table ['т'] = 't'
table ['у'] = 'u'
table ['ф'] = 'f'
table ['х'] = 'ch'
table ['ц'] = 'c'
table ['ч'] = 'č'
table ['ш'] = 'š'
table ['щ'] = 'šč'
table ['ѣ'] = 'ji'
# was used until 1945
table ['ю'] = 'ju'
table ['я'] = 'ja'
table ['ь'] = '' '
table ['ъ'] = '' '

for line in sys.stdin.readlines():
    line = line.strip()

    if '\t' not in line:
        print(line)
        continue
    row = line.strip().split('\t')
    if len(row) != 10:
        continue
    transliterated = row[1]
    for c in table: # c for character
        transliterated = transliterated.replace(c, table[c])

    row[9] = 'Translit=' + transliterated
    out = '\t'.join(row)
    print(out.strip())
