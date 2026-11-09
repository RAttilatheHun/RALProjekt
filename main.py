import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from RAL_sajatmodul import ral_betoltes
from RAL_sajatmodul import ral_mentes
from RAL_sajatmodul import ral_lista


class RALRuhatar:

    def __init__(self):
        self.ruhak = ral_betoltes()

    def uj_ruha(self, nev, marka, meret,
                platform, hirdetesi_ar):

        ruha = {
            "nev": nev,
            "marka": marka,
            "meret": meret,
            "platform": platform,
            "hirdetesi_ar": hirdetesi_ar,
            "elkelt": False,
            "eladasi_ar": 0,
            "archivalt": False
        }

        self.ruhak.append(ruha)
        ral_mentes(self.ruhak)

    def eladas(self, index, eladasi_ar):
        self.ruhak[index]["elkelt"] = True
        self.ruhak[index]["eladasi_ar"] = eladasi_ar
        ral_mentes(self.ruhak)

    def archivalas(self, index):
        self.ruhak[index]["archivalt"] = True
        ral_mentes(self.ruhak)

    def profit(self, index):
        return (
            self.ruhak[index]["eladasi_ar"] -
            self.ruhak[index]["hirdetesi_ar"]
        )


ruhatar = RALRuhatar()


def lista_frissites():

    lista.delete(0, tk.END)

    for ruha in ruhatar.ruhak:

        if ruha["archivalt"]:
            continue

        statusz = "Eladva"

        if not ruha["elkelt"]:
            statusz = "Aktív"

        szoveg = (
            f"{ruha['nev']} | "
            f"{ruha['marka']} | "
            f"{ruha['meret']} | "
            f"{ruha['platform']} | "
            f"{ruha['hirdetesi_ar']} Ft | "
            f"{statusz}"
        )

        lista.insert(tk.END, szoveg)


def hozzaad_esemeny():

    nev = entry_nev.get()
    marka = entry_marka.get()
    meret = entry_meret.get()

    platform = combo_platform.get()

    if nev == "":
        messagebox.showwarning(
            "Hiba",
           "A név mező üres!"
        )
        return

    try:
        ar = int(entry_ar.get())
    except:
        messagebox.showwarning(
            "Hiba",
            "Hibás ár!"
        )
        return

    ruhatar.uj_ruha(
        nev,
        marka,
        meret,
        platform,
        ar
    )

    lista_frissites()

    entry_nev.delete(0, tk.END)
    entry_marka.delete(0, tk.END)
    entry_meret.delete(0, tk.END)
    entry_ar.delete(0, tk.END)


def eladva_esemeny():

    if not lista.curselection():
        return

    try:
        eladasi_ar = int(
            entry_eladasi_ar.get()
        )
    except:
        messagebox.showwarning(
            "Hiba",
            "Adj meg eladási árat!"
        )
        return

    index = lista.curselection()[0]

    ruhatar.eladas(index, eladasi_ar)

    profit = ruhatar.profit(index)

    messagebox.showinfo(
        "Információ",
        f"Profit: {profit} Ft"
    )

    lista_frissites()


def archivalas_esemeny():

    if not lista.curselection():
        return

    index = lista.curselection()[0]

    if not ruhatar.ruhak[index]["elkelt"]:
        messagebox.showwarning(
            "Hiba",
            "Előbb eladottnak kell jelölni!"
        )
        return

    ruhatar.archivalas(index)

    lista_frissites()


def archivum_esemeny():

    uj_ablak = tk.Toplevel(root)

    uj_ablak.title("Archivált ruhák")

    archiv_lista = tk.Listbox(
        uj_ablak,
        width=100,
        height=20
    )

    archiv_lista.pack(
        fill=tk.BOTH,
        expand=True
    )

    for ruha in ral_lista(
            ruhatar.ruhak):

        szoveg = (
            f"{ruha['nev']} | "
            f"{ruha['platform']} | "
            f"{ruha['eladasi_ar']} Ft"
        )

        archiv_lista.insert(
            tk.END,
            szoveg
        )


root = tk.Tk()

root.title("RAL Ruhatár")
root.geometry("900x650")

tk.Label(
    root,
    text="Ruhadarab neve"
).pack()

entry_nev = tk.Entry(root)
entry_nev.pack()

tk.Label(
    root,
    text="Márka"
).pack()

entry_marka = tk.Entry(root)
entry_marka.pack()

tk.Label(
    root,
    text="Méret"
).pack()

entry_meret = tk.Entry(root)
entry_meret.pack()

tk.Label(
    root,
    text="Platform"
).pack()

combo_platform = ttk.Combobox(
    root,
    values=[
        "Vinted",
        "Facebook Marketplace",
        "Jófogás"
    ]
)

combo_platform.pack()
combo_platform.current(0)

tk.Label(
    root,
    text="Hirdetési ár"
).pack()

entry_ar = tk.Entry(root)
entry_ar.pack()

btn_hozzaad = tk.Button(
    root,
    text="Ruha hozzáadása",
    command=hozzaad_esemeny
)

btn_hozzaad.pack(pady=5)

lista = tk.Listbox(
    root,
    width=120,
    height=15
)

lista.pack(pady=10)

tk.Label(
    root,
    text="Eladási ár"
).pack()

entry_eladasi_ar = tk.Entry(root)
entry_eladasi_ar.pack()

btn_eladva = tk.Button(
    root,
    text="Eladottnak jelölés",
    command=eladva_esemeny
)

btn_eladva.pack(pady=5)

btn_archiv = tk.Button(
    root,
    text="Archiválás",
    command=archivalas_esemeny
)

btn_archiv.pack(pady=5)

btn_archivum = tk.Button(
    root,
    text="Archivált ruhák",
    command=archivum_esemeny
)

btn_archivum.pack(pady=5)

lista_frissites()

root.mainloop()