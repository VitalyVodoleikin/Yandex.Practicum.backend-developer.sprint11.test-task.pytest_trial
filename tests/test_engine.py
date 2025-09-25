# # Фикстуры в Pytest
# # ----------

# # test_engine.py
# import pytest

# # Импортируем класс двигателя.
# from engine_class import Engine


# @pytest.fixture
# def engine():
#     """Фикстура возвращает экземпляр класса двигателя."""
#     return Engine()


# # Эта фикстура не возвращает никаких значений, но изменяет объект,
# # созданный другой фикстурой.
# @pytest.fixture
# def start_engine(engine):  # Вызываем фикстуру получения объекта двигателя.
#     """Фикстура запускает двигатель."""
#     # Изменяем значение свойства объекта:
#     engine.is_running = True


# # def test_engine_is_running(engine, start_engine):  # Вызываем обе фикстуры.
# #     """Тест проверяет, работает ли двигатель."""
# #     assert engine.is_running  # Проверяем, что значение атрибута is_running - это True.

# # Фикстура start_engine указана в параметрах теста test_engine_is_running();
# # без фикстуры start_engine тест провалится. Но эта фикстура не возвращает
# # никаких объектов и не используется в самом тесте; получается, что
# # параметр start_engine не применяется в функции.
# # В таких случаях фикстуру можно вызывать не через параметр, а через
# # маркер @pytest.mark.usefixtures. Для этого в параметре декоратора
# # нужно указать название фикстуры в виде строки:

# # Добавляем маркер и указываем название фикстуры строкой.
# @pytest.mark.usefixtures('start_engine')
# def test_engine_is_running(engine):  # А из параметров функции фикстуру start_engine убираем.
#     assert engine.is_running 

# # Если фикстур нужно несколько — их названия можно перечислять через
# # запятую: @pytest.mark.usefixtures('one_fixture', 'another_fixture').
# # Обратите внимание, что такой способ работает только с тестирующими функциями.
# # Если в одной фикстуре нужно вызвать другую — этот маркер не сработает!




# # Автоматически используемые фикстуры
# # ---------->

# # test_engine.py
# import pytest

# from engine_class import Engine


# @pytest.fixture
# def engine():
#     """Фикстура возвращает экземпляр класса двигателя."""
#     return Engine()


# @pytest.fixture(autouse=True)  # Обозначаем фикстуру как автоматически вызываемую.
# def start_engine(engine):
#     """Фикстура запускает двигатель."""
#     engine.is_running = True


# # Вызываем только одну фикстуру. 
# # Запуск двигателя выполнится автоматически, без вызова.
# def test_engine_is_running(engine):  
#     """Тест проверяет, работает ли двигатель."""
#     assert engine.is_running




# # Области видимости фикстуры
# # ---------->

# import pytest

# from engine_class import Engine


# # Укажем для фикстуры engine область видимости 'session';
# # при такой области видимости результат однократного выполнения
# # фикстуры будет храниться для всех вызовов. 
# # Добавьте к декоратору фикстуры engine параметр scope
# # со значением 'session'

# # @pytest.fixture  # Было так
# @pytest.fixture(scope='session')  # Указали область видимости фикстуры
# def engine():
#     """Фикстура возвращает экземпляр класса двигателя."""
#     print('Engine factory')  # Добавьте вывод сообщения.
#     return Engine()


# @pytest.fixture(autouse=True)
# def start_engine(engine):
#     """Фикстура запускает двигатель."""
#     engine.is_running = True


# def test_engine_is_running(engine):  
#     """Тест проверяет, работает ли двигатель."""
#     assert engine.is_running


# # Допишите новый тест.
# def test_check_engine_class(engine):
#     """Тест проверяет класс объекта."""
#     assert isinstance(engine, Engine)





# # Очистка (teardown)
# # ---------->

# import pytest

# from engine_class import Engine


# @pytest.fixture(scope='session')
# def engine():
#     """Фикстура возвращает экземпляр класса двигателя."""
#     print('Engine factory')
#     return Engine()


# @pytest.fixture(autouse=True)
# def start_engine(engine):
#     """Фикстура запускает двигатель."""
#     engine.is_running = True  # Запустим двигатель.
#     # Распечатаем строчку до выполнения теста.
#     print(f'Before test engine.is_running {engine.is_running}') 
#     yield  # В этот момент начинает выполняться тест.
#     engine.is_running = False  # Заглушим двигатель.
#     # Распечатаем строчку после выполнения теста и остановки двигателя.
#     print(f'After test engine.is_running {engine.is_running}') 


# def test_engine_is_running(engine):  
#     """Тест проверяет, работает ли двигатель."""
#     print('test_engine_is_running')  # Выведем название теста.
#     assert engine.is_running


# def test_check_engine_class(engine):
#     """Тест проверяет класс объекта."""
#     print('test_check_engine_class')  # Выведем название теста.
#     assert isinstance(engine, Engine)

# # В отчёте должны отобразиться такие строки:
# # Engine factory
# # Before test engine.is_running True
# # test_engine_is_running
# # .After test engine.is_running False
# # Before test engine.is_running True
# # test_check_engine_class
# # .After test engine.is_running False

# # Выполнены два теста, в отчёте их выполнение обозначено точками. Видно, что строки печатаются именно так, как задумано:  после каждого теста управление переходит обратно к фикстуре, которая глушит двигатель. Таким образом запуск нужного процесса и «уборка за собой» происходит в одной функции-фикстуре.
# # Аналогичным образом можно создавать и закрывать соединения с БД, создавать и удалять файлы или любые объекты.




# conftest.py
# ---------->

# Создайте файл conftest.py; перенесите из файла
# test_engine.py две фикстуры и импорт класса двигателя.

# В файле test_engine.py должны остаться только тестирующие функции.
# Импортировать фикстуры в этот файл не нужно: импортируем
# только класс двигателя.

# test_engine.py
from engine_class import Engine


def test_engine_is_running(engine):  
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running


def test_check_engine_class(engine):
    """Тест проверяет класс объекта."""
    assert isinstance(engine, Engine)
