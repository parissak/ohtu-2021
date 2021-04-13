from matchers import All, And, HasAtLeast, HasFewerThan, Or, PlaysIn

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher_obj = matcher
    
    def playsIn(self, team):
        return QueryBuilder(And(self._matcher_obj, PlaysIn(team)))

    def hasAtLeast(self, points, attribute):
        return QueryBuilder(And(self._matcher_obj, HasAtLeast(points, attribute)))
    
    def hasFewerThan(self, points, attribute):
        return QueryBuilder(And(self._matcher_obj, HasFewerThan(points, attribute)))
    
    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))

    def build(self):
        return self._matcher_obj