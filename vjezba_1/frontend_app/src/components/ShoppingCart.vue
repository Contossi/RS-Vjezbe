<script setup>
import { computed } from 'vue'
import { formatPrice } from '../format.js'

const props = defineProps({
  lines: { type: Array, required: true },
  shipping: { type: Object, default: null }
})

defineEmits(['remove'])

const subtotal = computed(() => props.lines.reduce((sum, line) => sum + line.product.price * line.quantity, 0))
const total = computed(() => subtotal.value + (props.shipping?.price ?? 0))
</script>

<template>
  <section class="card">
    <h2>Košarica</h2>
    <p v-if="!lines.length" class="muted">Košarica je prazna.</p>
    <template v-else>
      <ul class="lines">
        <li v-for="line in lines" :key="line.product.id">
          <span class="name">{{ line.quantity }} × {{ line.product.name }}</span>
          <span>{{ formatPrice(line.product.price * line.quantity) }}</span>
          <button class="remove" :aria-label="`Ukloni ${line.product.name}`" @click="$emit('remove', line.product.id)">✕</button>
        </li>
      </ul>
      <p v-if="shipping" class="row">
        <span>{{ shipping.name }}</span>
        <span>{{ formatPrice(shipping.price) }}</span>
      </p>
      <p v-else class="muted">Odaberi način dostave.</p>
      <p class="row total">
        <span>Ukupno</span>
        <span>{{ formatPrice(total) }}</span>
      </p>
    </template>
  </section>
</template>

<style scoped>
.lines {
  list-style: none;
  margin: 0 0 8px;
  padding: 0;
}

.lines li {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 0;
  border-bottom: 1px solid #eee;
}

.name {
  flex: 1;
}

.row {
  display: flex;
  justify-content: space-between;
  margin: 8px 0;
}

.total {
  font-weight: bold;
}

.remove {
  background: none;
  border: none;
  color: #c00;
  cursor: pointer;
}
</style>
