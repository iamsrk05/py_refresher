# Set Practice 1 — Basic methods
# Start with:
# skills = {"Python", "SQL", "Excel"}

# Do these:
# 1. Add "Pandas" using .add()
# 2. Add "NumPy" and "Power BI" together using .update()
# 3. Remove "Excel" using .remove()
# 4. Try removing "Java" using .discard()
# 5. Print the final set
# Then explain: Why does .discard("Java") not crash even though "Java" is missing?

skills = {"Python", "SQL", "Excel"}

skills.add("Pandas")
skills.update({
    "NumPy", "Power BI"
})

skills.remove("Excel")
skills.discard("Java")

print(skills)