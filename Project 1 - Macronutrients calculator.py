#calculate daily macros for calisthenics day, running day, and rest day
#Nutrition guidelines: Protein 2-2.2 g/kg, Fat 0.8-1 g/kg, Fill in the rest of calories

print("DAILY MACROS CALCULATOR")
print("----------------------------------------")
print("t = Calisthenic, c = Running, r = Rest")
day_type = input("Enter today's day type (t/c/r): ")
print("----------------------------------------")
current_cal = int(input("Enter your current daily caloric metabolism: "))
current_weight = float(input("Enter current body weight (kg): "))


protein_min = current_weight * 2
protein_cal_min = protein_min * 4
protein_max = current_weight * 2.2
protein_cal_max = protein_max * 4

fat = current_weight * 1
fat_cal = fat * 9

if day_type == "t":
    current_cal *= 1.05
    CarbPmin = (current_cal - protein_cal_min - fat_cal)/4
    CarbPmax = (current_cal - protein_cal_max - fat_cal)/4
    print("----------------------------------------")
    print(f"Your today caloric intake is: {round(current_cal)} kcal")
    print(f"ProteinMIN = {round(protein_min)} g, ProteinMAX = {round(protein_max)} g")
    print(f"Fat = {round(fat)} g")
    print(f"For Carb, ProteinMIN = {round(CarbPmin)} g, ProteinMAX = {round(CarbPmax)} g")
elif day_type == "c":
    current_cal *= 0.9
    CarbPmin = (current_cal - protein_cal_min - fat_cal)/4
    CarbPmax = (current_cal - protein_cal_max - fat_cal)/4
    print("----------------------------------------")
    print(f"Your today caloric intake is: {round(current_cal)} kcal")
    print(f"ProteinMIN = {round(protein_min)} g, ProteinMAX = {round(protein_max)} g")
    print(f"Fat = {round(fat)} g")
    print(f"For Carb, ProteinMIN = {round(CarbPmin)} g, ProteinMAX = {round(CarbPmax)} g")
elif day_type == "r":
    current_cal *= 1
    CarbPmin = (current_cal - protein_cal_min - fat_cal)/4
    CarbPmax = (current_cal - protein_cal_max - fat_cal)/4
    print("----------------------------------------")
    print(f"Your today caloric intake is: {round(current_cal)} kcal")
    print(f"ProteinMIN = {round(protein_min)} g, ProteinMAX = {round(protein_max)} g")
    print(f"Fat = {round(fat)} g")
    print(f"For Carb, ProteinMIN = {round(CarbPmin)} g, ProteinMAX = {round(CarbPmax)} g")
else:
    print("----------------------------------------")
    print("Please enter the correct day type (t/c/r)")