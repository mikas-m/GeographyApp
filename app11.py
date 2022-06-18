from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.core.window import Window
Window.size = (500, 600)
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior


class Izbornik(BoxLayout):
    screen_manager = ObjectProperty(None)
    nav_drawer = ObjectProperty(None)

class gustoca(Screen):
    P_gust = ObjectProperty(float)
    A = ObjectProperty(float)

    def gust(self):
        P_gust = self.root.ids.P_gust.text
        A = self.root.ids.A.text

        if len(self.root.ids.P_gust.text) > 0:
            if len(self.root.ids.A.text) > 0:
                if int(self.root.ids.A.text) != 0:
                    gust_rez = float(P_gust) / float(A)
                    gust_rez = round(gust_rez, 3)
                    gust_rez = str(gust_rez)
                    self.dialog = MDDialog(title="Gustoća naseljenosti iznosi " + gust_rez + " stan./km[sup]2[/sup].")
                    self.dialog.open()
                else:
                    self.root.ids.A.line_color_focus: [255/255, 0/255, 0/255, 1]
                    self.root.ids.A.text = ''
            else:
                self.root.ids.A.text = "..."
                self.root.ids.A.text = ''
        else:
            self.root.ids.P_gust.text = "..."
            self.root.ids.P_gust.text = ''

    def close_dialog(self):
        self.dialog.dismiss()

    def gusto_info(self):
        self.dialog = MDDialog(
            text="Aplikacija izračunava aritmetičku gustoću naseljenosti, ali postoje i tzv. posebne "
                 "- fiziološka (broj stanovnika na jedinici površine pogodne za obradu), "
                 "te poljoprivredna, agrarna, ruralna i urbana gustoća naseljenosti.")
        self.dialog.open()

    def gusto_vise(self):
        self.dialog = MDDialog(
            text="Klasifikacija gustoće naseljenosti:\n"
                 "1) prenaseljeni prostori > 100 stan.km[sup]2[/sup]\n"
                 "2) gusto naseljeni prostori = 51 - 100 stan./km[sup]2[/sup]\n"
                 "3) srednje naseljeni prostori = 10 - 51 stan./km[sup]2[/sup]\n"
                 "4) rijetko naseljeni prostori < 10 stan./km[sup]2[/sup]")
        self.dialog.open()

class prir_kretanje(Screen):
    N = ObjectProperty(float)
    M = ObjectProperty(float)
    D = ObjectProperty(int)
    Z = ObjectProperty(float)
    f = ObjectProperty(float)
    P_kret = ObjectProperty(float)

    def prir(self):
        N = self.root.ids.N.text
        M = self.root.ids.M.text
        P_kret = self.root.ids.P_kret.text

        if len(self.root.ids.N.text) > 0:
            if len(self.root.ids.M.text) > 0:
                if len(self.root.ids.P_kret.text) > 0:
                    if float(self.root.ids.P_kret.text) != 0:
                        stopan = (float(N) * 1000 / float(P_kret))
                        stopan = round(stopan, 2)
                        stopam = (float(M) * 1000 / float(P_kret))
                        stopam = round(stopam, 2)
                        prirk = float(N) - float(M)
                        prirk = round(prirk, 0)
                        stopap = stopan - stopam
                        stopap = round(stopap, 2)
                        stopan = str(stopan)
                        stopam = str(stopam)
                        prirk = str(prirk)
                        stopap = str(stopap)
                        self.dialog = MDDialog(
                            title="Stopa rodnosti iznosi " + stopan + "‰,\n"
                                  "stopa smrtnosti iznosi " + stopam + "‰,\n"
                                  "prirodno kretanje iznosi " + prirk + " stanovnika,\n"
                                  "a njegova stopa " + stopap + "‰.")
                        self.dialog.open()

                    else:
                        self.root.ids.P_kret.text = "Nema stanovnika?"
                        self.root.ids.P_kret.text = ''
                else:
                    self.root.ids.P_kret.text = "Nema stanovnika?"
                    self.root.ids.P_kret.text = ''
            else:
                self.root.ids.M.text = "Nitko nije umro?"
                self.root.ids.M.text = ''
        else:
            self.root.ids.N.text = "Nitko se nije rodio?"
            self.root.ids.N.text = ''

    def prirodno_info(self):
        self.dialog = MDDialog(
            text="Izračunava se ukupno prirodno kretanje, njegova stopa te stope rodnosti i smrnosti u promilima, "
                 "dakle, na 1000 stanovnika.\n\n"
                 "Za izračun potreban je broj rođenih, umrlih i broj stanovnika.")
        self.dialog.open()

    def prirodno_vise(self):
        self.dialog = MDDialog(
            text="Klasifikacija stopa rodnosti:\n"
                 "1) visoke stope > 25‰\n"
                 "2) srednje stopa = 16 - 25‰\n"
                 "3) niske stope < 15‰"
                 )
        self.dialog.open()

    def doj(self):
        D = self.root.ids.D.text
        Z = self.root.ids.Z.text

        if len(self.root.ids.D.text) > 0:
            if len(self.root.ids.Z.text) > 0:
                if int(self.root.ids.Z.text) > 0:
                    stopasd = float(((int(D) * 1000) / int(Z)))
                    stopasd = round(stopasd, 2)
                    stopasd = str(stopasd)
                    self.dialog = MDDialog(
                        title="Stopa smrtnosti dojenčadi / infatilnog mortaliteta iznosi " + stopasd + "‰.")
                    self.dialog.open()
                else:
                    self.root.ids.Z.text = "Nitko se nije rodio?"
                    self.root.ids.Z.text = ''
            else:
                self.root.ids.Z.text = "Nitko se nije rodio?"
                self.root.ids.Z.text = ''
        else:
            self.root.ids.D.text = "Nitko nije umro?"
            self.root.ids.D.text = ''

    def doj_info(self):
        self.dialog = MDDialog(
            text="Izračunava se odnos umrle dojenčadi na 1000 stanovnika. Za izračun je potreban "
                 "broj umrle dojenčadi i živorođenih.")
        self.dialog.open()

    def doj_vise(self):
        self.dialog = MDDialog(
            text="Podatak primarno ukazuje na razvijenost zdravstvene zaštite, ali i društveno-gospodarskih "
                 "prilika.")
        self.dialog.open()

    def vit(self):
        Z = self.root.ids.Z.text
        M = self.root.ids.M.text

        if len(self.root.ids.Z.text) > 0:
            if len(self.root.ids.M.text) > 0:
                vitalni = ((float(Z) * 100) / float(M))
                vitalni = round(vitalni, 2)
                vitalni = str(vitalni)
                self.dialog = MDDialog(title="Vitalni indeks iznosi " + vitalni + ".")
                self.dialog.open()

            else:
                self.root.ids.M.text = "Nitko nije umro?"
                self.root.ids.M.text = ''
        else:
            self.root.ids.Z.text = "Nitko se nije rodio?"
            self.root.ids.Z.text = ''

    def vit_info(self):
        self.dialog = MDDialog(
            text="Izračunava odnos živorođenih na 100 umrlih osoba. Za izračun je potreban broj živorođenih "
                 "i umrlih.")
        self.dialog.open()

    def vit_vise(self):
        self.dialog = MDDialog(
            text="Vitalni indeks je pokazatelj smjera prirodnog kretanja stanovništva te ukazuje na zdravstvenu "
                 "zaštitu "
                 "i društvene procese.")
        self.dialog.open()

    def fert(self):
        N = self.root.ids.N.text
        f = self.root.ids.f.text

        if len(self.root.ids.N.text) > 0:
            if len(self.root.ids.f.text) > 0:
                stopaf = ((float(N) * 1000) / float(f))
                stopaf = round(stopaf, 2)
                stopaf = str(stopaf)
                self.dialog = MDDialog(title="Opća stopa fertiliteta iznosi " + stopaf + ".")
                self.dialog.open()
            else:
                self.root.ids.f.text = "Nema niti jedne ženske osobe?"
                self.root.ids.f.text = ''
        else:
            self.root.ids.N.text = "Nitko se nije rodio?"
            self.root.ids.N.text = ''

    def fert_info(self):
        self.dialog = MDDialog(
            text="Izračunava se totalna stopa fertiliteta za što je potreban broj rođenih i broj stanovnika u "
                 "plodnoj dobi.")
        self.dialog.open()

    def fert_vise(self):
        self.dialog = MDDialog(
            text="Osim stope ukupnog fertiliteta, može se izračunati i broj djece na 1000 žena u populaciji "
                 "(opća stopa)"
                 ", broj djece na 1000 žena određene dobi ili petogodišnjih skupina (specifična stopa) ili prosječan "
                 "broj "
                 "djece koje bi žena rodila u fertilnom razdoblju (15-49), ako bi fertilitet ostao isti (ukupna stopa "
                 "fertiliteta).")
        self.dialog.open()

class pros_kretanje(Screen):
    I = ObjectProperty(float)
    E = ObjectProperty(float)
    P_kreta = ObjectProperty(float)

    def pros(self):
        I = self.root.ids.I.text
        E = self.root.ids.E.text
        P_kreta = self.root.ids.P_kreta.text

        if len(self.root.ids.I.text) > 0:
            if len(self.root.ids.E.text) > 0:
                if len(self.root.ids.P_kreta.text) > 0:
                    if float(self.root.ids.P_kreta.text) != 0:
                        stopai = (float(I) * 1000 / float(P_kreta))
                        stopai = round(stopai, 2)
                        stopae = (float(E) * 1000 / float(P_kreta))
                        stopae = round(stopae, 2)
                        prosk = float(I) - float(E)
                        stopapr = stopai - stopae
                        stopapr = round(stopapr, 2)
                        stopai = str(stopai)
                        stopae = str(stopae)
                        prosk = str(prosk)
                        stopapr = str(stopapr)
                        self.dialog = MDDialog(
                            title="Stopa useljavanja iznosi " + stopai + "‰,\n"
                                  "stopa iseljavanja iznosi " + stopae + "‰,\n"
                                  "prostorno kretanje iznosi " + prosk + " stanovnika,\n"
                                  "a njegova stopa " + stopapr + "‰.")
                        self.dialog.open()

                    else:
                        self.root.ids.P_kreta.text = "Nema stanovnika?"
                        self.root.ids.P_kreta.text = ''
                else:
                    self.root.ids.P_kreta.text = "Nema stanovnika?"
                    self.root.ids.P_kreta.text = ''
            else:
                self.root.ids.E.text = "Nitko nije iselio?"
                self.root.ids.E.text = ''
        else:
            self.root.ids.I.text = "Nitko nije uselio?"
            self.root.ids.I.text = ''

    def pros_info(self):
        self.dialog = MDDialog(
            text="Izračunava se ukupno prostorno kretanje, njegova stopa te stope useljavanja i iseljavanja u "
                 "promilima, dakle, na 1000 stanovnika.\n\nZa izračun potreban je broj useljenih, iseljenih i "
                 "broj stanovnika.")
        self.dialog.open()

    def pros_vise(self):
        self.dialog = MDDialog(
            text="U ekonomiji znanja, u kojoj obrazovanje predstavlja temelj napretka, još važnija postaje kategorija "
                 "odljeva mozgova - Albert Einstein, Elon Musk, Hedy Lamarr!")
        self.dialog.open()

class tip(Screen):
    N_tip = ObjectProperty(float)
    M_tip = ObjectProperty(float)
    I_tip = ObjectProperty(float)
    E_tip = ObjectProperty(float)
    bspg = ObjectProperty(float)
    bsdg = ObjectProperty(float)

    def tipo(self):
        N_tip = self.root.ids.N_tip.text
        M_tip = self.root.ids.M_tip.text
        I_tip = self.root.ids.I_tip.text
        E_tip = self.root.ids.E_tip.text
        bspg = self.root.ids.bspg.text

        if len(self.root.ids.N_tip.text) > 0:
            if len(self.root.ids.M_tip.text) > 0:
                if len(self.root.ids.I_tip.text) > 0:
                    if int(self.root.ids.I_tip.text) > 0:
                        if len(self.root.ids.E_tip.text) > 0:
                            if int(self.root.ids.E_tip.text) > 0:
                                if len(self.root.ids.bspg.text) > 0:
                                    if int(self.root.ids.bspg.text) > 0:
                                        MS = int(I_tip) - int(E_tip)
                                        PP = int(N_tip) - int(M_tip)

                                        Puks = int(PP) + int(MS)
                                        Puks_rel = (int(Puks) * 100) / int(bspg)
                                        Puks_rel = float(Puks_rel)
                                        Puks_rel = round(Puks_rel, 1)
                                        bsdg = int(bspg) + int(Puks)
                                        Puks = str(Puks)
                                        Puks_rel = str(Puks_rel)
                                        bsdg = str(bsdg)

                                        self.dialog = MDDialog(
                                                title="Ukupna promjena broja stanovnika iznosi " + Puks + ", "
                                                        "njena stopa iznosti " + Puks_rel + ", "
                                                            "a broj stanovnika sljedeće godine iznosi " + bsdg + "."
                                        )
                                        self.dialog.open()
                                    else:
                                        self.root.ids.bspg.text = "Nema stanovnika?"
                                        self.root.ids.bspg.text = ''
                                else:
                                    self.root.ids.bspg.text = "Nema stanovnika?"
                                    self.root.ids.bspg.text = ''
                            else:
                                self.root.ids.E_tip.text = "Nema stanovnika?"
                                self.root.ids.E_tip.text = ''
                        else:
                            self.root.ids.E_tip.text = "Nema stanovnika?"
                            self.root.ids.E_tip.text = ''
                    else:
                        self.root.ids.I_tip.text = "Nema stanovnika?"
                        self.root.ids.I_tip.text = ''
                else:
                    self.root.ids.I_tip.text = "Nema stanovnika?"
                    self.root.ids.I_tip.text = ''
            else:
                self.root.ids.M_tip.text = "Nitko se nije rodio?"
                self.root.ids.M_tip.text = ''
        else:
            self.root.ids.N_tip.text = "Nitko nije umro?"
            self.root.ids.N_tip.text = ''

    def tip_info(self):
        self.dialog = MDDialog(
            text="Računa se promjena broja stanovnika, njena stopa i broj stanovnika sljedeće godine.\n\n"
                 "Ukoliko se računa opće kretanje za između više od dviju godina (npr. 2000. i 2018.), "
                 "utoliko se trebaju upisati zbrojevi svih parametara."
                 )
        self.dialog.open()

    def tip_vise(self):
        self.dialog = MDDialog(
            text="Kao relativni pokazatelj promjene broja stanovnika može se izračunati i geometrijska stopa, koja se "
                 "računa za razdoblje duže od 10 godina.")
        self.dialog.open()

    def tipo1(self):
        N_tip = self.root.ids.N_tip.text
        M_tip = self.root.ids.M_tip.text
        I_tip = self.root.ids.I_tip.text
        E_tip = self.root.ids.E_tip.text
        bspg = self.root.ids.bspg.text

        if len(self.root.ids.N_tip.text) > 0:
            if len(self.root.ids.M_tip.text) > 0:
                if len(self.root.ids.I_tip.text) > 0:
                    if int(self.root.ids.I_tip.text) > 0:
                        if len(self.root.ids.E_tip.text) > 0:
                            if int(self.root.ids.E_tip.text) > 0:
                                if len(self.root.ids.bspg.text) > 0:
                                    if int(self.root.ids.bspg.text) > 0:
                                        MS = int(I_tip) - int(E_tip)
                                        PP = int(N_tip) - int(M_tip)
                                        pp = (int(PP) * 1000) / int(bspg)
                                        pp = float(pp)
                                        pp = round(pp, 2)
                                        ms = (int(MS) * 1000) / int(bspg)
                                        ms = float(ms)
                                        ms = round(ms, 2)
                                        Puks = int(PP) + int(MS)

                                        if ms < 0:
                                            if pp < 0:
                                                self.dialog = MDDialog(
                                                    title="Prostor pripada podtipu IZUMIRANJA(E4) emigracijskog tipa "
                                                          "općeg kretanja stanovništva.")
                                                self.dialog.open()
                                            else:
                                                if Puks < 0:
                                                    if abs(pp) > abs(Puks):
                                                        self.dialog = MDDialog(
                                                            title="Prostor pripada podtipu DEPOPULACIJI(E2) "
                                                                  "emigracijskog tipa općeg kretanja stanovništva.")
                                                        self.dialog.open()
                                                    else:
                                                        self.dialog = MDDialog(
                                                            title="Prostor pripada podtipu IZRAZITOJ DEPOPULACIJI(E3) "
                                                                  "emigracijskog tipa općeg kretanja stanovništva.")
                                                        self.dialog.open()
                                                else:
                                                    self.dialog = MDDialog(
                                                        title="Prostor pripada podtipu EMIGRACIJI(E1) emigracijskog "
                                                              "tipa općeg kretanja stanovništva.")
                                                    self.dialog.open()
                                        else:
                                            if pp >= 0:
                                                self.dialog = MDDialog(
                                                    title="Prostor pripada podtipu EKSPANZIJI IMIGRACIJOM(I1) "
                                                          "imigracijskog tipa općeg kretanja stanovništva.")
                                                self.dialog.open()
                                            else:
                                                if Puks >= 0:
                                                    if abs(Puks) >= abs(pp):
                                                        self.dialog = MDDialog(
                                                            title="Prostor pripada podtipu REGENERACIJI "
                                                                  "IMIGRACIJOM(I2) imigracijskog tipa općeg kretanja "
                                                                  "stanovništva.")
                                                        self.dialog.open()
                                                    else:
                                                        self.dialog = MDDialog(
                                                            title="Prostor pripada podtipu SLABOJ REGENERACIJI "
                                                                  "IMIGRACIJOM(I3) imigracijskog tipa općeg kretanja "
                                                                  "stanovništva.")
                                                        self.dialog.open()
                                                else:
                                                    self.dialog = MDDialog(
                                                        title="Prostor pripada podtipu VRLO SLABOJ REGENERACIJI "
                                                              "IMIGRACIJOM(I4) imigracijskog tipa općeg kretanja "
                                                              "stanovništva.")
                                                    self.dialog.open()
                                    else:
                                        self.root.ids.bspg.text = "Nema stanovnika?"
                                        self.root.ids.bspg.text = ''
                                else:
                                    self.root.ids.bspg.text = "Nema stanovnika?"
                                    self.root.ids.bspg.text = ''
                            else:
                                self.root.ids.E_tip.text = "Nema stanovnika?"
                                self.root.ids.E_tip.text = ''
                        else:
                            self.root.ids.E_tip.text = "Nema stanovnika?"
                            self.root.ids.E_tip.text = ''
                    else:
                        self.root.ids.I_tip.text = "Nema stanovnika?"
                        self.root.ids.I_tip.text = ''
                else:
                    self.root.ids.I_tip.text = "Nema stanovnika?"
                    self.root.ids.I_tip.text = ''
            else:
                self.root.ids.M_tip.text = "Nitko se nije rodio?"
                self.root.ids.M_tip.text = ''
        else:
            self.root.ids.N_tip.text = "Nitko nije umro?"
            self.root.ids.N_tip.text = ''

    def tip_info1(self):
        self.dialog = MDDialog(
            text="Definira se tip općeg kretanja za jednu godinu.\n\n"
                 "Ukoliko se definira tip općeg kretanja za između više od dviju godina (npr. 2000. i 2018.), "
                 "utoliko se trebaju upisati zbrojevi svih parametara.")
        self.dialog.open()

    def tip_vise1(self):
        self.dialog = MDDialog(
            text="Ako je prostorno kretanje(I) > 0\n"
                 "I1 - stopa ukupnog kretanja(+) > stopa prirodne promjene(+)\n"
                 "I2 - stopa ukupnog kretanja(+) > stopa prirodne promjene(-)\n"
                 "I3 - stopa ukupnog kretanja(+) < stopa prirodne promjene(-)\n"
                 "I4 - stopa ukupne promjene(-) < stopa prirodne promjene(-)\n\n"
                 "Ako je prostorno kretanje(E) < 0\n"
                 "E1 - stopa ukupne promjene(+) > stopa prirodne promjene(-)\n"
                 "E2 - stopa ukupne promjene(+) > stopa prirodne promjene(-)\n"
                 "E3 - stopa ukupne promjene(+) < stopa prirodne promjene(-)\n"
                 "E4 - stopa ukupne promjene(-) < stopa prirodne promjene(-)")
        self.dialog.open()

class strukture(Screen):
    ZS = ObjectProperty(float)
    MS = ObjectProperty(float)
    ML = ObjectProperty(float)
    ZR = ObjectProperty(float)
    ST = ObjectProperty(float)

    def mask(self):
        ZS = self.root.ids.ZS.text
        MS = self.root.ids.MS.text
        if len(self.root.ids.ZS.text) > 0:
            if len(self.root.ids.MS.text) > 0:

                koef_m = (int(MS) / int(ZS)) * 100
                koef_z = (int(ZS) / int(MS)) * 100
                koef_m = round(koef_m, 2)
                koef_z = round(koef_z, 2)
                koef_m = str(koef_m)
                koef_z = str(koef_z)
                self.dialog = MDDialog(
                    title="Koeficijent maskuliniteta iznosi " + koef_m + ", koeficijent feminiteta " + koef_z + ".")
                self.dialog.open()

            else:
                self.root.ids.MS.text = "Nema muškaraca?"
                self.root.ids.MS.text = ''
        else:
            self.root.ids.ZS.text = "Nema žena?"
            self.root.ids.ZS.text = ''

    def masko_info(self):
        self.dialog = MDDialog(
            text="Koeficijenti se računaju dijeljenjem muškog i ženskog stanovništva te množenjem sa 100. "
                 "Posljedično, rezultati su paralelni - vrijednost koeficijenta maskuliniteta jednako je udaljen od "
                 "broja 100 kao i koeficijent feminiteta.")
        self.dialog.open()

    def masko_vise(self):
        self.dialog = MDDialog(
            text="Brojčane razlike po spolovima različite su prema dobnim skupinama. Uvijek se rodi više muške djece "
                 "- diferencijalna rodnost, ali uvijek i umire više muških osoba - diferencijalna smrtnost.")
        self.dialog.open()

    def ind_star(self):
        ML = self.root.ids.ML.text
        ST = self.root.ids.ST.text

        if len(self.root.ids.ML.text) > 0:
            if len(self.root.ids.ST.text) > 0:
                ind_st = (int(ST) / int(ML)) * 100
                ind_st = round(ind_st, 2)
                ind_st = str(ind_st)
                self.dialog = MDDialog(text="Indeks starosti iznosi " + ind_st + ".")
                self.dialog.open()

            else:
                self.root.ids.ST.text = "Nema starog stanovnika?"
                self.root.ids.ST.text = ''
        else:
            self.root.ids.ML.text = "Nema mladog stanovnika?"
            self.root.ids.ML.text = ''

    def dobn_info(self):
        self.dialog = MDDialog(
            text="Računa se kao odnos starijeg i mlađeg stanovništva te pomnoženo sa 100. Rezultat pokazuje koliko "
                 "imamo starijih ljudi na 100 mladih."
        )
        self.dialog.open()

    def dobn_vise(self):
        self.dialog = MDDialog(
            text="Klasifikacija indeksa starosti:\n"
                 "1) mladost =<22,9\n"
                 "2) na pragu starenja = 23 - 34,9\n"
                 "3) starenje = 35 - 44,9\n"
                 "4) starost = 45 - 54,9\n"
                 "5) duboka starost = 55 - 99,9\n"
                 "6) izrazito duboka starost >=100"
        )
        self.dialog.open()

    def stup_ost(self):
        ML = self.root.ids.ML.text
        ST = self.root.ids.ST.text
        P_struk = self.root.ids.P_struk.text

        if len(self.root.ids.ML.text) > 0:
            if len(self.root.ids.ST.text) > 0:
                if len(self.root.ids.P_struk.text) > 0:
                    ind_st = (int(ST) / int(ML)) * 100
                    ind_st = round(ind_st, 2)
                    ind_st = str(ind_st)
                    udio_mladih = (int(ML) * 100) / int(P_struk)
                    udio_mladih = round(udio_mladih, 1)
                    udio_starih = (int(ST) * 100) / int(P_struk)
                    udio_starih = round(udio_starih, 1)
                    st_bod = 70 - udio_starih
                    stup_ost = udio_mladih + st_bod
                    stup_ost = str(stup_ost)
                    self.dialog = MDDialog(
                        text="Indeks starosti iznosi " + ind_st + ", a stupanj ostarjelosti " + stup_ost + ".")
                    self.dialog.open()
                else:
                    self.root.ids.P_struk.text = "Nema stanovnika?"
                    self.root.ids.P_struk.text = ''
            else:
                self.root.ids.ST.text = "Nema starog stanovnika?"
                self.root.ids.ST.text = ''
        else:
            self.root.ids.ML.text = "Nema mladog stanovnika?"
            self.root.ids.ML.text = ''

    def stup_info(self):
        self.dialog = MDDialog(
            text="Računa se pridodavnjem bodova različitim udjelima mladog i starog stanovništva"
                         )
        self.dialog.open()

    def stup_vise(self):
        self.dialog = MDDialog(
            text="Klasifikacija stupnja ostarjelosti:\n"
                 "1) na pragu starosti = 90,5 - 100\n"
                 "2) starenje = 84,5 - 90\n"
                 "3) starost = 73 - 84\n"
                 "4) duboka starost = 65,5 - 72,5\n"
                 "5) vrlo duboka starost = 50,5 - 65\n"
                 "6) izrazito duboka starost = 30,5 - 50\n"
                 "7) krajnje duboka starost = 0 - 30"
        )
        self.dialog.open()


class Geokalkulator(MDApp, gustoca, prir_kretanje, pros_kretanje, tip, strukture):
    def build(self):
        self.title="Geokalkulator"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        KV = Builder.load_file("grafika11.kv")
        return KV

Geokalkulator().run()
