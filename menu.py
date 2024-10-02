import functions as f
import os

menu_options = {
    "1": ("Выборочное среднее", f.chosen_mean),
    "2": ("Исправленная выборочная дисперсия", f.fix_dispersion),
    "3": ("Мода", f.find_mode),
    "4": ("Медиана", f.find_median),
    "5": ("Эксцесс", f.find_excess),
    "6": ("Асимметрия", f.find_assimetr)
}

while True:
    print("Что вычисляем?\n1.Выборочное среднее\n2.Исправленную выборочную дисперсию\n3.Моду\n4.Медиану\n5.Эксцесс\n6.Асимметрию\nq.Выход")
    var = input("\nВаш выбор: ")

    if var == "q":
        break

    if var in menu_options:
        os.system('CLS')
        option_name, function = menu_options[var]
        print(f"{option_name}: {function()}\n")

    else:
        os.system('CLS')
        print("Ошибка: неверная функция.\n")