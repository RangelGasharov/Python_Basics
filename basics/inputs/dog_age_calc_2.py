DOG_AGE = int(input("Please write down the age of your dog (in human years): \n"))
dog_age_human_years = 0

if(DOG_AGE == 1):
    dog_age_human_years = 14
elif (DOG_AGE == 2):
    dog_age_human_years = 22
else:
    dog_age_human_years = 22 + 5 * (DOG_AGE - 2)
print(dog_age_human_years)
