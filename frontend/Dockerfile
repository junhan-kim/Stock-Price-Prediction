FROM node:12.2.0-alpine

WORKDIR /frontend

ENV PATH /node_modules/.bin:$PATH

COPY package.json .
RUN npm install 
COPY . .

CMD ["npm", "start"]