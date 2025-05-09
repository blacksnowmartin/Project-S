import random

def sissy_test():
    questions = [
        {
            "question": "1. Do you enjoy wearing feminine clothing?",
            "choices": ["A) Yes", "B) Sometimes", "C) Rarely", "D) No"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "2. How do you feel about makeup?",
            "choices": ["A) Love it", "B) Like it", "C) Indifferent", "D) Dislike it"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "3. Do you prefer high heels over sneakers?",
            "choices": ["A) Absolutely", "B) Occasionally", "C) Not really", "D) Never"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "4. How often do you watch romantic comedies?",
            "choices": ["A) All the time", "B) Sometimes", "C) Rarely", "D) Never"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "5. Do you enjoy shopping for clothes?",
            "choices": ["A) Very much", "B) A little", "C) Not much", "D) Not at all"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "6. How do you feel about nail polish?",
            "choices": ["A) Love it", "B) Like it", "C) Indifferent", "D) Dislike it"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "7. Do you prefer to hang out with girls?",
            "choices": ["A) Always", "B) Sometimes", "C) Rarely", "D) Never"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "8. How do you feel about your body image?",
            "choices": ["A) Very positive", "B) Somewhat positive", "C) Neutral", "D) Negative"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "9. Do you enjoy discussing emotions?",
            "choices": ["A) Very much", "B) A little", "C) Not much", "D) Not at all"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "10. How do you feel about being pampered?",
            "choices": ["A) Love it", "B) Like it", "C) Indifferent", "D) Dislike it"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "11. Do you enjoy cooking or baking?",
            "choices": ["A) Very much", "B) A little", "C) Not much", "D) Not at all"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "12. How do you feel about romantic gestures?",
            "choices": ["A) Love them", "B) Like them", "C) Indifferent", "D) Dislike them"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "13. Do you enjoy attending social gatherings?",
            "choices": ["A) Very much", "B) A little", "C) Not much", "D) Not at all"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "14. How do you feel about your fashion sense?",
            "choices": ["A) Very confident", "B) Somewhat confident", "C) Neutral", "D) Not confident"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "15. Do you enjoy reading romance novels?",
            "choices": ["A) Love them", "B) Like them", "C) Indifferent", "D) Dislike them"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "16. How do you feel about your social skills?",
            "choices": ["A) Very good", "B) Good", "C) Average", "D) Poor"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "17. Do you enjoy watching fashion shows?",
            "choices": ["A) Very much", "B) A little", "C) Not much", "D) Not at all"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "18. How do you feel about your ability to express feelings?",
            "choices": ["A) Very good", "B) Good", "C) Average", "D) Poor"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "19. Do you enjoy trying new hairstyles?",
            "choices": ["A) Very much", "B) A little", "C) Not much", "D) Not at all"],
            "points": [4, 3, 2, 1]
        },
        {
            "question": "20. How do you feel about your overall femininity?",
            "choices": ["A) Very feminine", "B) Somewhat feminine", "C) Neutral", "D) Not feminine"],
            "points": [4, 3, 2, 1]
        }
    ]

    total_score = 0

    for question in questions:
        print(question["question"])
        for choice in question["choices"]:
            print(choice)
        answer = input("Select A, B, C, or D: ").strip().upper()
        index = ord(answer) - ord('A')
        total_score += question["points"][index]

    print(f"Your total score is: {total_score}")
    
    if total_score >= 70:
        print("Remark: Highly feminine.")
    elif total_score >= 50:
        print("Remark: Moderately feminine.")
    elif total_score >= 30:
        print("Remark: Slightly feminine.")
    else:
        print("Remark: Not feminine.")
        
sissy_test()
