from PIL import Image,ImageDraw,ImageFont
from colorama import Fore,Style

print()
print(f"\t\t\t\t\t\t {Fore.MAGENTA}Генератор мемов запущен!{Style.RESET_ALL}\n")
text_type=int(input("Введите 1, если нужен только нижний текст, введите 2, если нужны и верхний, и нижний текст: "))
top_text=""
bottom_text=""

if text_type==1:
    bottom_text = input("Введите текст, который хотите видеть под картинкой: ")
elif text_type==2:
    top_text=input("Введите текст, который хотите видеть над картинкой: ")
    bottom_text=input("Введите текст, который хотите видеть под картинкой: ")
else:
    print(f"{Fore.RED}ОШИБКА! Введите либо 1, либо 2.{Style.RESET_ALL}")
    quit()

top_text=top_text.replace("не","")
bottom_text=bottom_text.replace("не","")
print(f"Ваш текст:{Fore.GREEN} {top_text} {bottom_text}{Style.RESET_ALL}")

print()
print("Список картинок: ")
pictures=["волк думает кто то спятил.png",
          "Кот в очках.png","Кот в ресторане.png",
          "котик стрымзил камеру.jpeg","это нужно видеть.jpg",
          "кошка с котёнком.jpg","котик на диване с вкусняшкой.jpeg",
          "боевой котик.jpg"]
number=0
while number<len(pictures):
    print(f"{Fore.CYAN} {number}.{pictures[number]} {Style.RESET_ALL}")
    number+=1
index=int(input("Введите номер картинки: "))


image = Image.open(pictures[index])
width, height = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=34)

text1 = draw.textbbox((0, 0), top_text, font)
text2 = draw.textbbox((0,0), bottom_text, font)
draw.text(((width - text1[2]) / 2, 10), top_text, font=font, fill="black", stroke_width=2, stroke_fill="white")
draw.text(((width - text2[2])/2, height - text2[3] - 10), bottom_text, font=font, fill="black", stroke_width=2, stroke_fill="white")
# image.show()
image.save("new meme.png")
image.show()

