#!/bin/bash
for ((x=1;x<=2;x++)); do
	read -p "Player$x, Enter your username:" username
        if [[ -z $(grep "^$username"$'\t' users.tsv) ]]; then
		echo "Username does not exist, do you want to register:[Y/N]"
		read response
                if [[ $response == "Y" ]]; then
			read -p "Make your password:" password
			echo -e "$username\t$(echo $password | sha256sum )" >> users.tsv
                fi
        else 
		while true; do
			read -p "Player$x, Enter your password:" password
			if [[  $(grep "^$username"$'\t' users.tsv | cut -d '$t' -f 2) != $(echo $password | sha256sum) ]]; then
				echo "Wrong password, Please try again"
		                continue
		        else 
			   break
		        fi
	        done	
        fi
done
echo "Both players Authenticated"
