#  Hangovers and more: Bacon 

s = '''VoiCI unE SUpeRbe reCeTtE cONcontee pAR un GrouPe d'ArtistEs culinaiRe, dONT le BOn Gout et lE SeNs de LA cLasSe n'est limIteE qUe par LE nombre DE cAlOries qU'ils PeUVEnt Ingurgiter. Ces virtuoses de la friteuse vous presente ce petit clip plein de gout savoureux !!'''
result = ''
for i in range(len(s)):
    if s[i].isalpha():
        if s[i] == s[i].lower():
            result += 'A'
        elif s[i] == s[i].upper():
            result += 'B'
print(result)