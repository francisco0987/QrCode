import qrcode

img = qrcode.make("https://www.linkedin.com/in/francisco-dias-6abb65168/")
img.save("my-linkdin.jpg")
