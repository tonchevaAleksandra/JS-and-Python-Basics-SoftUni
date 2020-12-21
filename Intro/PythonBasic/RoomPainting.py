count_paint_boxes= int(input())
count_roll_wallpaper=int(input())
price_pair_gloves=float(input())
price_paintbrush=float(input())

price_paint_box=21.50
price_roll_wallpaper=5.20
count_pair_gloves= math.ceil(0.35*count_roll_wallpaper)
count_paintbrush=math.floor(0.48*count_paint_boxes)

total_paint_price= count_paint_boxes*price_paint_box
total_roll_price=count_roll_wallpaper*price_roll_wallpaper
total_gloves_price= count_pair_gloves*price_pair_gloves
total_paintbrush_price= count_paintbrush*price_paintbrush

total_price=total_gloves_price+total_paint_price+total_paintbrush_price+total_roll_price
delivery_cost=total_price*1/15

print(f'This delivery will cost {delivery_cost:.2f} lv.')