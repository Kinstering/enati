# Деплой на Ubuntu сервер

## 1. Скопируй файлы на сервер
```bash
scp -r . user@your-server-ip:/path/to/project
```

## 2. На сервере установи зависимости
```bash
npm install
```

## 3. Создай .env файл
```bash
echo "PYTHON_SERVER_URL=http://127.0.0.1:5000" > .env
```

## 4. Установи PM2 для запуска в фоне
```bash
npm install -g pm2
pm2 start src/server.js --name "enati-server"
pm2 startup
pm2 save
```

## 5. Настрой nginx (опционально)
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## 6. Открой порты
```bash
sudo ufw allow 3001
sudo ufw allow 80
sudo ufw allow 443
```