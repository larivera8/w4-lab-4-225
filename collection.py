# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {              # added o
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    #No comma after "1889"
    "Gerard Manley Hopkins": "1889", }                       # added perentheses and comma

'''
for author, date in authors.items():
    print("%s" % author + " died in " + "%s." % date)
'''
for author, date in authors.items():                           #added comma
    print("%s" % authors + " died in " + "%d." % Date)         #added perentheses
