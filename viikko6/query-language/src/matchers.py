from pprint import pprint

class All:
    def matches(player):
        return True

class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class Not:
    def __init__(self, class_object):
        self._class_object = class_object

    def matches(self, player):
        value = self._class_object.matches(player)
        return not value

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)
        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value
