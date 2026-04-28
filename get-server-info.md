# Как узнать URL своего сервера

## На Ubuntu сервере выполни:

### 1. Узнать публичный IP:
```bash
curl ifconfig.me
# или
curl ipinfo.io/ip
```

### 2. Проверить, на каком порту запущен сервер:
```bash
netstat -tlnp | grep :3001
# или
ss -tlnp | grep :3001
```

### 3. Твой URL будет:
```
http://YOUR_PUBLIC_IP:3001
```

### 4. Если настроил домен и SSL:
```
https://your-domain.com
```

## Пример для Node.js сервера:

Когда запускаешь сервер, он покажет:
```
Server is running on http://localhost:3001
Leaderboards page: http://localhost:3001/leaderboards
...
```

Но для внешнего доступа замени `localhost` на публичный IP.