@echo off
set TEXT_FILE=Obama.txt
set FIRST_WORD=I
set LENGTH=300
if [%1] NEQ [] (
	set TEXT_FILE=%1
)
if [%2] NEQ [] (
	set FIRST_WORD=%2
)
if [%3] NEQ [] (
	set LENGTH=%3
)
chcp 65001 > null
python MarkovTextGenerator.py %TEXT_FILE% %FIRST_WORD% %LENGTH%
chcp 437 > null

