score = 0

if input("Правда ли, что в Phyton есть 3 основных типов данных?") == "да":
    score += 1

else:
    score -= 1

if input("Правда ли, что 3+5 == 1 -9?") == "да":
    score += 1
else:
    score += 1
if input("Правда ли,что 3.5 метра 350см?") == "да":
    score += 1
else:
    score-= 1
if input("Правда ли,что if - один из условных операторов") =="да": score += 1
else:
    score -= 1

print(f"У тебя {score} очков!")
if score > 0 : print("У Тебя положительный результат!")
else:
 print(" В следующий раз посторайся лучше!")


