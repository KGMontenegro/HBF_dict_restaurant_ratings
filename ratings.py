"""Restaurant rating lister."""

import sys

def get_ratings(filename):
    """creating dictionary from a given file, and return it.
    """
    # filename = sys.argv[1]
    f = open(filename)
    ratings = {}
    for line in f:
        #here it takes a line from the file, rstrip() removes the new line char
        # and all spaces on the right side and split(":") separates string by :
        # and upacks the string.
        restaurant, rating = line.rstrip().split(":")
        #taking rate_key making it a key in the rating_dicts and rate_value becomes a value in rate_dicts
        ratings[restaurant] = rating
        #Here we tried to unpack sentence inside a for loop it did not work
        #for rate_key, rate_value in sentence:

    f.close()
    return ratings




def print_sorted(ratings):
    """sorts and prints a given dictionary. """
    for restaurant, rating in sorted(ratings.items()):
        print "{}: {}".format(restaurant, rating)


filename = sys.argv[1]

print_sorted(get_ratings(filename))
