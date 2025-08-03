def search(query, ranking = lambda r:-r.stars):
    """Search for a restaurant by name or cuisine."""
    query = query.lower()
    results = []
    for restaurant in Restaurant.all:
        if query in restaurant.name.lower() :
            results.append(restaurant)
    return sorted(results, key=ranking)

def reviewed_both(r1, r2):
    """Return the number of reviewers who have reviewed both r1 and r2."""
    return fast_overlap(r1.reviewers, r2.reviewers)

def fast_overlap(s, t):
    """Return the overlap between two sorted lists."""
    i, j , count = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count

class Restaurant:
    all = []
    """A restaurant with a name, cuisine, and rating."""
    def __init__(self, name, stars, reviewers):
        self.name = name
        self.stars = stars
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def __repr__(self):
        return '<' + self.name + '>'
    
    def similar(self, k, similarity=reviewed_both):
        """Return a list of k restaurants similar to this one."""
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key=lambda r: similarity(self,r), reverse=True)[:k]
    
import json

reviewers_for_restaurant = {}
for line in open('reviews.json'):
    r = json.loads(line)
    biz = r['business_id']
    if biz not in reviewers_for_restaurant:
        reviewers_for_restaurant[biz] = [r['user_id']]
    else:
        reviewers_for_restaurant[biz].append(r['user_id'])

for line in open('restaurants.json'):
    r = json.loads(line)
    reviewers = reviewers_for_restaurant[r['business_id']]
    Restaurant(r['name'], r['stars'], sorted(reviewers))

while True:
    print('>', end=' ')
    results = search(input().strip())
    for r in results:
        print(r, 'shares reviewers with', r.similar(3))