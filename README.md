# eko201-tester
A Python program to read in a testbank in docx format and test the user with random questions from files.

I created this in Summer 2020, for the EKO201E course in ITU, where we were given a set of docx files containing questions related to each chapter. It felt easier to go through GUI interface instead of scrolling in hundreds of pages of docx files. By modifying getQuestions (and maybe getText based on your document), this might be used for files with different layouts.

I did not want to spend much time on this project, so I used [EasyGUI](https://github.com/robertlugg/easygui), which is a nice wrapper for simple GUI operations but not maintained anymore. I used [python-docx](https://github.com/python-openxml/python-docx) for reading the files.

## Usage
Download this repository. If you have python and pip installed in your environment,
`pip install -r requirements.txt` will install the required packages,
`python main.py` will start the program.
By default, it will look for a subdirectory called `files/eco201_docx_versions/`, and it will search for the filenames EKO201E questions used. Using a text editor, you can modify the main.py file to replace filepaths according to your needs.
