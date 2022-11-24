FROM node:latest
WORKDIR /usr/src/WebApp
COPY ./ ./server/
RUN cd server && npm install

EXPOSE 5000

CMD ["npm", "run", "dev"]