# szotar-solver

Segít megfejteni a napi [szózatot](https://szozat.miklosdanka.com/).

## Futtatáshoz szükséges eszközök

- [Python 3](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)

## A `solver.py` által használt szólista előállítása (Windows)
*(a repo root mappájában állva)*
```
prepare_data.bat
```

## Használat (CLI)
*(a repo root mappájában állva)*
```
py solver.py [--first-guess] [--present=<betűlista>] [--not-present=<betűlista>] [--correct-regex=<regex>]
```

### Argumentumok
##### A vesszővel elválasztás fontos a betűlistáknál és a regexben!

#### `--first-guess`
  - Nap első tippje (beégetve, az `alant` szót fogja kiadni)

#### `--present`
  - azon betűk listája, amelyek tippelés után narancssárgák(azaz szerepelnek a napi szóban)

##### Példa
  - `--present=a,é,p`
    - olyan szavakat fog kiadni, amelyekben szerepelnek az `a`, `é` és `p` betűk valamilyen sorrendben.

#### `--not-present`
  - azon betűk listája, amelyek tippelés utána szürkék(azaz **nem** szerepelnek a napi szóban)

##### Példa
  - `--not-present=a,é,p`
    - olyan szavakat fog kiadni, amelyekben **nem** szerepelnek az `a`, `é` és `p` betűk.

#### `--correct-regex`
  - egy speciálisan megadott karakter-sorozat, amely a jó helyen lévő betűk alapján szűkíti a lehetséges betűk listáját
    - a scripten belül ennek a paraméternek az értéke egy regex patternné áll össze és a python beépített regex
        engine-je dolgozza fel
      - ```
        "".join(correct_regex.split(","))  # egyszerűsített kód, de lényegében ez történik
        ```
  - célszerű azokat a betűket behelyettesíteni a megfelelő helyre, amelyek tippelés után zöldek(azaz helyes betű, és jó helyen is van)

##### Példa
  - `--correct-regex=a,.,[^gyéáe],.,f`
    - olyan szavakat fog kiadni, amelyekben
      1. az első betű `a`
      2. a második betű tetszőleges
      3. a harmadik betű bármi, ami nem `gy`, `é`, `á` vagy `e`
      4. a negyedik betű tetszőleges
      5. az ötödik betű `f`

## Használat (GUI)
solver_gui.py futtatása.

CLI-ből:
```
py solver_gui.py
```

A grafikus felületen megtalálhatóak a CLI-s felületen írt kapcsolók, csak máshogy elrendezve, illetve a listákból
törölni nem lehet. A CLI-s használatban leírtak érvényesek itt is.

## Használat (Releases)
Ez a GUI-t használja. Használatához szükség van a solver_gui.exe és usable_words.txt fájlokra. Ezeknek ugyanabban a
mappában kell lenniük. Azért nincs beleégetve a futtatható fájlba a usable_words.txt, hogy szólista változás esetén
elegendő legyen csak a szólistát frissíteni.
