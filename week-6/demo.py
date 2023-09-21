"""

Example of gaming logic

"""

TPYE_A = "lighting"
TPYE_B = "water"

ATK_A1 = "thunderbolt"
ATK_B1 = "water shot"

ATK_TYPE = "damage"
ATK_TYPE = "defense"

ATK_A2 = "flash"
ATK_B2 = "mist"

CON_A = True
CON_B = False
SP = TRUE

if SP or (ATK_TYPE == 'damage' and CON_A == False):
    # Damage
    pass
elif ATK_TYPE == "defense":
    # Defense
    pass
else:
    pass

if CON_A == False:
    # Not confused
    pass

if not CON_A:
    # Not confused
    pass