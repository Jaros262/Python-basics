'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.625 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu


def rozdil_mezi_gravitacemi(earth, moon, jmeno1, jmeno2):
    """
    rozdil_mezi_gravitacemi: Vypočítá jaký je rozdíl mezi gravitací 1 a gravitaci 2 v m/s
    """
    substract_1 = abs(earth - moon)
    print(f"Rozdil gravitací {jmeno1} a {jmeno2} je {substract_1:.2f} m/s")

rozdil_mezi_gravitacemi(EARTH_GRAVITY, MOON_GRAVITY, "země", "měsíce")

def kolikrat_je_vetsi_rychlost_svetla(light, sound, jmeno1, jmeno2):
    """
    rozdil_mezi_rychlost_light_sound Vypočítá kolikrát je rychlost1 vetsi nez rychlost 2
    """
    substract_2 = abs(light/sound)
    print(f"Rychlost {jmeno1} je {substract_2:.2f} krat vetsi nez rychlost {jmeno2}.")
kolikrat_je_vetsi_rychlost_svetla(SPEED_OF_LIGHT, SPEED_OF_SOUND, "světla", "zvuku")

''' 
Úkol:
1.x Doplňte správně hodnoty uvedených konstant. 
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''