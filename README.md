# Урок 14. SQL. Домашнее задание

На этой неделе мы начали работу с SQL и научились делать простейшие запросы к базам данных.  Сначала предлагаем применить полученные знания в тренажере, а потом попробовать написать свой простой проект с нуля.

**Шаг 0**

Создайте проект в PyCharm, поместите в ту же папку файл с базой данных.

[База данных находится тут.](https://github.com/skypro-008/lesson14/blob/master/part1/netflix.db) 

Импортируйте модуль `sqlite3` для работы с БД. 

Создайте подключение к БД с помощью метода `sqlite3.connect`.

**Шаг 1**

Реализуйте поиск по названию. 

Если таких фильмов несколько, выведите самый свежий. 

Сперва напишите SQL запрос

Затем напишите функцию, которая принимала бы title и возвращала бы данные  в таком формате:

```json
{
		"title": "title",
		"country": "country",
		"release_year": 2021,
		"genre": "listed_in",
		"description": "description"
}
```

Затем напишите вьюшку для маршрута `/movie/<title`> , которая бы выводила данные про фильм

**Шаг 2**

Сделайте поиск по диапазону лет выпуска. 

Сперва напишите SQL запрос. Фильмов будет много, так что ограничьте вывод 100 тайтлами. 

Затем напишите функцию, которая принимала бы два года и возвращала бы данные  в таком формате:

```json
[
	{"title":"title",
	 "release_year": 2021},
	{"title":"title",
	 "release_year": 2020}
]
```

Затем напишите вьюшку для маршрута `/movie/year/to/year`, которая бы выводила список словарей.

**Шаг 3**

Реализуйте поиск по рейтингу. Определите группы: для детей, для семейного просмотра, для взрослых.

- G — нет возрастных ограничений.
- PG — желательно присутствие родителей.
- PG-13 — для детей от 13 лет в присутствии родителей.
- R — дети до 16 лет допускаются на сеанс только в присутствии родителей.
- NC-17 — дети до 17 лет не допускаются.
- 

Сперва напишите SQL запрос.

Затем напишите функцию, которая принимала бы список допустимых рейтингов и возвращала данные в том же формате, что и в прошлом шаге. 

```python
Формат ответа:

[
	{
	 "title":"title",
	 "rating": "rating",
	 "description":"description"
	},
	{
		"title":"title",
	 "rating": "rating",
	 "description":"description"
   },
]
```

Создайте несколько вьюшку, которая обрабатывала бы несколько маршрутов в соответствии с определенными группами. Выведите в каждом список словарей, содержащий информацию о названии, рейтинге и описании.

```python
Формат запроса:

/rating/children #(включаем сюда рейтинг G)

/rating/family   #(G, PG, PG-13)

/rating/adult    #(R, NC-17)
```

**Шаг 4**

Напишите функцию, которая получает название жанра в качестве аргумента и возвращает 10 самых свежих фильмов в формате json. 

Сперва напишите SQL запрос.

Затем напишите функцию, которая принимала бы `жанр` и возвращала данные в формате:

```python
[{
	 "title":"title",
	 "description":"description"
}]
```

Создайте вьюшку `/genre/<genre>` которая возвращала бы список

В результате должно содержаться название и описание каждого фильма.

**Шаг 5**

Напишите функцию, которая получает в качестве аргумента имена двух актеров, сохраняет всех актеров из колонки cast и возвращает список тех, кто играет с ними в паре больше 2 раз. 

Для этого задания не требуется создавать вьюшку

В качестве теста можно передать: Rose McIver и Ben Lamb, Jack Black и Dustin Hoffman.

**Шаг 6**

Напишите функцию, с помощью которой можно будет передавать **тип** картины (фильм или сериал), **год выпуска** и ее **жанр** и получать на выходе список названий картин с их описаниями в JSON.

Сперва напишите SQL запрос, затем напишите функцию, которая принимала бы `тип, год, жанр`

Для этого задания не требуется создавать вьюшку