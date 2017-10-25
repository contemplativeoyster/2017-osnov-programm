import sys
sent_id = 1
lines = sys.stdin.readlines()

for line in lines:
    line = line.strip()
    if line == '':
        continue
    print('#sent_id = %d' % (sent_id))
    print('#text = %s' % (line.strip()))
    tok_id = 1
    punctuation = ['.', ':','(',')','!','?']
    for symbols in punctuation:
        line = line.split(' ')
        tokens = line.split(' ')
        for token in tokens:
            if token.strip() == '':
                continue
            print ('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (tok_id, token, '_', '_', '_', '_','_', '_', '_', '_'))
            tok_id = tok_id + 1
        print ('')
        sent_id = sent_id + 1
