# Task:
# Your component is to be used for calculating the scores of programming contest teams and determining a winner. You will be given the results from several teams and must determine the winner.

# Scoring:
# There are two components to a team's score. The first is the number of problems solved. The second is penalty points, which reflects the amount of time and incorrect submissions made before the problem is solved. For each problem solved correctly, penalty points are charged equal to the time at which the problem was solved plus 20 minutes for each incorrect submission. No penalty points are added for problems that are never solved.
# So if a team solved problem one on their second submission at twenty minutes, they are charged 40 penalty points. If they submit problem 2 three times, but do not solve it, they are charged no penalty points. If they submit problem 3 once and solve it at 120 minutes, they are charged 120 penalty points. Their total score is two problems solved with 160 penalty points.
# The winner is the team that solves the most problems. If teams tie for solving the most problems, then the winner is the team with the fewest penalty points.


# Input:
# For the programming contest your program is judging, there are four problems. You are guaranteed that the input will not result in a tie between teams after counting penalty points.
# Line 1 <nTeams>
# Line 2-n+1 <Name> <p1Sub> <p1Time> <p2Sub> <p2Time> ... <p4Time>
# The first element on the line is the team name, which contains no whitespace. Following that, for each of the four problems, is the number of times the team submitted a run for that problem and the time at which it was solved correctly (both integers). If a team did not solve a problem, the time will be zero. The number of submissions will be at least one if the problem was solved.

# Output:
# The output consists of a single line listing the name of the team that won, the number of problems they solved, and their penalty points.

