import os

def main():
    while True:
        choice = input("Выберите действие: (1) просмотреть заметки, (2) добавить заметку, (3) удалить заметку, (4) выход: ")
        if choice == "1":
            show_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            break
        else:
            print("Неправильный ввод. Попробуйте еще раз.")

def show_notes():
    if not os.path.exists("notes.txt"):
        print("Заметок нет.")
        return

    with open("notes.txt", "r") as f:
        notes = f.readlines()

    if not notes:
        print("Заметок нет.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note.strip()}")

def add_note():
    note = input("Введите заметку: ")
    with open("notes.txt", "a") as f:
        f.write(f"{note}\n")
    print("Заметка добавлена.")

def delete_note():
    show_notes()
    note_num = input("Введите номер заметки, которую нужно удалить: ")
    if not note_num.isdigit():
        print("Неправильный ввод. Попробуйте еще раз.")
        return

    note_num = int(note_num)
    with open("notes.txt", "r") as f:
        notes = f.readlines()

    if note_num < 1 or note_num > len(notes):
        print("Неправильный номер заметки. Попробуйте еще раз.")
        return

    notes.pop(note_num-1)
    with open("notes.txt", "w") as f:
        f.writelines(notes)

    print("Заметка удалена.")

if __name__ == "__main__":
    main()