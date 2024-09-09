def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
inner_function()
 # Ошибка NameError: потому что программа не может спуститься и глобального простраства имен в локальный, и тем более
 # объемлющий. процесс поиска переменных и фунций обратный.
