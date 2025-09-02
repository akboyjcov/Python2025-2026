def get_note_name(note_number):
    notes = {
        1: "до",
        2: "ре", 
        3: "ми",
        4: "фа",
        5: "соль",
        6: "ля",
        7: "си"
    }
    
    if note_number in notes:
        return notes[note_number]
    else:
        return None

note_input = input("Введите номер ноты (1-7): ")

if note_input.isdigit():
    note_num = int(note_input)
    note_name = get_note_name(note_num)
    
    if note_name:
        print(f"{note_num} – {note_name}")
    else:
        print("Ошибка! Номер ноты должен быть от 1 до 7")
else:
    print("Ошибка! Введите целое число от 1 до 7")