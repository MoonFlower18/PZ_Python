import hashlib
import itertools
import time
import threading


def hash_password(password):
    # функция для получения хэша пароля
    try:
        return hashlib.sha256(password.encode()).hexdigest()
    except Exception as e:
        print(f"Ошибка при хешировании пароля: {e}")
        return None


def brute_force_sha256(target_hash, start_letter, end_letter, result_list):
    # функция для подбора паролей методом полного перебора
    try:
        for password_tuple in itertools.product(range(start_letter, end_letter + 1), repeat=5):
            password = ''.join(chr(i) for i in password_tuple)
            if hash_password(password) == target_hash:
                result_list.append(password)
    except Exception as e:
        print(f"Ошибка при подборе пароля: {e}")


def threaded_brute_force(target_hash, num_threads):
    # запуск многопоточного подбора паролей
    threads = []
    result_list = []

    # разделение работы между потоками
    try:
        for i in range(num_threads):
            thread = threading.Thread(target=brute_force_sha256,
                                      args=(target_hash, ord('a'), ord('z'), result_list))
            threads.append(thread)
            thread.start()

        # ждем завершения всех потоков
        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"Ошибка при запуске потоков: {e}")

    return result_list


def main():
    # ввод хэш-значения с консоли
    try:
        target_hash = input("Введите хэш-значение SHA-256: ")

        mode = input("Выберите режим (1 - Однопоточный, 2 - Многопоточный): ")

        start_time = time.time()

        if mode == '1':
            result_list = []
            brute_force_sha256(target_hash, ord('a'), ord('z'), result_list)
            elapsed_time = time.time() - start_time

            if result_list:
                print(f"Пароль найден: {result_list[0]}")
            else:
                print("Пароль не найден.")

            print(f"Время затраченное на однопоточный подбор: {elapsed_time:.2f} секунд")

        elif mode == '2':
            num_threads = int(input("Введите количество потоков: ")) # не больше числа ядер (4)
            result_list = threaded_brute_force(target_hash, num_threads)
            elapsed_time = time.time() - start_time

            if result_list:
                print(f"Пароль найден: {result_list[0]}")
            else:
                print("Пароль не найден.")

            print(f"Время затраченное на многопоточный подбор: {elapsed_time:.2f} секунд")

        else:
            print("Некорректный ввод цифры режима.")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
