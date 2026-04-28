# Deployment Instructions for Vercel

## Current Setup:
- **Frontend (Vercel):** https://enati.vercel.app  
- **Backend (Python):** http://188.137.251.108:5001
- **Node.js Proxy:** Running on Vercel (serves frontend + proxies API calls)

## Environment Variables needed in Vercel:
- `PYTHON_SERVER_URL` = `http://188.137.251.108:5001`

## API Endpoints:
- `/api/top-groups` → proxies to Python server
- `/api/shared-contracts` → proxies to Python server  
- `/api/latest-records` → proxies to Python server
- `/api/top-coins/:groupId` → proxies to Python server
- `/api/token-image/:contractAddress` → proxies to Python server

## To update deployment:
1. Set environment variable in Vercel dashboard
2. Push code changes to GitHub
3. Vercel auto-deploys from main branch