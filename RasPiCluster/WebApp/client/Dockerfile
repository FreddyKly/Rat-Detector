FROM node:latest
WORKDIR /usr/src/WebApp
COPY ./ ./client/
RUN cd client && npm install


WORKDIR /usr/src/WebApp
COPY server/ ./server/
RUN npm install

EXPOSE 8080
EXPOSE 5000

CMD ["node", "./api/server.js"]