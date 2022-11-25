# FROM --platform=linux/arm64 node:latest
FROM node:latest
WORKDIR /usr/src/WebApp/client
COPY ./ ./
RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve"]
