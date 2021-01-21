# Program Name: Triplets
# Date: February 29th, 2020
# Programmer: Alex Dorodko
# Description: Generates a random three-line poem.

import random

def triplet():
    nouns = []

    nouns.append("elefant")
    nouns.append("dog")
    nouns.append("turtle")
    nouns.append("cat")
    nouns.append("zebra")
    nouns.append("fox")
    nouns.append("monkey")
    nouns.append("tiger")
    nouns.append("bear")
    nouns.append("frog")

    pst_vrbs = []

    pst_vrbs.append("came")
    pst_vrbs.append("ran")
    pst_vrbs.append("walked")
    pst_vrbs.append("drove")
    pst_vrbs.append("flew")
    pst_vrbs.append("swam")
    pst_vrbs.append("went")
    pst_vrbs.append("left")
    pst_vrbs.append("rode")
    pst_vrbs.append("crawled")

    prsnt_vrbs = []

    prsnt_vrbs.append("freeze")
    prsnt_vrbs.append("hide")
    prsnt_vrbs.append("hold")
    prsnt_vrbs.append("make")
    prsnt_vrbs.append("pay")
    prsnt_vrbs.append("read")
    prsnt_vrbs.append("sleep")
    prsnt_vrbs.append("speak")
    prsnt_vrbs.append("write")
    prsnt_vrbs.append("sell")

    rhyming_nouns = []

    rhyming_nouns.append("gate")
    rhyming_nouns.append("mate")
    rhyming_nouns.append("weight")
    rhyming_nouns.append("bait")
    rhyming_nouns.append("state")
    rhyming_nouns.append("plate")
    rhyming_nouns.append("date")
    rhyming_nouns.append("rate")

    print("The", nouns.pop(random.randint(0, len(nouns) - 1)), pst_vrbs.pop(random.randint(0, len(pst_vrbs) - 1)), "to the",
          rhyming_nouns.pop(random.randint(0, len(rhyming_nouns) - 1)), "\nSo it would",prsnt_vrbs.pop(random.randint(0, len(prsnt_vrbs) - 1)), "the",
          rhyming_nouns.pop(random.randint(0, len(rhyming_nouns) - 1)), "\nBut it was a",rhyming_nouns.pop(random.randint(0, len(rhyming_nouns) - 1)))

    again = input("\nWould you like to compose another triplet?(Y/N)\n")
    again = again.upper()
    while (again != "Y" and again != "N"):
        again = input("Invalid answer. Would you like to compose another triplet?(Y/N)\n")
        again = again.upper()

    if (again == "Y"):
        triplet()
    else:
        pass

triplet()