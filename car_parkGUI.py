# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox

window = Tkinter.Tk()
width = 600
height = 600
window.geometry("%sx%s" % (width, height))
window.resizable(0, 0)
greeting_text = "CarPark"
greeting = Tkinter.Label(window, text=greeting_text)
greeting.pack()


class Vozilo(object):
    def __init__(self, znamka, model, km, servis_datum):
        self.znamka = znamka
        self.model = model
        self.km = km
        self.servis_datum = servis_datum

    def izpis_vozil(self):
        return "Znamka: %s, Model: %s, Prevoženi km: %s, Zadnji servis: %s" % (
        self.znamka, self.model, self.km, self.servis_datum)


v0 = Vozilo('Man', 'Tgx-d38', 350000, '28.01.2019')
v1 = Vozilo('Renault', 'Megane 3', 215000, '04.12.2018')
v2 = Vozilo('BMW', '318', 151000, '01.07.2018')

vozila_list = [v0, v1, v2]


def izpis_vozil():
    new_line = 20
    position = 400

    for index, v in enumerate(vozila_list):
        izpis_vozil = Tkinter.Label(window, text="ID: %s; %s" % (index, v.izpis_vozil()))
        izpis_vozil.pack()
        izpis_vozil.place(x=10, y=position + (index * new_line))

def vpis_km():
    try:
        index = entry_id.get()
        izbrano_vozilo = vozila_list[int(index)]
        if index != '' and izbrano_vozilo != '':
            izbrano_vozilo.km = entry_km.get()
            izpis_vozil()
        else:
            tkMessageBox.showinfo("Sporočilo", 'Vpiši podatke avtomobila')
    except ValueError:
        tkMessageBox.showinfo("Sporočilo", 'Vpiši podatke avtomobila')


def vpis_servis():
    try:
        index = entry_servis_id.get()
        izbrano_vozilo = vozila_list[int(index)]
        if index != '' and izbrano_vozilo != '':
            izbrano_vozilo.servis_datum = entry_servis_date.get()
            izpis_vozil()
            zapis_v_dnevnik()
        else:
            tkMessageBox.showinfo("Sporočilo", 'Vpiši podatke avtomobila')
    except ValueError:
        tkMessageBox.showinfo("Sporočilo", 'Vpiši podatke avtomobila')
    except IndexError:
        tkMessageBox.showinfo("Sporočilo", 'Izbral si napačen zapis')



def vpis_novega_vozila():
    znamka = entry_new_znamka.get()
    model = entry_new_model.get()
    prevozeno_km = entry_new_km.get()
    servis = entry_new_servis.get()
    if znamka != '' and model != '' and prevozeno_km != '' and servis != '':
        novo_vozilo = Vozilo(znamka, model, prevozeno_km, servis)
        vozila_list.append(novo_vozilo)
        zapis_v_dnevnik()
        izpis_vozil()
    else:
        tkMessageBox.showinfo("Sporočilo", 'Vpiši podatke avtomobila')


def izbris_vozila():
    index = entry_delete_id.get()
    try:
        izbrano_vozilo = vozila_list[int(index)]
        vozila_list.remove(izbrano_vozilo)
        zapis_v_dnevnik()
    except (IndexError,ValueError):
        tkMessageBox.showinfo("Sporočilo", 'Vpiši ID avtomobila')

def zapis_v_dnevnik():
    with open('vozila.txt', 'w') as dnevnik:
        for index, v in enumerate(vozila_list):
            dnevnik.write("ID: %d; %s\n" % (index, v.izpis_vozil()))

izpis_vozil()


label_km = Tkinter.Label(window, text='Vpis Km:')
label_km.pack()
label_km.place(x=350, y=5)

entry_id_text = Tkinter.Label(window, text='Vpiši ID vozila:')
entry_id_text.pack()
entry_id_text.place(x=350, y=30)
entry_id = Tkinter.Entry(window)
entry_id.pack()
entry_id.place(x=440, y=30)

entry_km_text = Tkinter.Label(window, text='Vpiši Km vozila:')
entry_km_text.pack()
entry_km_text.place(x=350, y=60)
entry_km = Tkinter.Entry(window)
entry_km.pack()
entry_km.place(x=440, y=60)

vpis_km_btn = Tkinter.Button(window, text="Posodobi", command=vpis_km)
vpis_km_btn.pack()
vpis_km_btn.place(x=505 ,y=90)


label_new = Tkinter.Label(window, text='Vpis Novega vozila:')
label_new.pack()
label_new.place(x=20, y=5)

entry_new_znamka_text = Tkinter.Label(window, text='Vpiši znamko vozila:')
entry_new_znamka_text.pack()
entry_new_znamka_text.place(x=20, y=30)
entry_new_znamka = Tkinter.Entry(window)
entry_new_znamka.pack()
entry_new_znamka.place(x=130, y=30)

entry_new_model_text = Tkinter.Label(window, text='Vpiši model vozila:')
entry_new_model_text.pack()
entry_new_model_text.place(x=20, y=60)
entry_new_model = Tkinter.Entry(window)
entry_new_model.pack()
entry_new_model.place(x=130, y=60)

entry_new_km_text = Tkinter.Label(window, text='Vpiši Km vozila:')
entry_new_km_text.pack()
entry_new_km_text.place(x=20, y=90)
entry_new_km = Tkinter.Entry(window)
entry_new_km.pack()
entry_new_km.place(x=130, y=90)

entry_new_servis_text = Tkinter.Label(window, text='Vpiši zadnji servis:')
entry_new_servis_text.pack()
entry_new_servis_text.place(x=20, y=120)
entry_new_servis = Tkinter.Entry(window)
entry_new_servis.pack()
entry_new_servis.place(x=130, y=120)

novo_vozilo_btn = Tkinter.Button(window, text="Dodaj", command=vpis_novega_vozila)
novo_vozilo_btn.pack()
novo_vozilo_btn.place(x=215, y= 150)


label_servis= Tkinter.Label(window, text='Vpis servis vozila:')
label_servis.pack()
label_servis.place(x=20, y=180)

entry_servis_text = Tkinter.Label(window, text='Vpiši ID vozila:')
entry_servis_text.pack()
entry_servis_text.place(x=20, y=210)
entry_servis_id = Tkinter.Entry(window)
entry_servis_id.pack()
entry_servis_id.place(x=130, y=210)

entry_servis_date_text = Tkinter.Label(window, text='Vpiši datum:')
entry_servis_date_text.pack()
entry_servis_date_text.place(x=20, y=240)
entry_servis_date = Tkinter.Entry(window)
entry_servis_date.pack()
entry_servis_date.place(x=130, y=240)

vpis_servis_btn = Tkinter.Button(window, text="Posodobi", command=vpis_servis)
vpis_servis_btn.pack()
vpis_servis_btn.place(x=195, y= 270)


label_delete_text = Tkinter.Label(window, text='Izbris vozila:')
label_delete_text.pack()
label_delete_text.place(x=350, y=180)

entry_delete_text = Tkinter.Label(window, text='Vpiši ID vozila:')
entry_delete_text.pack()
entry_delete_text.place(x=350, y= 210)
entry_delete_id = Tkinter.Entry(window)
entry_delete_id.pack()
entry_delete_id.place(x=440, y=210)

izbris_btn = Tkinter.Button(window, text="Izbris vozil", command=izbris_vozila)
izbris_btn.pack()
izbris_btn.place(x=500, y= 240)

izhod = Tkinter.Button(window, text="Izhod", command=exit)
izhod.pack()
izhod.place(x=280, y=340)


if __name__ == '__main__':
    window.mainloop()