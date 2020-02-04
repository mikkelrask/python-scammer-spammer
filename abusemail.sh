#!/bin/sh
clear
echo "WHOIS information provided by whois.com "
echo ""
echo "****************************************"
echo $1
echo "****************************************"
echo ""
whois $1 | grep abuse
