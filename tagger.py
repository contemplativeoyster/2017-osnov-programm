import sys

# open the file ready for reading
fd = open ('model.tsv')

frequent_tag = 'X' # variable to store the most frequent tag we have seen
last_max = 0 # variable to store the maximum frequency we have seen

word_tag = {} 
word_prob = {} 
for line in fd.readlines():
    line = line.strip() # take away newline characters at the beginning / end of the line
    line = line.split('\t') # split the line on tab to make a list X
    if int(line[1]) > last_max: # if the frequency of tag is higher than the previous maximum
           last_max = int(line[1]) # congratulations, we have a new maximum!
           frequent_tag = line[2]
# if we have never seen the surface form before, the most frequent tag is one we just saw
           surface_form = line[3]
           prob = float(line[0])
           tag = line[2]
           if surface_form not in word_tag:
               word_tag[surface_form] = tag
               word_prob[surface_form] = prob
# read the input and assign the most frequent tag to each token

           input = sys.stdin.readlines()
           for line in input:
               line = line.strip() # strip off excess whitespace
           # if there is no tab in the line, print it out and skip it
           if '\t' not in line:
               print(line)
           continue
           line = line.split('\t')
           # if we have seen the surface form before (line[1]) then use the most probable tag
           if line[1] in word_tag:
               line[3] = word_tag[linr[1]]
        # otherwise assign the most frequent tag to the input token
           else:
               line[3] = frequent_tag

           #print out the tagged line
           print('\t'.join(line))
           
