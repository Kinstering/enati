#!/usr/bin/env python3
"""
Скрипт для полной очистки базы данных
ВНИМАНИЕ: Этот скрипт удалит ВСЕ данные в базе данных!
Используйте только для тестирования или сброса данных.
"""

from pymongo import MongoClient
import os
import sys

def get_database_connection():
    """Подключение к базе данных MongoDB"""
    try:
        # Твоя MongoDB ссылка - ВСТАВЬ СЮДА СВОЮ ССЫЛКУ
        mongo_uri = "ВСТАВЬ_СЮДА_СВОЮ_MONGODB_ССЫЛКУ"
        
        # Можно также использовать переменную окружения для безопасности
        # mongo_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
        
        print(f"Подключение к: {mongo_uri[:50]}...")  # Показываем только начало для безопасности
        client = MongoClient(mongo_uri)
        
        # Попробуй разные названия баз данных
        possible_db_names = ['enati', 'telegram_bot', 'bot_database', 'main']
        
        # Проверим какие базы есть
        existing_dbs = client.list_database_names()
        print(f"Доступные базы данных: {existing_dbs}")
        
        # Найдем нужную базу
        db_name = None
        for name in possible_db_names:
            if name in existing_dbs:
                db_name = name
                break
        
        if not db_name:
            print("Не найдена база данных. Доступные базы:")
            for db in existing_dbs:
                if db not in ['admin', 'local', 'config']:
                    print(f"  - {db}")
            db_name = input("Введите название базы данных: ")
        
        db = client[db_name]
        print(f"Подключено к базе данных: {db_name}")
        return client, db
        
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None, None

def show_collections_info(db):
    """Показать информацию о коллекциях"""
    collections = db.list_collection_names()
    print(f"\nНайдено коллекций: {len(collections)}")
    
    for collection_name in collections:
        collection = db[collection_name]
        count = collection.count_documents({})
        print(f"  - {collection_name}: {count} документов")
    
    return collections

def clear_database(db, collections):
    """Очистить все коллекции в базе данных"""
    print("\n" + "="*50)
    print("ВНИМАНИЕ! ВСЕ ДАННЫЕ БУДУТ УДАЛЕНЫ!")
    print("="*50)
    
    confirmation = input("Введите 'YES' для подтверждения удаления: ")
    
    if confirmation != 'YES':
        print("Операция отменена.")
        return
    
    print("\nОчистка базы данных...")
    
    deleted_total = 0
    for collection_name in collections:
        collection = db[collection_name]
        result = collection.delete_many({})
        deleted_count = result.deleted_count
        deleted_total += deleted_count
        print(f"  ✅ {collection_name}: удалено {deleted_count} документов")
    
    print(f"\n🎉 Всего удалено документов: {deleted_total}")
    print("База данных очищена!")

def main():
    """Основная функция"""
    print("🧹 Скрипт очистки базы данных")
    print("="*40)
    
    # Подключение к БД
    client, db = get_database_connection()
    if not db:
        print("❌ Не удалось подключиться к базе данных")
        sys.exit(1)
    
    # Показать текущее состояние
    collections = show_collections_info(db)
    
    if not collections:
        print("📭 База данных пуста")
        return
    
    # Очистка
    clear_database(db, collections)
    
    # Проверка результата
    print("\nПроверка результата:")
    show_collections_info(db)
    
    # Закрыть соединение
    client.close()
    print("\n✅ Соединение закрыто")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Операция прервана пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        sys.exit(1)