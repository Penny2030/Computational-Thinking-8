introvert_points = 0
extrovert_points =  0
ambivert_points = 0
print("Today we are going to find out if you are and Introvert, Extrovert, or Ambivert")
print ("Pls write either true or false or T or F")
print("First Question,")
answer1 = input("I prefer one-on-one conversations over large group gatherings.")
if answer1 == "true" or "T":
    introvert_points += 1
elif answer1 == "false" or "F":
    extrovert_points += 1
    ambivert_points += 1
answer2 = input("I feel energized by social events and meeting new people.")
if answer2 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer2 == "false" or "F":
    extrovert_points += 1
answer3 = input("I often prefer to express myself in writing rather than speaking.")
if answer3 == "true" or "T":
    introvert_points += 1
elif answer3 == "false" or "F":
    extrovert_points += 1
    ambivert_points += 1
answer4 = input("I enjoy being the center of attention at parties.")
if answer4 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer4 == "false" or "F":
    extrovert_points += 1
answer5 = input("I enjoy solitude and find it restorative.")
if answer5 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer5 == "false" or "F":
    extrovert_points += 1
answer6 = input("I get drained after long social events, even if I enjoyed them.")
if answer6 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer6 == "false" or "F":
    extrovert_points += 1
answer7 = input("I dislike small talk but enjoy deep, meaningful conversations.")
if answer7 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer7 == "false" or "F":
    extrovert_points += 1
answer8 = input("I'm comfortable making plans far in advance.")
if answer8 == "false" or "F":
    introvert_points += 1
elif answer8 == "true" or "T":
    extrovert_points += 1
    ambivert_points += 1
answer9 = input("I do my best work when I can focus without interruptions.")
if answer9 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer9 == "false" or "F":
    extrovert_points += 1
answer10 = input('I like to "think out loud" and talk through problems as I solve them.')
if answer10 == "false" or "F":
    introvert_points += 1
    ambivert_points += 1
elif answer10 == "true" or "T":
    extrovert_points += 1
answer11 = input("I find large crowds overwhelming and prefer smaller settings.")
if answer11 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer11 == "false" or "F":
    extrovert_points += 1
answer12 = input("I'm generally spontaneous and don't always need a plan.")
if answer12 == "true" or "T":
    introvert_points += 1
elif answer12 == "false" or "F":
    extrovert_points += 1
    ambivert_points += 1
answer13 = input("I'd rather have a quiet weekend with nothing planned than a busy one.")
if answer13 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer13 == "false" or "F":
    extrovert_points += 1
answer14 = input("I feel energized by other people")
if answer14 == "false" or "F":
    introvert_points += 1
    ambivert_points += 1
elif answer14 == "true" or "T":
    extrovert_points +=1
answer15 = input("I am often told I'm a good listener.")
if answer15 == "true" or "T":
    introvert_points += 1
elif answer15 == "false" or "F":
    extrovert_points += 1
    ambivert_points += 1
answer16 = input("I dislike conflict and try to avoid it.")
if answer16 == "true" or "T":
    introvert_points += 1
elif answer16 == "false" or "F":
    extrovert_points += 1
    ambivert_points += 1
answer17 = input("I prefer to celebrate special occasions with just a few close people.")
if answer17 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer17 == "false" or "F":
    extrovert_points += 1
answer18 = input("I enjoy multitasking and juggling several things at once.")
if answer18 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer18 == "false" or "F":
    extrovert_points += 1
answer19 = input("I often let my phone go to voicemail.")
if answer19 == "true" or "T":
    introvert_points += 1
elif answer19 == "false" or "F":
    extrovert_points += 1
    ambivert_points += 1
answer20 = input("I think before I speak.")
if answer20 == "true" or "T":
    introvert_points += 1
    ambivert_points += 1
elif answer20 == "false" or "F":
    extrovert_points += 1
if introvert_points > extrovert_points and introvert_points > ambivert_points:
    print ("You are an introvert. Shhhh stop talking so loud I'm trying to be introverted.")
elif extrovert_points > introvert_points and extrovert_points > ambivert_points:
    print ("You are an extrovert!!!!! PARTY TIME!!!!!!!!!!")
elif ambivert_points > introvert_points and ambivert_points > extrovert_points:
    print ("You are an ambivert. You are the best of both worlds!")