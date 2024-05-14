# Dokumentacja Python: https://docs.python.org/3.12/library/re.html?highlight=re#module-re
# Opis znaczników wyrażeń regularnych na stronie https://regex101.com/
# Można wygenerować taki kod ze strony  https://regex101.com/ dla jezyka Python

import re

# Sprawdzić działanie programu na każdym z wzorców
# regex = r"(\d{2})-(\d{3})"
regex = r"(\d{2}-\d{3})"
# regex = r"\d{2}-\d{3}"

test_str = "65-453 63-334 44-567"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print("Match {matchNum} was found at {start}-{end}: {match}".
          format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print("Group {groupNum} found at {start}-{end}: {group}".
              format(groupNum=groupNum, start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))
