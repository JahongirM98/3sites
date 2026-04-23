FROM node:18

WORKDIR /app

COPY package.json package-lock.json* ./

RUN npm install

COPY . .

CMD ["./node_modules/.bin/tailwindcss", "-i", "./services/tojirplast_site/static/css/tailwind.css", "-o", "./services/tojirplast_site/static/css/styles.css", "--watch"]