# Frontend App (Vue.js + Vite)

Jednostavna Vue 3 aplikacija (to-do lista). Build generira staticni sadrzaj u `dist/` (`dist/index.html` + `dist/assets/`).

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
