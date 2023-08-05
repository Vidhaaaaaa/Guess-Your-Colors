import random

COLORS = ['R', 'G', 'B', 'W', 'Y', 'V'] 
# defining colors to be used
# can be changed as per choice


inp_col_length = 4 
# defining length of the input color list
# can be changed as per choice

rand_col = random.sample(COLORS, inp_col_length) # taking random colors from main_col

tries = 10
# defining no. of tries in which the player needs to find the answer
# can be changed as per choice

print("Hi, This is Vidha's FIND YOUR COLORS game")

print('--------------------------------------------------------------------------------------')

print(f"""Rules are simple:
1. the computer will take a list of random colors from the following list. You have to guess the color names in {tries} tries
2. type your color names with a space in between. example- W R V B
3. ENJOY!!""")

print('The colours you should choose from are = ' , COLORS)
print('--------------------------------------------------------------------------------------')

print(f'you have {tries} tries to answer correctly, if you are not able to answer in {tries} tries, please restart!')
print('(for the first input please enter G B R Y to start the game)')

print('--------------------------------------------------------------------------------------')



def inv_col(x): # defining a function to check for invalid color
    for j in x:
            if j not in COLORS:
                print('please enter valid colors')
                break
            else:
                break

    return x


def user_inp():  # function for checking if the input is invalid (length of the input + invalid color entered)
    
    guess = input('enter colors: ').upper().split()   # taking user input with spaces and converting it into list

    if len(guess) != inp_col_length:
        print(f'please enter {inp_col_length} colors')
        
    inv_col(guess) # using the function to check for invalid color

    return guess


def compare(x = rand_col, y = user_inp()): # defining a function for comparing lists plus checking if they are in the object COLORS or not
     
    correct = 0
    incorrect = 0

    for i in range(len(rand_col)):

        if x[i] == y[i]:
            correct +=1
        else:
            incorrect +=1

    return correct , incorrect



# MAIN CODE TO COMPARE LISTS

for tryy in range(tries): # looping until the number of tries defined
    user_inp()
    corr_incorr_list = compare()
    if user_inp() == rand_col:
        print('yay, you guessed correctly!')
        break
    else:
        print(f'correct values: {corr_incorr_list[0]} | incorrect values: {corr_incorr_list[1]}')
