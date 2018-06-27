#!/bin/sh
if [ -z "$2" ]
then
	echo "Please provide a command line argument naming your experiment, and a second argument with your processed data file."
	exit 1
else
	echo "$1 will be the name of the directory you have created on the server."
fi
mkdir ~/public_html/$1
# initial copy of materials
cp -rp ~/public_html/exmpl/* ./$1
chmod 755 $1
# initial copy of cgi-bin materials
mkdir ~/public_html/cgi-bin/$1
chmod 755 ~/public_html/cgi-bin/$1
cp -p ~/public_html/cgi-bin/exmpl/* ~/public_html/cgi-bin/$1/
chmod 755 ~/public_html/cgi-bin/$1/
# add personalized data file
cp $2 ~/public_html/$1/data_includes
chmod 755 ~/public_html/$1/data_includes/*
rm -f ~/public_html/$1/cache/*
echo "completed"

python editFile.py ~/public_html/$1/other_includes/main.js ~/public_html/$1/www/experiment.html ~/public_html/$1/www/server.cgi ~/public_html/cgi-bin/$1/server_conf.py $1
