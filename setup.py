import docx
import random
import easygui


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def getQuestions(filename):
    text = getText(filename)
    questions = {}
    for question in text.split("MSC"):
        try:
            questions[question.split("ANS: ")[0]] = question.split('ANS: ')[1]
        except IndexError as e:
            pass
    return questions


def setupSession(chapters):
    qnum = easygui.integerbox("How many questions should be asked?")
    if not (easygui.ynbox("Asking from all chapters, YES to continue or NO to select chapters.")):
        cstart = easygui.integerbox("Chapter to start: ")
        clen = easygui.integerbox("How many chapters should be included (Max 22): ")
    else:
        cstart = 0
        clen = 22
    return qnum, chapters[cstart:cstart + clen]


def endSession():
    return not easygui.ccbox("Do you want to continue?")


def askQuestions(n=5, chapter_list=[]):
    testbank = dict()
    for chapter in chapter_list:
        testbank.update(chapter)
    question_list = list(testbank.keys())
    for _ in range(n):
        key = random.choice(question_list)
        if testbank[key][0] in ["T", "F"]:
            choice = showQuestion(key, 0)
        else:
            choice = showQuestion(key, 1)
#        i = input(key + ': ').upper()
        checkAnswer(choice, testbank[key])


def showQuestion(question, qtype):
    # qtype 0: true/false, qtype 1: multiple choice
    if qtype == 0:
        answer = ("T", "F")
    if qtype == 1:
        answer = ("A", "B", "C", "D")
    return easygui.buttonbox(question, 'Answer: ', answer)


def checkAnswer(choice, truth):
    if choice == truth[0]:
        easygui.msgbox('Correct!')
    else:
        easygui.msgbox('Incorrect, should have been ' + truth)

