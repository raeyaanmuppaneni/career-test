#bussinessperson, scientist, leader, artist

print("Are you confused between :bussinessperson, scientist, leader, artist. Answer these five questions to see which one suits you best")

carrer_points = {
    "bussinessperson":0,
    "scientist":0,
    "leader":0,
    "artist":0
}

# questions with options
questions = [
    {
    "question":"What will you do if you get a time machine?",
    "options":[["sell it for money","bussinessperson"],["see future","scientist"],["help others to use to use it","leader"],["travel to beautiful places","artist"]]
    },
    {
    "question":"What sounds like the worst idea to you?",
    "options":[["having an annoying boss","bussinessperson"],["traveling to the same place","scientist"],["not being allowed to run for student council","leader"],["wearing an outfit tht doesn't suit the occasion","artist"]]
    },
    {
     "question":"You feel happiest when you...",
    "options":[["have a chance to make money","bussinessperson"],["discover new things","scientist"],["collaborate with people","leader"],["wear an outfit that suits an occasion the best","artist"]]
    },
    {"question":"What do you do on social media?",
    "options":[["no time to spend on it","bussinessperson"],[" find new and interesting things","scientist"],["get along with people through social media","leader"],["scroll through pictures posted by others ","artist"]]
    },
    {
    "question":"If you get a surprise bonus at work, how are you going to spend it?",
    "options":[["invest it","bussinessperson"],["travel to new places","scientist"],["throw a party","leader"],["buy nice clothes","artist"]]
    },
    ]


for i in range(len(questions)):
    print()
    print(questions[i]["question"])
    for index,option  in enumerate(questions[i]["options"]):
        print(index+1 , option[0])
    a = int(input("Enter the number of the option you choose."))
  
    carrer = questions[i]["options"][a-1][1]

    carrer_points[carrer] += 1


points = list(carrer_points.values())
max_points=max(points)
rep = points.count(max_points)


if rep ==1:
    print("Based on your answers, it seems that this profession would suit you best:")
    print((max(carrer_points,key = carrer_points.get)))
else:
    print("Based on your answers, it seems that either of these two professions would suit you best:")
    for key,value in carrer_points.items():
        if value == max_points:
            print(key)



    
