from setup import getQuestions, askQuestions, setupSession, endSession

folder_path = "files/eco201_docx_versions/" 

filename_list = ["Prin_CH01.AISE_TB.docx",
                 "Prin_CH02.AISE_TB.docx",
                 "Prin_CH03.AISE_TB.docx",
                 "Prin_CH04.AISE_TB.docx",
                 "Prin_CH05.AISE_TB.docx",
                 "Prin_CH06.AISE_TB.docx",
                 "Prin_CH07.AISE_TB.docx",
                 "Prin_CH08.AISE_TB.docx",
                 "Prin_CH10.AISE_TB.docx",
                 "Prin_CH13.AISE_TB.docx",
                 "Prin_CH14.AISE_TB.docx",
                 "Prin_CH15.AISE_TB.docx",
                 "Prin_CH16.AISE_TB.docx",
                 "Prin_CH17.AISE_TB.docx",
                 "Prin_CH23.AISE_TB.docx",
                 "Prin_CH24.AISE_TB.docx",
                 "Prin_CH25.AISE_TB.docx",
                 "Prin_CH26.AISE_TB.docx",
                 "Prin_CH28.AISE_TB.docx",
                 "Prin_CH29.AISE_TB.docx",
                 "Prin_CH30.AISE_TB.docx",
                 "Prin_CH31.AISE_TB.docx"]

chapters = list()
for filename in filename_list:
    chapters.append(getQuestions(folder_path + filename))

while True:
    qnum, qlist = setupSession(chapters)

    askQuestions(qnum, qlist)

    if endSession():
        print("Güle güle")
        break
