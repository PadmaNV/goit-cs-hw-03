from pymongo import MongoClient


# Підключення до MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/?authSource=NVI_database_mongo&directConnection=true')
db = client['cats_database']
collection = db['cats_collection']


# Читання (Read)
def display_all_cats():
    cats = collection.find({})
    for cat in cats:
        print(cat)

def display_cat_info_by_name(name):
    cat = collection.find_one({'name': name})
    if cat:
        print(cat)
    else:
        print(f"Кіт з ім'ям '{name}' не знайдено.")

# Оновлення (Update)
def update_cat_age(name, new_age):
    collection.update_one({'name': name}, {'$set': {'age': new_age}})
    print(f"Вік кота з ім'ям '{name}' оновлено до {new_age} років.")

def add_feature_to_cat(name, new_feature):
    collection.update_one({'name': name}, {'$push': {'features': new_feature}})
    print(f"До кота з ім'ям '{name}' додано нову характеристику: '{new_feature}'.")

# Видалення (Delete)
def delete_cat_by_name(name):
    result = collection.delete_one({'name': name})
    if result.deleted_count > 0:
        print(f"Кіт з ім'ям '{name}' видалено.")
    else:
        print(f"Кіт з ім'ям '{name}' не знайдено.")

def delete_all_cats():
    result = collection.delete_many({})
    print(f"Видалено всі записи. Загалом видалено {result.deleted_count} котів.")



'''+++++++++++++  Приклад використанн  ++++++++++++++++'''

# Внесення даних в базу:
cats_data = [
    {
        "name": "Мурзик",
        "age": 2,
        "features": ["чорний", "любить снідати", "грається з мишами"],
    },
    {
        "name": "Барсік",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    },
    {
        "name": "Рябко",
        "age": 4,
        "features": ["полюбляє їсти", "весела іграшка", "ласкава до дітей"],
    }
]


result = collection.insert_many(cats_data)

if __name__ == "__main__":

    # Читання;
    print("Усі коти:")
    display_all_cats()
    print()

    # print("Інформація про кота за ім'ям:")
    # display_cat_info_by_name("Барсік")
    # print()

    # Оновлення
    # update_cat_age("Барсік", 5)
    # add_feature_to_cat("Барсік", "лінивий")
    # print()

    # # Видалення
    # delete_cat_by_name("Рябко")
    # delete_all_cats()
