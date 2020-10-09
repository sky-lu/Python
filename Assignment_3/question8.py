'''
---Write a Python program to display astrological sign for given date of birth.---
if condition statement
'''

day = int(input("Input Birthday : "))
month = input("Input month of birth (e.g. march, july etc): ")
if month == "december":
    if day < 22 :
        astro_sign = "Sagittarius"
    else :
        astro_sign = "Capricorn"
elif month == "january":
    if day < 20 :
        astro_sign = "Capricorn"
    else :
        astro_sign = "Aquarius"
elif month == "february":
    if day < 19 :
        astro_sign = "Aquarius"
    else:
        astro_sign = "Pisces"
elif month == "march" :
    if day < 21:
        astro_sign = "Pisces"
    else :
        astro_sign = "Aries"
elif month == "april" :
    if day < 20 :
        astro_sign = "Aries"
    else :
        astro_sign = "Taurus"
elif month == "may" :
    if day < 21 :
        astro_sign = "Taurus"
    else :
        astro_sign = "Gemini"
elif month == "june" :
    if day < 21 :
        astro_sign = "Gemini"
    else :
        astro_sign = "Cancer"
elif month == "july" :
    if day < 23 :
        astro_sign = "Cancer"
    else :
        astro_sign = "Leo"
elif month == "august" :
    if day < 23 :
        astro_sign = "Leo"
    else :
        astro_sign = "Virgo"
elif month == "september" :
    if day < 23 :
        astro_sign = "Virgo"
    else :
        astro_sign = "Libra"
elif month == "october" :
    if day < 23 :
        astro_sign = "Libra"
    else :
        astro_sign = "Scorpio"
elif month == "november" :
    if day < 22 :
        astro_sign = "Scorpio"
    else :
        astro_sign = "Sagittarius"
print("Your Astrological sign is : ", astro_sign)


    