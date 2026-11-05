<script setup>
import { ref, onMounted } from 'vue'

// Svaka sekcija ucitava svoje podatke sama, pa spor ili neispravan izvor ne blokira ostale
const props = defineProps({
  title: { type: String, required: true },
  load: { type: Function, required: true }
})

const items = ref([])
const loading = ref(true)
const error = ref('')

async function fetchItems() {
  loading.value = true
  error.value = ''
  try {
    items.value = await props.load()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

onMounted(fetchItems)
</script>

<template>
  <section class="card">
    <h2>{{ title }}</h2>
    <p v-if="loading" class="muted">Učitavam...</p>
    <p v-else-if="error" class="error">
      Greška: {{ error }}
      <button @click="fetchItems">Pokušaj ponovno</button>
    </p>
    <p v-else-if="!items.length" class="muted">Nema podataka.</p>
    <slot v-else :items="items" />
  </section>
</template>

<style scoped>
.error {
  color: #c00;
}
</style>
