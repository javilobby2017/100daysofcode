print("math game!")

multiple=int(input("multiple of : "))
times= 1
score= 0
while times < 11:
    userans1 =input(str(multiple) + " x " + str(times) + " = ")
    answer = multiple * times
    if int(userans1) == answer:
        print("correct answer")
        score += 1
    else:
        print("incorrect")
    times += 1
    print("")
print("Score: " + str(score))
if score >= 8:
    print("you are a smart guy")
