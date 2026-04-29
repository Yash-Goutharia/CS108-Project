#!/bin/bash
FILE="history.csv"
SORT_BY=$1 

printf "%-15s | %-5s | %-6s | %-5s | %-6s\n" "Player" "Wins" "Losses" "Ratio"

awk -F',' '
{
    p1 = $3; p2 = $4;
    players[p1]=1; players[p2]=1;

    if ($1 == "Win") {
        wins[p1]++;
        losses[p2]++;
    }
}
END {
    for (p in players) {
        w = wins[p] + 0;
        l = losses[p] + 0;
        d = draws[p] + 0;
        
        if (l == 0) {
            ratio = w;
        } else {
            ratio = w / l;
        }
        
        printf "%-15s   %-5d   %-6d   %-5d   %-6.2f\n", p, w, l, ratio;
    }
}' "$FILE" | sort -k"$SORT_BY" -nr