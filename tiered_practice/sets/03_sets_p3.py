# Set Practice 3 — Job skillsb
# Start with:
required_skills = {"Python", "SQL", "Pandas"}
candidate_skills = {"Python", "SQL", "Pandas", "NumPy", "Excel"}

# Ask and answer these questions in code:
# 1. Does the candidate have every required skill?
#    Use the issubset() method.

print(required_skills.issubset(candidate_skills))

# 2. Does the required set contain all of the candidate skills?
#    Use the issuperset() method.
print(candidate_skills.issuperset(required_skills))
# 3. What happens when we compare a different candidate?
#    Create:
candidate2_skills = {"Python", "SQL"}
print(candidate2_skills.issuperset(required_skills))
#
#    Then check whether candidate 2 has all the required skills.
#
# Print each result and explain what the difference between issubset() and issuperset() means.