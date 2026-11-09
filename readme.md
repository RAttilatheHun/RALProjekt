# Ruhatár

## **Név:** Rács Attila László

## **NK:** E7MRCF

---

## **Feladat leírása**

Python alkalmazás grafikus **Tkinter** grafikus felülettel, eladásra szánt ruhák nyilvántartására.

Felvehetünk vele a rendszerbe új ruhákat a ruha nevének, márkájának, méretének, hirdetési platformjának és hirdetési árának megadásával, ezen felül rögzíthető az eladási ár, és archiválhatóak a már eladott darabok.

Az aktuális, nem archivált ruhák egy **ruhak.json** JSON fájlba kerülnek kiírásra, innen tölti be a program következő indításnál az adatokat.

---

## **Felhasználói leírás**

Egyedül a Pythonra van szükség, mást külön telepíteni nem szükséges.

A programot a következő paranccsal indíthatjuk el:

```bash
python main.py
```

---

## **A program felépítése**

### **RAL_sajatmodul.py**

Saját modul, a JSON fájl kezeléséért és az adatok mentéséért felelős.

### **Függvényei**

#### **ral_betoltes()**

Betölti a korábban mentett ruhák adatait a JSON fájlból.

#### **ral_mentes()**

Elmenti az aktuális ruhák adatait a JSON fájlba.

#### **ral_lista()**

Visszaadja az archivált ruhák listáját.

---

## **Osztályok**

### **RALRuhatar**

Fő osztály, a ruhadarabokat kezeli.

### **Metódusai**

#### **uj_ruha()**

Új darabot vesz fel.

#### **eladas()**

A kiválasztott darabot eladottnak jelöli, eladási árat rögzíti.

#### **archivalas()**

Eladott darabot archiválja.

#### **profit()**

Eladott darab profitját vagy veszteségét számolja ki.
