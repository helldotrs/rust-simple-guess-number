import random

num_random  = 0
num_input   = 0
score       = 0

while num_random != num_input {
    if num_random == 0 {
        num_random = random.randrange(1,100)
    }

    #no error handeling
    
    if 1 <= num_input <= 100 {
        if num_input < num_random {
            print("guess a higher number!")
        }
        elif num_input > num_random {
            print("guess a smaller number!")
        }
    }

    num_input = input("guess a number 1-100: ")


}

print(num_random)
