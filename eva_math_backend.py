from fastapi import FastAPI
import random

app = FastAPI()


def generate_linear_equation(difficulty):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    if difficulty == 'easy':
        question = f"{a} + {b}"
        answer = a + b
    elif difficulty == 'medium':
        a *= 2
        b *= 3
        question = f"{a} - {b}"
        answer = a - b
    else:  # hard
        a *= random.randint(2, 5)
        b *= random.randint(2, 5)
        question = f"{a} * {b}"
        answer = a * b

    return {"question": question, "answer": round(answer, 2), "difficulty": difficulty}


@app.get("/api/generate-weekly-quiz")
def generate_weekly_quiz():
    quiz = []
    difficulties = ['easy'] * 10 + ['medium'] * 10 + ['hard'] * 5
    random.shuffle(difficulties)

    for diff in difficulties:
        quiz.append(generate_linear_equation(diff))

    return {"quiz": quiz}


# Test block — useful if running locally, ignored in deployment
if __name__ == "__main__":
    print("Running test cases for generate_linear_equation:")
    for level in ['easy', 'medium', 'hard']:
        sample = generate_linear_equation(level)
        print(f"Difficulty: {level}", sample)

    print("\nRunning test case for generate_weekly_quiz:")
    sample_quiz = generate_weekly_quiz()
    print(f"Total questions generated: {len(sample_quiz['quiz'])}")
    assert len(sample_quiz['quiz']) == 25, "Quiz should contain exactly 25 questions."