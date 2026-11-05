// URL backenda se postavlja kroz VITE_API_URL u trenutku builda (lokalno .env.development, na Renderu environment varijabla)
const API_URL = (import.meta.env.VITE_API_URL || 'http://localhost:3000').replace(/\/$/, '')

async function request(path) {
  const res = await fetch(`${API_URL}${path}`)
  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    throw new Error(body.error || `HTTP ${res.status}`)
  }
  return res.json()
}

export const api = {
  url: API_URL,
  health: () => request('/api/health'),
  getProducts: () => request('/api/products'),
  getReviews: () => request('/api/reviews'),
  getShipping: () => request('/api/shipping')
}
