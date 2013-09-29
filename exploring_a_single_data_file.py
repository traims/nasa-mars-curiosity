# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json
path = 'data/usagov_bitly_data2012-05-21-1337634399.txt'
records = [json.loads(line) for line in open(path)]

# <codecell>

# Display a couple of records
records[0:2]

# <codecell>

# Display the user agent from the first record
records[0]["a"]

# <codecell>

# Utility function: get counts for each element from a collection

from collections import defaultdict

def get_counts(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        count[x] += 1
    return counts

# <codecell>

# How a time zone looks like
records[0]['tz']

# <codecell>

# Check if a time zone is listed for the record
def time_zone_listed(record):
    return 'tz' in record
    
time_zone_listed(records[0])

# <codecell>

# See where the timezone is not listed       
[item for item in records if not time_zone_listed(item)]

# <codecell>

time_zones = [item['tz'] for item in records if time_zone_listed(item)]
time_zones[0:3]

# <codecell>

from collections import Counter

Counter(time_zones).most_common(10)

