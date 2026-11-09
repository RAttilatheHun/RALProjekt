Ruhatár

Név: Rács Attila László
NK: E7MRCF

Python alkalmazás grafikus TKinter grafikus felülettel, eladásra szánt ruhák nyilvántartására.
Felvehetünk vele a rendszer új ruhákat a ruha nevének, márkájának, méretének, hirdetési platformjának, és hirdetési árának megadásával, ezen felül rögzíthető az eladási ár, és archiválhatóak a már eladott darabok.
Az aktuális, nem archivált ruhák egy ruhak.json JSON fáljba kerülnek kiírásra, innen tölti be a program következő indításnál az adatokat.

Egyedül a Pythonra van szükség, mást külön telepíteni nem szükséges.

A programot a következő paranccsal indíthatjuk el: "python main.py"

A program felépítése

RAL_sajatmodul.py: Saját modul, a JSON fájl kezeléséért és az adatok mentéséért felelős.

Függvényei: 

ral_betoltes()
Betölti a korábban mentett ruhák adatait a JSON fájlból.

ral_mentes()
Elmenti az aktuális ruhák adatait a JSON fájlba.

ral_lista()
Visszaadja az archivált ruhák listáját.

Osztályok:

RALRuhatar: fő osztály, a ruhadarabokat kezeli.

Metódusai:

uj_ruha()
Új darabot vesz fel.

eladas()
A kiválasztott darabot eladottnak jelöli, eladási árat rögzíti.

archivalas()
Eladott darabot archiválja.

profit()
Eladott darab profitját vagy veszteségét számolja ki.