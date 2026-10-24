# Set Practice 2 — Comparing two groups
# Start with:
team_a = {"Sam", "Alex", "John", "Sara"}
team_b = {"Alex", "Sara", "Mike", "David"}

# Answer these questions in code:
# 1. Who is in either team?
#    Use the union operator: |

print(team_a | team_b)
#this union operator unites two dataset.

# 2. Who appears in both teams?
#    Use the intersection operator: &

print(team_a & team_b)
#this ensures us the common variables exists on both datasets.

# 3. Who is only in team_a?
#    Use the difference operator: -

print(team_a-team_b)
#this only gives us the values that only exists in team a.

# 4. Who is only in team_b?
#    Use the difference operator: -

print(team_b - team_a)
#does the same as the last one.

# 5. Who appears in exactly one of the two teams?
#    Use the symmetric difference operator: ^

print(team_a ^ team_b)


# Then explain the difference between:
# team_a - team_b
# and:
# team_a ^ team_b

# in the first part of doing a-b will give us the values only exists in a, like uncommon values. and a^b gives us the both sides unique values..



