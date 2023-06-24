phone_book = []
path = 'phones.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment, *_ = contact.strip().split(':')
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})

def save_file():
    contact = []
    new_phone_book = []
    for dictionary in phone_book:
        for value in dictionary:
            contact.append(str(dictionary[value]))
        new_phone_book.append(':'.join(contact)+'\n')
        contact.clear()
    with open(path, 'w', encoding='UTF-8') as file:
        file.writelines(new_phone_book)
    file.close()
    

def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list) + 1}


def add_contact(new: dict):
    new.update(check_id())
    phone_book.append(new)

def delete_contact(index: int):
    phone_book.pop(index-1)
    
          
def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field


