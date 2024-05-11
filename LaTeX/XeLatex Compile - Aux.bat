@echo off
::It runs the compilation twice to ensure the TOC is made, as that requires information from a first pass

pushd %~dp1

:start
TITLE XeLaTeX - %~n1

echo XeLaTeX %~n1 Running
xelatex -aux-directory="AUX files" -quiet -no-pdf "%~1"
xelatex -aux-directory="AUX files" -quiet "%~1"
echo XeLaTeX %~n1 Done

shift

if "%~1"=="" goto end
goto start

:end

rmdir /s /q "AUX files"

REM pause