# Backend App (Express.js REST API)

Jednostavan REST API za zadatke. Podaci se drze u memoriji, pa se resetiraju pri svakom restartu servera.

## Endpointi

| Metoda | Putanja          | Opis                               |
| ------ | ---------------- | ---------------------------------- |
| GET    | `/api/health`    | Status servera                     |
| GET    | `/api/tasks`     | Svi zadaci                         |
| GET    | `/api/tasks/:id` | Jedan zadatak                      |
| POST   | `/api/tasks`     | Novi zadatak, body `{ "text": "" }` |
| PATCH  | `/api/tasks/:id` | Izmjena, body `{ "done": true }`   |
| DELETE | `/api/tasks/:id` | Brisanje zadatka                   |

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
