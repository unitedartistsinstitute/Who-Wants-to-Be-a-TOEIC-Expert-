<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Who Wants to Be a TOEIC Expert?</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://upload.wikimedia.org/wikipedia/en/8/8d/WWTBAM_Logo.png');
            background-size: cover;
            background-position: center;
            color: #fff;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.8);
            border-radius: 10px;
        }
        .question {
            font-size: 24px;
            margin-bottom: 20px;
            padding: 15px;
            background-color: rgba(70, 130, 180, 0.6);
            border-radius: 5px;
        }
        .answers {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        .answer {
            padding: 15px;
            border: 2px solid #fff;
            border-radius: 5px;
            cursor: pointer;
            background-color: rgba(70, 130, 180, 0.4);
            transition: background-color 0.3s;
        }
        .answer:hover {
            background-color: rgba(70, 130, 180, 0.6);
        }
        .answer.correct {
            background-color: rgba(0, 255, 0, 0.6);
        }
        .answer.wrong {
            background-color: rgba(255, 0, 0, 0.6);
        }
        .lifeline {
            margin-top: 20px;
            margin-right: 10px;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .lifeline:disabled {
            background-color: #666;
            cursor: not-allowed;
        }
        .next-button, .reset-button {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .next-button {
            display: none;
        }
        .reset-button {
            background-color: #dc3545;
            margin-left: 10px;
        }
        .score {
            font-size: 20px;
            margin: 15px 0;
            color: #ffd700;
        }
        .signature {
            margin-top: 30px;
            font-size: 14px;
            color: #ccc;
        }
        .signature a {
            color: #007bff;
            text-decoration: none;
        }
        .signature a:hover {
            text-decoration: underline;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Who Wants to Be a TOEIC Expert?</h1>
        <div class="score" id="score">Current Prize: $0</div>
        <div class="question" id="question"></div>
        <div class="answers">
            <div class="answer" id="answer1" onclick="checkAnswer(0)"></div>
            <div class="answer" id="answer2" onclick="checkAnswer(1)"></div>
            <div class="answer" id="answer3" onclick="checkAnswer(2)"></div>
            <div class="answer" id="answer4" onclick="checkAnswer(3)"></div>
        </div>
        <div>
            <button class="lifeline" id="lifeline5050" onclick="useLifeline('5050')">50:50</button>
            <button class="lifeline" id="lifelineAudience" onclick="useLifeline('audience')">Ask the Audience</button>
            <button class="lifeline" id="lifelinePhone" onclick="useLifeline('phone')">Phone a Friend</button>
        </div>
        <div class="button-container">
            <button class="next-button" id="nextButton" onclick="nextQuestion()">Next Question</button>
            <button class="reset-button" id="resetButton" onclick="resetGame()">Reset Game</button>
        </div>
        
        <div class="signature">
            &copy; 2025 Daniel Rojas :: TΣʃ ::  &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
        </div>
    </div>

    <script>
        const questions = [
            {
                question: "What is the primary focus of the TOEIC exam?",
                answers: [
                    "Academic English",
                    "Workplace and business English",
                    "Conversational English",
                    "Technical English"
                ],
                correct: 1,
                money: 100
            },
            {
                question: "What is the total possible TOEIC score range?",
                answers: [
                    "0-120",
                    "0-990",
                    "10-900",
                    "10-990"
                ],
                correct: 3,
                money: 200
            },
            {
                question: "How many main sections does the standard TOEIC Listening and Reading test have?",
                answers: [
                    "1 section",
                    "2 sections",
                    "3 sections",
                    "4 sections"
                ],
                correct: 1,
                money: 300
            },
            {
                question: "How many total questions are there in the TOEIC Listening and Reading test?",
                answers: [
                    "100 questions",
                    "150 questions",
                    "200 questions",
                    "250 questions"
                ],
                correct: 2,
                money: 500
            },
            {
                question: "How long are TOEIC scores valid?",
                answers: [
                    "1 year",
                    "2 years",
                    "3 years",
                    "5 years"
                ],
                correct: 1,
                money: 1000
            },
            {
                question: "What is the approximate duration of the TOEIC Listening and Reading test?",
                answers: [
                    "1 hour",
                    "2 hours",
                    "3 hours",
                    "4 hours"
                ],
                correct: 1,
                money: 2000
            },
            {
                question: "Which of these is NOT a part of the standard TOEIC Listening and Reading test?",
                answers: [
                    "Photograph descriptions",
                    "Essay writing",
                    "Reading comprehension",
                    "Conversations"
                ],
                correct: 1,
                money: 4000
            },
            {
                question: "How many tasks are there in the TOEIC Speaking test?",
                answers: [
                    "4 tasks",
                    "6 tasks",
                    "8 tasks",
                    "10 tasks"
                ],
                correct: 2,
                money: 8000
            },
            {
                question: "Which organization administers the TOEIC test?",
                answers: [
                    "Cambridge Assessment English",
                    "University of Michigan",
                    "Educational Testing Service (ETS)",
                    "MIT"
                ],
                correct: 2,
                money: 16000
            },
            {
                question: "How many tasks are there in the TOEIC Writing test?",
                answers: [
                    "1 task",
                    "2 tasks",
                    "3 tasks",
                    "4 tasks"
                ],
                correct: 1,
                money: 32000
            },
            {
                question: "Which of these contexts is MOST commonly found in TOEIC test materials?",
                answers: [
                    "Academic lectures",
                    "Business meetings and workplace scenarios",
                    "Medical consultations",
                    "Scientific research"
                ],
                correct: 1,
                money: 64000
            },
            {
                question: "How many questions are there in the TOEIC Listening section?",
                answers: [
                    "50 questions",
                    "75 questions",
                    "100 questions",
                    "120 questions"
                ],
                correct: 2,
                money: 125000
            },
            {
                question: "In which part of the TOEIC Listening test would you hear short conversations between two speakers?",
                answers: [
                    "Photographs",
                    "Question-Response",
                    "Short Conversations",
                    "Small Talk"
                ],
                correct: 2,
                money: 250000
            },
            {
                question: "What is unique about the TOEIC Speaking and Writing tests compared to the Listening and Reading test?",
                answers: [
                    "They are scored on a different scale",
                    "They are offered as separate, optional tests",
                    "They are only available online",
                    "They are only available in certain countries"
                ],
                correct: 1,
                money: 500000
            },
            {
                question: "What type of questions predominate in the TOEIC test?",
                answers: [
                    "Open-ended questions",
                    "Fill-in-the-blank",
                    "Multiple choice",
                    "True/False"
                ],
                correct: 2,
                money: 1000000
            },
            {
                question: "Which of these skills is NOT directly tested in either the TOEIC Listening & Reading or Speaking & Writing tests?",
                answers: [
                    "Translation",
                    "Comprehension",
                    "Composition",
                    "Pronunciation"
                ],
                correct: 0,
                money: 2500000
            },
            {
                question: "What kind of English accent is primarily used in the TOEIC Listening section?",
                answers: [
                    "Only American English",
                    "Only British English",
                    "A variety of accents including American, British, Canadian, and Australian",
                    "Regional dialects"
                ],
                correct: 2,
                money: 5000000
            },
            {
                question: "What is a typical TOEIC score considered sufficient for international business communication?",
                answers: [
                    "Above 450",
                    "Above 600",
                    "Above 750",
                    "Above 900"
                ],
                correct: 1,
                money: 7500000
            },
            {
                question: "Which section of the TOEIC Reading test focuses on grammatical accuracy?",
                answers: [
                    "Incomplete Sentences",
                    "Text Completion",
                    "Single Passages",
                    "Multiple Passages"
                ],
                correct: 0,
                money: 10000000
            },
            {
                question: "What distinguishes the TOEIC test from other English language tests like TOEFL?",
                answers: [
                    "TOEIC is more difficult",
                    "TOEIC focuses on workplace English rather than academic English",
                    "TOEIC is cheaper",
                    "TOEIC is only available in Asian countries"
                ],
                correct: 1,
                money: 50000000
            }
        ];

        let currentQuestion = 0;
        let lifelinesUsed = { '5050': false, 'audience': false, 'phone': false };
        let currentMoney = 0;

        function loadQuestion() {
            const question = questions[currentQuestion];
            document.getElementById('question').textContent = question.question;
            
            const answers = document.querySelectorAll('.answer');
            answers.forEach((answer, index) => {
                answer.textContent = question.answers[index];
                answer.classList.remove('correct', 'wrong');
                answer.style.visibility = 'visible';
            });
            
            document.getElementById('nextButton').style.display = 'none';
            document.getElementById('score').textContent = `Current Prize: $${currentMoney}`;
        }

        function checkAnswer(selected) {
            const correct = questions[currentQuestion].correct;
            const answers = document.querySelectorAll('.answer');
            
            answers[selected].classList.add(selected === correct ? 'correct' : 'wrong');
            if (selected === correct) {
                currentMoney = questions[currentQuestion].money;
                document.getElementById('score').textContent = `Current Prize: $${currentMoney}`;
            } else {
                currentMoney = 0;
                document.getElementById('score').textContent = `Game Over! Final Prize: $0`;
                endGame();
            }
            
            document.getElementById('nextButton').style.display = 'block';
        }

        function useLifeline(lifeline) {
            const question = questions[currentQuestion];
            const correct = question.correct;
            const answers = document.querySelectorAll('.answer');

            if (lifeline === '5050' && !lifelinesUsed['5050']) {
                lifelinesUsed['5050'] = true;
                const incorrectAnswers = [0, 1, 2, 3].filter(i => i !== correct);
                incorrectAnswers.slice(0, 2).forEach(index => {
                    answers[index].style.visibility = 'hidden';
                });
                document.getElementById('lifeline5050').disabled = true;
            } else if (lifeline === 'audience' && !lifelinesUsed['audience']) {
                lifelinesUsed['audience'] = true;
                alert(`The audience suggests answer ${String.fromCharCode(65 + correct)}!`);
                document.getElementById('lifelineAudience').disabled = true;
            } else if (lifeline === 'phone' && !lifelinesUsed['phone']) {
                lifelinesUsed['phone'] = true;
                alert(`Your TOEIC expert friend suggests answer ${String.fromCharCode(65 + correct)}!`);
                document.getElementById('lifelinePhone').disabled = true;
            }
        }

        function nextQuestion() {
            currentQuestion++;
            if (currentQuestion < questions.length) {
                loadQuestion();
            } else {
                endGame();
            }
        }

       function resetGame() {
    currentQuestion = 0;
    currentMoney = 0;
    lifelinesUsed = { '5050': false, 'audience': false, 'phone': false };
    
    const container = document.querySelector('.container');
    container.innerHTML = `
        <h1>Who Wants to Be a TOEIC Expert?</h1>
        <div class="score" id="score">Current Prize: $0</div>
        <div class="question" id="question"></div>
        <div class="answers">
            <div class="answer" id="answer1" onclick="checkAnswer(0)"></div>
            <div class="answer" id="answer2" onclick="checkAnswer(1)"></div>
            <div class="answer" id="answer3" onclick="checkAnswer(2)"></div>
            <div class="answer" id="answer4" onclick="checkAnswer(3)"></div>
        </div>
        <div>
            <button class="lifeline" id="lifeline5050" onclick="useLifeline('5050')">50:50</button>
            <button class="lifeline" id="lifelineAudience" onclick="useLifeline('audience')">Ask the Audience</button>
            <button class="lifeline" id="lifelinePhone" onclick="useLifeline('phone')">Phone a Friend</button>
        </div>
        <div class="button-container">
            <button class="next-button" id="nextButton" onclick="nextQuestion()">Next Question</button>
            <button class="reset-button" id="resetButton" onclick="resetGame()">Reset Game</button>
        </div>
        
        <div class="signature">
            &copy; 2025 Daniel Rojas :: TΣʃ ::  &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
        </div>
    `;
    
    // Re-enable lifelines
    document.getElementById('lifeline5050').disabled = false;
    document.getElementById('lifelineAudience').disabled = false;
    document.getElementById('lifelinePhone').disabled = false;
    
    loadQuestion();
}
        function endGame() {
            const container = document.querySelector('.container');
            container.innerHTML = `
                <h1>Game Over!</h1>
                <div class="score">Final Prize: $${currentMoney}</div>
                <p>Congratulations on completing the TOEIC Millionaire Challenge!</p>
                <button class="reset-button" id="resetButton" onclick="resetGame()">Play Again</button>
                <div class="signature">
                    &copy; 2025 Daniel Rojas :: TΣʃ :: &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
                </div>
            `;
        }

        window.onload = loadQuestion;
    </script>
</body>
</html>
