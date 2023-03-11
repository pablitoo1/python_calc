import math                     #import biblioteki math
from tkinter import *           #import biblioteki tkinter


#definicja funkcji działającej po kliknięciu danego klawisza
def click(wartosc):
    stan = pole_robocze.get()       #pobranie aktualnego stanu na wyswietlaczu
    wynik = ''                      #definicja zmiennej wynik


    #sprawdzenie czy nie wystąpił żaden SyntaxError - np. brak liczb na wyswietlaczu i kliknięcie pierwiastka
    try:

        if wartosc == "\u232B":                     #jesli klikniety zostanie dany przycisk wykonaj nastepujace dzialania
            stan = stan[0:len(stan)-1]              #stan bez ostaniego znaku z wyswietlacza
            pole_robocze.delete(0, END)             #usuniecie calej zawartosci z wyswietlacza
            pole_robocze.insert(0, stan)            #dodanie do wyswietlacza wartosci w zmiennej stan
            return                                  #konczy dzialanie funkcji w tym miejscu

        elif wartosc == "C":
            pole_robocze.delete(0, END)

        elif wartosc == "x\u00B2":
            wynik = eval(stan) ** 2                 #eval() wykonuje działanie przekazane jako argument (np jeśli w zmiennej
                                                    #stan juz bylo wykonane dzialanie to przekazuje wynik jako argument),
        elif wartosc == "x\u00B3":                  #jesli uzyty bylby int() to przy 2 wykonaniu dzialania wystąpilby blad
            wynik = eval(stan) ** 3

        elif wartosc == "x\u02b8":
            pole_robocze.insert(END, "**")
            return

        elif wartosc == "√":
            wynik = math.sqrt(eval(stan))

        elif wartosc == chr(8731):
            wynik = eval(stan) ** (1 / 3)

        elif wartosc == "1/x":
            wynik = 1/eval(stan)

        elif wartosc == 'ln':
            wynik = math.log(eval(stan))

        elif wartosc == "log":
            wynik = math.log10(eval(stan))

        elif wartosc == "sin°":
            wynik = math.sin(math.radians(eval(stan)))          #math.sin() dziala na radianach, więc wprowadzone dane ze
                                                                #stopni zmieniamy na radiany
        elif wartosc == "cos°":
            wynik = math.cos(math.radians(eval(stan)))

        elif wartosc == "tg°":
            wynik = math.tan(math.radians(eval(stan)))

        elif wartosc == "\u03C0":
            wynik = math.pi

        elif wartosc == "x!":
            wynik = math.factorial(eval(stan))

        elif wartosc == "|x|":
            wynik = abs(eval(stan))

        elif wartosc == "\u00F7":
            pole_robocze.insert(END, "/")
            return

        elif wartosc == "\u00D7":
            pole_robocze.insert(END, "*")
            return

        elif wartosc == "mod":
            pole_robocze.insert(END, "%")
            return

        elif wartosc == "=":
            wynik = eval(stan)

        else:                                       #dla wszystkich innych przyciskow program po prostu wypisuje je na wyswietlaczu
            pole_robocze.insert(END, wartosc)
            return

        pole_robocze.delete(0, END)                 #usuniecie wszystkiego z wyswietlacza
        pole_robocze.insert(0, wynik)               #dodanie wyniku na wyswietlacz

    #jesli wystąpi SyntaxError - pomiń i nie wyswietlaj go
    except SyntaxError:
        pass


root = Tk()                                 #tworzy okno

root.title('Kalkulator naukowy')            #tytul aplikacji
root.config(bg='#333333')                   #kolor tla
root.geometry('450x461+500+100')            #rozmiar okna, po plusach odleglosc w pixelach od krancow ekranu
root.resizable(False, False)                #wylaczona mozliwosc zmiany rozmiaru okna

fotoLink = PhotoImage(file='logo.png')              #podana sciena do pliku z obrazkiem
foto = Label(root, image=fotoLink, bg="#333333")    #okreslenie parametrow
foto.grid(row=0, column=0)                          #dodanie obrazka


pole_robocze = Entry(root, font=('arial', 20, 'bold'), bg='#292525', fg='white', bd=0)      #stworzenie pola roboczego z parametrami
pole_robocze.grid(row=0, column=1, columnspan=5,                                            #dodanie pola roboczego
                  padx=5, pady=5, ipady=20)         #zlaczenie 5 kolumn, marginesy

lista = ["x\u00B2", "x\u00B3", "x\u02b8", "C", "\u232B",            #lista wszystkich uzywanych przyciskow
         "√", chr(8731), "1/x", "x!", "|x|",
         "ln", "(", ")", "mod", "\u00F7",
         "log", "7", "8", "9", "\u00D7",
         "sin°", "4", "5", "6", "-",
         "cos°", "1", "2", "3", "+",
         "tg°", "\u03C0", "0", ".", "="]

wiersz = 1
kolumna = 0

#pętla, która wyswietla na ekran poszczegolne przyciski z odpowiednimi argumentami i stylami
for i in lista:
    if i == "7" or i == "8" or i == "9" or i == "4" or i == "5" or i == "6" or i == "1" or i == "2" or i == "3" or i == "0":
        przycisk = Button(root, width=8, height=2, bd=2, relief=SUNKEN, text=i, bg='#322f2f', fg='whitesmoke',
                          font=('arial', 12, 'bold'), activebackground='#d1d0d0', command=lambda button=i: click(button))   #funckcja lambda z parametrem
        przycisk.grid(row=wiersz, column=kolumna, pady=1)                                                                   #button=i oraz jej zawartosc, czyli
    elif i == "C" or i == "\u232B":                                                                                         #fukncja click z argumentem button
        przycisk = Button(root, width=8, height=2, bd=2, relief=SUNKEN, text=i, bg='#737373', fg='whitesmoke',
                          font=('arial', 12, 'bold'), activebackground='#d1d0d0', command=lambda button=i: click(button))
        przycisk.grid(row=wiersz, column=kolumna, pady=1)
    elif i == "=":
        przycisk = Button(root, width=8, height=2, bd=2, relief=SUNKEN, text=i, bg='#4a7985', fg='whitesmoke',
                          font=('arial', 12, 'bold'), activebackground='#d1d0d0', command=lambda button=i: click(button))
        przycisk.grid(row=wiersz, column=kolumna, pady=1)
    else:
        przycisk = Button(root, width=8, height=2, bd=2, relief=SUNKEN, text=i, bg='#443f3d', fg='whitesmoke',
                          font=('arial', 12, 'bold'), activebackground='#d1d0d0', command=lambda button=i: click(button))
        przycisk.grid(row=wiersz, column=kolumna, pady=1)
    kolumna += 1
    if kolumna > 4:             #ten  warunek wypisuje wszystkie przyciski
        wiersz += 1             #we wlasciwej kolejnosci
        kolumna = 0

root.mainloop()                             #utrzymuje okno w "pętli", konczy sie gdy uzytkownik zamknie okno aplikacji,
                                            #mainloop automatycznie odbiera zdarzenia z systemu okienkowego i dostarcza je
                                            #do aplikacji; zaden kod po tej komendzie nie będzie wyswietleny