import winsound
from time import sleep

class Card:
    def __init__(self, expression:str, points:tuple=(2,-1), height:int=5, width:int=10, borders:tuple=('|','-')):
        self.height = height
        self.width = width
        self.vborder = borders[0]
        self.hborder = borders[1]
        self.win = points[0]
        self.loss = points[1]
        self.x = expression
        self.xvalue = eval(expression)
        self.correct = False

class Board:
    def __init__(self, cols:int=4, rows:int=4, spacing:tuple=(2,1), leftpad:int=3):

        if (cols*rows)%2 == 1:
            print("WidthxHeight must be divisible by 2")
            raise Exception
        self.w = cols
        self.h = rows
        self.cards = self.__initialiseCards()
        self.xpad = spacing[0]*' '
        self.ypad = spacing[1]*'\n'
        self.lpad = leftpad


    def __generateRandomPair(self, a:int=2) -> list: #generates x random equations that are equals to one another in value #Andy
        import random, operator

        """Function to find factors of value1 (from first set of values)"""
        def factors_of_value1(x):

            # To ensure this function can find the positive factor of its absolute number
            x = abs(x)

            factor_list = []
            for i in range(1, x + 1):
                if x % i == 0:
                    factor_list.append(i)
            return factor_list

        """Function to find the other value of the expression on the LHS"""
        def lhs_value(number, sign, selected_factor_number):

            if sign == "+":
                lhs = number - selected_factor_number 
            if sign == "-":
                lhs = number + selected_factor_number
            if sign == "*":
                lhs = number / selected_factor_number
            if sign == "/":
                lhs = number * selected_factor_number

            return (int(lhs))


        """ DEFAULT SETTINGS that you can adjust"""

        lowest_range = -20
        highest_range = 20

        """a represents the number of pairs of expression you wants
        lowest range represents the lowest value you want for your answer
        highest value represents the highest value you want for your answer"""


        """ Generating first random set of values"""
        count1 = 0
        first_set_list = []

        while count1 < a:
            x = random.randint(lowest_range, highest_range)

            if x not in [-1, 0, 1] and x not in first_set_list:
                for i in range(2):
                    first_set_list.append(x)
                count1 += 1


        """Generating random maths operators"""
        count2  = 0
        operators_list = []
        operators = ["+","-","*","/"]

        while count2 < a:
            picked_operator = random.choice(operators)
            operators_list.append(picked_operator)
            count2 += 1


        """Defining operators (Operators in list are str types, cannot be used as operators itself)"""
        allowed_operators={
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv}
        answer_output = []
    #Display of results
        for answer, operator_sign in zip (first_set_list, operators_list):
            # Randomly select a value from the list of factors
            selected_factor_number = random.choice(factors_of_value1(answer))

            answer_output.append(f'{lhs_value(answer, operator_sign, selected_factor_number)}{operator_sign}{selected_factor_number}')
        return (answer_output)


    def __initialiseCards(self) -> list:
        from random import shuffle
        width = self.w
        height = self.h
        expList = []
        for i in range(width*height//2):
            exp1, exp2 = self.__generateRandomPair(a=2)
            expList += [exp1, exp2]
        shuffle(expList)
        outList = []
        for h in range(height):
            temp = []
            for w in range(width):
                temp += [Card(expList.pop())]
            outList += [temp]
        return outList



    def __repr__(self) -> str:
        sampleC = self.cards[0][0] #as all cards are the same
        c_w, c_h = sampleC.width, sampleC.height
        c_vb, c_hb = sampleC.vborder, sampleC.hborder
        lpad = f'{" ":^{self.lpad}}'
        header =  lpad+self.xpad.join([f"{i:^{c_w+2}}" for i in range(1,self.w+1)])+'\n'
        bor_line = lpad+self.xpad.join([str(c_hb)*(c_w+2) for i in range(self.w)])+'\n'
        body = ''
        for row in range(self.h):
            body += bor_line
            exp_row = c_h//2
            for sub_row in range(c_h):
                temp = []
                for col in range(self.w):
                    if sub_row == exp_row:
                        t = self.cards[row][col].x
                    else:
                        t = ' '
                    temp += [f"{c_vb}{t:^{c_w}}{c_vb}"]
                if sub_row == exp_row:
                    lpad = f'{chr(65+row):^{self.lpad}}'
                else:
                    lpad = f'{" ":^{self.lpad}}'
                body += lpad+self.xpad.join(temp)+'\n'
            body += bor_line
            if row < self.h-1:
                body += self.ypad
        return header + body

    
    
    
    #check the nested list
    def check_game_finish(self) -> bool:
    #return true if game not finished
        for x in self.cards:
            for y in x:
                if y.correct == False:
                    return True 
        return False
    
    
    
    
  #update the board
    def check_card(self) -> bool:
        
 #check whether cards have been cleared
        #card1
        
        while True:
            row1,col1 = validate_user_input()
            if a.cards[row1][col1].correct == False:    
                print(f'\n\n\nyou have chosen {a.cards[row1][col1].x}')
                break
            else:
                print('\n\ncant pick that card')
        #card2
        while True:
            row2,col2 = validate_user_input()
            if a.cards[row2][col2].correct == False and (row1,col1) != (row2,col2):    
                print(f'\n\n\n\n\nyou have chosen {a.cards[row2][col2].x}')
                break
            else:
                print('\n\ncant pick that card')

        if a.cards[row1][col1].xvalue == a.cards[row2][col2].xvalue:
            a.cards[row1][col1].x = '-----'
            a.cards[row2][col2].x = '-----'
            a.cards[row1][col1].correct = True
            a.cards[row2][col2].correct = True
            return True
        else:
            return False


        
        

        
        

#check user gave a valid input
#returns a tuble containing the row and col
def validate_user_input() -> tuple:
#what alphabets we are accepting
    valid_alphabets = ['A', 'B', 'C', 'D']
    while True:
        while True:
            #ask user to input an alphabet
            ui_alphabet = (input("Please enter an alphabet from A to D: ")).upper()
            if ui_alphabet not in valid_alphabets:
                print("Please re-enter a valid alphabet.")
            else:
                break

        while True:
            #ask user to input a number
            try:
                ui_number = int(input("Please enter a whole number from 1 to 4: "))
            except ValueError:
                print("Please enter only whole numbers.")
                continue
            if ui_number < 1 or ui_number > 4:
                print("Please re-enter a valid number.")
            else:
                break
        break


    ui_alphabet2 = ord(ui_alphabet)-65
    ui_number -= 1
    user_input = (ui_alphabet2,ui_number)
    return user_input 
    
    

def intro():
    try:
        for line in splashScreen("welcome.txt")[:]:
            print(line, end='')
            PlaySound("sans.wav", asynC=False)
        PlaySound("intro.wav")
        input("\nPress any key to continue\n>")
    except KeyboardInterrupt:
        pass

def ProveWorth():
    try:    
        print(''.join(splashScreen("monke_prove_ur_worth.txt")))
        PlaySound("sigma.wav", loop=True)
        input("Enter to begin:")
    except KeyboardInterrupt:
        pass
    PlaySound(None)

def gameOver():
    """Game over screen"""
    try:
        print(''.join(splashScreen("monke.txt")))
        PlaySound("sigma.wav", loop=True)
        input("Game over. Press enter to return to menu:\n>")
    except KeyboardInterrupt:
        pass
    PlaySound(None)

def fireworks():
    """Win Screen"""
    print(''.join(splashScreen("fireworks.txt")))
    PlaySound("fireworks.wav",loop=True)
    input()
    PlaySound(None)



def displayMenu(functions:list):
    """Display Menu"""
    menuart = splashScreen("menu.txt")
    header = ''
    in_width = max([len(f) for f in menuart])-2
    outer_width = in_width+2
    out = ['-'*(outer_width)]
    for i,f in enumerate(functions,1):
        text = str(i)+': '+f.__doc__
        out += [f"|{text:^{in_width}}|"]
    out += ['-'*(outer_width)]
    print(''.join(menuart))
    print('\n'.join(out))
        
    

def getMenuOption(options:list) -> object:
    if options:
        option = getInputInRange(1,len(options),"Enter menu option:\n>")
        return options[option-1]
    else:
        print("There must be at least one function in the options.")
        raise Exception
        

def getInputInRange(start:int, end:int, message="Enter option:\n") -> int:
    while True:
        ui = input(message)
        if ui.isdigit():
            option = int(ui)
            if option >= start and option <= end:
                return option
            else:
                print(f"Only integers from {start} to {end} are accepted.")
        else:
            print("Please enter an integer.")

def displayCredits():
    """Credits"""
    try:
        for i in range(50):
            print()
        print(''.join(splashScreen("superidols.txt")))
        PlaySound("credits.wav")
        sleep(1.45)
        print('Andy: Math')
        sleep(1.74)
        print('Senna & Bryan:User Input')
        sleep(1.74)
        print('Samuel: Main game loop')
        sleep(1.74)
        print('Jiaqi: Everything else')
        sleep(1.74)
        print('Music used in this game:')
        sleep(1.74)
        print('Intro: Unreal Superhero 3 by Kenet & Rez')
        sleep(1.74)
        print('Main Game: Spectronosis by FearofDark')
        sleep(1.74)
        print('Monke: Sigma Male Theme Song')
        sleep(1.74)
        print('This song: Superidol + Neon genesis Evangelion Opening Mashup by yours truly :)')
        sleep(13.8)
        print(''.join(splashScreen("credits.txt")))
        sleep(0.2)
        for i in range(100):
            print()
        sleep(1)
    except KeyboardInterrupt:
        pass
    
    

    


def startGame():
    """Start Game"""
    global a
    a = Board()
    ProveWorth()
    PlaySound("spectronosis.wav",loop=True)
    print("POV: you are an APE in ELON MUSK's NEURALINK experiment, \n\nMAFIA ELON MUSK:PICK TWO CARDS WITH THE SAME VALUE MAMAMIA\n\n\nPROVE ur WORTH or be disposed of")
    wrong_attempts = 0
    turn_count = 1
#loop till game is completed
    while True:
        print(a)
        
        #check player input
        #and update
        if a.check_card():
            print('\n\n\n\n\n\n giga chad smiles\n that was the right move, THE SIGMA WAY')
            PlaySound("yay.wav")
        else:
            wrong_attempts += 1
            print('\n\n\n\nbruh this is elementary\nmath total is different')
            print('\n\ngiga chads furrow his brows')
            PlaySound("no.wav")
        input("Press enter to continue:")
        PlaySound("spectronosis.wav",loop=True)
        print(f'TURN {turn_count} HAS ENDED')
        turn_count += 1
        if wrong_attempts == 3:
            gameOver()
            break
            
        #check game is completed
        if a.check_game_finish() == False:
            print('\n\n\n\n\n\n\n\n\n Congrats u are PROBABLY a HuMan')
            fireworks()
            displayCredits()
            break


def splashScreen(filename:str) -> list:
    filename = "ascii_art/"+filename
    with open(filename) as f:
        return f.readlines()

def PlaySound(filename:str, loop:bool=False, asynC:bool = True):
    if filename:
        filename = "music_and_sounds/"+filename
    if asynC:
        if loop:
            winsound.PlaySound(filename, winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
        else:
            winsound.PlaySound(filename, winsound.SND_FILENAME|winsound.SND_ASYNC)
    else:
        if loop:
            winsound.PlaySound(filename, winsound.SND_FILENAME|winsound.SND_LOOP)
        else:
            winsound.PlaySound(filename, winsound.SND_FILENAME)

def main():
    options = [startGame, displayCredits]
    intro()
    try:
        while True:
            displayMenu(options)
            f = getMenuOption(options)
            try:
                f()
            except KeyboardInterrupt:
                pass
            PlaySound("intro.wav")
    except KeyboardInterrupt:
        PlaySound(None)
        input("Exiting game. Goodbye!")
        exit()

main()


        

