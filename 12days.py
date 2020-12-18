import time
import winsound

filename="12day.wav"
winsound.PlaySound(filename,winsound.SND_FILENAME)

numbers=["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth","eleventh","twelfth"]

gifts=["a partridge in a pear tree","turtle doves","french hens","calling birds","gold rings","geece a laying","swans a swimming","maids a milking","ladies dancing","lords a leaping","pipers piping","drummers drumming"]

for i in range (0,12):
    print("On the",numbers[i],"day of Christmas my true love gave to me,",i+1,gifts[i])

    for j in range (0,i):          
        print(i-j,gifts[i-j-1])
    
    time.sleep(1)
    print("-----------------------")
