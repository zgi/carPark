# -*- coding: utf-8 -*-
class Vozilo(object):
    def __init__(self, znamka, model, km, servis_datum):
        self.znamka = znamka
        self.model = model
        self.km = km
        self.servis_datum = servis_datum

    def izpis_vozil(self):
        return "Znamka: %s, Model: %s, Prevoženi km: %d, Zadnji servis: %s" % (
        self.znamka, self.model, self.km, self.servis_datum)


v0 = Vozilo('Man', 'Tgx-d38', 350000, '28.01.2019')
v1 = Vozilo('Renault', 'Megane 3', 215000, '04.12.2018')
v2 = Vozilo('BMW', '318', 151000, '01.07.2018')

vozila_list = [v0, v1, v2]


def izpis_vozil():
    for index, v in enumerate(vozila_list):
        print "ID: %d; %s" % (index, v.izpis_vozil())

def vpis_km():
    znamka = raw_input("Vpiši znamko vozila: ").title()
    model = raw_input("Vpiši model vozila: ").title()
    for index, v in enumerate(vozila_list):
        if znamka in v.izpis_vozil():
            if model in v.izpis_vozil():
                print "ID: %d; %s" % (index, v.izpis_vozil())
                novi_km = int(raw_input("Vpiši št. km: "))
                izbrano_vozilo = vozila_list[int(index)]
                izbrano_vozilo.km = novi_km
                zapis_v_dnevnik()
                print "Zapis posodobljen\n"

def vpis_servis():
    znamka = raw_input("Vpiši znamko vozila: ").title()
    model = raw_input("Vpiši model vozila: ").title()
    for index, v in enumerate(vozila_list):
        if znamka in v.izpis_vozil():
            if model in v.izpis_vozil():
                print "ID: %d; %s" % (index, v.izpis_vozil())
                servis = raw_input("Vpiši datum zadnjega servisa: ")
                izbrano_vozilo = vozila_list[int(index)]
                izbrano_vozilo.servis_datum = servis
                zapis_v_dnevnik()
                print "Zapis posodobljen\n"

def vpis_novega_vozila():
    znamka = raw_input("Vpiši znamko vozila: ")
    model = raw_input("Vpiši model vozila: ")
    prevozeno_km = int(raw_input("Vpiši prevožene km: "))
    servis = raw_input("Vpiši datum zadnjega servisa: ")
    novo_vozilo = Vozilo(znamka, model, prevozeno_km, servis)
    vozila_list.append(novo_vozilo)
    zapis_v_dnevnik()
    print "Zapis posodobljen\n"

def izbris_vozila():
    for index, v in enumerate(vozila_list):
        print "ID: %d; %s" % (index, v.izpis_vozil())
    index = raw_input("Vpiši ID vozila za izbris: ")
    izbrano_vozilo = vozila_list[int(index)]
    vozila_list.remove(izbrano_vozilo)
    zapis_v_dnevnik()
    print "Zapis posodobljen\n"

def zapis_v_dnevnik():
    with open('vozila.txt', 'w') as dnevnik:
        for index, v in enumerate(vozila_list):
            dnevnik.write("ID: %d; %s\n" % (index, v.izpis_vozil()))
def main():
    run = True
    while run:
        print "a) Izpis vozil"
        print "b) Vpis stanja km"
        print "c) Vpis zadnjega servisa"
        print "d) Vpis novega vozila"
        print "e) Izbris vozila"
        print "f) Izhod"

        izbirnik = raw_input("Vpiši željeno izbiro: (a, b, c, d, e, f)")

        if izbirnik.lower() == 'a':
            print "Izpis vseh vozil\n"
            izpis_vozil()
        elif izbirnik.lower() == 'b':
            print "Vpis stanja km za vozilo\n"
            vpis_km()
        elif izbirnik.lower() == 'c':
            print "Vpis zadnjega servisa za vozilo\n"
            vpis_servis()
        elif izbirnik.lower() == 'd':
            print "Vpis novega vozila\n"
            vpis_novega_vozila()
        elif izbirnik.lower() == 'e':
            print "Izbris vozila\n"
            izbris_vozila()
        elif izbirnik.lower() == "f":
            print "Hvala lepa, Lep pozdrav!\n"
            run = False

if __name__ == '__main__':
    main()
