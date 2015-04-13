# your code goes here
scores_text = open('scores.txt')

rest_dictionary = {}

for line in scores_text:
    line = line.rstrip()
    restaurant, score = line.split(":")
    rest_dictionary[restaurant] = score
  
for restaurant, score in sorted(rest_dictionary.items()):
    print "%s has a score of %s." % (restaurant, score)