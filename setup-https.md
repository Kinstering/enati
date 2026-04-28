# Настройка HTTPS для Python сервера

## Вариант 1: Cloudflare Tunnel (Быстро и бесплатно)

### 1. На Ubuntu сервере установи cloudflared:
```bash
# Скачай cloudflared
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb

# Создай туннель (нужен аккаунт Cloudflare)
cloudflared tunnel login
cloudflared tunnel create enati-api
```

### 2. Настрой туннель на порт 5001:
```bash
cloudflared tunnel --url localhost:5001
```

**Ты получишь HTTPS URL типа: `https://abc-def-ghi.trycloudflare.com`**

### 3. Обнови переменную в Vercel:
- `PYTHON_SERVER_URL` = `https://abc-def-ghi.trycloudflare.com`

## Вариант 2: Nginx + Let's Encrypt

### 1. Установи Nginx:
```bash
sudo apt install nginx
```

### 2. Настрой proxy в Nginx:
```nginx
# /etc/nginx/sites-available/enati-api
server {
    listen 80;
    server_name your-domain.com;  # или используй IP
    
    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 3. Включи сайт:
```bash
sudo ln -s /etc/nginx/sites-available/enati-api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## Вариант 3: Переместить Python сервер на облако

Деплой Python сервера на:
- **Railway** (рекомендую)
- **Render** 
- **Heroku**