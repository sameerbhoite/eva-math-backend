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


@app.get("/")
def home():
    return {"message": "Eva Math Algebra 1 Backend is running. Use /api/generate-weekly-quiz to get a quiz."}


# Optional: Local testing block
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("eva_math_backend:app", host="0.0.0.0", port=8000, reload=True)
