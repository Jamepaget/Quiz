#question list
questions_list = [["5*3=",15], ["10*2=",20], ["2*2=",4],
                  ["20*2=",40],["8*8=",64],  ["4*3=",12],
                  ["5*5=",25], ["10*3",30],  ["8*4=",32],
                  ["4*9=",36]]


#for loop
points =1

for question in questions_list:
    guess=int (input(question[0]))
    if guess == question[1]:
        print("correct!")
        print("You got {}points".format(points))
        points +=1

    else:
        print("incorrect!")
