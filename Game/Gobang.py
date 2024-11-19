from tkinter import *
import tkinter.messagebox as mb
from PIL import ImageTk
import math

class Menu(Tk):
    def __init__(self):
        super().__init__()
        self.start_of_the_prog()

    def start_of_the_prog(self):                # отрисовка меню и всех кнопок
        self.wm_iconphoto(False, ImageTk.PhotoImage(file="Gobang/go-ban_icon.png", master=self))
        self.title('Го-Бан')
        self.configure(bg="#c29b6b")
        w = 800
        h = 450
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False, False)
        self.change_lbl = False
        self.image = ImageTk.PhotoImage(file="Gobang/go-ban.png", master=self)
        self.lbl_front = Label(self, image=self.image, bg="#c29b6b", font='Areal 14', justify="left",
                               wraplength=525)
        self.lbl_front.place(x=0, y=-15)
        lbl_name = Label(self, bg="#c29b6b", text="Игра Го-Бан", font='Arial 24')
        lbl_name.place(x=545, y=40)
        self.btn_startgame = Button(self, bg="#c29b6b", text="Начать игру", font="Arial 14", command=self.new_game)
        self.btn_startgame.place(x=583, y=240)
        self.btn_rule = Button(self, bg="#c29b6b", text="Правила игры", font="Arial 14", command=self.changing_lbl)
        self.btn_rule.place(x=575, y=285)
        self.btn_out = Button(self, bg="#c29b6b", text="Выход", font="Arial 14", command=lambda: exit(0))
        self.btn_out.place(x=602, y=330)

    def changing_lbl(self):         # смена правил игры на иконку го и наоборот
        if self.change_lbl:
            self.lbl_front.configure(image=self.image, text="")
            self.change_lbl = False
            return
        if not self.change_lbl:
            with open('Gobang/rules.txt', 'r', encoding='utf8') as file:
                rules = file.read()
                file.close()
            self.lbl_front.configure(image="", text=rules)
            self.change_lbl = True
            return

    def new_game(self):             # кнопка НАЧАТЬ ИГРУ
        self.btn_guest = Button(self, bg="#c29b6b", text="Продолжить как гость", font="Arial 14", command=
        self.start_game_without_user)
        self.btn_enter = Button(self, bg="#c29b6b", text="Войти в профиль", font="Arial 14", command=self.enter)
        self.btn_regist = Button(self, bg="#c29b6b", text="Зарегистрироваться", font="Arial 14",
                                 command=self.register)
        self.btn_back = Button(self, bg="#c29b6b", text="Назад", font="Arial 14", command=self.back)
        self.btn_guest.place(x=542, y=240)
        self.btn_enter.place(x=565, y=285)
        self.btn_regist.place(x=550, y=330)
        self.btn_back.place(x=610, y=375)

    def back(self):                             # кнопка НАЗАД
        self.btn_guest.destroy()
        self.btn_enter.destroy()
        self.btn_regist.destroy()
        self.btn_back.destroy()

    def start_game_without_user(self):          # кнопка ПРОДОЛЖИТЬ КАК ГОСТЬ
        self.withdraw()
        with open("Gobang/User.txt", 'r+') as f:
            f.truncate()
        Gobang(self)
        self.deiconify()

    def overwrite_user(self, username):
        with open("Gobang/User.txt", "w+") as f2:
            f2.truncate()
            f2.write(username)

    def CreateNewUser(self, username, password, password_again):  # проверка на правильное заполнение полей в окне регистрации
        if username == '' or password == '' or password_again == '':
            msg = 'Заполните все поля'
            mb.showerror("Ошибка", msg)
        else:
            try:
                f1 = open('Gobang/Users.txt', 'r+')
                text = f1.read().split()
                for i in text:
                    if username == i.split(':')[0]:
                        msg = 'Имя пользователя уже существует'
                        mb.showerror("Ошибка", msg)
                        return
                else:
                    if password != password_again:
                        msg = 'Пароли не совпадают'
                        mb.showerror("Ошибка", msg)
                        return
                    else:
                        f1.write(username + ':' + password + ':' + '0' + '\n')
                        self.overwrite_user(username)
                        f1.close()
                        self.window_Reg.destroy()
                        self.withdraw()
                        Gobang(self)
                        self.deiconify()
                        return
            except:
                f1 = open('Gobang/Users.txt', 'w')
                if password != password_again:
                    msg = 'Пароли не совпадают'
                    mb.showerror("Ошибка", msg)
                    return
                else:
                    f1.write(username + ':' + password + ':' + '0' + '\n')
                    self.overwrite_user(username)
                    f1.close()
                    self.window_Reg.destroy()
                    self.back()
                    self.withdraw()
                    Gobang(self)
                    self.deiconify()
                return

    def register(self):                     # отрисовка окна регистрации
        self.window_Reg = Tk()
        self.window_Reg.title('Регистрация')
        self.window_Reg.geometry('300x300')
        self.window_Reg.eval('tk::PlaceWindow . center')
        username_label = Label(self.window_Reg, text='Имя пользователя', )
        username_entry = Entry(self.window_Reg)
        password_label = Label(self.window_Reg, text='Пароль')
        password_entry = Entry(self.window_Reg)
        password_label_confirm = Label(self.window_Reg, text='Повторите пароль')
        password_entry_confirm = Entry(self.window_Reg)
        send_btn = Button(self.window_Reg, text='Зарегистрироваться', command=lambda:
        self.CreateNewUser(username_entry.get(), password_entry.get(), password_entry_confirm.get(), ))
        username_label.pack(padx=10, pady=8)
        username_entry.pack(padx=10, pady=8)
        password_label.pack(padx=10, pady=8)
        password_entry.pack(padx=10, pady=8)
        password_label_confirm.pack(padx=10, pady=8)
        password_entry_confirm.pack(padx=10, pady=8)
        send_btn.pack(padx=10, pady=8)
        self.window_Reg.mainloop()

    def CheckExist(self, username, password):           # проверка на правильность заполнения полей в окне входа
        if username == '' or password == '':
            msg = 'Заполните все поля'
            mb.showerror("Ошибка", msg)
        else:
            f1 = open('Gobang/Users.txt', 'r')
            text = f1.read().split()
            for i in text:
                if i.split(':')[0] == username:
                    if password == i.split(':')[1]:
                        self.overwrite_user(username)
                        f1.close()
                        self.window_enter.destroy()
                        self.withdraw()
                        Gobang(self)
                        self.deiconify()
                        return
                    else:
                        msg = 'Пароль не совпадает'
                        mb.showerror("Ошибка", msg)
                        return
            msg = 'Такой пользователь не зарегестрирован'
            mb.showerror("Ошибка", msg)
            self.window_enter.destroy()
            self.register()
            return

    def enter(self):                # функция отрисовки окна входа
        self.window_enter = Tk()
        self.window_enter.title('Вход')
        self.window_enter.geometry('300x250')
        self.window_enter.eval('tk::PlaceWindow . center')
        username_label = Label(self.window_enter, text='Имя пользователя', )
        username_entry = Entry(self.window_enter)
        password_label = Label(self.window_enter, text='Пароль')
        password_entry = Entry(self.window_enter)
        send_btn = Button(self.window_enter, text='Войти', command=lambda:
        self.CheckExist(username_entry.get(), password_entry.get()))

        username_label.pack(padx=10, pady=8)
        username_entry.pack(padx=10, pady=8)
        password_label.pack(padx=10, pady=8)
        password_entry.pack(padx=10, pady=8)
        send_btn.pack(padx=10, pady=8)

        self.window_enter.mainloop()


class Gobang(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.reload()               # запуски игры

    def reload(self):            # запуск/перезагрузка игры
        self.wm_iconphoto(False, ImageTk.PhotoImage(file="Gobang/go-ban_icon.png"))
        self.title('Го-Бан')
        self.configure(bg="#c29b6b")
        w = 1050
        h = 680
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False, False)
        self.flag_is_first_part_game = True     # флаг этапа игры (первый этап - расставление, второй - передвижение)
        self.sequence_weights = {2: 200, 3: 1000, 4: 5000, 5: 100000}
        self.choice = False            # флаг, выбрана ли фишка во втором этапе
        self.count_figur = 0     # счетчик поставленных фишек для перехода во второй этап игры
        self.field = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"],
                      ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"],
                      ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"],
                      ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"],
                      ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"],  # поле игры ("-" и "|" - ограничение поля, 0 - пустое поле, 1 - игрок, 2 - компьютер)
                      ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"],
                      ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"],
                      ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]
        self.weight_matrix = [[1, 2, 3, 4, 4, 3, 2, 1],
                              [2, 3, 4, 5, 5, 4, 3, 2],
                              [3, 4, 5, 6, 6, 5, 4, 3],
                              [4, 5, 6, 7, 7, 6, 5, 4],
                              [4, 5, 6, 7, 7, 6, 5, 4],
                              [3, 4, 5, 6, 6, 5, 4, 3],
                              [2, 3, 4, 5, 5, 4, 3, 2],
                              [1, 2, 3, 4, 4, 3, 2, 1]]
        self.image1 = ImageTk.PhotoImage(file="Gobang/black.png")
        self.image2 = ImageTk.PhotoImage(file="Gobang/white.png")
        self.image3 = ImageTk.PhotoImage(file="Gobang/empty.png")
        image_settings = ImageTk.PhotoImage(file="Gobang/question_mark.png")
        self.button_help = Button(self, bg="#c29b6b", image=image_settings, command=self.rules)
        self.button_help.place(x=1000, y=0)
        lbl_2 = Label(self, bg="#c29b6b", text='<--ИГРОК')
        lbl_1 = Label(self, bg="#c29b6b", text='<--ИИ')
        lbl_2.place(x=795, y=38)
        lbl_1.place(x=940, y=38)
        panel1 = Label(self, bg="#c29b6b", image=self.image1)
        panel2 = Label(self, bg="#c29b6b", image=self.image2)
        panel1.place(x=860, y=0)
        panel2.place(x=715, y=0)
        self.lbl_part = Label(self, bg="#c29b6b", text="Сейчас идёт ПЕРВЫЙ этап игры", font='Areal 12')
        self.lbl_part.place(x=720, y=120)
        self.lbl_popup = Label(self, bg="#c29b6b", text='', font='Areal 12', justify='left', wraplength=278)
        self.lbl_popup.place(x=720, y=175)
        self.b = []               # заготовка поля из матрицы кнопок для визуала
        for i in range(10):
            self.b.append(i)
            self.b[i] = []
            for j in range(10):
                self.b[i].append(j)
                if (0 < i < 9) and (0 < j < 9):         # выводим только поле размером 8х8 с сохранением координат 9х9
                    self.b[i][j] = Button(self, height=80, width=80, image=self.image3,
                                          command=lambda row=i, col=j: self.click(row, col))
                    self.b[i][j].grid(row=i, column=j)
        self.colour_change()
        self.wait_window(self)

    def rules(self):               # окно с правилами во время игры
        self.button_help.configure(command="")
        rule = Toplevel(self)
        rule.wm_iconphoto(False, ImageTk.PhotoImage(file="Gobang/icon.png"))
        rule.title("Правила игры")
        rule.geometry("462x330")
        rule.configure(bg="#c29b6b")
        rule.resizable(False, False)
        with open('Gobang/rules.txt', 'r', encoding='utf8') as file:
            rules = file.read()
        lbl = Label(rule, bg="#c29b6b", text=rules, font='Areal 12', justify="left", wraplength=460)
        lbl.place(x=0, y=0)

        def quit_window():
            self.button_help.config(command=self.rules)
            rule.destroy()
        rule.protocol("WM_DELETE_WINDOW", quit_window)

    def colour_change(self):        # перекраска поля
        for i in range(1, 9):
            for j in range(1, 9):
                if (i + j) % 2 == 0:
                    self.b[i][j].configure(bg="#dbbb8a")
                else:
                    self.b[i][j].configure(bg="#b38349")
        return

    def change_part(self):              # смена игры из первой части во второую
        if self.count_figur == 12:
            self.count_figur = 0
            self.flag_is_first_part_game = False
            self.lbl_part.configure(text='Сейчас идёт ВТОРОЙ этап игры')
        return

    def click(self, row, col):         # обработчик кнопок поля
        try:
            self.lbl_popup.configure(text='')
            if self.flag_is_first_part_game:  # если идёт первый этап игры
                self.colour_change()
                count = 0
                if self.field[row][col] == 0:
                    self.b[row][col].configure(image=self.image2)
                    self.field[row][col] = 1
                    count += 1
                    if self.is_game_over(True):
                        win = mb.askquestion('Игра окончена', f'  Вы выиграли!\n Начать новую игру?')
                        self.reload() if win == 'yes' else self.destroy()
                if count == 1:
                    count = 0
                    self.computer_move(2, 1)
                    if self.is_game_over(False):
                        win = mb.askquestion('Игра окончена', f'  Вы проиграли!\n Начать новую игру?')
                        self.reload() if win == 'yes' else self.destroy()
                    self.count_figur += 1
                    self.change_part()
            else:                                       # если второй этап игры
                if not self.choice:                     # выбор своей фишки для хода ею
                    if self.field[row][col + 1] != 0 and self.field[row][col - 1] != 0 \
                            and self.field[row + 1][col] != 0 and self.field[row - 1][col] != 0 \
                            and self.field[row][col] == 1:
                        self.lbl_popup.configure(text='Выбирите другую свободную фишку')
                    elif self.field[row][col] == 2:
                        self.lbl_popup.configure(text='Это фишка противника.\nВыбирете свою фишку')
                    elif self.field[row][col] == 1:
                        self.colour_change()
                        self.row2, self.col2 = row, col
                        self.b[row][col].configure(bg='yellow')
                        self.choice = True
                elif self.row2 == row and self.col2 == col:  # отменить выбранную фишку
                    self.choice = False
                    self.colour_change()
                else:  # ход выбранной фишкой
                    if (abs(row - self.row2) + abs(col - self.col2) == 1) and self.field[row][col] == 0:
                        self.b[row][col].configure(image=self.image2)
                        self.field[row][col] = 1
                        self.b[self.row2][self.col2].configure(image=self.image3)
                        self.colour_change()
                        self.field[self.row2][self.col2] = 0
                        self.choice = False
                        if self.is_game_over(True):
                            win = mb.askquestion('Игра окончена', f'  Вы выиграли!\n Начать новую игру?')
                            self.reload() if win == 'yes' else self.destroy()
                        self.computer_move(2, 1)
                        if self.is_game_over(False):
                            win = mb.askquestion('Игра окончена', f'  Вы проиграли!\n Начать новую игру?')
                            self.reload() if win == 'yes' else self.destroy()
            return
        except Exception as e:
            pass

    def get_possible_move_part_1(self, maximizing_player, computer_symbol, player_symbol): # возможные ходы компа часть 1
        lines = self.find_all_lines(maximizing_player)
        moves = []
        if maximizing_player:
            symbol = player_symbol
        else:
            symbol = computer_symbol
        for item in lines:
            row1, col1 = item[0]
            row2, col2 = item[1]
            lengh = len(item)
            if self.field[row1][col1] == symbol:
                if col2 - col1 == 1 and row1 == row2:
                    if self.field[row1][col1 - 1] == 0 and not((row1, col1 - 1) in moves):
                        moves.append((row1, col1 - 1))
                    if self.field[row1][col1 + lengh] == 0 and not((row1, col1 + lengh) in moves):
                        moves.append((row1, col1 + lengh))
                elif row2 - row1 == 1 and col1 == col2:
                    if self.field[row1 - 1][col1] == 0 and not((row1 - 1, col1) in moves):
                        moves.append((row1 - 1, col1))
                    if self.field[row1 + lengh][col1] == 0 and not((row1 + lengh, col1) in moves):
                        moves.append((row1 + lengh, col1))
                elif row2 - row1 == 1 and col2 - col1 == 1:
                    if self.field[row1 - 1][col1 - 1] == 0 and not((row1 - 1, col1 - 1) in moves):
                        moves.append((row1 - 1, col1 - 1))
                    if self.field[row1 + lengh][col1 + lengh] == 0 and not((row1 + lengh, col1 + lengh) in moves):
                        moves.append((row1 + lengh, col1 + lengh))
                else:
                    if self.field[row1 - 1][col1 + 1] == 0 and not((row1 - 1, col1 + 1) in moves):
                        moves.append((row1 - 1, col1 + 1))
                    if self.field[row1 + lengh][col1 - lengh] == 0 and not((row1 + lengh, col1 - lengh) in moves):
                        moves.append((row1 + lengh, col1 - lengh))
        if not moves:
            for row in range(1, 9):
                for col in range(1, 9):
                    if self.field[row - 1][col] == self.field[row + 1][col] == symbol and self.field[row][col] == 0:
                        moves.append((row, col))
                    if self.field[row][col - 1] == self.field[row][col + 1] == symbol and self.field[row][col] == 0:
                        moves.append((row, col))
                    if self.field[row - 1][col - 1] == self.field[row + 1][col + 1] == symbol and self.field[row][col] == 0:
                        moves.append((row, col))
                    if self.field[row - 1][col + 1] == self.field[row + 1][col - 1] == symbol and self.field[row][col] == 0:
                        moves.append((row, col))
                    if not moves:
                        if row < 5 and col < 5 and self.field[row][col] == symbol:
                            if self.field[5][col] == 0 and not((5, col) in moves):
                                moves.append((5, col))
                            if self.field[row][5] == 0 and not((row, 5) in moves):
                                moves.append((row, 5))
                            if self.field[5][5] == 0 and row == col == 4:
                                moves.append((5, 5))
                            elif self.field[row + 2][col + 2] == 0 and not((row + 2, col + 2) in moves):
                                moves.append((row + 2, col + 2))
                        if row < 5 <= col and self.field[row][col] == symbol:
                            if self.field[5][col] == 0 and not((5, col) in moves):
                                moves.append((5, col))
                            if self.field[row][4] == 0 and not((row, 4) in moves):
                                moves.append((row, 4))
                            if self.field[5][4] == 0 and row == 4 and col == 5:
                                moves.append((5, 4))
                            elif self.field[row + 2][col - 2] == 0 and not((row + 2, col - 2) in moves):
                                moves.append((row + 2, col - 2))
                        if row >= 5 > col and self.field[row][col] == symbol:
                            if self.field[4][col] == 0 and not((4, col) in moves):
                                moves.append((4, col))
                            if self.field[row][5] == 0 and not((row, 5) in moves):
                                moves.append((row, 5))
                            if self.field[4][5] == 0 and row == 5 and col == 4:
                                moves.append((4, 5))
                            elif self.field[row - 2][col + 2] == 0 and not((row - 2, col + 2) in moves):
                                moves.append((row - 2, col + 2))
                        if row >= 5 and col >= 5 and self.field[row][col] == symbol:
                            if self.field[4][col] == 0 and not((4, col) in moves):
                                moves.append((4, col))
                            if self.field[row][4] == 0 and not((row, 4) in moves):
                                moves.append((row, 4))
                            if self.field[4][4] == 0 and row == col == 5:
                                moves.append((4, 4))
                            elif self.field[row - 2][col - 2] == 0 and not((row - 2, col - 2) in moves):
                                moves.append((row - 2, col - 2))
        return moves

    def get_possible_move_part_2(self, maximizing_player, computer_symbol, player_symbol): # возможные ходы компа часть 2
        possible_move = []
        for row in range(1, 9):
            for col in range(1, 9):
                if maximizing_player:
                    if self.field[row + 1][col] == 0 and self.field[row][col] == computer_symbol:
                        possible_move.append([(row, col), (row + 1, col)])
                    if self.field[row][col + 1] == 0 and self.field[row][col] == computer_symbol:
                        possible_move.append([(row, col), (row, col + 1)])
                    if self.field[row - 1][col] == 0 and self.field[row][col] == computer_symbol:
                        possible_move.append([(row, col), (row - 1, col)])
                    if self.field[row][col - 1] == 0 and self.field[row][col] == computer_symbol:
                        possible_move.append([(row, col), (row, col - 1)])
                else:
                    if self.field[row + 1][col] == 0 and self.field[row][col] == player_symbol:
                        possible_move.append([(row, col), (row + 1, col)])
                    if self.field[row][col + 1] == 0 and self.field[row][col] == player_symbol:
                        possible_move.append([(row, col), (row, col + 1)])
                    if self.field[row - 1][col] == 0 and self.field[row][col] == player_symbol:
                        possible_move.append([(row, col), (row - 1, col)])
                    if self.field[row][col - 1] == 0 and self.field[row][col] == player_symbol:
                        possible_move.append([(row, col), (row, col - 1)])
        return possible_move

    def counter_sequences(self, maximizing_player):  # счетчик последовательностей игрока/компьютера
        sequences = {2: 0, 3: 0, 4: 0}
        lines = self.find_all_lines(maximizing_player)
        for item in lines:
            if len(item) == 2:
                sequences[2] += 1
            if len(item) == 3:
                sequences[3] += 1
            if len(item) == 4:
                sequences[4] += 1
        return sequences

    def search_sequence_player(self, computer_symbol, player_symbol):  # бонус за блокировку последовательностей игрока
        score = 0
        lines = self.find_all_lines(True)
        for item in lines:
            row1, col1 = item[0]
            row2, col2 = item[1]
            lengh = len(item)
            if col2 - col1 == 1 and row1 == row2:
                if self.field[row1][col1 - 1] == computer_symbol:
                    if self.field[row1][col1 + lengh] == computer_symbol:
                        score += 3750 if lengh >= 4 else 1250 if lengh == 3 else 750
                    else:
                        score += 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                elif self.field[row1][col1 - 1] == player_symbol:
                    score -= 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                if self.field[row1][col1 + lengh] == computer_symbol:
                    if self.field[row1][col1 - 1] == computer_symbol:
                        score += 3750 if lengh >= 4 else 1250 if lengh == 3 else 750
                    else:
                        score += 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                elif self.field[row1][col1 + lengh] == player_symbol:
                    score -= 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
            elif row2 - row1 == 1 and col1 == col2:
                if self.field[row1 - 1][col1] == computer_symbol:
                    if self.field[row1 + lengh][col1] == computer_symbol:
                        score += 3750 if lengh >= 4 else 1250 if lengh == 3 else 750
                    else:
                        score += 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                elif self.field[row1 - 1][col1] == player_symbol:
                    score -= 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                if self.field[row1 + lengh][col1] == computer_symbol:
                    if self.field[row1 - 1][col1] == computer_symbol:
                        score += 3750 if lengh >= 4 else 1250 if lengh == 3 else 750
                    else:
                        score += 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                elif self.field[row1 + lengh][col1] == player_symbol:
                    score -= 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
            elif row2 - row1 == 1 and col2 - col1 == 1:
                if self.field[row1 - 1][col1 - 1] == computer_symbol:
                    if self.field[row1 + lengh][col1 + lengh] == computer_symbol:
                        score += 3750 if lengh >= 4 else 1250 if lengh == 3 else 750
                    else:
                        score += 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                elif self.field[row1 - 1][col1 - 1] == player_symbol:
                    score -= 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                if self.field[row1 + lengh][col1 + lengh] == computer_symbol:
                    if self.field[row1 + lengh][col1 + lengh] == computer_symbol:
                        score += 3750 if lengh >= 4 else 1250 if lengh == 3 else 750
                    else:
                        score += 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                elif self.field[row1 + lengh][col1 + lengh] == player_symbol:
                    score -= 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
            else:
                if self.field[row1 - 1][col1 + 1] == computer_symbol:
                    if self.field[row1 + lengh][col1 - lengh] == computer_symbol:
                        score += 3700 if lengh >= 4 else 1200 if lengh == 3 else 750
                    else:
                        score += 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                elif self.field[row1 - 1][col1 + 1] == player_symbol:
                    score -= 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                if self.field[row1 + lengh][col1 - lengh] == computer_symbol:
                    if self.field[row1 - 1][col1 + 1] == computer_symbol:
                        score += 3750 if lengh >= 4 else 1250 if lengh == 3 else 750
                    else:
                        score += 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
                elif self.field[row1 + lengh][col1 - lengh] == player_symbol:
                    score -= 7000 if lengh >= 4 else 3500 if lengh == 3 else 1000
        return score

    def evaluation_function(self, computer_symbol, player_symbol): # расчётная функция
        score = 0
        player_sequences = self.counter_sequences(True)
        computer_sequences = self.counter_sequences(False)
        for length, count in computer_sequences.items():        # 1 оценка: посчет последовательностей фишек
            score += self.sequence_weights.get(length, 0) * count
        for length, count in player_sequences.items():
            score -= self.sequence_weights.get(length, 0) * count
        for row in range(len(self.field)):         # 2 оценка: бонус за позиции на основе весовой матрицы
            for col in range(len(self.field)):
                if self.field[row][col] == computer_symbol:
                    score += self.weight_matrix[row - 1][col - 1]
                elif self.field[row][col] == player_symbol:
                    score -= self.weight_matrix[row - 1][col - 1]
        score += self.search_sequence_player(computer_symbol, player_symbol)  # 3 оценка: бонус за блокировку игрока
        return score

    def minimax(self, depth, alpha, beta, maximizing_player, computer_symbol, player_symbol):  # минимакс
        if depth == 0 or self.is_game_over(maximizing_player):
            return self.evaluation_function(computer_symbol, player_symbol), None
        if self.flag_is_first_part_game:
            possible_move = self.get_possible_move_part_1(maximizing_player, computer_symbol, player_symbol)
        else:
            possible_move = self.get_possible_move_part_2(maximizing_player, computer_symbol, player_symbol)
        if maximizing_player:
            max_eval = -math.inf
            best_move = None
            if self.flag_is_first_part_game:
                for move in possible_move:
                    row, col = move
                    self.field[row][col] = computer_symbol
                    eval, _ = self.minimax(depth - 1, alpha, beta, False, computer_symbol, player_symbol)
                    self.field[row][col] = 0
                    if eval > max_eval:
                        max_eval = eval
                        best_move = move
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
                return max_eval, best_move
            else:
                for move1, move2 in possible_move:
                    row1, col1 = move1
                    row2, col2 = move2
                    self.field[row1][col1] = 0
                    self.field[row2][col2] = computer_symbol
                    eval, _ = self.minimax(depth - 1, alpha, beta, False, computer_symbol, player_symbol)
                    self.field[row1][col1] = computer_symbol
                    self.field[row2][col2] = 0
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (move1, move2)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
                return max_eval, best_move
        else:
            min_eval = math.inf
            best_move = None
            if self.flag_is_first_part_game:
                for move in possible_move:
                    row, col = move
                    self.field[row][col] = player_symbol
                    eval, _ = self.minimax(depth - 1, alpha, beta, True, computer_symbol, player_symbol)
                    self.field[row][col] = 0
                    if eval < min_eval:
                        min_eval = eval
                        best_move = move
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
                return min_eval, best_move
            else:
                for move1, move2 in possible_move:
                    row1, col1 = move1
                    row2, col2 = move2
                    self.field[row1][col1] = 0
                    self.field[row2][col2] = player_symbol
                    eval, _ = self.minimax(depth - 1, alpha, beta, True, computer_symbol, player_symbol)
                    self.field[row1][col1] = player_symbol
                    self.field[row2][col2] = 0
                    if eval > min_eval:
                        min_eval = eval
                        best_move = (move1, move2)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
                return min_eval, best_move

    def computer_move(self, computer_symbol, player_symbol, depth=3):  # ход компьютера
        if self.flag_is_first_part_game:
            _, move = self.minimax(depth, -math.inf, math.inf, True, computer_symbol, player_symbol)
            if move:
                row, col = move
                self.field[row][col] = computer_symbol
                self.b[row][col].configure(image=self.image1)
        else:
            _, move = self.minimax(depth, -math.inf, math.inf, True, computer_symbol, player_symbol)
            if move:
                row1, col1 = move[0]
                row2, col2 = move[1]
                self.field[row1][col1] = 0
                self.b[row1][col1].configure(image=self.image3)
                self.field[row2][col2] = computer_symbol
                self.b[row2][col2].configure(image=self.image1)
        return

    def find_all_lines(self, maximizing_player):  # функция поиска линий игрока/компьютера
        n = len(self.field)
        lines = []
        if maximizing_player:
            symbol = 1
        else:
            symbol = 2

        def find_lines_in_sequence(sequence, coords):  # обработчик одной линии поля
            current_value = None
            current_length = 0
            start_index = 0
            for i, value in enumerate(sequence):
                if value == current_value and value == symbol:
                    current_length += 1
                else:
                    if current_length >= 3:
                        line_coords = coords[start_index:start_index + current_length]
                        lines.append(line_coords)
                    current_value = value
                    current_length = 1 if value == symbol else 0
                    start_index = i
            if current_length >= 3:  # Проверка последней последовательности
                line_coords = coords[start_index:start_index + current_length]
                lines.append(line_coords)

        for start_row in range(n):    # Поиск линий на основных диагоналях (слева направо, сверху вниз)
            diagonal = []             # налево вниз
            diag_coords = []
            row, col = start_row, 0
            while row < n and col < n:
                diagonal.append(self.field[row][col])
                diag_coords.append((row, col))
                row += 1
                col += 1
            find_lines_in_sequence(diagonal, diag_coords)
        for start_col in range(1, n):  # направо вверх
            diagonal = []
            diag_coords = []
            row, col = 0, start_col
            while row < n and col < n:
                diagonal.append(self.field[row][col])
                diag_coords.append((row, col))
                row += 1
                col += 1
            find_lines_in_sequence(diagonal, diag_coords)
        for start_row in range(n):    # Поиск линий на побочных диагоналях (справа налево, сверху вниз)
            diagonal = []             # напрво вниз
            diag_coords = []
            row, col = start_row, n - 1
            while row < n and col >= 0:
                diagonal.append(self.field[row][col])
                diag_coords.append((row, col))
                row += 1
                col -= 1
            find_lines_in_sequence(diagonal, diag_coords)
        for start_col in range(n - 2, -1, -1):  # налево вверх
            diagonal = []
            diag_coords = []
            row, col = 0, start_col
            while row < n and col >= 0:
                diagonal.append(self.field[row][col])
                diag_coords.append((row, col))
                row += 1
                col -= 1
            find_lines_in_sequence(diagonal, diag_coords)
        for row in range(n):          # Поиск горизонтальных линий (по строкам)
            horizontal = []
            horiz_coords = []
            for col in range(n):
                horizontal.append(self.field[row][col])
                horiz_coords.append((row, col))
            find_lines_in_sequence(horizontal, horiz_coords)
        for col in range(n):          # Поиск вертикальных линий (по столбцам)
            vertical = []
            vert_coords = []
            for row in range(n):
                vertical.append(self.field[row][col])
                vert_coords.append((row, col))
            find_lines_in_sequence(vertical, vert_coords)
        return lines

    def is_game_over(self, maximizing_player):  # функция проверки окончания игры
        lines = self.find_all_lines(maximizing_player)
        for lengh in lines:
            if len(lengh) >= 5:
                return True
        return False


menu = Menu()
menu.mainloop()