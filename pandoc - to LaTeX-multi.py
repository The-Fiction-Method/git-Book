import sys, os, re

#	identify the type of file to be produced
outType	=	"LaTeX"
outExtn	=	"ltx"

#	sentences to lines, but not quotes that do not end sentences
def sent2line(PARA):
	PARA	=	re.sub('." ([^a-z])', r'."\n\1', PARA.replace('. ', '.\n'))
	PARA	=	re.sub('!" ([^a-z])', r'!"\n\1', PARA.replace('! ', '!\n'))
	PARA	=	re.sub('\?" ([^a-z])', r'?"\n\1', PARA.replace('? ', '?\n'))
	return(PARA)

#	clean up unwanted spaces
def spaceClean(TEXT):
	return(	re.sub("[ ]{2,}", ' ', TEXT)\
				.lstrip())

def md2LaTeX(TEXT):
	# TEXT	=	'<p>' + TEXT.rstrip() + '</p>\n'
	TEXT	=	re.sub('\*\*(.*?)\*\*', r'\\textbf{\1}', TEXT)
	TEXT	=	re.sub('\*(.*?)\*', r'\\textit{\1}', TEXT)
	# TEXT	=	TEXT.replace('\dinkus', '<center>***</center>')
	return(TEXT)

for file in sys.argv[1:]:
#	set the different variables necessary for accessing the file
	droppedFile	=	file
	droppedPath	=	file.rsplit("\\",1)[0] + '\\'
	droppedName =	file.rsplit("\\",1)[1].rsplit(".",1)[0]
#	set the working directory so the files go where desired
	os.chdir(droppedPath)

#	pandoc command to create the markdown file
#		quotes are straightened by +smart and line wrapping of the original document is preserved
	os.system('pandoc -t markdown_strict+smart --wrap=preserve "' + droppedFile + '" -o "' + droppedName + '.md"')

#	Chapters folder is created for the files to be held in
	if not os.path.exists(droppedPath + outType):
		os.mkdir(droppedPath + outType)
	if not os.path.exists(droppedPath + outType + '\\Chapters'):
		os.mkdir(droppedPath + outType + '\\Chapters')

#	contents of the created markdown file are read into lines variable
	with open(droppedName + '.md', 'r') as file:
		lines	=	file.readlines()

#	loop through the lines
	for line in lines:
#		if the line starts with #, a header, the header is pulled out, an empty file with that name is created, and we go to the next line
		if '# ' in line:
			sect	=	line.replace('# ', '').rstrip()
			with open(outType + '\\Chapters\\' + sect + '.' + outExtn, 'w') as file:
				# file.write('<h1>' + sect + '</h1>\n\n')
				pass
			print(sect)
			continue

#		blank lines in markdown are skipped
		if line == '\n':
			continue

#		space cleaning: regex to replace repeat spaces with one and lstrip to remove them at the start of lines
		line	=	spaceClean(line)
		line	=	md2LaTeX(line)
#		EOL doubled so paragraphs are separated
		line	=	line.replace('\n', '\n\n')
#		separating sentences to lines
		line	=	sent2line(line)

#		section files are written
		with open(outType + '\\Chapters\\' + sect + '.' + outExtn, 'a') as file:
			file.write(line)

# os.system("pause")
