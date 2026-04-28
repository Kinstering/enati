# Тестирование Python сервера

## Твой Python сервер запущен на: http://188.137.251.108:5001

## Проверь работает ли он:

### 1. В браузере открой:
```
http://188.137.251.108:5001/api/top-groups
http://188.137.251.108:5001/api/shared-contracts
http://188.137.251.108:5001/api/latest-records
```

### 2. Или через curl на сервере:
```bash
curl http://127.0.0.1:5001/api/top-groups
curl http://127.0.0.1:5001/api/shared-contracts
curl http://127.0.0.1:5001/api/latest-records
```

### 3. Открой порт 5001 в файрволе:
```bash
sudo ufw allow 5001
sudo ufw status
```

### 4. Проверь что порт доступен извне:
```bash
# На другом компьютере:
curl http://188.137.251.108:5001/api/top-groups
```