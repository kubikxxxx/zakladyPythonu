import math

# Konstanty
EARTH_GRAVITY = 9.81 # normální pozemské tíhové zrychlení v m/s²
MOON_GRAVITY = 1.62 # měsíční gravitace v m/s²
GRAVITIES = {
    "Merkur": 3.7,
    "Venuše": 8.87,
    "Země": 9.81,
    "Mars": 3.71,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uran": 8.69,
    "Neptun": 11.15
}
SPEED_OF_LIGHT = 299796 # rychlost světla ve vakuu v km/s
SPEED_OF_SOUND = 343 # rychlost zvuku při teplotě 20 °C v suchém vzduchu v m/s

# Funkce
def padVeVakuu(h, g):
    """
    Funkce vrací délku pádu v sekundách a rychlost dopadu tělesa ve vakuu.
    Parametry: výška tělesa od místa dopadu v metrech (h) a tíhové zrychlení (g) v místě pádu tělesa.

    Použití:
    cas, rychlost = padVeVakuu(vyska, tihove_zrychleni)
    """
    t = math.sqrt(2 * h / g)
    v = g * t
    return t, v

def vahaNaPlanete(hmotnost, g):
    """
    Funkce vrací váhu tělesa na planetě s tíhovým zrychlením g.
    Parametry: hmotnost tělesa (hmotnost) v kg a tíhové zrychlení (g) v m/s².

    Použití:
    vaha = vahaNaPlanete(hmotnost, tihove_zrychleni)
    """
    vaha = hmotnost / EARTH_GRAVITY * g
    return vaha

def vzdalenostBlesku(t):
    """
    Funkce vypočítá vzdálenost blesku od místa pozorování.
    Parametr: časová prodleva (t) mezi bleskem a hromem v sekundách.

    Použití:
    vzdalenost = vzdalenostBlesku(casova_prodleva)
    """
    return t * SPEED_OF_SOUND

def jak_rychle_urazi_svetlo(s):
    """
    Funkce vypočítá dobu, za jakou světlo urazí vzdálenost s v metrech.
    Parametr: vzdálenost (s) v metrech.

    Použití:
    cas = jak_rychle_urazi_svetlo(vzdalenost)
    """
    return s / 1000 / SPEED_OF_LIGHT

# Nové funkce
def rychlostNaPlanete(v0, t, g):
    """
    Funkce vrací konečnou rychlost tělesa v pohybu na planetě s tíhovým zrychlením g.
    Parametry: počáteční rychlost v m/s (v0), čas v sekundách (t) a tíhové zrychlení v m/s² (g).

    Použití:
    konecna_rychlost = rychlostNaPlanete(pocatecni_rychlost, cas, tihove_zrychleni)
    """
    v = v0 + g * t
    return v

def energieTelesa(m, v):
    """
    Funkce vypočítá kinetickou energii tělesa o hmotnosti m a rychlosti v.
    Parametry: hmotnost (m) v kg a rychlost (v) v m/s.

    Použití:
    energie = energieTelesa(hmotnost, rychlost)
    """
    e = 0.5 * m * v ** 2
    return e

def dobaLetuZvuku(d):
    """
    Funkce vypočítá dobu, za kterou zvuk urazí vzdálenost d při rychlosti zvuku (343 m/s).
    Parametr: vzdálenost (d) v metrech.

    Použití:
    cas = dobaLetuZvuku(vzdalenost)
    """
    t = d / SPEED_OF_SOUND
    return t
