from project import load_questions, ask_question

def test_load_questions():
    questions = load_questions()
    
    # Check it's a list
    assert isinstance(questions, list)
    
    # Check it has items
    assert len(questions) > 0
    
    # Check structure of first question
    q = questions[0]
    assert "question" in q
    assert "options" in q
    assert "answer" in q
    
    # Check options format
    assert isinstance(q["options"], list)
    assert len(q["options"]) == 4


def test_correct_answer(monkeypatch):
    question = {
        "question": "Test?",
        "options": ["A. One", "B. Two", "C. Three", "D. Four"],
        "answer": "A"
    }

    # Simulate user input "A"
    monkeypatch.setattr("builtins.input", lambda _: "A")
    
    assert ask_question(question) == True


def test_wrong_answer(monkeypatch):
    question = {
        "question": "Test?",
        "options": ["A. One", "B. Two", "C. Three", "D. Four"],
        "answer": "A"
    }

    # Simulate user input "B"
    monkeypatch.setattr("builtins.input", lambda _: "B")
    
    assert ask_question(question) == False


def test_invalid_then_valid_input(monkeypatch):
    question = {
        "question": "Test?",
        "options": ["A. One", "B. Two", "C. Three", "D. Four"],
        "answer": "A"
    }

    inputs = iter(["X", "A"])  # first invalid, then correct
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    assert ask_question(question) == True