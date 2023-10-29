#Write an if-elif-else chain that determines a person’s stage of life.

year = 70

if year <2:
    print("Dear user, you are a baby.")
elif year<4:
    print("Dear user, you are a toddler.")
elif year<13:
    print("Dear user, you are a kid.")
elif year<20:
    print("Dear user, you are a teenager!")
elif year<65:
    print("Dear user, you are an adult.")
else:
    print("Oh dear. You are an elder.")