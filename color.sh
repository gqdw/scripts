#!/bin/bash 
# for bash color test 
COLOR_REST='\033[0m'
COLOR_RED='\033[42;37m'
#COLOR_RED='\e[1;5;32;47m'
#COLOR_RED='\e[0;31m'
echo -e "${COLOR_RED} ok ${COLOR_REST}"
echo -e "\e[1;5;32;47m OK \e[0m"

echo -e "\033[42;37m 绿底白字 \033[0m"
echo -e "$COLOR_RED test $COLOR_REST"
fun()
{
	echo -e "$COLOR_RED$1$COLOR_REST"
}
fun aaa
fun bbb
