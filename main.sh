#!/bin/bash

USER_FILE="users.tsv"

# create file if not exists
touch $USER_FILE

hash_password() {
    echo -n "$1" | sha256sum | awk '{print $1}'
}

authenticate_user() {
    while true; do
        read -p "Enter username: " username
        read -s -p "Enter password: " password
        echo ""

        hash=$(hash_password "$password")

        if grep -q "^$username" "$USER_FILE"; then
            stored_hash=$(grep "^$username" "$USER_FILE" | cut -f2)

            if [ "$hash" == "$stored_hash" ]; then
                echo "Login successful!" >&2   
                echo "$username"
                return
            else
                echo "Incorrect password. Try again." >&2
            fi

        else
            read -p "User not found. Register? (y/n): " choice

            if [ "$choice" == "y" ]; then
                echo -e "$username\t$hash" >> "$USER_FILE"
                echo "User registered!" >&2
                echo "$username"
                return
            fi
        fi
    done
}

echo "===== Player 1 Login ====="
user1=$(authenticate_user)

echo "===== Player 2 Login ====="
while true; do
    user2=$(authenticate_user)

    if [ "$user1" != "$user2" ]; then
        break
    else
        echo "Players must be different!"
    fi
done

 # launch game i used in my pc for git bash running 
# "/c/Users/iitbo/AppData/Local/Programs/Python/Python310/python" game.py "$user1" "$user2"
