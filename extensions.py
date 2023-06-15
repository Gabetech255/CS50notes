txt = input("enter filename   ")
txt = txt.strip()
txt = txt.lower()
dot = txt.find('.')

if txt.endswith(".gif", dot) == True:
    print("image/gif")

elif txt.endswith(".jpg", dot) == True:
    print("image/jpg")

elif txt.endswith(".jpeg", dot) == True:
    print("image/jpg")

elif txt.endswith(".png", dot) == True:
    print("image/png")

elif txt.endswith(".pdf", dot) == True:
    print("application/pdf")

elif txt.endswith(".txt", dot) == True:
    print("text/plain")

elif txt.endswith(".zip", dot) == True:
    print("application/zip")

else:
    print('application/octet-stream')



