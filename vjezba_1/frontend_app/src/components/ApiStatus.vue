<script setup>
import { ref, onMounted } from 'vue'
import { api } from '../api.js'

const status = ref('Provjeravam...')
const ok = ref(null)

async function check() {
  status.value = 'Provjeravam...'
  try {
    const data = await api.health()
    ok.value = true
    status.value = `Server radi (uptime ${Math.round(data.uptime)} s)`
  } catch (err) {
    ok.value = false
    status.value = `Server nedostupan: ${err.message}`
  }
}

onMounted(check)
</script>

<template>
  <section class="status" :class="{ ok: ok === true, error: ok === false }">
    <span>API: {{ api.url }} · {{ status }}</span>
    <button @click="check">Provjeri</button>
  </section>
</template>

<style scoped>
.status {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  margin-bottom: 24px;
  border-radius: 8px;
  background: #eee;
  font-size: 14px;
}

.status.ok {
  background: #e3f6ec;
}

.status.error {
  background: #fde8e8;
}
</style>
