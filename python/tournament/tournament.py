from collections import defaultdict

def tally(rows):
    results = [line.split(';') for line in rows]

    matches = defaultdict(list)

    for row in results:
        if row[2] == 'win':
            matches[row[0]].append(3)
            matches[row[1]].append(0)
        elif row[2] == 'loss':
            matches[row[0]].append(0)
            matches[row[1]].append(3)
        else:
            matches[row[0]].append(1)
            matches[row[1]].append(1)

    points = defaultdict(list)
    for club in matches:
        club_points = sum(matches[club])
        points[club_points].append(club)

    table = list()
    table.append("Team                           | MP |  W |  D |  L |  P")
    for point in sorted(points.items(), reverse=True):
        print(point)
        for club in sorted(point[1]):
            table.append(f"{club.ljust(31)}"
                         f"|{str(len(matches[club])).rjust(3)} |"
                         f"{str(matches[club].count(3)).rjust(3)} |"
                         f"{str(matches[club].count(1)).rjust(3)} |"
                         f"{str(matches[club].count(0)).rjust(3)} |"
                         f"{str(sum(matches[club])).rjust(3)}")

    return table

