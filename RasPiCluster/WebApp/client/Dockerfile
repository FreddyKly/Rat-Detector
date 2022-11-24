FROM node:latest
WORKDIR /usr/src/WebApp
COPY ./ ./client/
RUN cd client && npm install

EXPOSE 8080

CMD ["npm", "run", "serve"]