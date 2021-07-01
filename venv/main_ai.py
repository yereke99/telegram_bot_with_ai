import telebot
from io import BytesIO
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

bot = telebot.TeleBot('1215118820:AAFgD63OYl_hV8LMU2yJ2N5D_Z9uMcpeCW8')

@bot.message_handler(content_types=['photo'])
def recognition(message):
    fileId = message.photo[-1].file_id
    file = bot.get_file(fileId)
    down_file = bot.download_file(file.file_path)
    with open("image.jpg", "wb") as f:
        f.write(down_file)
    img = cv2.imread("image.jpg")
    gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        img = cv2.rectangle(img, (x,y),(x+y, y+h), (255, 0, 0), 2)
    cv2.imwrite("image.jpg", img)
    img = BytesIO(open("image.jpg", "rb").read())
    bot.send_message(message.chat.id, img)

bot.polling(none_stop = True)

