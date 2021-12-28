FROM node:alpine
WORKDIR /client
COPY client/package.json /client
RUN npm install
COPY client/src /client/src

WORKDIR /client/client
CMD ["npm", "start"]
