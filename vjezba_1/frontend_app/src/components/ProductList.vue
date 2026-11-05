<script setup>
import DataSection from './DataSection.vue'
import { api } from '../api.js'
import { formatPrice } from '../format.js'

defineEmits(['add'])
</script>

<template>
  <DataSection title="Proizvodi" :load="api.getProducts" v-slot="{ items }">
    <ul class="products">
      <li v-for="product in items" :key="product.id">
        <span class="muted">{{ product.category }}</span>
        <strong>{{ product.name }}</strong>
        <span>{{ formatPrice(product.price) }}</span>
        <button @click="$emit('add', product)">Dodaj u košaricu</button>
      </li>
    </ul>
  </DataSection>
</template>

<style scoped>
.products {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 12px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.products li {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 12px;
  border: 1px solid #eee;
  border-radius: 8px;
}

.products button {
  margin-top: auto;
}
</style>
