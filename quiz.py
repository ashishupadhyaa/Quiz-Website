from flask import Flask, render_template, request, redirect, url_for, jsonify
from file import paper_read, match_ans  # Using functions defined in the 'file.py'

app = Flask(__name__)

with app.app_context():
	content = paper_read('paper.txt')  # read the queston paper and store it in 'content variable'

# Page for Person's information like 'Name', 'email' and time for quiz
@app.route("/", methods=['POST', 'GET'])
def detail():
	if request.method == "POST":
		t = request.form['host']  # to get time from dropdown box in the form
		name = request.form['name']  # to get the name of the person from form
		num = t.split(" ")  # to get only digit from 't' variable
		return redirect(url_for('quiz_page', num=int(num[0]) * 60, lengt=len(content), len1=len(content[0]['options']), name=name))  # it will direct to the question page when submitted
	else:
		return render_template("p_detail.html")  # it will direct to the person's detail form page

# Page for giving question to the candidate(person)
@app.route("/quiz_page/<int:num>/<int:lengt>/<int:len1>/<name>", methods=['POST', 'GET'])
def quiz_page(num, lengt, len1, name):
	if request.method == "POST":
		dans = []  # to store the answers given by the candidate
		for x in range(1, 11):
			dans.append(request.form['question' + str(x)])
		with app.app_context():
			score = match_ans(dans)  # to get score of the candidate
		return redirect(url_for("score_card", name=name, score=score))  # it will direct to the page where candidate's name and score will be shown
	else:
		return render_template('quiz_tem.html', num=int(num), lengt=int(lengt), len1=int(len1), data=content)  # it will direct to the page where candidate can take quiz

# Page for showing candidate's name and score
@app.route("/score_card/<score>/<name>")
def score_card(name, score):
	return render_template("score.html", name=name, score=score) 


if __name__ == "__main__":
	app.run(debug=True)
