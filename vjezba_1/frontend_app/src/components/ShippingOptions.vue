<script setup>
import DataSection from './DataSection.vue'
import { api } from '../api.js'
import { formatPrice } from '../format.js'

const selected = defineModel()

const deliveryTime = (days) => (days === 1 ? '1 dan' : `${days} dana`)
</script>

<template>
  <DataSection title="Dostava" :load="api.getShipping" v-slot="{ items }">
    <label v-for="option in items" :key="option.id" class="option">
      <input type="radio" name="shipping" :value="option" v-model="selected" />
      <span class="name">{{ option.name }}</span>
      <span class="muted">{{ deliveryTime(option.days) }}</span>
      <span>{{ formatPrice(option.price) }}</span>
    </label>
  </DataSection>
</template>

<style scoped>
.option {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 0;
  cursor: pointer;
}

.name {
  flex: 1;
}
</style>
