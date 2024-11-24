from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
import random

app = FastAPI()

# CORS ミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 必要に応じて特定のオリジンを許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ダミーデータ（テストデータ）
questions = [
    {"id": 1, "category": "Tech Quiz", "question_text": "T1_questiontext", "options": ["opT11", "opT12", "opT13", "opT14"]},
    {"id": 1, "category": "Tech Quiz", "question_text": "T2_questiontext", "options": ["opT21", "opT22", "opT23", "opT24"]},
    {"id": 1, "category": "Tech Quiz", "question_text": "T3_questiontext", "options": ["opT31", "opT32", "opT33", "opT34"]},
    {"id": 2, "category": "Biz Basics", "question_text": "B1_questiontext", "options": ["opB11", "opB12", "opB13", "opB14"]},
    {"id": 2, "category": "Biz Basics", "question_text": "B2_questiontext", "options": ["opB21", "opB22", "opB23", "opB24"]},
    {"id": 2, "category": "Biz Basics", "question_text": "B3_questiontext", "options": ["opB31", "opB32", "opB33", "opB34"]},
    {"id": 3, "category": "Design Thinking", "question_text": "D1_questiontext", "options": ["opD11", "opD12", "opD13", "opD14"]},
    {"id": 3, "category": "Design Thinking", "question_text": "D2_questiontext", "options": ["opD21", "opD22", "opD23", "opD24"]},
    {"id": 3, "category": "Design Thinking", "question_text": "D3_questiontext", "options": ["opD31", "opD32", "opD33", "opD34"]},
]

# 今日のテストを取得
@app.get("/get_today_test")
def get_today_test():
    today = date.today().isoformat()
    tests = [
        {"id": 1, "title": "Tech Quiz", "date": "2024-11-24"},
        {"id": 2, "title": "Biz Basics", "date": "2024-11-25"},
        {"id": 3, "title": "Design Thinking", "date": "2024-11-26"},
    ]
    for test in tests:
        if test["date"] == today:
            return test
    return None

# ランダムに3問の問題を取得
@app.get("/get_questions/{category}")
def get_questions(category: str):
    filtered_questions = [q for q in questions if q["category"] == category]
    if not filtered_questions:
        return {"error": "No questions found for this category."}
    return random.sample(filtered_questions, 3)
