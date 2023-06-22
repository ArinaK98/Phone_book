main_menu = '''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать новый контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход
    '''

menu_choice = 'Выберите пункт меню: '
input_error = 'Некорректный ввод. Введите от 1 до 8'
book_error = 'Телефонная книга пуста или файл не открыт'

open_successful = 'Телефонная книга успешно открыта'
save_successful = 'Телефонная книга успешно сохранена'
input_new_contact = 'Введите данные нового контакта'
new_contact = ['Введите имя контакта: ', 'Введите телефон: ', 'Введите коммент: ']
search_word = 'Введите искомый элемент: '
delete_contact = 'Введите номер контакта, который необходимо удалить: '
delete_contact_error = 'Такого контакта не существует'
delet_contact_successful = 'Контакт успешно удален'
# input_change_contact = 'Введите данные нового контакта'
input_index = 'Введите индекс изменяемого контакта: '
input_change_contact = 'Введите данные изменяемого контакта или Enter? чтоб оставить без изменений: '

def contact_saved(name: str):
    return f'Контакт {name} успешно сохранен'

def contact_changed(name: str):
    return f'Контакт {name} успешно изменен'


