guestlist = ['Jim','Danny','Kevin']
for i in range(len(guestlist)):
    print("I invited " + guestlist[i] + " for dinner")
    i =+1
print("But " + guestlist[1] + " won't be able to come")
#Substitui Danny por Patrick na lista
guestlist [1] = 'Patrick'
print("So I invited " + guestlist[1] + " for dinner")
print("I'm getting a bigger dinner table, so I can invite more people")
guestlist.insert(0, 'Harry')
guestlist.insert(2, 'Will')
guestlist.append('Tom')
print(guestlist)
for i in range(len(guestlist)):
    print("I invited " + guestlist[i] + " for dinner")
    i =+1
print("Bad news, the table won't arrive on time")
print("And I already sold my old one")
print("Best I can do is have two of you for dinner")
unwanted_guests = ['Harry' , "Patrick" , "Tom"  , "Will"]
for guest in guestlist:
    if guest in unwanted_guests:
        guestlist.remove(guest)
print(unwanted_guests)
for not_guest in unwanted_guests:
    print(not_guest)
    print('Sorry ' + not_guest + ", I can't invite you")
print (guestlist)
#not_guest = guests.pop()
#print('Sorry ' + not_guest + ", I can't invite you")
#not_guest = guests.pop(3)
#print('Sorry ' + not_guest + ", I can't invite you")
#not_guest = guests.pop(2)
#print('Sorry ' + not_guest + ", I can't invite you")
#not_guest = guests.pop(0)
#print('Sorry ' + not_guest + ", I can't invite you")
for i in range(len(guestlist)):
    print(guestlist[i]+ ", you're still invited for dinner")
    i =+1
guestlist.clear()
print (guestlist)