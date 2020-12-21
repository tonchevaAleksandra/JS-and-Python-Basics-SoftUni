team = input()
souvenir_type = input()
souvenir_count = int(input())
 
souvenir_price = 0
total_price = 0
 
if team == "Argentina":
    if souvenir_type == "flags":
        souvenir_price = 3.25
    elif souvenir_type == "caps":
        souvenir_price = 7.20
    elif souvenir_type == "posters":
        souvenir_price = 5.10
    elif souvenir_type == "stickers":
        souvenir_price = 1.25
        else print("Invalid stock!")
elif team == "Brazil":
    if souvenir_type == "flags":
        souvenir_price = 4.20
    elif souvenir_type == "caps":
        souvenir_price = 8.50
    elif souvenir_type == "posters":
        souvenir_price = 5.35
    elif souvenir_type == "stickers":
        souvenir_price = 1.20
     else print("Invalid stock!")
elif team == "Croatia":
    if souvenir_type == "flags":
        souvenir_price = 2.75
    elif souvenir_type == "caps":
        souvenir_price = 6.90
    elif souvenir_type == "posters":
        souvenir_price = 4.95
    elif souvenir_type == "stickers":
        souvenir_price = 1.10
    else print("Invalid stock!")
elif team == "Denmark":
    if souvenir_type == "flags":
        souvenir_price = 3.10
    elif souvenir_type == "caps":
        souvenir_price = 6.50
    elif souvenir_type == "posters":
        souvenir_price = 4.80
    elif souvenir_type == "stickers":
        souvenir_price = 0.90
        else print("Invalid stock!")
else print("Invalid country!")
 
 if(souvenir_price!=0)
 {
total_price = souvenir_count * souvenir_price
print(f'Pepi bought {souvenir_count} {souvenir_type} of {team} for {total_price:.2f} lv.')
 }
 
