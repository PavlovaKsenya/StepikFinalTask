# StepikFinalTask
Project with Page Object model

[Ссылка на курс](https://stepik.org/course/575)

### Запуск тестов и генерация отчёта
1. Установить pytest, selenium, allure-pytest, pytest-xdist:
```
pip install pytest selenium allure-pytest pytest-xdist
```
2. Выполнить:
```
pytest tests -n auto --dist loadscope --alluredir report 
```
```
allure serve report
```