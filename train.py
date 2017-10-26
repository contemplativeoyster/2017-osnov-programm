import sys

lines = sys.stdin.readlines()

# variable to store counts for individual tags
tag_count = {}
# variable to store counts of tags given words
tag_word = {}
# variable to store the counts of individual surface forms/ words
form_count = {}

total = 0

for line in lines:
    line = line.strip()
    if '\t' not in line:
        continue
    # take the line and return a list of columns
    row = line.split('\t')
    # print(row)
    # if there aren't exactly ten columns skip the line
    if len(row) != 10:
        continue
    tag = row[3]
    # print(tag)
    if '_' in tag:
        continue
    if tag not in tag_count:
        tag_count[tag] = 0

        word = row[1]
        if '_' in word:
            continue
        # print(word)
        if word not in form_count:
            form_count[word] = 0
            form_count[word] = form_count[word] + 1
        # print(form_count[word])

        if word not in tag_word:
            tag_word[word] = {}

        if tag not in tag_word[word]:
            tag_word[word][tag] = tag_word[word][tag] + 1

        # print(tag_word)
        # print(tag_word[word][tag])

        tag_count[tag] = tag_count[tag] + 1
        total = total + 1

    # print(tag_count)
    # print('total of tagged words =', total)

    print('# P\tcount\ttag\tform')

    for tag in tag_count:
        freq = tag_count[tag]/total
        print('%.2f' % (freq), '\t', tag_count[tag], '\t', tag, '\t', '_')

        # for each of the words in the matrix
        for word in tag_word:
            # for each of the tag
            for tag in tag_word[word]:
                freq = tag_word[word][tag]/form_count[word]

                print('%.2f\t%d\t%s\t%s' % (freq, tag_word[word][tag], tag, word))
                
