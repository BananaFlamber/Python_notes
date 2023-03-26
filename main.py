import json
from datetime import datetime

FILENAME = 'notes.json'

def main():
    while True:
        command = input('Введите команду (add, edit, delete, filter, list, exit): ')
        if command == 'add':
            add_note()
        elif command == 'edit':
            edit_note()
        elif command == 'delete':
            delete_note()
        elif command == 'filter':
            filter_notes()
        elif command == 'list':
            print_all_notes()
        elif command == 'exit':
            break
        else:
            print("Неправильный ввод. Попробуйте еще раз.")

def load_notes():
    try:
        with open(FILENAME, 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open(FILENAME, 'w') as f:
        json.dump(notes, f)

def add_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
    timestamp = datetime.now().isoformat()
    note = {
        'id': len(load_notes()) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print('Заметка успешно сохранена')

def edit_note():
    note_id = input('Введите номер заметки, которую нужно отредактировать: ')
    notes = load_notes()
    for note in notes:
        if note['id'] == int(note_id):
            note['title'] = input('Введите новый заголовок заметки: ')
            note['body'] = input('Введите новое тело заметки: ')
            note['timestamp'] = datetime.now().isoformat()
            save_notes(notes)
            print('Заметка успешно отредактирована')
            return
    print('Заметка не найдена')

def delete_note():
    note_id = input('Введите номер заметки, которую нужно удалить: ')
    notes = load_notes()
    for note in notes:
        if note['id'] == int(note_id):
            notes.remove(note)
            save_notes(notes)
            print('Заметка успешно удалена')
            return
    print('Заметка не найдена')

def filter_notes():
    date_str = input('Введите дату в формате ГГГГ-ММ-ДД: ')
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print('Неверный формат даты')
        return
    notes = load_notes()
    filtered_notes = [note for note in notes if datetime.fromisoformat(note['timestamp']).date() == date.date()]
    print_notes(filtered_notes)

def print_notes(notes):
    for note in notes:
        print(f"{note['id']}. {note['title']}\n{note['body']}\n{note['timestamp']}\n")

def print_all_notes():
    notes = load_notes()
    print_notes(notes)

if __name__ == "__main__":
    main()