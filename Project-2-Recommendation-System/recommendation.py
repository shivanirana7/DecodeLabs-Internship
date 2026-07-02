scourses = [
    {
        "name": "Python for Beginners",
        "tags": ["Python", "Programming"]
    },
    {
        "name": "Web Development",
        "tags": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "Machine Learning Fundamentals",
        "tags": ["Python", "AI", "Machine Learning"]
    },
    {
        "name": "Artificial Intelligence Basics",
        "tags": ["AI", "Python"]
    },
    {
        "name": "Data Science Essentials",
        "tags": ["Python", "Data Science"]
    }
]
user_interests = input(
    "Enter your interests (comma separated): "
).split(",")
user_interests = [
    interest.strip()
    for interest in user_interests
]
recommendations = []
for course in courses:
    score = 0
    for tag in course["tags"]:
        if tag in user_interests:
            score += 1
    recommendations.append(
        (course["name"], score)
    )
recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)
print("\nRecommended Courses:\n")
for course, score in recommendations:
    if score > 0:
        print(f"{course} (Match Score: {score})")
