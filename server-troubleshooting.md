# Решение проблемы с портом 5000

## 1. Найти что использует порт 5000:
```bash
sudo lsof -i :5000
# или
sudo netstat -tlnp | grep :5000
# или
sudo ss -tlnp | grep :5000
```

## 2. Остановить процесс (замени PID на реальный):
```bash
sudo kill -9 PID_ПРОЦЕССА
```

## 3. Или запустить Python сервер на другом порту:
```python
# В конце server.py измени:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  # Используй порт 5001
```

## 4. Если изменил порт Python сервера, обнови Node.js server.js:
```javascript
// Замени все упоминания :5000 на :5001
const pythonServerUrl = process.env.PYTHON_SERVER_URL || 'http://127.0.0.1:5001'
```

## 5. Команды для запуска на Ubuntu:

### Запуск Python сервера в фоне:
```bash
nohup python3 server.py > server.log 2>&1 &
```

### Проверить что запущено:
```bash
ps aux | grep python
```

### Остановить все Python процессы:
```bash
pkill -f "python.*server.py"
```