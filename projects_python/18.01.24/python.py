all_contacts = []
contacts = []
i = 1

while(True):
    name = input("Введіть ім`я контакта: ")
    number = input("Введіть номер контакта: ")
    contacts_dict = { f"Контакт {i}": {"Ім`я контакта": name,
                                          "Номер контакта":number},}
    all_contacts.append(contacts_dict)
    i += 1
    while(True):
        quastion = input("Що далі? \n 1 - додати новий контакт, 2 - подивитися всі контакти \n 3 - видалити контакт \n 4 - поширити контакт ")
        if (quastion == "1"):
            numbers_contacts = len(all_contacts)
            if(numbers_contacts == 9):
                print("\nУ вас вже максимально контактів\n")
                break
            else:
                break
        elif (quastion == "2"):
            numbers_contacts = len(all_contacts)
            if(numbers_contacts == 9):
                print(all_contacts)
            elif(numbers_contacts < 9):
                print(all_contacts)
                break
        elif (quastion == "3"):
            print(all_contacts)
            delete = int(input("Який контакт хочете видалити? "))
            if(delete >= 1 and delete <= 10):
                all_contacts.pop(delete-1)
                for j in range(delete-1, len(all_contacts)):
                    all_contacts[j] = {f"Контакт {j+1}": all_contacts[j][f"Контакт {j+2}"]}
                i -= 1
                break
            else:
                print("Помилка, такого контакта нема")
                break
        elif (quastion == "4"):
            print(all_contacts)
            quastion3 = int(input("Який контакт ви хочете відправити "))
            if(quastion3 >= 1):
                current_contact = all_contacts[quastion3 - 1]
                print(f"Вам прийшов новий контакт: {current_contact}")
                break
            else:
                print("Помилка")
                break
        else:
            print("\nПомилка, спробуйте ще раз\n")