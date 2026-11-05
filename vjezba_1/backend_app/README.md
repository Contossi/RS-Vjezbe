# Backend App (Express.js REST API)

REST API webshopa. Podaci se citaju iz JSON datoteka u `data/`, a svaki izvor je neovisan o ostalima.

## Endpointi

| Metoda | Putanja         | Datoteka              | Opis            |
| ------ | --------------- | --------------------- | --------------- |
| GET    | `/api/health`   |                       | Status servera  |
| GET    | `/api/products` | `data/products.json`  | Proizvodi       |
| GET    | `/api/reviews`  | `data/reviews.json`   | Recenzije       |
| GET    | `/api/shipping` | `data/shipping.json`  | Opcije dostave  |

## Format podataka

Svaka datoteka sadrzi JSON listu objekata s ovim poljima:

| Datoteka        | Polja                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------- |
| `products.json` | `id` (broj), `name` (tekst), `price` (broj, EUR), `category` (tekst)                           |
| `reviews.json`  | `id` (broj), `customer` (tekst), `rating` (cijeli broj 1-5), `comment` (tekst)                 |
| `shipping.json` | `id` (broj), `name` (tekst), `price` (broj, EUR), `days` (cijeli broj, rok isporuke u danima)  |

## Vlastiti generator podataka

Program koji priprema podatke (npr. Python s korutinama) treba samo prepisati ove datoteke u istom formatu. Lokalno server novi sadrzaj vraca odmah, bez restarta. Za Render datoteke treba commitati i pushati, jer se tako pokrece novi deploy.

## Lokalno

```bash
npm install
npm run dev   # http://localhost:3000
```

## Deploy na Render.com (Web Service)

| Postavka       | Vrijednost             |
| -------------- | ---------------------- |
| Root Directory | `vjezba_1/backend_app` |
| Runtime        | Node                   |
| Build Command  | `npm install`          |
| Start Command  | `npm start`            |
