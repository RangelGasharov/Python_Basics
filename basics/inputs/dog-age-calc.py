DOG_AGE = int(input("Please write down the age of your dog (in human years): \n"))
dog_age_human_years = 0

for i in range(0, DOG_AGE):
    if i == 0:
        dog_age_human_years = 14
    elif i == 1:
        dog_age_human_years = 22
    else:
        dog_age_human_years += 5

print("Age of dog in dog years:", dog_age_human_years)
