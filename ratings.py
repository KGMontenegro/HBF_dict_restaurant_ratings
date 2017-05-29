"""Restaurant rating lister."""

#import sys

def get_dict_ratings(filename):
    """Opens file, converts each line into a list and separates by : 
        then  unpacks and converts into dictionary
    """
    #filename = sys.argv[1]
    filename = open(filename)
    rating_dicts = {}
    for line in filename:
        #here it takes a line from the file, rstrip() removes the new line char and all spaces on the right side and split(":") separates string by :
        sentence = line.rstrip().split(":")
        # unpacking the list
        rate_key, rate_value = sentence
        #taking rate_key making it a key in the rating_dicts and rate_value becomes a value in rate_dicts
        rating_dicts[rate_key] = rate_value
        #Here we tried to unpack sentence inside a for loop it did not work
        #for rate_key, rate_value in sentence:
    return rating_dicts
#make separate func for soted dict
print get_dict_ratings('scores.txt')
