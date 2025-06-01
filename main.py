import random
import time

import sys
import keyboard

import shutil
import textwrap


class Utility:
    @staticmethod
    def error():
        Utility.fixed_print("--ERRORE: Inserisci una scelta valida--\n")

    @staticmethod
    def name_err():
        print("--ERRORE: Inserisci un nome valido--")

    @staticmethod
    def check_valid_name():
        while True:
            check_username = input("Scegli il tuo nome\n").strip()
            if any(char.isalpha() for char in check_username):
                username = check_username.capitalize()
                print("\n")
                break
            else:
                Utility.name_err()

        return username

    @staticmethod
    def go_on():
        input("\n------------------------------"
              "\nPREMI INVIO PER ANDARE AVANTI."
              "\n------------------------------"
              "\n")

        for _ in range(4):
            print("\033[1A\033[2K", end="")

    @staticmethod
    def fixed_print(text):
        width = shutil.get_terminal_size().columns

        formatted_text = textwrap.fill(text, width=width)
        print(formatted_text)

    @staticmethod
    def timeout():
        time.sleep(5)

    def print_points(self):
        print(self)

    @staticmethod
    def gameover():
        sys.exit()

    @staticmethod
    def quitgame():
        if keyboard.record(until='esc'):
            sys.exit()


coin = [
    [
        " /‾‾‾‾‾\ ",
        "|       |",
        "| TESTA |",
        "|       |",
        " \_____/ "
    ],
    [
        " /‾‾‾‾‾\ ",
        "|       |",
        "| CROCE |",
        "|       |",
        " \_____/ "
    ]
]

d4_faces = [
    [
        "    ▲    ",
        "  / 1 \  ",
        " /_____\ "
    ],
    [
        "    ▲    ",
        "  / 2 \  ",
        " /_____\ "
    ],
    [
        "    ▲    ",
        "  / 3 \  ",
        " /_____\ "
    ],
    [
        "    ▲    ",
        "  / 4 \  ",
        " /_____\ "
    ]
]

d6_faces = [
    [
        "+---------+",
        "|         |",
        "|         |",
        "|    ●    |",
        "|         |",
        "|         |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●       |",
        "|         |",
        "|         |",
        "|         |",
        "|       ● |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●       |",
        "|         |",
        "|    ●    |",
        "|         |",
        "|       ● |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●     ● |",
        "|         |",
        "|         |",
        "|         |",
        "| ●     ● |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●     ● |",
        "|         |",
        "|    ●    |",
        "|         |",
        "| ●     ● |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●     ● |",
        "|         |",
        "| ●     ● |",
        "|         |",
        "| ●     ● |",
        "+---------+"
    ]
]


class Dices:
    @staticmethod
    def roll_dice(faces_num):
        return random.randint(1, faces_num)

    @staticmethod
    def launch_coin():
        return random.choice(["Testa", "Croce"])

    @staticmethod
    def roll_animation(faces):
        duration = 1.5
        interval = 0.2
        end_time = time.time() + duration

        if faces == 2:
            for _ in range(5):
                print()

            while time.time() < end_time:
                for face in coin:
                    sys.stdout.write("\033[5A")
                    for line in face:
                        sys.stdout.write("\r" + line + " " * 10 + "\n")
                    sys.stdout.flush()
                    time.sleep(interval)

        elif faces == 4:
            for _ in range(3):
                print()

            while time.time() < end_time:
                for face in d4_faces:
                    sys.stdout.write("\033[3A")  # Move cursor up 3 lines
                    for line in face:
                        sys.stdout.write("\r" + line + " " * 10 + "\n")
                    sys.stdout.flush()
                    time.sleep(interval)
        elif faces == 6:
            for _ in range(7):
                print()

            while time.time() < end_time:
                for face in d6_faces:
                    sys.stdout.write("\033[7A")
                    for line in face:
                        sys.stdout.write("\r" + line + " " * 10 + "\n")
                    sys.stdout.flush()
                    time.sleep(interval)
        else:
            Utility.error()

    @staticmethod
    def print_final_face(ascii_lines, faces):
        returns = 0

        if faces == 2:
            returns = 5
        elif faces == 4:
            returns = 3
        elif faces == 6:
            returns = 7
        else:
            Utility.error()

        sys.stdout.write(f"\033[{returns}A")
        for line in ascii_lines:
            sys.stdout.write("\r" + line + " " * 10 + "\n")
        sys.stdout.flush()

    def face_2(self):
        input("Premi Invio per tirare il dado...")

        self.roll_animation(2)
        result = self.roll_dice(2)

        self.print_final_face(coin[result - 1], 2)

        coin_result = "Testa" if result == 1 else "Croce"
        print(f"\nÈ uscita {coin_result}!")

    def face_4(self):
        input("Premi Invio per tirare il dado...")

        self.roll_animation(4)
        result = self.roll_dice(4)

        self.print_final_face(d4_faces[result - 1], 4)

        print(f"\nÈ uscito {result}!")

    def face_6(self):
        input("Premi Invio per tirare il dado...")

        self.roll_animation(6)
        result = self.roll_dice(6)

        self.print_final_face(d6_faces[result - 1], 6)

        print(f"\nÈ uscito {result}!")


class CardinalsValues:
    @staticmethod
    def voc():
        return random.randint(40, 60)

    @staticmethod
    def pop_agr():
        return random.randint(40, 60)

    @staticmethod
    def pol_infl():
        return random.randint(40, 60)

    @staticmethod
    def cur_rel():
        return random.randint(40, 60)

    @staticmethod
    def dipl_skills():
        return random.randint(40, 60)


cardinals = {
    "Giovanni de' Medici": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                            CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Bernardino López de Carvajal": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Francesco Alidosi": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                          CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Marco Cornaro": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                      CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Bandinello Sauli": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                         CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Francesco Soderini": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                           CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Alessandro Farnese": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                           CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Antonio Maria Ciocchi del Monte": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                        CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Raffaele Riario": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                        CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Leonardo Grosso della Rovere": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Gabriele de' Gabrielli": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                               CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Giovanni Battista Pallavicino": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                      CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Lorenzo Pucci": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                      CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Giulio de' Medici": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                          CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Matthäus Schiner": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                         CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Tamás Bakócz": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "René de Prie": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Robert Guibé": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Georges d'Amboise": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                          CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Jean-François de la Trémoille": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                      CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Luis de Borja-Lanzol": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                             CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Juan Castellar y de Borja": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                  CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Guillaume Briçonnet": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                            CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Pierre d'Ailly": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                       CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Jean de La Palud": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                         CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Fazio Giovanni Santori": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                               CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Galeotto Franciotti della Rovere": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                         CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Niccolò Fieschi": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                        CardinalsValues.cur_rel(), CardinalsValues.dipl_skills()],
    "Francesco Armellini Pantalassi de' Medici": [CardinalsValues.voc(), CardinalsValues.pop_agr(),
                                                  CardinalsValues.pol_infl(), CardinalsValues.cur_rel(),
                                                  CardinalsValues.dipl_skills()]
}

families_data = {
    "Gonzaga": {
        "multiplier": [1, 1.1, 1.3, 0.8, 1.2],
        "context": "Milano sotto gli Sforza, Firenze sotto i Medici, la Repubblica di Venezia e la tua Mantova "
                   "sotto il controllo gonzaghese",
        "city": "Mantova"
    },
    "Orseolo": {
        "multiplier": [1, 1.4, 1.2, 0.75, 1.5],
        "context": "Milano sotto gli Sforza, Mantova sotto i Gonzaga, Firenze e la tua Repubblica di Venezia",
        "city": "Venezia"
    },
    "Scotti": {
        "multiplier": [1.1, 1, 1.4, 1, 1.1],
        "context": "Firenze sotto i Medici, Mantova sotto i Gonzaga, la Repubblica di Venezia e la tua Milano sotto "
                   "il controllo sforzesco",
        "city": "Milano"
    },
    "Strozzi": {
        "multiplier": [1, 0.85, 1.3, 1.1, 1],
        "context": "Milano sotto gli Sforza, Mantova sotto i Gonzaga, la Repubblica di Venezia e la tua Firenze "
                   "sotto il controllo mediceo",
        "city": "Firenze"
    }
}


class Families:
    def __init__(self):
        self.fam_name = ""
        self.fam_city = ""
        self.fam_context = ""
        self.fam_multipliers = []
        self.voc = 0
        self.pop_agr = 0
        self.pol_infl = 0
        self.cur_rel = 0
        self.dipl_skills = 0

    def family(self):
        self.fam_name, info = random.choice(list(families_data.items()))
        self.fam_multipliers = info["multiplier"]
        self.fam_city = info["city"]
        self.fam_context = info["context"]
        self.voc, self.pop_agr, self.pol_infl, self.cur_rel, self.dipl_skills = self.fam_multipliers
        return self.fam_name, self.fam_city, self.fam_context, self.fam_multipliers

    def print_stats(self):
        print(f'Famiglia: {self.fam_name} di {self.fam_city}'
              '\n')
        print(f'Moltiplicatori della famiglia di {self.fam_name}:'
              f'\nVocazione: {self.voc}'
              f'\nConsenso popolare: {self.pop_agr}'
              f'\nInfluenza politica: {self.pol_infl}'
              f'\nRilevanza curiale: {self.cur_rel}'
              f'\nAbilità diplomatica: {self.dipl_skills}'
              '\n')
        print(f'Contesto: {self.fam_context}')


class PlayerValues:
    @staticmethod
    def voc():
        return random.randint(1, 5)

    @staticmethod
    def pop_agr():
        return random.randint(1, 5)

    @staticmethod
    def pol_infl():
        return random.randint(1, 5)

    @staticmethod
    def cur_rel():
        return random.randint(1, 5)

    @staticmethod
    def dipl_skills():
        return random.randint(1, 5)


class Player:
    def __init__(self, name, voc, pop_agr, pol_infl, cur_rel, dipl_skills):
        # Player Name
        self.player_name = name

        # Family assignment
        self.fam = Families()
        self.fam_name, self.fam_city, self.fam_context, self.fam_val = self.fam.family()

        # Family Multipliers
        self.fam_voc = self.fam_val[0]
        self.fam_pop_agr = self.fam_val[1]
        self.fam_pol_infl = self.fam_val[2]
        self.fam_cur_rel = self.fam_val[3]
        self.fam_dipl_skills = self.fam_val[4]

        # Player Attributes
        self.voc = round(random.randint(1, 5) * self.fam_voc) + voc
        self.pop_agr = round(random.randint(1, 5) * self.fam_pop_agr) + pop_agr
        self.pol_infl = round(random.randint(1, 5) * self.fam_pol_infl) + pol_infl
        self.cur_rel = round(random.randint(1, 5) * self.fam_cur_rel) + cur_rel
        self.dipl_skills = round(random.randint(1, 5) * self.fam_dipl_skills) + dipl_skills

        self.player_values = [self.voc, self.pop_agr, self.pol_infl, self.cur_rel, self.dipl_skills]

        # Status
        self.isnothing = True
        self.issoldier = False
        self.ispriest = False
        self.isparson = False
        self.isbishop = False
        self.iscardinal = False

        # Calculation of consensus
        if self.isbishop or self.iscardinal:
            self.consensus = round(
                (self.voc + self.pop_agr + self.pol_infl + self.cur_rel + self.dipl_skills) * self.fam_val[1])
        else:
            self.consensus = round(
                (self.voc + self.pop_agr + self.pol_infl) * self.fam_val[1])

    def add_points(self, voc, pop_agr, pol_infl, cur_rel, dipl_skills):
        self.voc += voc
        self.pop_agr += pop_agr
        self.pol_infl += pol_infl
        self.cur_rel += cur_rel
        self.dipl_skills += dipl_skills

        # Calculation of new consensus
        if self.isbishop or self.iscardinal:
            self.consensus = round(
                (self.voc + self.pop_agr + self.pol_infl + self.cur_rel + self.dipl_skills) * self.fam_val[1])
        else:
            self.consensus = round(
                (self.voc + self.pop_agr + self.pol_infl) * self.fam_val[1])

    def print_stats(self):
        print(f'''Statistiche del giocatore:
Famiglia: {self.fam_name}, {self.fam_val}
Vocazione: {self.voc}
Consenso popolare: {self.pop_agr}
Influenza politica: {self.pol_infl}
Rilevanza curiale: {self.cur_rel}
Abilità diplomatica: {self.dipl_skills}
Consenso totale: {self.consensus}
''')


class Game:
    username = Utility.check_valid_name()

    def __init__(self):
        self.player = Player(Game.username, PlayerValues.voc(), PlayerValues.pop_agr(), PlayerValues.pol_infl(),
                             PlayerValues.cur_rel(), PlayerValues.dipl_skills())

    def start(self):
        player_name = self.player.player_name

        family_name = self.player.fam_name
        city = self.player.fam_city
        context = self.player.fam_context

        Utility.fixed_print("Ci troviamo a cavallo tra ‘400 e ‘500, nel cuore del Rinascimento italiano."
                            "Periodo in cui la penisola è ampiamente frammentata in una moltitudine di ducati,"
                            "signorie, regni e repubbliche in costante competizione tra loro. A dominare la scena"
                            f"politica sono le grandi potenze di {context}, senza dimenticare la rilevanza dello Stato "
                            "pontificio in centro Italia, che ha influenza in tutta Europa."
                            "Il Papato pur attraversando momenti di crisi, come lo scisma d’Occidente, è in grado "
                            "di riacquistare e rafforzare il proprio potere temporale, sotto il pontificato di Sisto "
                            "IV e di Alessandro VI; la politica ecclesiastica si fa sempre più attiva e ambiziosa, "
                            "spesso intrecciata con gli interessi delle grandi famiglie italiane."
                            f"È in questo scenario che, nel 1475, nasci tu {player_name} della famiglia {family_name}, "
                            f"tra le più antiche e influenti di {city}. Sei un figlio cadetto: il diritto di eredità "
                            "è sfumato solo per - di scegliere il tuo destino. In un’età in cui ogni decisione può "
                            "cambiare i destini di"
                            "una famiglia, o addirittura di uno Stato, dovrai ponderare adeguatamente ogni tua mossa. "
                            "Sta a te, quindi, decidere che carriera intraprendere…"
                            "\n")

        Utility.go_on()

        while True:
            choice = input('Il tuo cuore è giovane, ma la vita ti chiede già di scegliere: quale strada '
                           'percorrerai per lasciare un segno nel mondo? Il destino ti pone davanti due vie.'
                           '\n1 - Prete: Una vita dedicata a Dio, alla parola, al mistero.'
                           '\n2 - Soldato: Una vita forgiata nel ferro e nel sangue, al servizio del potere.'
                           '\n')
            if choice == "1":
                Utility.fixed_print("Da giovane, hai dovuto scegliere una strada. Il destino ti ha posto davanti alla "
                                    "tonaca.")
                self.player.ispriest = True

                Utility.go_on()

                Game.Priest(self.player).why_priest()
                break
            elif choice == "2":
                self.player.issoldier = True

                if city == "Firenze":
                    Game.Soldier(self.player).firenze()

                elif city == "Milano" or "Mantova" or "Venezia":
                    Game.Soldier(self.player).milano_venezia_mantova()

                else:
                    Utility.error()

                break
            else:
                Utility.error()

    class Soldier:
        def __init__(self, player):
            self.player = player

        def firenze(self):
            self.player.issoldier = True

            while True:
                Utility.fixed_print("Nel 1494 viene installato il regime teocratico del savonarola, il profeta"
                                    "disarmato. Applica una riforma dei costumi, però è criticato per svariati "
                                    "aspetti e,"
                                    "e profetizza l'arrivo di un nemico che invaderà l'Italia dalle alpi. ")

                Utility.go_on()

                choice = input("Cosa fai?"
                               "\n1 - Lo difendi dalle accuse"
                               "\n2 - Limiti soltanto i disordini"
                               "\n")
                if choice == "1":
                    Utility.fixed_print(
                        "Decidi di difendere Savonarola, convinto che la sua visione ascetica rappresenti "
                        "una vera rinascita spirituale per Firenze. Le sue parole incendiano le coscienze, "
                        "e sotto la tua influenza i suoi sermoni si fanno ancora più ascoltati. Il popolo lo "
                        "acclama, i corrotti tremano.Ma la tua alleanza ha un prezzo.I potenti ti guardano con "
                        "sospetto. Le corti straniere e Roma ti accusano di eresia mascherata da zelo. Firenze "
                        "diventa un campo di battaglia ideologica. Eppure, resisti. Quando l’invasore varca le "
                        "Alpi, proprio come Savonarola aveva profetizzato, il popolo ti riconosce come colui che ha "
                        "dato ascolto al “profeta disarmato”.Hai guadagnato rispetto, ma ti sei esposto al giudizio "
                        "del mondo."
                        "\n")

                    Player.add_points(self.player, 2, 0, 0, 0, 0)
                    Utility.print_points(self.player.print_stats())
                    self.player.issoldier = False
                    self.player.ispriest = True

                    Utility.go_on()

                    Game.Priest(self.player).why_priest()
                    break
                elif choice == "2":
                    prob = random.randint(1, 100)
                    if prob <= 95:
                        Utility.fixed_print(
                            "Non ti schieri del tutto. Lasci che Savonarola predichi, ma impedisci che la sua furia "
                            "moralizzatrice travolga la città. Le sue “riforme dei costumi” vengono contenute, "
                            "le processioni del fuoco sono vietate, e i tribunali popolari sciolti.Firenze resta "
                            "inquieta, ma stabile. I nobili ti rispettano per la tua moderazione, e la Chiesa ti "
                            "osserva con approvazione prudente. Savonarola, isolato, comincia a perdere "
                            "presa.Quando l’invasore scende dalle Alpi, la città è incerta, ma non nel caos.Hai "
                            "evitato lo scontro, ma anche la gloria. Sei un mediatore, non un profeta."
                            "\n")

                        Player.add_points(self.player, 2, 0, 0, 0, 0)
                        Utility.print_points(self.player.print_stats())
                        self.player.issoldier = False
                        self.player.ispriest = True

                        Utility.go_on()

                        Game.Priest(self.player).why_priest()
                    elif prob > 95:
                        Utility.fixed_print(
                            "Hai cercato l’equilibrio. Un compromesso.Controlli i roghi, smorzi gli eccessi di "
                            "Savonarola, plachi l’ira dei nobili e della Curia. Firenze rimane sospesa in un "
                            "silenzioso malcontento. Nessuno è del tutto contro di te… ma nessuno è veramente con "
                            "te.Poi accade l’inevitabile.L’invasore, che Savonarola aveva annunciato come punizione "
                            "divina, cala dalle Alpi con la furia di una profezia compiuta. Firenze si trova "
                            "impreparata, divisa, e tu sei colto nel mezzo. I sostenitori del profeta ti accusano "
                            "di aver spento la voce di Dio. I tuoi alleati politici ti abbandonano nel caos.In una "
                            "notte di torce e tradimenti, vieni catturato da una folla furente. Non c’è processo. "
                            "Solo urla, una piazza in fiamme e un giudizio senza appello.Il tuo corpo è lasciato "
                            "penzolare come monito.Il mediatore è morto. E la storia… non si ricorda mai dei "
                            "moderati."
                            "\n")

                        Utility.gameover()
                    else:
                        Utility.error()
                    break
                else:
                    Utility.error()

        def milano_venezia_mantova(self):
            self.player.issoldier = True

            while True:
                choice = input("Nel 1495 nasce la Lega Santa, che fu un'alleanza militare stipulata tra il Papa"
                               "Alessandro VI, il re di Napoli Ferdinando d'Aragona, il Sacro Romano Impero, gli "
                               "Sforza di Milano e la Repubblica di Venezia. L'obiettivo principale della lega era"
                               "contrastare la discesa in Italia di Carlo VIII di Francia e la sua pretesa di"
                               "conquistare il Regno di Napoli, mentre nella Repubblica di Firenze si instaurava"
                               "un controverso regime teocratico. "
                               "Risalendo la penisola l'obiettivo di Carlo VIII passò dalla conquista di Napoli alla"
                               "conquista di Milano, e l'evento risolutivo fu la battaglia di Fornovo a cui presero"
                               "parte contro i Francesi Mantova, Venezia, Milano e Bologna. Tu sei un soldato"
                               f"cadetto e in quanto cittadino di {self.player.fam_city} Prendi parte alla battaglia. "
                               "\nTi viene consigliato il combattimento in seconda linea, tuttavia puoi decidere se "
                               "andare in prima linea, a te la scelta..."
                               "\n1 - Prima linea"
                               "\n2 - Seconda linea"
                               "\n")

                if choice == "1":
                    Utility.fixed_print("La battaglia si risolve rapidamente, ma sanguinosamente ed essendoti fatto "
                                        "valore combattendo in prima linea sei rimasto ferito gravemente. Dopo qualche "
                                        "giorno ti viene fatta l'estrema unzione ma riesci alla fine a sopravvivere, "
                                        "e vedi"
                                        "questo come un miracolo che ti è stato concesso dal signore; perciò lesionato "
                                        "termina la tua carriera militare, e ti dedichi dopo questo evento alla "
                                        "carriera"
                                        "ecclesiastica."
                                        "\n")

                    prob = random.randint(1, 100)

                    if prob <= 85:
                        self.player.issoldier = False
                        self.player.ispriest = True
                        Player.add_points(self.player, 3, 0, 0, 0, 0)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        Game.Priest(self.player).why_priest()
                        break
                    elif prob > 85:
                        Utility.fixed_print(
                            "I tuoi sforzi in battaglia non sono bastati, la picac nemica trapassa il tuo torace. I "
                            "tuoi occhi si spengonoper sempre...")
                        Utility.gameover()
                elif choice == "2":
                    Utility.fixed_print("La battaglia si risolve rapidamente, ma sanguinosamente ed essendo tu soldato "
                                        "cadetto alla prima battaglia rimani scioccato dall'atrocità della guerra, "
                                        "pertanto"
                                        "abbandoni la carriera militare per aiutare il prossimo e diventi prete."
                                        "\n")
                    self.player.issoldier = False
                    self.player.ispriest = True
                    Player.add_points(self.player, 1, 0, 0, 0, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    Game.Priest(self.player).why_priest()
                    break
                else:
                    Utility.error()

    class Priest:
        def __init__(self, player):
            self.player = player

        def why_priest(self):
            self.player.ispriest = True

            while True:
                choice = input('Perché hai deciso di diventare prete?'
                               '\n1 - Per vocazione: Sentivi il richiamo di Dio, limpido come una campana nel silenzio.'
                               '\n2 - Per necessità: Era l’unica via per sfuggire alla miseria, un rifugio tra mura '
                               'sacre.'
                               '\n')
                if choice == "1":
                    Utility.fixed_print(
                        "“Sentivi il richiamo di Dio, limpido come una campana nel silenzio.”Fin da piccolo, "
                        "tra le pietre fredde della chiesa del villaggio, sentivi qualcosa. Non era solo la "
                        "bellezza delle candele accese o il canto solenne del sacerdote: era una voce. Una "
                        "presenza. Come se Dio ti sussurrasse da dietro l’altare.Quando indossasti la tonaca per la "
                        "prima volta, non fu una maschera: fu pelle nuova. Ogni preghiera era un passo verso la "
                        "verità. Ogni atto di carità, un tassello nella volontà divina.Ora che cammini tra le ombre "
                        "del potere e le luci dell’ambizione, il ricordo di quella voce ti guida. Forse diventerai "
                        "Papa. Ma prima, eri solo un ragazzo che voleva servire qualcosa di eterno.")
                    Player.add_points(self.player, 2, 0, 0, 0, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "“Era l’unica via per sfuggire alla miseria, un rifugio tra mura sacre.”La fame era una "
                        "compagna più fedele della speranza. Le strade erano dure, e nessuno tendeva una mano senza "
                        "pretesa. Ma la Chiesa… offriva pane, tetto, libri. Un mondo diverso.Diventare prete non fu "
                        "scelta di spirito, ma di sopravvivenza. Imparasti il latino per fame, non per fede. "
                        "Pregavi con occhi aperti, scrutando i meccanismi del potere sotto le vesti del sacro.Ora, "
                        "salendo la scala ecclesiastica, non dimentichi chi eri. Non sei cieco: conosci il gioco. E "
                        "se il Signore ti ha davvero chiamato… forse, lo ha fatto con la voce della fame."
                        "\n")

                    Utility.go_on()

                    break
                else:
                    Utility.error()

            Utility.go_on()
            self.sermon()

        def sermon(self):
            while True:
                choice = input('Gli anni passano. Ora sei sacerdote. Ogni domenica, il tuo volto si alza tra la '
                               'folla, e la tua voce guida i cuori. \nQual è il cuore della tua predica?'
                               '\n1 - Giustizia e misericordia: Parli del perdono, della pace, del dovere di aiutare '
                               'chi soffre.'
                               '\n2 - Decadimento morale: Denunci i peccati del tempo, l’abisso che cresce sotto i'
                               'piedi della società.'
                               '\n')
                if choice == "1":
                    Utility.fixed_print(
                        "“Parli del perdono, della pace, del dovere di aiutare chi soffre.”Le tue parole scendono "
                        "leggere, come pioggia d’estate sulle coscienze assetate.Ogni domenica, dal pulpito, "
                        "inviti i fedeli a guardarsi negli occhi. A perdonare i debiti, a spezzare il pane con "
                        "l’affamato, a chinarsi sulle ferite del mondo. Non gridi: accarezzi. Non accusi: consoli.I "
                        "poveri iniziano a venire solo per sentirti. I peccatori ti ascoltano in silenzio. Anche "
                        "chi non crede trova in te qualcosa che manca altrove: un’eco di bontà autentica.I potenti "
                        "storcono il naso, ma non possono ignorarti. La tua fama cresce come un seme nella terra "
                        "buona.Forse la santità non è nel potere… ma tu, senza cercarlo, ti stai avvicinando."
                        "\n")

                    Player.add_points(self.player, 2, 3, 0, 0, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "“Denunci i peccati del tempo, l’abisso che cresce sotto i piedi della società.”Quando "
                        "parli, la tua voce è fuoco. Non edulcori. Non addolcisci.Denunci l’avidità dei mercanti, "
                        "la lussuria dei nobili, la corruzione del clero. I tuoi sermoni risuonano come tuoni tra "
                        "le navate. Alcuni si alzano e se ne vanno. Altri restano, rapiti, tremanti.Dici che Roma è "
                        "divenuta Babilonia. Che il mondo danza sul ciglio dell’inferno, e nessuno lo vuole vedere. "
                        "Qualcuno ti chiama profeta. Qualcun altro, fanatico.Ma non ti importa.Non vuoi essere "
                        "amato. Vuoi che si ravvedano.E così, sermone dopo sermone, diventi il volto di un tempo "
                        "che cambia. O di una tempesta in arrivo."
                        "\n")

                    Player.add_points(self.player, 0, 1, (-2), 0, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                else:
                    Utility.error()

            Utility.go_on()
            self.present()

        def present(self):
            while True:
                choice = input('Un tuo zio, uomo ricco e influente, ti offre una somma ingente. '
                               'Ma in cambio, chiede silenzio su un affare sporco che hai scoperto. '
                               '\nCosa fai con il dono?'
                               '\n1 - Lo dai in beneficienza: Il denaro va ai poveri, ma il peccato resta nel silenzio.'
                               '\n2 - Lo tieni per te: Pensando che forse un giorno ti servirà per “un bene più '
                               'grande”.'
                               '\n3 - Non accetti il dono: Rifiuti, anche se ciò significa rovinare i rapporti con la '
                               'tua famiglia.'
                               '\n')
                if choice == "1":
                    Utility.fixed_print(
                        "“Il denaro va ai poveri, ma il peccato resta nel silenzio.”Accetti la somma, ma con il "
                        "cuore stretto.Non per te. Mai per te. I denari sporchi diventano pane per gli orfani, "
                        "medicine per i malati, coperte per chi dorme tra le pietre. In pubblico, sei lodato come "
                        "un prete generoso. Le folle ti seguono. I tuoi gesti ispirano imitazione.Ma di notte, "
                        "quando preghi, la coscienza non tace. Sai cosa hai coperto. Il peccato dell’altro è "
                        "diventato anche il tuo, vestito di carità.La tua fama cresce… ma anche l’ombra che la "
                        "accompagna."
                        "\n")

                    Player.add_points(self.player, 1, 2, 0, 0, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "“Pensando che forse un giorno ti servirà per un bene più grande.”Accetti il denaro in "
                        "silenzio, e lo nascondi. Non per avidità, ti dici, ma per lungimiranza. Forse un giorno "
                        "potrai usarlo per comprare un libro proibito, finanziare un convento in segreto, "
                        "o corrompere il corrotto per fermare un male peggiore.Così inizia la discesa. Piccole "
                        "bugie, discreti spostamenti di denaro. Ma nessun peccato resta nascosto per sempre.Un "
                        "giovane chierico, troppo curioso, scopre le tue carte. Le voci corrono. E infine, "
                        "arriva la tempesta: vieni convocato da un tribunale ecclesiastico. Non importa quanto ti "
                        "giustifichi, quanto invochi “il bene futuro” — le monete che hai accettato pesano più "
                        "delle tue parole.Vieni scomunicato.Il tuo nome è bandito dalle preghiere. I tuoi paramenti "
                        "strappati. I fedeli ti voltano le spalle. Anche la tua famiglia, già complice, ti rinnega "
                        "per salvare se stessa.Hai perso.Non sei diventato Papa.Sei diventato un esempio… di ciò "
                        "che non si deve essere."
                        "\n")

                    Utility.gameover()

                    break
                elif choice == "3":
                    Utility.fixed_print(
                        "“Rifiuti, anche se ciò significa rovinare i rapporti con la tua famiglia.”Guardi tuo zio "
                        "negli occhi. Senti il peso della storia familiare, dei pranzi d’infanzia, dei favori "
                        "ricevuti. Ma la tua fede – o forse solo il tuo orgoglio – è più forte.Rifiuti.La sua "
                        "espressione cambia: rispetto, poi gelo. Da quel giorno, vieni escluso. La tua famiglia ti "
                        "chiude le porte. Sei un estraneo tra i tuoi. Ma dentro, una pace profonda.Hai scelto la "
                        "verità. Anche se fa male. Anche se costa.Forse Dio ha visto. Forse no. Ma tu sai di non "
                        "dover abbassare gli occhi davanti a nessuno."
                        "\n")

                    Player.add_points(self.player, 0, 0, (-1), 0, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                else:
                    Utility.error()

            Utility.go_on()
            self.become_parson()

        def become_parson(self):
            while True:
                choice = input('Ti viene offerto di diventare parroco proprio nella tua parrocchia natale. La '
                               'comunità ti conosce, ti ama e anche ti giudica. \nAccetti l’incarico?'
                               '\n1 - Sì: Vuoi guidare la tua gente.'
                               '\n2 - No: Temi che il passato ti segua troppo da vicino.'
                               '\n')
                if choice == "1":
                    Utility.fixed_print(
                        "“Accetti. Vuoi essere la guida dove un tempo eri solo un volto tra gli altri. ”Tornare a "
                        "casa non è facile, ma lo fai a testa alta. Cammini tra le stesse strade dove da bambino "
                        "correvi scalzo, ora con la tonaca addosso e il peso della guida sulle spalle. Alcuni ti "
                        "guardano con affetto sincero, altri con sospetto. Ti ricordano com’eri, e forse non "
                        "credono a ciò che sei diventato. Ma tu non ti lasci frenare. Celebri messe con ardore, "
                        "ascolti confessioni con pazienza, offri consiglio anche a chi ti aveva disprezzato.Giorno "
                        "dopo giorno, il tuo esempio comincia a parlare più forte dei ricordi.Il passato ti "
                        "accompagna, sì — ma non ti comanda.E forse è proprio lì, tra chi ti ha visto nascere, "
                        "che inizia la tua vera ascesa."
                        "\n")

                    Player.add_points(self.player, 0, 2, 2, 0, 0)
                    Utility.print_points(self.player.print_stats())
                    self.player.isparson = True

                    Utility.go_on()

                    self.cardinal_letter()
                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "“Rinunci. Non per paura, ma per prudenza.” L’offerta ti tocca il cuore, ma sai che il "
                        "terreno lì è fragile. Ogni tua parola verrebbe pesata. Ogni tuo gesto confrontato con chi "
                        "eri, non con chi sei.Preferisci declinare.Lasci il posto a un altro, e ti allontani in "
                        "silenzio. Un distacco doloroso, ma necessario. In un luogo nuovo, potrai costruire senza "
                        "ombre, senza vecchi sguardi che leggono il passato in ogni tuo sermone.Forse un giorno "
                        "tornerai. Da vescovo, da cardinale… o da papa.Ma non ancora."
                        "\n")

                    Player.add_points(self.player, 0, 0, 0, 0, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    self.annul_marriage()
                    break
                else:
                    Utility.error()

        def cardinal_letter(self):
            while True:
                choice = input('Una mattina, ricevi una lettera sigillata. È di un cardinale influente: sta avviando '
                               'un progetto ambizioso per “rinnovare la Chiesa”. Il tono è solenne, ma le parole '
                               'lasciano spazio a interpretazioni. \nCosa fai?'
                               '\n1 - Entri attivamente nel progetto: Ti unisci con entusiasmo, pronto a scalare la '
                               'gerarchia.'
                               '\n2 - Appoggi in maniera informale: Mostri interesse, ma resti prudente.'
                               '\n3 - Ignori la lettera: Forse è meglio non farsi coinvolgere.'
                               '\n')
                if choice == "1":
                    Utility.fixed_print(
                        "“Ti unisci con entusiasmo, pronto a scalare la gerarchia.” Rispondi senza esitazioni. Le "
                        "tue parole sono decise, rispettose ma ambiziose. Ti metti al servizio del cardinale, "
                        "offri idee, ti rendi visibile. Incontri prelati, partecipi a concili riservati, "
                        "impari a muoverti tra silenzi e sguardi. Il progetto prende forma. Si parla di riforme, "
                        "ma dietro le quinte si stringono alleanze. Tu sei lì. E quando qualcuno deve parlare in "
                        "pubblico, o firmare un documento delicato, spesso tocca a te.Ti stai costruendo un nome. La "
                        "strada verso Roma non è più un sogno. È una mappa, e tu hai appena ottenuto una guida."
                        "\n")

                    Player.add_points(self.player, (-1), 0, 2, 2, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    self.annul_marriage()
                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "“Mostri interesse, ma resti prudente.” Scrivi una risposta cortese. Lusingato, "
                        "interessato, ma non ti sbilanci. Partecipi a qualche incontro, invii commenti riservati, "
                        "mantieni un profilo basso. Il tuo nome appare nei documenti, ma in fondo alle pagine. Se "
                        "il progetto fallisse, potresti sempre dire di non essere mai stato davvero coinvolto. Ma "
                        "se avrà successo… potresti salire senza esserti mai esposto troppo. La prudenza ti "
                        "protegge. Ma rallenta anche la tua ascesa."
                        "\n")

                    Player.add_points(self.player, 0, 0, 0, 1, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    self.annul_marriage()
                    break
                elif choice == "3":
                    Utility.fixed_print(
                        "“Forse è meglio non farsi coinvolgere.” La lasci sul tavolo per giorni, poi la riponi tra "
                        "le altre. Nessuna risposta. Forse è paura. O forse è saggezza. Hai visto troppi "
                        "rinnovatori bruciarsi, troppi sogni diventare eresie nel giro di un sinodo.  Continui il "
                        "tuo lavoro locale. Messe, confessioni, carità. Qualcuno dice che sei un uomo giusto, "
                        "ma poco ambizioso. Altri ti dimenticano. La lettera, col tempo, diventa solo un rimpianto "
                        "sigillato."
                        "\n")

                    Utility.go_on()

                    self.annul_marriage()
                    break
                else:
                    Utility.error()

        def annul_marriage(self):
            while True:
                choice = input('Un nobile e un borghese ti chiedono entrambi l’annullamento dei loro matrimoni. '
                               'Sai che uno è politicamente utile. L’altro è solo… umano. \nCosa decidi?'
                               '\n1 - Annulli entrambi: La legge è la legge.'
                               '\n2 - Annulli solo quello del nobile: Un favore strategico.'
                               '\n3 - Annulli solo quello del borghese: Segui la tua coscienza.'
                               '\n4 - Non ne annulli nessuno: Il matrimonio è sacro.'
                               '\n')
                if choice == "1":
                    Utility.fixed_print(
                        "“La legge è la legge.” Esamini i casi con rigore. Studi documenti, ascolti testimonianze, "
                        "valuti secondo dottrina. Non importa il rango, non conta l’influenza: conta solo la verità "
                        "canonica.Annulli entrambi i matrimoni, suscitando stupore e scompiglio.Il nobile ti guarda "
                        "con rispetto freddo: non sei manipolabile. Il borghese ti abbraccia in lacrime: per lui, "
                        "sei stato giusto.La tua reputazione cresce come quella di un uomo equo, ma temuto.Chi "
                        "cerca un favore facile, da te non otterrà nulla."
                        "\n")

                    Utility.gameover()

                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "Un favore strategico.”  Non esiti troppo. Sai che il nobile ha amici a Roma, appoggi "
                        "potenti, voci che possono alzarti… o schiacciarti. L’annullamento è concesso. Rapido, "
                        "pulito, ben motivato.  Il borghese riceve una risposta fredda, formale. Soffre. Ma tu "
                        "guardi altrove.  Pochi mesi dopo, ricevi un invito a un banchetto. Poi una lettera "
                        "sigillata da un cardinale. Stai salendo, è vero.  Ma dentro di te… qualcosa ha smesso di "
                        "guardarti negli occhi."
                        "\n")

                    Player.add_points(self.player, (-2), 0, 2, 0, 0)
                    Utility.print_points(self.player.print_stats())

                    if not self.player.isparson:
                        Utility.fixed_print(
                            "Tentare di annullare solo uno dei matrimoni è un azione mortale. La Curia lo scopre "
                            "subito. L’abuso della tua autorità viene giudicato grave. Vieni scomunicato. I fedeli ti"
                            "voltano le spalle, la famiglia ti rinnega. La tua carriera ecclesiastica finisce qui."
                            "\n")

                        Utility.gameover()
                    else:
                        Utility.go_on()

                        self.try_become_bishop()
                    break
                elif choice == "3":
                    Player.add_points(self.player, (-2), 0, 1, 0, 0)
                    Utility.print_points(self.player.print_stats())

                    if not self.player.isparson:
                        Utility.fixed_print(
                            "Tentare di annullare solo uno dei matrimoni è un azione mortale. La Curia lo scopre "
                            "subito. L’abuso della tua autorità viene giudicato grave. Vieni scomunicato. I fedeli ti"
                            "voltano le spalle, la famiglia ti rinnega. La tua carriera ecclesiastica finisce qui."
                            "\n")

                        Utility.gameover()
                    else:
                        Utility.fixed_print(
                            "“Segui la tua coscienza.”La richiesta del nobile è politicamente utile, ma piena di "
                            "falsità. Il suo matrimonio è solo una pedina. Invece, il borghese viene con la moglie "
                            "al fianco, le mani tremanti e gli occhi pieni di dolore sincero.Ti prendi giorni per "
                            "pregare. E alla fine, scegli: annulli solo quel matrimonio.Il nobile è furioso. Fa "
                            "pressione. Le voci su di te diventano velenose nei circoli del potere.Ma la gente ti "
                            "difende. E qualcuno, in silenzio, inizia a credere che tu sia davvero diverso."
                            "\n")

                        Utility.go_on()

                        self.try_become_bishop()
                    break
                elif choice == "4":
                    Utility.fixed_print(
                        "“Il matrimonio è sacro.”  Li ricevi entrambi. Ascolti. Ma resti fermo. La tua voce non "
                        "trema quando pronunci la sentenza: “Quello che Dio ha unito, l’uomo non separi.”  I due "
                        "uomini lasciano la sala con espressioni opposte: il nobile, offeso. Il borghese, "
                        "sconfitto. Ma tu non giudichi le emozioni — solo le anime.  Per molti sei inflessibile. "
                        "Per altri, incorruttibile.  Ma dentro la Chiesa, ci sono voci che cominciano a chiedersi: "
                        "è fermezza… o semplice rigidità?"
                        "\n")

                    Player.add_points(self.player, 0, 0, (-3), 0, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    self.try_become_bishop()
                    break
                else:
                    Utility.error()

        def try_become_bishop(self):
            if self.player.consensus >= 20:
                Utility.fixed_print("Il giorno è grigio, come se il cielo stesso volesse trattenere il fiato."
                                    "Nella tua stanza, silenziosa e austera, una lettera reca il sigillo della Santa "
                                    "Sede."
                                    "Le mani tremano. Le labbra si muovono in una preghiera che non è solo di"
                                    "gratitudine, ma anche di timore."
                                    "“Per la grazia di Dio e la volontà del Santo Padre, sei stato scelto come nuovo"
                                    "Vescovo di…” Il resto svanisce, inghiottito dal battito del tuo cuore."
                                    "Hai scelto, a volte con fermezza, altre con esitazione."
                                    "Hai parlato alle folle, a volte con verità, altre con prudenza."
                                    "Hai stretto mani sporche per costruire ponti e forse, talvolta, per non restare"
                                    "solo. Eppure, sei arrivato fin qui."
                                    "Nel giorno della consacrazione, la cattedrale è piena."
                                    "Gli occhi puntati su di te sono molti: alcuni pieni di speranza, altri di "
                                    "sospetto,"
                                    "alcuni cercano solo segni di debolezza"
                                    "Quando l’anello episcopale viene infilato al tuo dito, non senti solo l’onore. "
                                    "Senti il peso"
                                    "Quando ti consegnano il bastone pastorale, non senti solo il potere. Senti la "
                                    "responsabilità."
                                    "Quando il coro intona il Te Deum, tu guardi in alto. Ma pensi anche a ciò che si"
                                    "cela in basso: ambizione, compromesso, scelta."
                                    "\n")
                self.player.ispriest = False
                self.player.isbishop = True

                Utility.go_on()

                Game.Bishop(self.player).residence()
            elif self.player.consensus < 20:
                Utility.fixed_print("Hai camminato lungo i corridoi del potere con passo incerto, indossando l’abito"
                                    "dell’umiltà ma senza mai ottenere il peso della grazia."
                                    "Il Concistoro ha parlato. I tuoi sforzi, sebbene ferventi, non hanno convinto. I"
                                    "tuoi sermoni sono stati ascoltati, ma non ricordati. Le tue opere hanno sollevato"
                                    "polvere, ma non anime."
                                    "Il Collegio dei Cardinali ha deciso di guardare altrove."
                                    "Il titolo di Vescovo resta irraggiungibile."
                                    "Il soglio pontificio, un sogno che svanisce come incenso nel vento."
                                    "Ora torni al tuo monastero, tra gli scaffali di manoscritti dimenticati e le ombre"
                                    "delle candele spente. Il tuo viaggio si conclude qui, non con una scomunica, ma"
                                    "con un silenzio."
                                    "Non sei diventato Papa. Non sei nemmeno diventato Vescovo."
                                    "Forse, in un’altra vita, con più fede… o più astuzia…"
                                    "\n")
                Utility.gameover()
            else:
                Utility.error()

    class Bishop:
        def __init__(self, player):
            self.player = player
            self.was_neutral = False
            self.was_france_ambassador = False
            self.was_sri_strong = False
            self.was_sri_calm = False
            self.was_opposer = False
            self.battle_neutral = False
            self.battle_injured = False

        def residence(self):
            self.player.ispriest = False
            self.player.isbishop = True

            while True:
                choice = input("Ora che sei diventato Vescovo la tua importanza all’ interno della vita politica del"
                               "tuo paese è estremamente più elevata, in particolar modo hai la possibilità di"
                               "riscuotere tasse, gestire documenti, conservare risorse e portare alla curia le"
                               "questioni locali."
                               "Però, proprio perché hai tale rilevanza, ti viene proposto, come di norma in"
                               f"questi anni, di poter risiedere a Roma, invece che a {self.player.fam_city}."
                               "Chiaramente la scelta spetta a te, se preferisci dare valore alla tua missione"
                               "locale o cercare di acquisire maggiore rilevanza nel clero."
                               "\n1 - Resta nel tuo vescovato"
                               "\n2 - Vai a risiedere nello Stato della Chiesa"
                               "\n")

                if choice == "1":
                    Utility.fixed_print("Scegliendo di risedere nel tuo vescovato, ti sei guadagnato l’appoggio dei "
                                        "cittadini, che ora ti vedono come figura di riferimento fondamentale della "
                                        "vita"
                                        "del paese, il tuo consenso popolare aumenta di conseguenza."
                                        "\n")
                    Player.add_points(self.player, 2, 0, 0, 0, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    self.taxation()
                    break
                elif choice == "2":
                    Utility.fixed_print("Bene! Ti sei trasferito a Roma, adesso potrai gestire le grande questioni "
                                        "teologiche da vicine conoscere i “pezzi grossi” e avere un rapporto diretto "
                                        "con le"
                                        "decisioni prese dalla curia. A pagarne le spese però è la tua gente, che si "
                                        "sente"
                                        "abbandonata e lasciata alla mercè delle importanti famiglie nobiliari della "
                                        "zona."
                                        "\n")
                    Player.add_points(self.player, 0, (-2), 0, 3, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    self.help_cardinal()
                    break
                else:
                    Utility.error()

        def taxation(self):
            while True:
                choice = input("Appena insediato nel tuo vescovato, ti rendi conto che governare una diocesi richiede "
                               "più della sola fede. I conti sono in disordine, il raccolto è stato scarso e i "
                               "bisogni del clero crescono ogni giorno. Seduto nel tuo studio, con il bilancio aperto "
                               "davanti a te, ti viene posta la prima vera scelta del tuo mandato:"
                               "\n1 - Aumenta la tassazione"
                               "\n2 - Mantieni la tassazione invariata"
                               "\n")

                if choice == "1":
                    Utility.fixed_print(
                        "Le casse della diocesi si riempiono lentamente, e i tuoi progetti iniziano a prendere "
                        "forma: nuove panche nella cattedrale, pergameni più pregiati, un coro che finalmente canta "
                        "all’unisono."
                        "Ma nelle strade, le voci si fanno più amare. I contadini sussurrano preghiere stanche, "
                        "e qualcuno comincia a guardare verso i monasteri vicini, dove la vita pare più giusta."
                        "Hai rafforzato il trono… ma incrinato il pulpito."
                        "\n")
                    Player.add_points(self.player, 0, (-2), 0, 1, 2)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "Il popolo ti benedice nei mercati e nei campi. I bambini ti salutano correndo, e i vecchi "
                        "ti chiamano “padre buono”. Ma il tetto della sacrestia continua a gocciolare, "
                        "e il tuo segretario scuote la testa mentre scorre i registri contabili. A Roma, "
                        "pochi notano i vescovi misericordiosi. Hai guadagnato i cuori del tuo gregge… ma forse "
                        "perso terreno sulla via per il soglio pontificio."
                        "\n")
                    Player.add_points(self.player, 0, 2, 0, (-1), 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                else:
                    Utility.error()

            self.lega_cambrai()

        def help_cardinal(self):
            while True:
                choice = input("Bene! Ti sei trasferito a Roma, adesso potrai gestire le grande questioni "
                               "teologiche da vicine conoscere i “pezzi grossi” e avere un rapporto diretto con le "
                               "decisioni prese dalla curia. A pagarne le spese però è la tua gente, che si sente "
                               "abbandonata e lasciata alla mercè delle importanti famiglie nobiliari della zona. "
                               "Nella tua nuova casa, fai conoscenza di un Cardinale molto importante, il "
                               "cardinale Petrucci, senese, che ti chiede un aiuto. Il fratello, funzionario fiscale a "
                               "Siena, è stato condannato per corruzione, e avrebbe bisogno di un luogo in cui "
                               "risiedere per nascondersi aspettando che venga ritirata l’accusa. Essendo tu "
                               "appena arrivato, il cardinal Petrucci reputa che sia più facile avere un si da te, "
                               "ma devi decidere cosa fare."
                               "\n1 - Accetti e aiuti il cardinal Petrucci"
                               "\n2 - Non accetti e rimani fedele ai tuoi principi"
                               "\n")

                if choice == "1":
                    Utility.fixed_print(
                        "Il Cardinale Petrucci te ne è grato, se ne ricorderà, ora hai anche degli importanti "
                        "amici nello stato pontificio. Ma i cittadini del tuo vescovato non sono così "
                        "contenti di ciò, la voce si spande e un criminale in paese non è gradito, "
                        "specialmente se ciò può inasprire i rapporti con le altre signorie."
                        "\n")
                    Player.add_points(self.player, 0, (-1), (-1), 1, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "Hai tenuto una linea dura, hai negato l’aiuto ad un cardinale, egli riconosce il tuo "
                        "carattere, ma non ne sarà contento. Ciò è comunque apprezzato dai cittadini "
                        "che ti vedono come un importante figura per loro e per la tua città."
                        "\n")
                    Player.add_points(self.player, 3, 1, 0, (-2), 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                else:
                    Utility.error()

            self.lega_cambrai()

        def lega_cambrai(self):
            while True:
                choice = input("Siamo ormai nel 1508, i conflitti in Italia, che non ti hanno toccato "
                               "particolarmente, hanno fatto si che Venezia sia diventata una potenza grande, "
                               "forse troppo, in Italia. A questo punto il papa, Giulio II, propone la creazione "
                               "della Lega di Cambrai, unendo Francia, Impero e Spagna per contrastare la questione "
                               "italiana. In quento vescovo vieni chiamato a decidere come comportarti, "
                               "ormai hai abbastanza importanza per ricoprire diversi ruoli."
                               "\n1 - Rimani neutrale"
                               "\n2 - Opponiti alla Lega"
                               "\n3 - Vai in battaglia"
                               "\n4 - Diventa ambiasciatore per lo Stato della Chiesa"
                               "\n")

                if choice == "1":
                    Utility.fixed_print(
                        "“Preferisci non schierarti in questo conflitto.” Decidi che la Chiesa deve mantenere un "
                        "ruolo di pace, evitando di farsi coinvolgere direttamente nelle guerre terrene. La "
                        "neutralità è un terreno sicuro, ma anche fragile: i potenti ti osservano con sospetto, "
                        "chiedendosi se tu sia coraggio o timore. Mentre Venezia cresce incontrollata, "
                        "tu preghi per la saggezza e la pace, consapevole che il silenzio è a volte più eloquente "
                        "delle armi."
                        "\n")
                    self.was_neutral = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "“Vedi nella Lega una minaccia per l’equilibrio e per l’Italia.”  Con fermezza, "
                        "prendi posizione contro l’alleanza proposta da Giulio II. Metti in guardia i confratelli "
                        "sulle conseguenze di un potere eccessivo concentrato nelle mani straniere e sulla "
                        "devastazione che la guerra porterebbe.  La tua voce è un faro per chi teme la perdita "
                        "della sovranità italiana, ma guadagni anche nemici potenti che ti vedono come un ostacolo "
                        "da rimuovere."
                        "\n")

                    Player.add_points(self.player, 0, (-1), 0, (-2), 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    self.opposer()
                    break
                elif choice == "3":
                    Utility.fixed_print(
                        "“La fede si difende anche con la spada.”  Accetti di guidare o appoggiare le truppe della "
                        "Chiesa in questa guerra decisiva. Il tuo ruolo si fa concreto, fra le spade e i fumi della "
                        "battaglia.  Rischi la vita, ma anche la gloria. Il sangue versato per la fede può aprire "
                        "la strada a un futuro di potere e rispetto. Oppure a una fine prematura."
                        "\n")

                    Player.add_points(self.player, (-2), (-1), 0, 3, 0)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    break
                elif choice == "4":
                    Utility.fixed_print(
                        "“Preferisci la diplomazia alla guerra.”  Accetti l’incarico di rappresentare il Papa "
                        "presso le corti straniere. Il tuo carisma e la tua intelligenza saranno armi decisive "
                        "nella complessa rete di alleanze e tradimenti.  Nel palazzo, tra banchetti e intrighi, "
                        "plasmerai il destino della Chiesa senza versare una goccia di sangue. Ma la diplomazia è "
                        "un gioco sottile, dove un passo falso può costare tutto."
                        "\n")

                    Player.add_points(self.player, 0, 0, 0, 0, 3)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    self.ambassador()
                    break
                else:
                    Utility.error()

        def opposer(self):
            while True:
                choice = input("Opporsi alla Lega, sì… ma come? Con voce alta e pubblica, rischiando scomuniche e "
                               "accuse di tradimento? O nell’ombra, con discrezione e diplomazia, per preservare il "
                               "tuo ruolo e la tua ascesa?"
                               "\n1 - Pubblicamente"
                               "\n2 - Nell'ombra"
                               "\n")

                if choice == "1":
                    prob = random.randint(1, 100)
                    if prob <= 70:
                        Utility.fixed_print(
                            "Ti alzi in piedi, facendo scricchiolare il legno della sedia, e afferri la penna con "
                            "mano ferma. La tua firma comparirà su lettere aperte, proclami e omelie: parole "
                            "pesanti come spade. Denuncerai l’avidità travestita da crociata, sfiderai apertamente "
                            "i principi della Lega e forse, persino, la volontà del Santo Padre. Sai che questo "
                            "potrebbe costarti tutto: la diocesi, la protezione politica, forse anche la vita. Ma "
                            "il tuo cuore è saldo, e la tua fede ti guida. Se la verità deve essere detta, la dirai "
                            "tu."
                            "\n")
                        Player.add_points(self.player, 0, 3, 0, 0, 0)
                        Utility.print_points(self.player.print_stats())
                        self.was_opposer = True

                        Utility.go_on()

                        self.lega_santa()
                        break
                    elif prob > 70:
                        Utility.fixed_print(
                            "Il decreto arriva all’alba, portato da un cavallo stremato e mani tremanti. Il "
                            "messaggero non osa guardarti negli occhi mentre consegna la pergamena. Rompi il "
                            "sigillo con dita fredde. Le parole, vergate in latino solenne, ti colpiscono come un "
                            "giudizio eterno: anathema sit.Scomunicato.Le campane della cattedrale suonano a morto, "
                            "ma non per un corpo — per un’anima tagliata fuori dalla Chiesa. I tuoi alleati si "
                            "dissolvono come nebbia al sole, i fedeli evitano il tuo sguardo, e persino le statue "
                            "sembrano voltarsi. In un istante, sei passato da vescovo rispettato a ombra "
                            "maledetta.Eppure, nel fondo della tua cella privata, tra le pareti nude e il silenzio "
                            "dei rinnegati, senti ancora ardere la fiamma della giustizia. La Chiesa ti ha "
                            "cacciato."
                            "\n")
                        Utility.gameover()
                        break
                    else:
                        Utility.error()

                elif choice == "2":
                    Utility.fixed_print(
                        "Rimani seduto, lo sguardo fisso sul calice d’argento sullo scaffale. Sai che un solo passo "
                        "falso potrebbe farti scomparire dal gioco sacro del potere. Ma il silenzio non è "
                        "complicità, se usato con astuzia. Agirai attraverso contatti fidati, favorirai i nemici "
                        "della Lega con discreti appoggi, sosterrai la pace dove puoi e indebolirai la guerra dove "
                        "serve. Non sarai un martire, ma una mente nell’ombra. Un giorno, forse, servirà un papa "
                        "abile più che audace — e tu sarai pronto."
                        "\n")
                    Player.add_points(self.player, 0, 0, 0, (-1), 2)
                    Utility.print_points(self.player.print_stats())

                    Utility.go_on()

                    self.lega_santa()
                    break
                else:
                    Utility.error()

        def battle(self):
            while True:
                choice = input("Vesti l’armatura sopra l’abito da vescovo e guida uomini alla guerra. Sarai al fianco "
                               "del Papa nelle campagne contro Venezia, e la tua fedeltà non passerà inosservata. "
                               "Puoi scegliere cosa fare, come vivere la battaglia"
                               "\n1 - Vai in prima linea"
                               "\n2 - Rimani nelle retrovie"
                               "\n")

                if choice == "1":
                    Utility.fixed_print(
                        "Sali a cavallo, stringi la spada, e ti metti davanti ai tuoi uomini. Urli un salmo, "
                        "e lanci la carica. Vuoi mostrare che la fede può essere anche fuoco e acciaio. "
                        "Guadagnandoti il ripetto del soglio pontificio"
                        "\n")

                    Utility.go_on()

                    self.front_battle()
                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "Ti fermi vicino alle retrovie. Le mani tremano, le preghiere si intrecciano con il panico. "
                        "Non sei fatto per la guerra, lo capisci adesso. Guardi i tuoi uomini andare, e speri solo "
                        "che tornino. Ora però, l’attacco non è detto che vada bene, potresti fallire o riuscire in "
                        "una grande impresa."
                        "\n")

                    self.battle_neutral = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                else:
                    Utility.error()

        def front_battle(self):
            prob1 = random.randint(1, 100)

            if prob1 <= 65:
                prob2 = random.randint(1, 100)

                if prob2 <= 75:
                    Utility.fixed_print(
                        "Un colpo improvviso ti sbalza da cavallo. Le truppe si disperdono, i tamburi nemici "
                        "battono forte. Il fango ti avvolge, il tuo elmo è rotto. Qualcuno ti salva, "
                        "forse un soldato fedele, forse solo il caso.  Le tue braccia sono lesionate, il tuo corpo "
                        "sanguina, ma tu ti tiene aggrappato alla vita con un filo di respiro, sei costretto a "
                        "ritiraru, ma nonostante ciò sipravvivo fino, dopo dei mesi, a riprenderti completamente."
                        "\n")

                    Player.add_points(self.player, 3, (-1), 0, (-2), 0)
                    Utility.print_points(self.player.print_stats())
                    self.battle_injured = True

                    self.lega_santa()
                elif prob2 > 75:
                    Utility.fixed_print(
                        "Il sangue ormai scorre a fiumi, non senti più il tuo corpo, i tuoi occhi si spengono, "
                        "la ferita ti ha portato alla morte. La tua ascesa al soglio di Pietro finisce qui."
                        "\n")
                    Utility.gameover()
                else:
                    Utility.error()

            elif prob1 > 65:
                Utility.fixed_print(
                    "Il sole sorgeva rosso sul campo di battaglia, tingendo il cielo del colore del sangue versato "
                    "e di quello che ancora sarebbe stato sparso. Avevi ormai lasciato da tempo le aule silenziose "
                    "dei monasteri e i corridoi marmorei delle cattedrali: ora portavi la croce sul petto, "
                    "ma anche la spada al fianco.Vestivi ancora gli abiti da vescovo, ma sopra di essi, l'armatura "
                    "scintillava. La tua decisione di unirti alla Lega di Cambrai non era stata presa a cuor "
                    "leggero. Ma il Papa stesso, Giulio II — il \"Papa guerriero\" — aveva benedetto la causa. "
                    "Venezia aveva sfidato l'autorità della Santa Sede troppo a lungo, e tu, uomo di Dio e uomo "
                    "d'azione, avevi risposto alla chiamata.Le truppe marciavano al tuo comando. Nobili e soldati, "
                    "contadini e cavalieri, ti seguivano non solo per la tua abilità strategica, ma per la tua fede "
                    "incrollabile. Portavi con te una reliquia sacra, e pregavi ogni sera prima della battaglia. I "
                    "tuoi uomini dicevano che dove tu alzavi lo stendardo, la vittoria non tardava ad arrivare.E "
                    "così fu.La battaglia fu aspra, ma la tua guida ferma, il tuo coraggio e la tua devozione "
                    "ispirarono un fervore che neppure i più esperti condottieri potevano replicare. Le forze "
                    "veneziane si dispersero come polvere al vento. Al termine dello scontro, col campo quieto e la "
                    "nebbia della guerra che si ritirava, il tuo nome era sulle labbra di tutti.Giunse presto il "
                    "messaggero da Roma. Era vestito di porpora e oro, e portava un sigillo papale. Si inginocchiò "
                    "dinanzi a te e lesse ad alta voce:“In riconoscimento del tuo valore in battaglia, "
                    "della tua incrollabile fedeltà alla Santa Chiesa, e della tua sacra devozione, Sua Santità "
                    "Papa Giulio II ti eleva alla dignità di Cardinale della Santa Romana Chiesa. Che la tua nuova "
                    "porpora sia tanto ardente quanto il fuoco della tua fede.”La folla esplose in un coro di "
                    "giubilo. Tu chinasti il capo, in silenziosa preghiera. Ma sapevi, nel profondo, che questo era "
                    "solo un passo. Un passo sulla via per la Tiara. La Croce ora brillava più vicina."
                    "\n")
                self.player.isbishop = False
                self.player.iscardinal = True

                Utility.go_on()

                Game.Conclave(self.player)
            else:
                Utility.error()

        def ambassador(self):
            while True:
                choice = input("Hai scelto il cammino dell’ambasciatore. Ora il Papa conta su di te per difendere gli "
                               "interessi della Chiesa in terra straniera. Prima di partire, però, devi decidere dove "
                               "andrai a svolgere la tua missione. Il segretario papale ti porge due lettere "
                               "sigillate. Una ti manda in Francia, l’altra nel Sacro Romano Impero. Cosa scegli?"
                               "\n1 - Francia"
                               "\n2 - Sacro Romano Impero"
                               "\n")

                if choice == "1":
                    Utility.fixed_print(
                        "Scegli di andare nel Regno di Francia, alla corte di Luigi XII, i rapporti sono ottimi. La "
                        "Francia è alleata del Papa nella guerra contro Venezia. Il Re è potente e la sua corte è "
                        "piena di nobili e vescovi."
                        "\n")
                    Player.add_points(self.player, 0, 0, 2, 0, 0)
                    Utility.print_points(self.player.print_stats())
                    self.was_france_ambassador = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                elif choice == "2":
                    Player.add_points(self.player, 0, (-2), 0, 0, 0)
                    Utility.print_points(self.player.print_stats())

                    self.sri_ambassador()
                    break
                else:
                    Utility.error()

        def sri_ambassador(self):
            while True:
                choice = input("L’Impero è grande e complicato. I principi locali iniziano a dubitare della Chiesa, "
                               "e il Papa guarda con sospetto a certe idee che iniziano a circolare. Puoi agire in "
                               "due modi:"
                               "\n1 - Duramente"
                               "\n2 - In maniera pacata"
                               "\n")

                if choice == "1":
                    Utility.fixed_print(
                        "Parli chiaro e forte. Rappresenti l’autorità del Papa. Pretendi obbedienza e minacci chi "
                        "si oppone."
                        "\n")
                    Player.add_points(self.player, 0, 0, 0, 2, (-1))
                    Utility.print_points(self.player.print_stats())
                    self.was_sri_strong = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                elif choice == "2":
                    Utility.fixed_print(
                        "Cerchi il dialogo, ascolti, parli con tatto. Tratti con principi e città per mantenere "
                        "la pace e rafforzare la fede."
                        "\n")
                    Player.add_points(self.player, 0, 1, 2, 0, 1)
                    Utility.print_points(self.player.print_stats())
                    self.was_sri_calm = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                else:
                    Utility.error()

        def lega_santa(self):
            while True:
                choice = input("È il 1511, Giulio II ha forgiato un nuovo patto: la Lega Santa. Contro la Francia, "
                               "ex alleata, ora minaccia crescente. I confini tremano, le alleanze si spezzano, "
                               "le coscienze si dividono. Il mondo osserva… e tu? Hai custodito il silenzio mentre "
                               "altri gridavano. Hai protetto il gregge mentre vescovi e ambasciatori si spartivano "
                               "le mappe. Ma ora la guerra non ti lascia più margine. I campi bruciano, le chiese si "
                               "dividono, i nobili bussano alla tua porta esigendo una risposta. Il tempo "
                               "dell’equilibrio è finito. Ora devi scegliere come schierarti."
                               "\n1 - A favore della Lega Santa"
                               "\n2 - Contro la Lega Santa"
                               "\n")

                if choice == "1":
                    if self.was_neutral:
                        Utility.fixed_print(
                            "Dopo mesi di silenzio e riflessione, decidi che il tempo dell’inazione è finito. Ora "
                            "che la minaccia francese si fa più reale, schierarti con la Lega Santa significa "
                            "difendere la Chiesa e l’Italia da un pericolo imminente. I tuoi confratelli apprezzano "
                            "il coraggio, e tu entri con forza nella partita, pronto a sostenere il Papa nella "
                            "guerra che divampa. Il tuo silenzio si trasforma in voce, la tua prudenza in decisione."
                            "\n")

                        Player.add_points(self.player, (-1), 0, 2, 2, 0)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_france_ambassador:
                        Utility.fixed_print(
                            "Come ambasciatore, la tua diplomazia ora sostiene la Lega Santa. Usi ogni parola, "
                            "ogni sorriso per tessere alleanze e rafforzare la posizione del Papa. Il tuo ruolo è "
                            "decisivo per evitare che la guerra si trasformi in un disastro totale. Dietro le "
                            "quinte, però, sai che ogni trattativa nasconde compromessi dolorosi e tradimenti "
                            "silenziosi."
                            "\n")

                        Player.add_points(self.player, (-1), (-2), (-1), 2, 0)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_sri_strong:
                        Utility.fixed_print(
                            "Come ambasciatore, la tua diplomazia ora sostiene la Lega Santa. Usi ogni parola, "
                            "ogni sorriso per tessere alleanze e rafforzare la posizione del Papa. Il tuo ruolo è "
                            "decisivo per evitare che la guerra si trasformi in un disastro totale. Dietro le "
                            "quinte, però, sai che ogni trattativa nasconde compromessi dolorosi e tradimenti "
                            "silenziosi."
                            "\n")

                        Player.add_points(self.player, (-1), 0, (-2), 1, (-2))
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_sri_calm:
                        Utility.fixed_print(
                            "Come ambasciatore, la tua diplomazia ora sostiene la Lega Santa. Usi ogni parola, "
                            "ogni sorriso per tessere alleanze e rafforzare la posizione del Papa. Il tuo ruolo è "
                            "decisivo per evitare che la guerra si trasformi in un disastro totale. Dietro le "
                            "quinte, però, sai che ogni trattativa nasconde compromessi dolorosi e tradimenti "
                            "silenziosi."
                            "\n")

                        Player.add_points(self.player, 1, 1, 0, 1, 2)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_opposer:
                        Utility.fixed_print(
                            "Nonostante la tua opposizione passata, la situazione ti costringe a un ripensamento. "
                            "La Lega Santa è l’ultima speranza per fermare la Francia, un nemico troppo pericoloso "
                            "per essere ignorato. Il tuo sostegno arriva come un segnale di unità, un gesto che "
                            "mira a salvare ciò che resta della pace e dell’autorità papale. Ma i tuoi detrattori "
                            "ti accusano di incoerenza. Tu rispondi che la fedeltà alla Chiesa viene prima di ogni "
                            "altra cosa."
                            "\n")

                        Player.add_points(self.player, (-1), (-2), 0, 1, 0)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.battle_injured:
                        Utility.fixed_print(
                            "Il sangue scorre, le ferite bruciano, ma non pieghi il ginocchio. La tua dedizione "
                            "alla Lega Santa ti ha portato a rischiare tutto, e il dolore fisico è solo un prezzo "
                            "da pagare per la fede e il potere. Il tuo coraggio ispira chi ti sta vicino, "
                            "la tua sofferenza diventa leggenda. Eppure, sai che le cicatrici porteranno un peso "
                            "anche oltre la guerra, segnando ogni tuo passo futuro."
                            "\n")

                        Player.add_points(self.player, (-1), 0, 0, 2, 0)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.battle_neutral:
                        Utility.fixed_print(
                            "Il campo di battaglia è un teatro di fuoco e fiamme, ma la fortuna è stata dalla tua "
                            "parte. Hai guidato le truppe con coraggio e astuzia, senza subire ferite. La tua "
                            "figura emerge come un simbolo di forza e resilienza, pronto a sostenere la causa della "
                            "Lega Santa con il vigore di chi ha dimostrato il proprio valore senza mai vacillare. I "
                            "tuoi alleati ti guardano con ammirazione, i nemici con rispetto — ma sai che la guerra "
                            "è solo all’inizio."
                            "\n")

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    else:
                        Utility.error()
                elif choice == "2":
                    if self.was_neutral:
                        Utility.fixed_print(
                            "Rimani coerente alla tua scelta di neutralità, ma questa volta la posta è più alta. La "
                            "Lega Santa, con la sua ferocia, ti sembra un’ulteriore fonte di devastazione. Critichi "
                            "apertamente l’alleanza, ma molti ti guardano con sospetto. Il Papa vede in te un "
                            "ostacolo, e i nobili iniziano a dubitare della tua fedeltà. Il tempo della neutralità "
                            "è passato. Ora ti giochi tutto."
                            "\n")

                        Player.add_points(self.player, 2, 2, 0, (-1), 0)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_france_ambassador:
                        Utility.fixed_print(
                            "Mentre altri firmano patti e stringono mani, tu scegli la via del dissenso "
                            "diplomatico. Denunci la Lega Santa come fonte di conflitto inutile, "
                            "proponi alternative pacifiche, anche se pochi ti ascoltano. La tua posizione è "
                            "rischiosa: metti in gioco la tua carriera e la tua stessa vita. Ma nella storia, "
                            "forse sarai ricordato come colui che ha avuto il coraggio di dire no."
                            "\n")

                        Player.add_points(self.player, 2, 1, 0, (-2), 2)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_sri_strong:
                        Utility.fixed_print(
                            "Mentre altri firmano patti e stringono mani, tu scegli la via del dissenso "
                            "diplomatico. Denunci la Lega Santa come fonte di conflitto inutile, "
                            "proponi alternative pacifiche, anche se pochi ti ascoltano. La tua posizione è "
                            "rischiosa: metti in gioco la tua carriera e la tua stessa vita. Ma nella storia, "
                            "forse sarai ricordato come colui che ha avuto il coraggio di dire no."
                            "\n")

                        Player.add_points(self.player, (-1), 2, 0, (-2), 2)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_sri_calm:
                        Utility.fixed_print(
                            "Mentre altri firmano patti e stringono mani, tu scegli la via del dissenso "
                            "diplomatico. Denunci la Lega Santa come fonte di conflitto inutile, "
                            "proponi alternative pacifiche, anche se pochi ti ascoltano. La tua posizione è "
                            "rischiosa: metti in gioco la tua carriera e la tua stessa vita. Ma nella storia, "
                            "forse sarai ricordato come colui che ha avuto il coraggio di dire no."
                            "\n")

                        Player.add_points(self.player, 3, 0, (-2), (-2), 1)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_opposer:
                        Utility.fixed_print(
                            "Rimani saldo nelle tue convinzioni: la Lega Santa è solo un’altra forma di guerra e "
                            "oppressione. La tua opposizione si fa più dura, quasi un atto di ribellione. Molti ti "
                            "temono, alcuni ti evitano. Ma fra la gente comune e i nobili disillusi, "
                            "raccogli consensi silenziosi. Sei un faro per chi sogna un’Italia libera e una Chiesa "
                            "meno guerriera."
                            "\n")

                        Player.add_points(self.player, 2, 3, 2, (-2), 0)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.battle_injured:
                        Utility.fixed_print(
                            "Ferito in battaglia, la tua scelta di opporsi alla Lega Santa assume un significato "
                            "ancor più profondo. Il tuo corpo segna il prezzo del conflitto, mentre la tua anima "
                            "resta fedele a ciò in cui credi. La tua sofferenza ti rende simbolo di resistenza, "
                            "un esempio per chi rifiuta la guerra imposta dalla Lega. Ma la strada è dura e la "
                            "ripresa incerta. Il rischio è grande, ma la tua causa vale ogni dolore."
                            "\n")

                        Player.add_points(self.player, 3, (-2), 0, (-2), 0)
                        Utility.print_points(self.player.print_stats())

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.battle_neutral:
                        Utility.fixed_print(
                            "Hai scelto di combattere, ma non al fianco della Lega. Pur non subendo ferite, "
                            "il peso della battaglia grava su di te: combatti per un ideale, sfidando i poteri "
                            "consolidati. La tua presenza sul campo è un segnale forte di dissenso, "
                            "eppure la mancanza di ferite ti permette di mantenere lucidità e strategia per guidare "
                            "chi condivide la tua causa. Il prezzo della guerra è alto, ma la tua determinazione "
                            "non si spegne."
                            "\n")

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    else:
                        Utility.error()
                else:
                    Utility.error()

        def try_become_cardinal(self):
            if self.player.isbishop and self.player.consensus >= 1:
                Utility.fixed_print(
                    "Le campane di Roma risuonano con un’eco solenne e profonda, mentre il Papa stesso ti "
                    "conferisce il prezioso anello rosso. Quel segno di fuoco non è solo un ornamento, "
                    "ma un simbolo di potere e responsabilità che ora porti con dignità sulle dita.Sei entrato "
                    "nell’élite della Chiesa, tra coloro che plasmano il destino della fede e delle nazioni. I tuoi "
                    "passi echeggiano nei corridoi del Vaticano, dove le decisioni si intrecciano con intrighi e "
                    "visioni di un mondo migliore.Il tuo sguardo si posa oltre l’orizzonte: la tiara papale non è "
                    "lontana, e tu sei pronto a salire, un gradino alla volta, verso quel sogno."
                    "\n")

                self.player.isbishop = False
                self.player.iscardinal = True

                Utility.go_on()

                Game.Conclave(self.player).compare()

    class Conclave:
        def __init__(self, player):
            self.player = player

            self.cardinal_name = ""
            self.cardinal_values = []

            # Cardinal Values
            (self.card_voc, self.card_pop_agr, self.pol_infl,
             self.card_cur_rel, self.card_dipl_skills) = [0, 0, 0, 0, 0]

            # Cardinal that will vote for you
            self.infavor = 0

        def compare(self):
            self.player.isbishop = False
            self.player.iscardinal = True

            Utility.fixed_print(
                "Le porte del Vaticano si chiudono con un tonfo secco, isolando i cardinali dal mondo esterno. La "
                "Cappella Sistina si trasforma in un teatro di silenzi pesanti, dove ogni sguardo pesa come un "
                "giudizio, e ogni sussurro può essere un segreto o una minaccia.Fuori, Roma attende con il fiato "
                "sospeso, consapevole che lì dentro si sta decidendo il destino della Chiesa e forse del mondo "
                "intero. Le fumate bianche e nere si alternano, segnali misteriosi di speranza o di stallo.Ore e "
                "giorni si susseguono, mentre le voci si intrecciano tra alleanze oscure e promesse non dette. Il "
                "tuo cuore batte forte, sapendo che una sola parola, un solo voto, può cambiare tutto.Infine, "
                "arriva il momento dello spoglio. I cardinali si raccolgono attorno al grande tavolo, "
                "le mani tremano appena, gli occhi si incrociano con un misto di speranza e paura.Una pergamena "
                "dopo l’altra, i nomi vengono letti ad alta voce. Ogni voto è un colpo che riecheggia nella "
                "cappella: c’è chi trattiene il respiro, chi stringe i pugni, chi prega silenziosamente. Il tuo "
                "nome potrebbe comparire da un momento all’altro.Il silenzio si fa quasi palpabile, rotto solo dal "
                "fruscio dei fogli e dal sussurro delle promesse infrante. Il destino di secoli è nelle mani di "
                "quel piccolo gruppo, e ogni voto pesa come un macigno.Il cuore ti batte forte, il respiro si fa "
                "corto, mentre l’ultimo voto viene pronunciato.Un momento di attesa estenuante, poi la sentenza: "
                "qualcuno è stato scelto. O forse no, e la fumata tornerà a salire, nera, portando con sé la "
                "tensione di un nuovo giorno di incertezza."
                "\n")

            Utility.go_on()

            if self.player.iscardinal:
                for i in cardinals.values():
                    points = 0

                    (self.card_voc, self.card_pop_agr, self.card_pol_infl,
                     self.card_cur_rel, self.card_dipl_skills) = i

                    if self.player.voc >= self.card_voc:
                        points += 1
                    if self.player.pop_agr >= self.card_pop_agr:
                        points += 1
                    if self.player.pol_infl >= self.card_pol_infl:
                        points += 1
                    if self.player.cur_rel >= self.card_cur_rel:
                        points += 1
                    if self.player.dipl_skills >= self.card_dipl_skills:
                        points += 1

                    # Check for cardinal favor
                    if points >= 3:
                        self.infavor += 1

                # Check if sufficient cardinals are in favor
                if self.infavor >= 20:
                    self.popenomination()

        @staticmethod
        def popenomination():
            Utility.fixed_print(
                "Dopo anni di intrighi vaticani, manovre diplomatiche, preghiere segrete e miracoli sospetti… ci "
                "sei riuscito.La Cappella Sistina è silenziosa.La folla in Piazza San Pietro trattiene il respiro. "
                "Un sottile filo di fumo bianco si alza lento nel cielo di Roma. È il segnale. È il momento.Sei "
                "tu.I cardinali ti hanno scelto. Dopo lunghe votazioni e sussurri dietro stalli di legno antico, "
                "la decisione è arrivata: sei stato eletto Pontefice, guida spirituale di oltre un miliardo di "
                "fedeli. Il trono di Pietro ora è tuo.Il Maestro delle Celebrazioni Liturgiche Pontificie si "
                "avvicina e ti sussurra:“Sanctitas tua, come desiderate chiamarvi?”Scegli un nome. Forse un tributo "
                "ai santi. Forse un segno di rottura. Ma ora non sei più solo un uomo. Sei il Vicario di "
                "Cristo.Indossi la bianca veste papale. Ti guardi un’ultima volta allo specchio, ma l’uomo riflesso "
                "non sei più tu: è il Papa.Il Cardinale Protodiacono si affaccia al balcone centrale e "
                "annuncia:“Habemus Papam!”La piazza esplode in un boato di giubilo.Campane. Lacrime. Fedi che si "
                "rinnovano.Hai vinto.Non solo il gioco. Hai conquistato il cuore della Chiesa.Il mondo ora ti "
                "guarda. Ogni parola, ogni gesto sarà storia.FINE DEL GIOCOMa solo l’inizio del pontificato.Che Dio "
                "ti guidi… Santità."
                "\n")

            Utility.gameover()


game = Game()
game.start()
