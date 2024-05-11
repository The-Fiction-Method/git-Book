# Introduction
This repository contains the base files I use when writing a story and generating the appropriate versions for publishing.

The **Book.docx** file is the most important, as it is where I write the book using an application such as *Microsoft Word* or *[LibreOffice Writer](https://www.libreoffice.org/)*, though any word processor capable of working with the Docx format is appropriate.
The **Notes.txt** file the next most important, as that is where I store various notes, such as names and short descriptions of characters, places, &c. as well as any ideas I have for specific events, the timeline, and so on.
Every other file is concerned with publication, or *git* tracking in the case of the **.gitignore** file and this **README.md**.

Here is a list of the different software involved:
- [LibreOffice Writer](https://www.libreoffice.org/) (or other word processor)
- [git](https://git-scm.com/) (or other git repository manager)
- LaTeX via [MiKTeX](https://miktex.org/) (or other distrubtions, but some aspects may vary)
	- packages used (if not installed, MiKTeX will ask to install):
		- [opensans](https://ctan.org/pkg/opensans) (uses opensans font)
		- [geometry](https://ctan.org/pkg/geometry) (controls page size and margins)
		- [ragged2e](https://ctan.org/pkg/ragged2e) (controls text alignment, such as left-align rather than justify)
		- [hyphenat](https://ctan.org/pkg/hyphenat) (to disable words breaking with hyphenation across lines)
		- [graphicx](https://ctan.org/pkg/graphicx) (to enable adding images to book)
		- [indentfirst](https://ctan.org/pkg/indentfirst) (indent the first paragraph of a chapter; my preference)
		- [titletoc](https://ctan.org/pkg/titletoc) (for controlling the table of contents)
		- [tocloft](https://ctan.org/pkg/tocloft) (for controlling the table of contents)
		- [titlesec](https://ctan.org/pkg/titlesec) (for customizing section/chapter titles)
		- [fancyhdr](https://ctan.org/pkg/fancyhdr) (controlling headers and footers)
		- [emptypage](https://ctan.org/pkg/emptypage) (ensures pages without text lack headers and footers)
		- [hyperref](https://ctan.org/pkg/hyperref) (enables linking within document and PDF metadata control)
		- [imakeidx](https://ctan.org/pkg/imakeidx) (for making book indices)
		- [xpatch](https://ctan.org/pkg/xpatch) (for controlling book indices)
- [Sigil](https://sigil-ebook.com/)
- [Python](https://www.python.org/)
	- modules used (all built-in to Python):
		- sys
		- os
		- re
- [pandoc]{https://pandoc.org/}

It should be noted I use Windows and everything is configured around that.
While the software is available on other operating systems, I cannot guarantee everything will work without some translation to other formats or features.
Best example is the **XeLatex Compile - Aux.bat** file under the LaTeX folder.
Batch is a Windows script type, and so will not work on other OSes directly.
Also it uses some MiKTeX CLI arguments that might not be present with other LaTeX distrubtions (though I can believe the main one, setting the auxiliary folder location, does exist for the others, if under a different name).

# My Process
After creating a repository from this template, I will rename **Book.docx** and **Book.tex** files to whatever the working title is.
Within **Book.tex**

It should be noted, **.docx** files are set to be ignored, and this is intentional.
The renamed file will not be tracked.

After finishing a writing session, the **pandoc - to LaTeX-multi.py** script will be used by dragging and dropping the Docx file onto it.
(The **pandoc - to HTML-multi.py** script can be used instead, but I prefer to work in LaTeX at this time and leave the *HTML* and ePub for later.)
This script will create a Markdown file of the same name as the Docx, using *pandoc*.
This is an intermediate file Python uses to generate the **.ltx** files for *LaTeX*, with the appropriate formatting.
(I use **.tex** for the main control files and **.ltx** for the content files, but both are *LaTeX* file types.)
The repository will ignore all **.md** files.

In addition to translating the text formatting from the Markdown file to the appropriate *LaTeX* (or *HTML*) code, the *Python* script will create a separate file corresponding to the headings within the book, such as chapter names.
(I believe it will be necessary to use what corresponds to *Heading 1* for proper recognition and translation of these headers.)

It will be necessary to add these files to the renamed **Book.tex** file.
Simply copy the `\Chapter{FILENAME}` line and the `\cleardoublepage` beneath it, writing the name of the new **.ltx** file in for the filename.
It is set to automatically increment the chapter number, so if you wish to use a different name, change the line to resemble `\Chapter[NEW_NAME]{FILENAME}` with whatever the new name is you desire.

With the individual *LaTeX* (or *HTML*) files made, they can be added and committed to the *git* repository.
Being plain-text files, *git*'s features of tracking differences and compressing the data it stores can be taken advantage of.

To compile the *LaTeX* PDF, drag and drop the **Book.tex** file onto the **XeLatex Compile - Aux.bat** file.
This will call the *XeLaTeX* engine to compile the PDF, which I have found reliable and prefer to others.
