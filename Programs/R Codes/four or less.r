#find the probability of having four or less correct answers in a student attempts to answer every question at random
dbinom(4,size=12,prob=0.2)
dbinom(0,size=12,0.2)+
dbinom(1,size=12,0.2)+
dbinom(2,size=12,0.2)+
dbinom(3,size=12,0.2)+
dbinom(4,size=12,0.2)