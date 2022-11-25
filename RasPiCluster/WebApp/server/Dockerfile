# FROM --platform=linux/arm64 node:latest
FROM node:latest
WORKDIR /usr/src/WebApp/server
COPY ./ ./
RUN npm install

EXPOSE 5000

CMD ["npm", "run", "start"]