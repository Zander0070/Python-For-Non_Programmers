cats = {"jane":14,
         "tom" : 12,
         "sarah" : 17}

cats["wilson"] = 1
del(cats["jane"])

print(cats)

dictionaryTest = {
    12 : True,
    14 : False,
    17 : True
}


if dictionaryTest[12] == True:
    print("That is correcr")
else:
    print("that is incorret ")