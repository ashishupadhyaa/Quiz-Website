# Function to read the question paper
def paper_read(f_name):
	list1 = []  # for storing the neccesary data to show the question on the quiz page in website
	dict2 = {}  # to storing each question and related data (options and ids) individual
	qu = []  # to read the question paper and store the content of question paper
	k = 0  # for ids
	with open(f_name, "r") as f:
		content = f.read()
		data = content.strip().split("\n")  # creating the list of the content present in questioin paper

		for i in range(len(data)):
			if data[i] != "":
				qu.append(data[i])  # content of 'data' without blank line present in it
		
		i = 0
		qu.append('Question')  # to iterate easily

		for line in qu:
			if line[0:8] == 'Question':  # to check the start of the question
				list1.append(dict2)
				dict2 = {}
				op = []  # to store the options of the question
				ids = []  # to store the ids of the options so that radio buttons can be easily made
				i += 1
				j = 0
				dict2['question_no'] = i
				dict2['options'] = op
				dict2['question'] = line[9:]
				dict2['ids'] = ids
			else:  # to check the options of the question
				j += 1
				k += 1
				op.append(line)
				ids.append(k)

	return list1[1:]

# Function to calculate the score of the candidate
def match_ans(ans):
	with open('answers.txt') as af:
		con = af.read().strip().split('\n')  # rading answers and storing them in 'con' variable

	score = 0
	for i in range(len(con)):
		if ans[i] == con[i]:  # to check the correct answer
			score += 10

	return score