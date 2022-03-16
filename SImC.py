from PIL import Image, ImageChops
import os as s

class Check:
    def __init__(self, __first_dir, __second_dir):
        # "D:\Code\same_copy\img104"
        # "D:\Code\same_copy\img86"

        self.__img_from = s.listdir(__first_dir)
        self.__img_same = s.listdir(__second_dir)

        n = 1

        with open("list.txt", "w",  encoding="utf-8") as l:
            l.close()

        for i in self.__img_from:

            im1 = Image.open(f"{__first_dir}\{i}")
            exlusive = True
            num = 1

            for j in self.__img_same:

                im2 = Image.open(f"{__second_dir}\{j}")

                result = ImageChops.difference(im2, im1).getbbox()

                print(f"From 104:{__first_dir}\{i}", n, num, result)
                num += 1

                if result == None:
                    exlusive = False
                    break

            if exlusive:
                with open("list.txt", "a",  encoding="utf-8") as l:
                    l.write(f"{__first_dir}\{i}\n")
                    l.close()
            n += 1
        

