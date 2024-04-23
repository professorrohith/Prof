from pytube import YouTube as yt
link = str(input("Please Enter The Video URL here : "))
v = yt(link)
print("title : ",v.title)
print("views : ",v.views)
print("Processing..")
dl = v.streams.get_highest_resolution()
dl.download("C:\\Users\\user\\Videos")
print("Thankyou For Using this Program \n It will be downloaded in C:/Users/user/Videos .by --Rohit")