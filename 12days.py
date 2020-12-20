G=print; F=range; import winsound as B; B.PlaySound('12day.wav',B.SND_FILENAME); E=['first','second','third','fourth','fifth','sixth','seventh','eigth','ninth','tenth','eleventh','twelfth']; C=['a partridge in a pear tree','turtle doves','french hens','calling birds','gold rings','geece a laying','swans a swimming','maids a milking','ladies dancing','lords a leaping','pipers piping','drummers drumming']
for A in F(0,12):
	G('On the',E[A],'day of Christmas my true love gave to me,',A+1,C[A])
	for D in F(0,A):G(A-D,C[A-D-1])
