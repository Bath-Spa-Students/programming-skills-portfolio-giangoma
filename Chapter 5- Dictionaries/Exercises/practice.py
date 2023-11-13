hello = {}
print(hello, type(hello))

#add in dictiknary
identification = {'uni':'bsu',
                'name':'gian',
                'house':'uae',
                'course':'cc'}
print(identification["uni"])
print(identification.get("uni"))

del identification ["house"]
print(identification.items())
print(identification.keys())
print(identification.values())

for uni in identification:
    print("hahahahahahhaha")


