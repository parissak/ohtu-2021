from matchers import All, And, HasAtLeast, HasFewerThan, PlaysIn


class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher_obj = matcher
    
    def playsIn(self, team):
        return QueryBuilder(And(self._matcher_obj, PlaysIn(team)))

    def hasAtLeast(self, points, attribute):
        return QueryBuilder(And(self._matcher_obj, HasAtLeast(points, attribute)))
    
    def HasFewerThan(self, points, attribute):
        return QueryBuilder(And(self._matcher_obj, HasFewerThan(points, attribute)))

    def build(self):
        return self._matcher_obj