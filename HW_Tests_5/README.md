# Академия Аналитиков Авито
# Домашняя работа по тестированию
# Задание 5

## Инструкция по запуску

1. Проверьте, что python установлен на ваш компьютер
2. Установите зависимости
```bash
pip install -r requirements.txt
```

3. Для выполнения тестов используйте`coverage`: 

```bash
coverage run what_is_year_now.py
```

4. Для генерации отчета используйте: (такой же файл как в этой папке)

```bash
coverage html 
```

5. Для записи все в файл result (такой же файл как в этой папке)
```bash
{ 
    echo "Установка зависимостей:"; 
    echo "$ pip install -r requirements.txt"; pip install -r requirements.txt; 
    echo "\nЗапуск тестов:"; 
    echo "$ coverage run what_is_year_now.py"; coverage run what_is_year_now.py; 
    echo "\nГенерация отчета о покрытии:"; 
    echo "$ coverage html"; coverage html; 
} &> result.txt
```


