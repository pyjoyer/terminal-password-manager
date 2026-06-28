import getpass

print("\n" * 40)
file = open(r'Q:\programming\passwordmanager\masterpassword.txt', 'r')
master_password = file.read().strip()
file.close()
print("Добро пожаловать в терминальный менеджер паролей, введите Мастер-пароль: ")
password = getpass.getpass()
if password == master_password:
    print("Доступ разрешен!")
    while True:
        print("\n" * 40)
        print("1 - добавить пароль")
        print("2 - посмотреть сохраненный пароль")
        print("3 - изменить пароль от сайта/сервиса")
        print("4 - очистить базу паролей")
        print("5 - выйти")
        choice = input("Выберете действие: ")
        if choice == "5":
            break
        elif choice == "1":
            service = input("Введите название сервиса/сайта: ")
            password = input("Введите пароль от сервиса/сайта: ")
            service_password = f'{service}: {password}\n'
            file = open(r'Q:\programming\passwordmanager\passwords.txt', 'a')
            file.write(service_password)
            file.close()
            input("Пароль успешно сохранен! Нажмите Enter чтобы вернуться в главное меню...")
        elif choice == "2":
            search = input("Введите название сайта/сервиса: ").lower()
            found = False
            file = open(r'Q:\programming\passwordmanager\passwords.txt', 'r')
            for line in file:
                line = line.strip()
                parts = line.split(": ")
                if parts[0].lower() == search:
                    print(f'Пароль от {search}: {parts[1]}')
                    found = True
                    break
            file.close()
            if found == False:
                    print("Ошибка: такого сайта нет в базе данных!")
            a = input("Нажмите Enter чтобы продолжить...")
        elif choice == "4":
            answer = input("Вы уверены? Все пароли будут удалены навсегда! (да/нет)\n")
            if answer.lower() == "да":
                file = open(r'Q:\programming\passwordmanager\passwords.txt', 'w')
                file.close()
                print("Пароли успешно удалены!")
                input("Нажмите Enter чтобы вернуться в главное меню...")
            elif answer.lower() == "нет":
                continue
        elif choice == "3":
            search = input("Пароль от какого сайта хотите изменить?\n").lower()
            new_pass = input("Какой новый пароль хотите установить?\n")
            found = False
            passwords_and_services = []
            file = open(r'Q:\programming\passwordmanager\passwords.txt', 'r')
            for line in file:
                line = line.strip()
                parts = line.split(": ")
                if search == parts[0]:
                    service_password = f'{parts[0]}: {new_pass}\n'
                    passwords_and_services.append(service_password)
                    found = True
                else:
                    old_line = f'{parts[0]}: {parts[1]}\n'
                    passwords_and_services.append(old_line)
            file.close()
            if found == True:
                file = open(r'Q:\programming\passwordmanager\passwords.txt', 'w')
                for char in passwords_and_services:
                    file.write(char)
                file.close()
                print(f"Пароль успешно изменен для сервиса {search}!")
                input("Нажмите Enter для возвращения в главное меню...")
            else:
                print("Ошибка,такого файла нет в базе!")
else:
    print("Ошибка! Неверный пароль")