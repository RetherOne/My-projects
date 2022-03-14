from PIL import Image, ImageChops
import os as s


first_dir = "D:\Code\same_copy\img104"
second_dir = "D:\Code\same_copy\img86"
# exl = "D:\Code\same_copy\exlusive"


img_from = s.listdir(first_dir)
img_same = s.listdir(second_dir)

n = 1
for im in img_from:
    im1 = Image.open(f"{first_dir}\{im}")
    exlusive = True
    num = 1

    for i in img_same:
    
        im2 = Image.open(f"{second_dir}\{i}")

        result = ImageChops.difference(im2, im1).getbbox()
        
        print(f"From 104:{first_dir}\{im}",n, num, result)
        num += 1
        if result == None:
            exlusive = False
            break

    if exlusive:
        with open("list.txt", "a",  encoding="utf-8") as l:
            l.write(f"{first_dir}\{im}\n")
    n += 1
