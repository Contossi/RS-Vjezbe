import express from 'express'
import cors from 'cors'
import { readFile } from 'node:fs/promises'

const app = express()
const PORT = process.env.PORT || 3000

app.use(cors())

// Datoteka se cita pri svakom zahtjevu, pa novi podaci u data/ vrijede bez restarta servera
function serveData(fileName) {
  const file = new URL(`./data/${fileName}`, import.meta.url)
  return async (req, res) => {
    res.json(JSON.parse(await readFile(file, 'utf8')))
  }
}

app.get('/', (req, res) => {
  res.json({ message: 'REST API radi. Pogledaj /api/products, /api/reviews i /api/shipping' })
})

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', uptime: process.uptime(), time: new Date().toISOString() })
})

app.get('/api/products', serveData('products.json'))
app.get('/api/reviews', serveData('reviews.json'))
app.get('/api/shipping', serveData('shipping.json'))

app.listen(PORT, () => {
  console.log(`Server slusa na portu ${PORT}`)
})
