// Пример интеграции LiqPay для Node.js

const crypto = require('crypto');
const express = require('express');

// Настройки LiqPay
const LIQPAY_PUBLIC_KEY = 'твой_публичный_ключ';
const LIQPAY_PRIVATE_KEY = 'твой_приватный_ключ';

// Функция для создания подписи
function createSignature(data, privateKey) {
    const string = Buffer.from(data).toString('base64') + privateKey;
    return crypto.createHash('sha1').update(string).digest('base64');
}

// Создание платежной формы
function createPaymentForm(amount, orderId, description) {
    const data = {
        version: 3,
        public_key: LIQPAY_PUBLIC_KEY,
        action: 'pay',
        amount: amount,
        currency: 'UAH',
        description: description,
        order_id: orderId,
        result_url: 'https://yourdomain.com/payment/success',
        server_url: 'https://yourdomain.com/payment/callback'
    };
    
    const dataBase64 = Buffer.from(JSON.stringify(data)).toString('base64');
    const signature = createSignature(JSON.stringify(data), LIQPAY_PRIVATE_KEY);
    
    return {
        data: dataBase64,
        signature: signature,
        form_html: `
            <form method="POST" action="https://www.liqpay.ua/api/3/checkout" accept-charset="utf-8">
                <input type="hidden" name="data" value="${dataBase64}" />
                <input type="hidden" name="signature" value="${signature}" />
                <button type="submit">Оплатить ${amount} грн</button>
            </form>
        `
    };
}

// API endpoint для создания платежа
app.post('/api/create-payment', (req, res) => {
    const { amount, description } = req.body;
    const orderId = 'order_' + Date.now();
    
    const payment = createPaymentForm(amount, orderId, description);
    
    res.json({
        success: true,
        payment_data: payment.data,
        signature: payment.signature,
        form_html: payment.form_html
    });
});

// Callback для обработки результата платежа
app.post('/payment/callback', (req, res) => {
    const { data, signature } = req.body;
    
    // Проверяем подпись
    const expectedSignature = createSignature(data, LIQPAY_PRIVATE_KEY);
    
    if (signature !== expectedSignature) {
        return res.status(400).send('Invalid signature');
    }
    
    // Декодируем данные
    const paymentData = JSON.parse(Buffer.from(data, 'base64').toString());
    
    if (paymentData.status === 'success') {
        // Платеж успешен - активируем услугу
        console.log('Payment successful:', paymentData);
        
        // Здесь твоя логика:
        // - Обновить базу данных
        // - Активировать премиум функции
        // - Отправить email подтверждение
        
        updateUserSubscription(paymentData.order_id, paymentData.amount);
    }
    
    res.send('OK');
});

function updateUserSubscription(orderId, amount) {
    // Твоя логика обновления подписки
    console.log(`Activating subscription for order ${orderId}, amount: ${amount}`);
}