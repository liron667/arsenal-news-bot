"""Minimal check for the relevance filter. Run: python test_matcher.py"""
from bot import matches

KW = ["ארסנל", "Arsenal", "התותחנים"]
EX = []

assert matches("ארסנל ניצחה 2-0 בליגה האנגלית", KW, EX)
assert matches("Arsenal sign a new midfielder", KW, EX)
assert matches("התותחנים ממשיכים להוביל את הטבלה", KW, EX)
assert not matches("ליברפול ניצחה את מנצ'סטר סיטי", KW, EX)   # no keyword
print("ok")
