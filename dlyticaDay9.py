# Name: Samir Khatiwada
# Assignment 1 — Student Grade Analyser
# Date: 08 June 2026

def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError(f"Invalid score: {score}. Score must be between 0 and 100.")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def analyse(students):
    results = {}
    
    for name, score in students.items():
        results[name] = {
            "score": score,
            "grade": letter_grade(score)
        }
    
    return results

def summary(results):
    total = sum(info["score"] for info in results.values())
    average = total / len(results)
    highest = max(results, key=lambda k: results[k]["score"])
    lowest = min(results, key=lambda k: results[k]["score"])
    
    counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for info in results.values():
        grade = info["grade"]
        counts[grade] = counts.get(grade, 0) + 1
    
    print("\nClass Summary")
    print("-" * 40)
    print(f"Class Average : {average:.2f}")
    print(f"Highest Score : {highest} ({results[highest]['score']})")
    print(f"Lowest Score  : {lowest} ({results[lowest]['score']})")
    print(
        f"Grade Counts  : "
        f"A={counts['A']}  "
        f"B={counts['B']}  "
        f"C={counts['C']}  "
        f"D={counts['D']}  "
        f"F={counts['F']}"
    )

try:
    students = {
        "Alice": int(input("Enter score for Alice: ")),
        "Bob": int(input("Enter score for Bob: ")),
        "Carol": int(input("Enter score for Carol: ")),
        "Dave": int(input("Enter score for Dave: ")),
        "Eve": int(input("Enter score for Eve: ")),
        "Frank": int(input("Enter score for Frank: "))
    }

    results = analyse(students)

    print("Student Results")
    print("-" * 40)

    for name in sorted(results):
        score = results[name]["score"]
        grade = results[name]["grade"]
        print(f"{name:<8}: {score} → {grade}")

    summary(results)

except ValueError as e:
    print(f"Error: {e}")