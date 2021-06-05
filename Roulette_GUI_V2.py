import random, string
import tkinter as tk
import sys, os, math
from PIL import Image, ImageTk
from functools import partial
from playsound import playsound
import pickle

debug_mode = False # Set this to false to display output to tkinter
#game_surface.fill(color="grey")
root = tk.Tk()
root.configure(bg='#0A3D62')    # Change BG color
root.title('Roulette')
unex = "1020x700"
ex = "1520x700"
root.geometry(unex)
root.update()


# Wheel Positions taken at dimensions of 425x425 length*width
# wheel position, table position
number_positions = {"0": [(227, 369), (22, 90)],
                 "1": [(319, 87), (58, 140)],
                 "2": [(90, 304), (58, 90)],
                 "3": [(279, 353), (58, 40)],
                 "4": [(130, 343), (108, 140)],
                 "5": [(215, 53), (108, 90)],
                 "6": [(58, 208), (108, 40)],
                 "7": [(354, 284), (158, 140)],
                 "8": [(138, 75), (158, 90)],
                 "9": [(372, 182), (158, 40)],
                 "10": [(190, 62), (208, 140)],
                    "11": [(98, 111), (208, 90)],
                    "12": [(324, 323), (208, 40)],
                    "13": [(66, 155), (258, 140)],
                    "14": [(349, 131), (258, 90)],
                    "15": [(174, 366), (258, 40)],
                    "16": [(270, 65), (308, 140)],
                    "17": [(68, 257), (308, 90)],
                    "18": [(371, 233), (308, 40)],
                    "19": [(151, 357), (358, 140)],
                    "20": [(334, 110), (358, 90)],
                    "21": [(108, 327), (358, 40)],
                    "22": [(372, 205), (408, 140)],
                    "23": [(164, 66), (408, 90)],
                    "24": [(240, 60), (408, 40)],
                    "25": [(77, 284), (458, 140)],
                    "26": [(252, 364), (458, 90)],
                    "27": [(60, 181), (458, 40)],
                    "28": [(339, 310), (508, 140)],
                    "29": [(362, 258), (508, 90)],
                    "30": [(117, 91), (508, 40)],
                    "31": [(360, 156), (558, 140)],
                    "32": [(201, 372), (558, 90)],
                    "33": [(290, 77), (558, 40)],
                    "34": [(56, 232), (608, 140)],
                    "35": [(301, 344), (608, 90)],
                    "36": [(81, 131), (608, 40)]
                    }

row_1, row_2, row_3 = [], [], []
red= [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36]
black = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]
for i in range(1, 37, 3):
    row_1.append(str(i))
for i in range(2, 37, 3):
    row_2.append(str(i))
for i in range(3, 37, 3):
    row_3.append(str(i))
#wheel_order = [0, 26, 3, 35, 12, 28, 7, 29, 18, 22, 9, 31, 14, 20, 1, 33, 16, 24, 5, 10, 23, 8, 30, 11, 36, 13, 27,
               #6, 34, 17, 25, 2, 21, 4, 19, 15, 32]

class RouletteWheel:
    def __init__(self):
        self.wheel_path = Image.open(r"roulette_wheel.png")
        self.wheel = ImageTk.PhotoImage(self.wheel_path)
        self.wheel_frame = tk.Frame(root, height=430, width=430)
        self.wheel_canvas = tk.Canvas(self.wheel_frame, width=425, height=425, bg="#006600")
        self.wheel_canvas.create_image(212.5, 215, image=self.wheel)
        self.wheel_frame.place(x=580, y=5)
        self.roulette_ball_path = Image.open(r"roulette_ball.png")
        self.roulette_ball = ImageTk.PhotoImage(self.roulette_ball_path)
        self.roll = self.wheel_canvas.create_text(200, 120, font="times 15 bold", text="")

    def draw_wheel(self):
        self.wheel_canvas.image = self.wheel
        self.wheel_canvas.place(x=1, y=1)

    def draw_roll(self, roll):
        try:
            self.wheel_canvas.delete(self.ball) # delete previous ball if it exists
        except:
            pass
        number_pos = number_positions.get(str(roll))
        self.ball = self.wheel_canvas.create_image(number_pos[0][0], number_pos[0][1], image=self.roulette_ball)
        self.roll = self.wheel_canvas.create_text(220, 120, font="times 15 bold", text="You rolled " + str(roll))


class RouletteTable:
    def __init__(self):
        self.table_path = Image.open(r"roulette_table.png")
        self.table = ImageTk.PhotoImage(self.table_path)
        self.chip_path = Image.open(r"roulette_ball.png")
        self.chip_image = ImageTk.PhotoImage(self.chip_path, (1, 1))
        self.win_ball_path = Image.open(r"win_ball.png")
        self.win_ball_image = ImageTk.PhotoImage(self.win_ball_path, (1, 1))
        self.lose_ball_path = Image.open(r"lose_ball.png")
        self.lose_ball_image = ImageTk.PhotoImage(self.lose_ball_path, (1, 1))
        self.table_frame = tk.Frame(root, height=260, width=710)
        self.table_canvas = tk.Canvas(self.table_frame, width=725, height=425, bg="#006600")
        self.table_canvas.create_image((350, 125), image=self.table)
        self.range_buttons = tk.Button(self.table_canvas,)

    def draw_table(self):
        self.table_canvas.image = self.table
        self.table_canvas.place(x=0, y=0)

    def draw_chips(self, roll):
        number_pos = number_positions.get(str(roll))
        x = number_pos[1][0]
        y = number_pos[1][1]
        self.chip = self.table_canvas.create_image((x, y), image=self.chip_image)

    def draw_win_chip(self, roll, win=True):
        number_pos = number_positions.get(str(roll))
        x = number_pos[1][0]
        y = number_pos[1][1]
        if win == True:
            self.win_chip = self.table_canvas.create_image((x, y), image=self.win_ball_image)
        else:
            self.win_chip = self.table_canvas.create_image((x, y), image=self.lose_ball_image)


class Roulette:
    def __init(self, make_bet):
        self.result = roulette_wheel.wheel_canvas.create_text(300, 450, text="", font="times 15 bold")
        pass

    def format_money(self, m):
        return "${:,.2f}".format(m)

    def win(self, bet):
        game_data.record_money_data(bet, player_won=True)
        data = game_data.get_dicts()
        money_won_label.config(text="Total money won: " + "${:,.2f}".format(data[1]["Won"]))
        net_earnings_label.config(text="Net earnings: " + "${:,.2f}".format(data[1]["Won"] + data[1]["Lost"]))
        if mute_var.get() == 0:
            playsound("ka-ching.mp3", block=False)
        string = "You won: " + self.format_money(bet)
        print(string + "\n")
        self.result = roulette_wheel.wheel_canvas.create_text(220, 150, font='times 15 bold', text=string, justify="center")
        return self.result

    def lose(self, bet):
        game_data.record_money_data(bet, player_won=False)
        data = game_data.get_dicts()
        money_lost_label.config(text="Total money lost: " + "${:,.2f}".format(data[1]["Lost"]))
        net_earnings_label.config(text="Net earnings: " + "${:,.2f}".format(data[1]["Won"] + data[1]["Lost"]))
        if mute_var.get() == 0:
            playsound("lose.mp3", block=False)
        string = "You lost: " + self.format_money(-bet)
        print(string + "\n")
        self.result = roulette_wheel.wheel_canvas.create_text(220, 150, font='times 15 bold', text=string, justify="center")
        return self.result

    def make_bet(self, money):
        try:
            roulette_wheel.wheel_canvas.delete(self.result) # Remove previous text first
            roulette_wheel.wheel_canvas.delete(roulette_wheel.roll)
            roulette_table.table_canvas.delete("all")   # This seemed like a dumb idea at first but it works lmao
            roulette_table.table_canvas.create_image((350, 125), image=roulette_table.table)
        except:
            pass
        try:
            #bet = float(input("How much do you want to bet?"))
            bet = float(bet_var.get().replace(",", ""))
            if bet > money:
                print("ERROR: You do not have enough money for that!")
                return 0
            if bet <= 0:
                print("ERROR: You must bet something!")
                return 0
        except ValueError:
            print("ERROR: Could not read a number from 'Bet'")
            return 0

        money -= bet

        try:
            bet_type = bet_type_var.get()

            if bet_type == "":
                print("ERROR: You did not enter anything into bet type!")
                return 0
            if bet_type == "0" or int(bet_type) > 36:
                print("ERROR: Invalid range!")
                return 0
        except:
            pass
        bet_type.lower().replace(" ", "")   # input correction we can omit spaces because we won't need them later.
        roll = random.randint(0, 36)
        game_data.record_roll_data(roll)
        roulette_wheel.draw_wheel()
        roulette_wheel.draw_roll(roll)
        root.update()

        def display_roll_info(number):
            print("Your bet was $", bet.__round__(2), sep="")
            print("You bet on", bet_type, "and rolled", roll)
            bet_chance = number/37
            pay_rate = 36/number - 1
            print("Odds: ", bet_chance.__round__(4), " or (", number, "/", "37)", sep="")
            print("Payrate: (36/ " + str(number) + ") - 1 = ", pay_rate.__round__(4))

        update_data_labels(roll)
        if bet_type == "even":
            display_roll_info(18)
            for i in range(1, 37):
                if i % 2 == 0:
                    roulette_table.draw_chips(i)
            if roll % 2 == 0 and roll != 0:   # If even and not = 0
                roulette_table.draw_win_chip(roll)
                payout = bet
                self.win(payout)
            else:
                roulette_table.draw_win_chip(roll, False)   # win= False
                payout = -bet
                self.lose(payout)
        elif bet_type == "odd":
            display_roll_info(18)
            for i in range(1, 37):
                if i % 2 != 0:
                    roulette_table.draw_chips(i)
            if roll % 2 != 0 and roll != 0:    # if odd
                roulette_table.draw_win_chip(roll)
                payout = bet
                self.win(payout)
            else:
                roulette_table.draw_win_chip(roll, False)
                payout = -bet
                self.lose(payout)
        # colors

        elif bet_type == "black":
            display_roll_info(18)
            for num in black:
                roulette_table.draw_chips(num)
            if roll in black:
                roulette_table.draw_win_chip(roll)
                payout = bet
                self.win(payout)
            else:
                roulette_table.draw_win_chip(roll, False)
                payout = -bet
                self.lose(payout)
        elif bet_type == "red":
            display_roll_info(18)
            for num in red:
                roulette_table.draw_chips(num)
            if roll in red:
                roulette_table.draw_win_chip(roll)
                payout = bet
                self.win(payout)
            else:
                roulette_table.draw_win_chip(roll, False)
                payout = -bet
                self.lose(payout)
        # specific numbers
        elif bet_type.isdigit():
            if 0 >= int(bet_type) > 36:
                print("ERROR: Invalid number.")
                return 0
            display_roll_info(1)
            roulette_table.draw_chips(int(bet_type))
            if roll == int(bet_type):
                roulette_table.draw_win_chip(roll)
                payout = bet * 36
                self.win(payout)
            else:
                roulette_table.draw_win_chip(roll, False)
                payout = -bet
                self.lose(payout)
        # Inequalities
        elif bet_type[0] == "<":   # input should be something like < 5
            fixed_str = bet_type.replace(" ", "")   # get rid of any spaces
            number = int(fixed_str[1:].strip(string.punctuation).strip(string.ascii_letters))

            if 0 >= number > 36:
                print("Invalid number.")
                return 0
            display_roll_info(number)
            for i in range(1, number):
                roulette_table.draw_chips(i)
            pay_rate = 36/number - 1

            if number >= roll != 0:   # if number chosen is less than the roll
                roulette_table.draw_win_chip(roll)
                payout = bet * pay_rate
                self.win(payout)
            else:
                roulette_table.draw_win_chip(roll, False)
                payout = -bet
                self.lose(payout)

        elif bet_type[0] == ">":
            fixed_str = bet_type.replace(" ", "")  # get rid of any spaces
            number = int(fixed_str[1:].strip(string.punctuation).strip(string.ascii_letters)) # strip any typos
            if 0 >= number > 36:
                print("ERROR: Invalid number.")
                return 0
            for i in range(number, 37):
                roulette_table.draw_chips(i)
            bet_chance = (37 - number) / 36   # 36 - number here because we're dealing with the complement
            pay_rate = 36 / (36 - number) - 1
            print("Your bet was $", bet.__round__(2), sep="")
            print("You bet on", bet_type, "and rolled", roll)
            print("Odds: ", bet_chance.__round__(4), " or (37-", number, ")/36", sep="")
            print("Payrate: (36/ (36 -" + str(number) + ") - 1 = ", pay_rate.__round__(4))   # This is unique so we can't use the function here
            if number <= roll != 0:  # if number chosen is less than the roll
                roulette_table.draw_win_chip(roll)
                payout = bet * pay_rate
                self.win(payout)
            else:
                roulette_table.draw_win_chip(roll, False)
                payout = -bet
                self.lose(payout)

        # List
        elif bet_type[0] == "[":
            new_str = bet_type.strip(string.punctuation).strip(string.ascii_letters)   # input correction
            num_list = new_str.split(",")
            new_list = list(set(num_list))  # remove dupes
            for num in new_list:
                if 0 >= int(num) > 36:
                    new_list.remove(num)
            #print("newlist:", new_list)  # No duplicates
            number = len(new_list)      # Number will refer to the input variable that we need to calculate the payout.
            #print("number", number)
            try:
                pay_rate = (36 / number) - 1
            except ZeroDivisionError:
                print("ERROR: Tried to divide by zero! Did you enter anything into the list?")
                return 0
            display_roll_info(number)
            #print(new_list)
            for num in new_list:
                roulette_table.draw_chips(num)
            if str(roll) in new_list:
                roulette_table.draw_win_chip(roll)
                payout = bet * pay_rate
                self.win(payout)
            else:
                roulette_table.draw_win_chip(roll, False)
                payout = -bet
                self.lose(payout)

        # Range
        elif bet_type[0] == "(":
            new_str = bet_type.strip(string.punctuation).strip(string.ascii_letters).replace(" ", "")  # input correction
            range_list = new_str.split("-")
            num_list = []
            if len(range_list) != 2:
                print("ERROR: Invalid input. It should look something like (1-4)")
                return 0
            else:
                for num in range(int(range_list[0]), int(range_list[1]) + 1):
                    if 0 < num <= 36:
                        num_list.append(int(num))
                if len(num_list) < 1:
                    print("Error: No valid values entered in the range!")
                    return 0
            number = len(num_list)  # Number will refer to the input variable that we need to calculate the payout.
            display_roll_info(number)
            for num in num_list:
                roulette_table.draw_chips(num)
            pay_rate = (36 / number) - 1

            if roll in num_list:
                roulette_table.draw_win_chip(roll)
                payout = bet * pay_rate
                self.win(payout)
            else:
                roulette_table.draw_win_chip(roll, False)
                payout = -bet
                self.lose(payout)
        else:
            print("ERROR: Your input was invalid!")
            return 0
        return payout


class GameData:
    def load_data(self):
        if not os.path.exists("Game_data"):     # Create a new, empty dictionary for new players
            print("Created game_data file")
            self.file = open("Game_data", "wb+")
            rolls_dict = {}
            money_dict = {"Won": 0, "Lost": 0}
            for i in range(37):
                rolls_dict[str(i)] = 0
            dicts = [rolls_dict, money_dict]
            pickle.dump(dicts, self.file)
            self.file.close()   # Do not forget to close after writing to file
        else:
            print("Loaded game_data file")
            self.file = open("Game_data", "rb")
            pickle.load(self.file)
            self.file.close()

    def record_roll_data(self, number):
        self.file = open("Game_data", "rb")
        dicts = pickle.load(self.file)
        dicts[0][str(number)] += 1

        self.file = open("Game_data", "wb")
        pickle.dump(dicts, self.file)
        #print(dicts)
        self.file.close()

    def record_money_data(self, payout, player_won):
        self.file = open("Game_data", "rb")
        dicts = pickle.load(self.file)
        self.file = open("Game_data", "wb")
        if player_won:
            dicts[1]["Won"] += payout
        else:
            dicts[1]["Lost"] += payout
        dicts[1]["Won"] = dicts[1]["Won"].__round__(2)
        dicts[1]["Lost"] = dicts[1]["Lost"].__round__(2)
        pickle.dump(dicts, self.file)
        self.file.close()

    def get_dicts(self):    # returns the dictionaries
        self.file = open("Game_data", "rb")
        dicts = pickle.load(self.file)
        return dicts



# Note to self: TextRedirector() may be useful in the future.
# Source: https://stackoverflow.com/questions/12351786/how-to-redirect-print-statements-to-tkinter-text-widget
# This redirects text from console to the the text_box widget
class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

expanded = False

def show_more():    # Hides and expands the window when button is pressed
    global expanded
    if not expanded:
        root.geometry(ex)    # expanded
        expanded = True
    else:
        root.geometry(unex)    # default
        expanded = False

# Initialize stuff here
roulette_wheel = RouletteWheel()
roulette_table = RouletteTable()
game = Roulette()
game_data = GameData()
game_data.load_data()

roulette_wheel.draw_wheel()
roulette_table.draw_table()


text_box = tk.Text(root, bg="#A4B0BD", height=22, width=70, font=("times", 12, "bold"))
text_box.config(state="disabled")
if debug_mode == False:
    sys.stdout = TextRedirector(text_box)   # Redirect console output to text widget
    sys.stderr = TextRedirector(text_box)   # Redirect error messages to text widget in case user somehow breaks the game

# Bet frame
bet_frame = tk.Frame(root, bg="#A4B0BD", height=140, width=220)
dev_label = tk.Label(bet_frame, text='Made by Hoswoo', font=('times', 10, 'bold'), bg="#A4B0BD", fg="darkblue",
                     anchor="w")  # Hoswoo

money = 100000
money_var = tk.StringVar()
money_var.set("${:,.2f}".format(money))     # Formatting money to look nice




money_text_label = tk.Label(bet_frame, text="Money:", bg="#A4B0BD")
money_label = tk.Label(bet_frame, textvariable=money_var, bg="#A4B0BD")

bet_var = tk.StringVar()
bet_var.set("0")
bet_label = tk.Label(bet_frame, text="Bet:$", bg="#A4B0BD")
bet_entry = tk.Entry(bet_frame, textvariable=bet_var, width=13)

bet_type_var = tk.StringVar()
bet_type_label = tk.Label(bet_frame, text="Bet Type:", bg="#A4B0BD")
bet_type_entry = tk.Entry(bet_frame, textvariable=bet_type_var, width=8)
check_var = tk.BooleanVar()
mute_var = tk.BooleanVar()
quick_bet_check_button = tk.Checkbutton(bet_frame, text="Quick bet", bg="#A4B0BD", variable=check_var, onvalue=1,
                                        offvalue=0)
mute_check_button = tk.Checkbutton(bet_frame, text="Mute", bg="#A4B0BD", variable=mute_var, onvalue=1,
                                        offvalue=0)
check_var.set(1)
quick_bet_check_button.place(x=2, y=100)
mute_check_button.place(x=2, y=118)

def set_bet_type(bet_type):
    bet_type_var.set(bet_type)
    if check_var.get() == 1:    # quick bet if check button is checked
        play()

# Table stuff
num_button = []
for num in range(37):
    if num in black:
        num_button.append(tk.Button(roulette_table.table_frame, text=num, bg="#000000", fg="white", height=1, width=2,
                                    font=("times", 12, "bold"), command=partial(set_bet_type, num)))
    else:
        num_button.append(tk.Button(roulette_table.table_frame, text=num, bg="#FF0000", fg="white", height=1, width=2,
                                    font=("times", 12, "bold"), command=partial(set_bet_type, num)))

for i in range(len(row_1)): # placement on the table frame
    x_pos = 69 + i * 50
    num_button[int(row_1[i])].place(x=x_pos, y=102)
for i in range(len(row_2)):
    x_pos = 69 + i * 50
    num_button[int(row_2[i])].place(x=x_pos, y=52)
for i in range(len(row_3)):
    x_pos = 69 + i * 50
    num_button[int(row_3[i])].place(x=x_pos, y=2)
row_1_button = tk.Button(roulette_table.table_frame, text="2:1", bg="#006600", fg="white", height=1, width=2,
                         font=("times", 18, "bold"), command=partial(set_bet_type, "[" + ",".join(row_1) + "]"))
row_2_button = tk.Button(roulette_table.table_frame, text="2:1", bg="#006600", fg="white", height=1, width=2,
                         font=("times", 18, "bold"), command=partial(set_bet_type, "[" + ",".join(row_2) + "]"))
row_3_button = tk.Button(roulette_table.table_frame, text="2:1", bg="#006600", fg="white", height=1, width=2,
                         font=("times", 18, "bold"), command=partial(set_bet_type, "[" + ",".join(row_3) + "]"))
row_1_button.place(x=655, y=102)
row_2_button.place(x=655, y=52)
row_3_button.place(x=655, y=2)

range_1_to_12_button = tk.Button(roulette_table.table_frame, text="(1 to 12)", bg="#006600", fg="white", height=1,
                                 width=13, font=("times", 18, "bold"), command=partial(set_bet_type, "(1-12)"))
range_13_to_24_button = tk.Button(roulette_table.table_frame, text="(13 to 24)", bg="#006600", fg="white", height=1,
                                  width=13, font=("times", 18, "bold"), command=partial(set_bet_type, "(13-24)"))
range_25_to_36_button = tk.Button(roulette_table.table_frame, text="(25 to 36)", bg="#006600", fg="white", height=1,
                                  width=13, font=("times", 18, "bold"), command=partial(set_bet_type, "(25-36)"))
range_1_to_12_button.place(x=52, y=152)
range_13_to_24_button.place(x=252, y=152)
range_25_to_36_button.place(x=452, y=152)

range_1_to_18_button = tk.Button(roulette_table.table_frame, text="(1 to 18)", bg="#006600", fg="white", height=1,
                                 width=6, font=("times", 18, "bold"), command=partial(set_bet_type, "(1-18)"))
even_button = tk.Button(roulette_table.table_frame, text="Even", bg="#006600", fg="white", height=1, width=6,
                        font=("times", 18, "bold"), command=partial(set_bet_type, "even"))
red_button = tk.Button(roulette_table.table_frame, text="Red", bg="#FF0000", fg="white", height=1, width=6,
                       font=("times", 18, "bold"), command=partial(set_bet_type, "red"))
black_button = tk.Button(roulette_table.table_frame, text="Black", bg="#000000", fg="white", height=1, width=6,
                         font=("times", 18, "bold"), command=partial(set_bet_type, "black"))
odd_button = tk.Button(roulette_table.table_frame, text="Odd", bg="#006600", fg="white", height=1, width=6,
                       font=("times", 18, "bold"), command=partial(set_bet_type, "odd"))
range_19_to_36_button = tk.Button(roulette_table.table_frame, text="(19 to 36)", bg="#006600", fg="white", height=1,
                                  width=6, font=("times", 18, "bold"), command=partial(set_bet_type, "(19-36)"))
range_1_to_18_button.place(x=52, y=202)
even_button.place(x=152, y=202)
red_button.place(x=252, y=202)
black_button.place(x=352, y=202)
odd_button.place(x=452, y=202)
range_19_to_36_button.place(x=552, y=202)

# Show more frame stuff
show_more_button = tk.Button(bet_frame, text="Show More", command=show_more, bg="#2C3335", fg="#7ddeff", width=10)
show_more_frame = tk.Frame(root, bg="#A4B0BD", height=525, width=480)

data_list = []
gap = 29
offset_x = 25
offset_y = 30
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]
data = game_data.get_dicts()
roll_history_label = tk.Label(show_more_frame, text="Roll history", font=("times", 15, "bold"), bg="#A4B0BD")
roll_history_label.place(x=185, y=3)
offset_x = 25
# Making all labels in show_more
num_list = []
for i in range(37):
    num_list.append(
        tk.Label(show_more_frame, text=str(i) + "| " + str(data[0][str(i)]), fg="white", font=("times", 15, "bold"),
                 bg="#A4B0BD"))
    if i in red:
        num_list[i].config(bg="#FF0000")
    else:
        num_list[i].config(bg="black")
num_list[0].config(bg="#006600")
# place them on show_more frame
for i in range(1, len(data[0])):
    if i <= 6:
        num_list[i].place(x=0 + offset_x, y=2 + gap * i - gap + offset_y)
    elif i <= 12:
        num_list[i].place(x=75 + offset_x, y=2 + gap * i - gap * 7 + offset_y)
    elif i <= 18:
        num_list[i].place(x=150 + offset_x, y=2 + gap * i - gap * 13 + offset_y)
    elif i <= 24:
        num_list[i].place(x=225 + offset_x, y=2 + gap * i - gap * 19 + offset_y)
    elif i <= 30:
        num_list[i].place(x=300 + offset_x, y=2 + gap * i - gap * 25 + offset_y)
    else:
        num_list[i].place(x=375 + offset_x, y=2 + gap * i - gap * 31 + offset_y)
num_list[0].place(x=offset_x, y=3)

money_won_label = tk.Label(show_more_frame, text="Total money won: " + "${:,.2f}".format(float(data[1]["Won"])), fg="Black",
                           font=("times", 15, "bold"), bg="#A4B0BD")

money_lost_label = tk.Label(show_more_frame, text="Total money lost: " + "${:,.2f}".format(float(data[1]["Lost"])), fg="Black",
                           font=("times", 15, "bold"), bg="#A4B0BD")

net_earnings_label = tk.Label(show_more_frame, text="Net earnings: " + "${:,.2f}".format(data[1]["Won"] + data[1]
                              ["Lost"]), fg="Black", font=("times", 15, "bold"), bg="#A4B0BD")

money_won_label.place(x=offset_x, y=215)
money_lost_label.place(x=offset_x, y=250)
net_earnings_label.place(x=offset_x, y=285)
# update every time we roll
def update_data_labels(roll):
    data = game_data.get_dicts()
    num_list[roll].config(text=str(roll) + "| " + str(data[0][str(roll)]))
    # This needed to be handled in the actual game function. Leaving it here for reference
    #money_won_label.config(text="Total money won: " + "${:,.2f}".format(data[1]["Won"]))
    #money_lost_label.config(text="Total money lost: " + "${:,.2f}".format(data[1]["Lost"]))
show_more_frame.place(x=1020, y=5)
tutorial_label = tk.Label(show_more_frame, text="How to play:\n"
                                     "Type in a bet amount, then click the buttons on the table to make a bet."
                                     "\nYou can also type your bets into bet type. \n\nUse the random bet button to see what kind of bets you can make!"
                                     "\n\nQuick bet will allow you to automatically roll after clicking a button."
                                     "\nWhen it's off, you will have to click roll after placing your bet."
                                     "\n\nIn Roulette, zero will not count as an even number."
                          , justify="left", bg='#A4B0BD', font=("times", 12, "normal"))


def play():
    converted_money = money_var.get().replace("$", "").replace(",", "")  # Since we formatted money earlier we need to remove $ and commas from string
    payout = game.make_bet(float(converted_money))
    money_var.set("${:,.2f}".format(float(converted_money) + payout))    # Convert new value back to money format
    text_box.see("end")


def random_bet():
    money = float(money_var.get().replace(",", "").replace("$", ""))
    #max_bet = float(money_var.get().replace(",", "").replace("$", "")) / 2  # /2 will ensure that the max_bet is never over half of the money left
    max_bet = 5000
    if money < 5000:
        max_bet = money / 2
    bet_var.set(random.uniform(0, max_bet).__round__(2)) # random.uniform randomizes a range with floats

    decision_maker_val = random.random().__round__(2)
    # print("Decision value: ", decision_maker_val)  # Turn this on if you ever need to debug this again
    if decision_maker_val < .25:
        if decision_maker_val < .03125:  # This is set to a low probability because we do not want to bet on specific numbers too often.
            bet_var.set((random.uniform(0, max_bet)/2).__round__(2))  # Lower bet because potential money loss is high
            bet_type_var.set(str(random.randint(1, 36)))
        elif decision_maker_val < .125:
            bet_type_var.set("(" + str(random.randint(1, 18)) + "-" + str(random.randint(18, 36)) + ")")
        else:
            rand_list = [str(random.randint(1, 36)) for i in range(random.randint(4, 30))]  # get 4 to 30 random integers from 1 through 36
            rand_list = list(set(rand_list))    # remove duplicates
            bet_type_var.set("[" + ",".join(rand_list) + "]")
    elif decision_maker_val < .5:   #interval = 0.625
        if decision_maker_val < .3125:
            bet_type_var.set("black")
        elif decision_maker_val < .375:
            bet_type_var.set("red")
        elif decision_maker_val < .4375:
            bet_type_var.set("even")
        else:
            bet_type_var.set("odd")
    elif decision_maker_val < .75:  # interval = .083333333
        return_str = "["
        if decision_maker_val < .583333333:
            return_str += ",".join(row_1)
        elif decision_maker_val < .66666666:
            return_str += ",".join(row_2)
        else:
            return_str += ",".join(row_3)
        return_str += "]"
        bet_type_var.set(return_str)
    elif decision_maker_val < .875:
        if decision_maker_val < .8125:
            bet = str(random.randint(5, 35))
            bet_type_var.set("<" + bet)
        else:
            bet = str(random.randint(2, 31))
            bet_type_var.set(">" + bet)
    else:
        if decision_maker_val < .9375:
            return_str = "(1-18)"
            bet_type_var.set(return_str)
        else:
            return_str = "(19-36)"
            bet_type_var.set(return_str)
    if check_var.get() == 1:  # quick play
        play()

random_bet_button = tk.Button(bet_frame, text="Random bet", command=random_bet, bg="#2C3335", fg="#7ddeff", width=10)
roll_button = tk.Button(bet_frame, text="Roll", command=play, width=10, bg="#2C3335", fg="#7ddeff")
money = float(money_var.get().replace(",", "").replace("$", ""))




roulette_table.table_frame.place(x=5, y=435)
bet_frame.place(x=720, y=443)
dev_label.place(x=0, y=0)
text_box.place(x=5, y=5)  # Manually placing these is stupid but whatever
money_text_label.place(x=1, y=25)
money_label.place(x=45, y=25)
bet_label.place(x=1, y=50)
bet_entry.place(x=30, y=50)
bet_type_label.place(x=1, y=75)
bet_type_entry.place(x=60, y=75)
roll_button.place(x=118, y=25)
random_bet_button.place(x=118, y=55)
show_more_button.place(x=118, y=85)
tutorial_label.place(x=25, y=330)

root.mainloop()


