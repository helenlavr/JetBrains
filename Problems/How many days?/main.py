seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
day = 60 * 60 * 24
print([i // day for i in seconds if i // day >= 1])
