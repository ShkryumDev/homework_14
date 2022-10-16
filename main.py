# Импортируем необходимые данные
import sqlite3
import flask
from flask import json


# Создаем подключение к базе данных
def run_sql(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        result = []
        for item in connection.execute(sql).fetchall():
            result.append(dict(item))

        return result


# Передаем переменную приложению app
app = flask.Flask(__name__)


# Функция, которая принимает title и возвращает данные
@app.get("/movie/<title>")
def step_1(title):
    sql = f'''select title, country, release_year, listed_in as genre, description from netflix where title="{title}"
    order by date_added desc
    limit 1'''

    result = run_sql(sql)
    if result:
        result = result[0]

    return flask.jsonify(result)


# Функция, которая принимает два года и возвращает данные
@app.get("/movie/<int:year1>/to/<int:year2>")
def step_2(year1, year2):
    sql = f'''
            select title, release_year from netflix
            where release_year between {year1} and {year2}
            order by release_year desc'''

    return flask.jsonify(run_sql(sql))


# Функция, которая выполняет поиск по рейтингу
@app.get("/rating/<rating>")
def step_3(rating):
    my_dict = {
        "children": ("G", "G"),
        "family": ("G", "PG", "PG-13"),
        "adult": ("R", "NC-17")
    }

    sql = f'''
            select title, rating, description from netnetflix
            where rating in {my_dict.get(rating, ("PG-13", "NC-17"))}
    '''


# Функция, которая получает название жанра и возвращает фильмы в формате json
@app.get("/genre/<genre>")
def step_4(genre):
    sql = f'''select * from netflix
    where listed_in like "%{genre.title()}%"
     '''
    return flask.jsonify(run_sql(sql))


# Функция, которая получает имена двух актеров, сохраняет всех актеров из колонки cast и возвращает
# список, кто играет с ними в паре больше 2 раз
def step_5(name1="Rose McIver", name2="Ben Lamb"):
    sql = f'''select "cast" from netflix
    where "cast" like "%{name1}%" and "cast" like "%{name2}%"
    '''
    result = run_sql(sql)

    actor_name = {}
    for item in result:
        names = item.get("cast").split(", ")
        for name in names:
            actor_name[name] = actor_name.get(name, 0) + 1

    result = []
    for item in actor_name:
        if item not in (name1, name2) and actor_name[item] > 2:
            result.append(item)
    return result


# Функция, с помощью которой передаем тип картины, год выпуска и жанр и получаем список названий картин с
# их описаниями в формате JSON
def step_6(types="TV Show", release_year=2021, genre="TV"):
    sql = f'''select * from netflix
    where type = "{types}"
    and release_year = "{release_year}"
    and listed_in like "%{genre}%"
    '''
    return json.dumps(run_sql(sql), indent=4, ensure_ascii=False)


# Пишем условие, которое проверяет, что файл запущен напрямую
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
