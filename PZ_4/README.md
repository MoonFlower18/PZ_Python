# Практичеcкое задание №4
Проектирование и разработка безопасного программного обеспечения информационно-аналитических систем

## Задание
Разработать программное обеспечение проверки криптостойкости паролей с использованием атаки методом грубой силы 
(брутфорс). Найдите с помощью алгоритма полного перебора пятибуквенные  пароли, соответствующие следующим  
хэш-значениям SHA-256 и выведите их  на экран:

**_Первый хэш:_**
```{}
1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad
```

**_Второй хэш:_**
```{}
3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b
```

**_Третий хэш:_**
```{}
74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f
```

Хэш значения могут считываться из файла или непосредственно с консоли (формы для ввода хэш-значения). Ваша 
программа должна перебрать все возможные пароли, состоящие только из пяти строчных букв английского алфавита ASCII.
Программа должна иметь возможность запуска перебора в однопоточном режиме или в многопоточном режиме (количество 
потоков может задаваться пользователем). Для каждого режима необходимо выводить затраченное время на подбор