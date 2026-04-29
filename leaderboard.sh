#!/bin/bash
FILE="history.csv"
SORT_BY=$1 
echo "Player,no. of wins,no. of losses,W/L ratio"
awk -F',' '
function clean(x){
gsub(/^ +| +$/, "", x);
gsub(/\r/,"",x);
return x}
{
    p1 = clean($3); 
    p2 = clean($4);
    if (p1 != ""){
    players[p1]=1;}
    if (p2 != ""){ 
    players[p2]=1;}

    if ($1 == "Win") {
        wins[p1]++;
        losses[p2]++;
    }
}
END {
    for (p in players) {
        w = wins[p] + 0;
        l = losses[p] + 0;
        if (l == 0) {
            ratio = w;
        } 
        else {
            ratio = w / l;
        }
        
        printf "%s,%5d,%10d,%15.2f\n", p, w, l, ratio;
    }
}' "$FILE" | sort -t ',' -k"$SORT_BY" -nr