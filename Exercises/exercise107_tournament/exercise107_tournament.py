"""Tournament exercise"""

from re import match

def tally(rows):
    """Given a list of match results, tallies the matches played (MP), wins (W), draws (D),
    losses (L) and points (P) of each team, returning them as a formatted table.
 
    :param list[str] rows: The matches.
    :raises ValueError: Raised when there's no input.
    :raises TypeError: Raised when the input is not a list.
    :raises TypeError: Raised when there are matches that are not strings.
    :raises ValueError: Raised when the match input is malformed.
    :return list[str]: The processed tally.
    """

    if rows is None:
        raise ValueError("No input.")
    if not isinstance(rows, list):
        raise TypeError("Input must be a list.")

    results = {}
    for row in rows:
        if not isinstance(row, str):
            raise TypeError("Matches must be strings")
        if not match(r"([\w -]+;){2}(win|draw|loss)", row):
            raise ValueError("Malformed match input.")
        team_1, team_2, result = row.split(";")
        for team in [team_1, team_2]:
            if team not in results:
                results[team] = {'matches_played': 0,
                                 'wins':           0,
                                 'draws':          0,
                                 'losses':         0,
                                 'points':         0}
        results[team_1]['matches_played'] += 1
        results[team_2]['matches_played'] += 1
        if result == "win":
            results[team_1]['wins']   += 1
            results[team_1]['points'] += 3
            results[team_2]['losses'] += 1
        elif result == "loss":
            results[team_1]['losses'] += 1
            results[team_2]['wins']   += 1
            results[team_2]['points'] += 3
        else:
            results[team_1]['draws']  += 1
            results[team_1]['points'] += 1
            results[team_2]['draws']  += 1
            results[team_2]['points'] += 1
    results = dict(sorted(
                    sorted(results.items()),
                    key=lambda item: item[1]['points'], reverse=True))
    header = f"{'Team':<30} | {'MP':>2} | {'W':>2} | {'D':>2} | {'L':>2} | {'P':>2}"
    results_table = [header]
    for result in results.items():
        results_table.append(f"{result[0]:<30} | {result[1]['matches_played']:>2} | " +
                             f"{result[1]['wins']:>2} | {result[1]['draws']:>2} | " +
                             f"{result[1]['losses']:>2} | {result[1]['points']:>2}")
    return results_table
