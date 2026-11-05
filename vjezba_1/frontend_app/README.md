# Frontend App (Vue.js + Vite)

Vue 3 webshop: proizvodi, recenzije i opcije dostave ucitavaju se s API-ja istovremeno i neovisno jedni o drugima, a kosarica se drzi u pregledniku. Build generira staticni sadrzaj u `dist/` (`dist/index.html` + `dist/assets/`).

## Lokalno

```bash
npm install
npm run dev      # razvojni server
npm run build    # generira dist/
npm run preview  # posluzuje dist/ lokalno
```

## Deploy na Render.com (Static Site)

| Postavka          | Vrijednost                     |
| ----------------- | ------------------------------ |
| Root Directory    | `vjezba_1/frontend_app`        |
| Build Command     | `npm install && npm run build` |
| Publish Directory | `dist`                         |

Na Static Siteu dodaj environment varijablu `VITE_API_URL` s URL-om backenda (npr. `https://rs-backend-app.onrender.com`), pa pokreni novi deploy.
