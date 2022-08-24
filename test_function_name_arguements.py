import inspect

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def your_function():
    pass


def print_function_info(names):
    function_names = names.__name__
    arguments_values = names.__code__.co_varnames
    print('Function: ', *function_names.capitalize().replace("_", " "), sep='')
    if len(arguments_values) > 0:
        print('Argument: ', *arguments_values, '\n')
    else:
        print("The function has no arguments")


list_functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page, your_function]
for names in list_functions:
    print_function_info(names)