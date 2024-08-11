from flask import Flask , render_template , request , redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'super secret key' 

quizzes = {
    "Artificial Intelligence" : [
        {"question" : "The intelligence displayed by humans and other animals is termed?", "options": ["constance" , "ability" , "natural intelligence" , "cognition" ], "answer": "natural intelligence"},

        {"question" : "which of the following following architecture is also known as systolic arrays?" , "options": ["MISD" , "SISD" , "SIMD" , "None"], "answer": "MISD"},

         {"question" : "What does AI stand for?" , "options": ["artificial indentation" , "advance intelligence" , "automated interaction" , "artificial intelligence"], "answer": "artificial intelligence"},

          {"question" : "Which field is closely related to AI?" , "options": ["Astrology" , "Biology" , "Chemistry" , "Computer Science"], "answer": "Computer Science"},

           {"question" : "What is the primary goal of AI?" , "options": ["acquiring insects" , "achieving illusion" , "analyzing individuals" , "autonomous intelligence"], "answer": "autonomous intelligence"},
    ],
    "Python Programming" : [
        {"question" : f"What is a correct syntax to output {{Hello World}} in Python?", "options": ["echo('hello world')" , "Print('hello world')" , "p('hello world')" , "echo hello world"] , "answer":"Print('hello world')"},

        {"question": "which symbol is used for COMMENTS in Python code?", "options": ["#" , "//" , "/* */" , "all of the above"], "answer": "#"},

        {"question": "Which one is NOT a legal variable name?" , "options": ["my_var" , "Myvar" , "_myvar" , "my-var"], "answer": "Myvar"},

        {"question": "How do you create a variable with the numeric value 5?" , "options":["x=5" , "x=int(5)" , "5" , "all of the above"], "answer": "x=5"}, 

        {"question": "What is the correct file extension for Python files?" , "options": [".pt" , ".py" , ".pyt" , ".pyth"], "answer": ".py"}
    ],
    "Mathematics" : [
        {"question" : "121 is divided 11 ", "options": ["11" , "10" , "19" , "18"] , "answer":"11"},

        {"question": "60 times of 8 equals to", "options": ["480" , "300" , "250" , "400"], "answer": "480"},

        {"question": "What is the Next Prime Number after 7 ?" , "options": ["13" , "12" , "14" , "11"], "answer": "11"},

        {"question": "The Product of 131 * 0 * 300 * 4" , "options":["11" , "0" , "46" , "45"], "answer": "0"}, 

        {"question": "What is 6 percentage equals to" , "options": ["0.06" , "0.6" , "0.006" , "0.00006"], "answer": "0.06"}
    ]
}

@app.route('/')
def home():
    return render_template('index.html' , quizzes=quizzes.keys())

@app.route('/quiz/<topic>' , methods = ['GET' , 'POST'])
def quiz(topic):
    if request.method == 'POST':
        score = 0
        questions = quizzes[topic]
        for question in questions:
            useranswer = request.form.get(question['question'], '').strip().lower()
            correctanswer = question['answer'].strip().lower()
            if useranswer == correctanswer:
                score += 1
        session['score'] = score  # Store the score in the session
        session['total'] = len(quizzes[topic])  # Store the total in the session
        return redirect(url_for('results'))
    
    return render_template('quiz.html' ,topic = topic,  questions = quizzes[topic])

@app.route('/results')
def results():
    score = session.get('score', 0)  # Get the score from the session, default to 0
    total = session.get('total', 0)  # Get the total from the session, default to 0
    
    print(f"Score: {score}, Total: {total}")
    return render_template('results.html', score=score, total=total)

@app.route("/templates/about.html")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)