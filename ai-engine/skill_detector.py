skills_db = [
    "python",
    "machine learning",
    "deep learning",
    "sql",
    "tensorflow",
    "pytorch",
    "data analysis",
    "numpy",
    "pandas",
    "scikit-learn",
    "java",
    "c++",
    "javascript",
    "react",
    "node.js"
]


def detect_skills(text):
    
    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))