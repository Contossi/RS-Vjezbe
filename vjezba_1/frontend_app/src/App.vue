<script setup>
import { ref } from 'vue'
import ApiStatus from './components/ApiStatus.vue'
import ProductList from './components/ProductList.vue'
import ReviewList from './components/ReviewList.vue'
import ShippingOptions from './components/ShippingOptions.vue'
import ShoppingCart from './components/ShoppingCart.vue'

const cart = ref([])
const shipping = ref(null)

function addToCart(product) {
  const line = cart.value.find((l) => l.product.id === product.id)
  if (line) line.quantity++
  else cart.value.push({ product, quantity: 1 })
}

function removeFromCart(productId) {
  cart.value = cart.value.filter((l) => l.product.id !== productId)
}
</script>

<template>
  <main class="container">
    <h1>Webshop</h1>
    <ApiStatus />
    <div class="layout">
      <div class="column">
        <ProductList @add="addToCart" />
        <ReviewList />
      </div>
      <div class="column">
        <ShippingOptions v-model="shipping" />
        <ShoppingCart :lines="cart" :shipping="shipping" @remove="removeFromCart" />
      </div>
    </div>
  </main>
</template>

<style scoped>
.container {
  max-width: 960px;
  margin: 32px auto;
  padding: 0 16px;
}

.layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 16px;
  align-items: start;
}

.column {
  display: flex;
  flex-direction: column;
  gap: 16px;
  min-width: 0;
}

@media (max-width: 720px) {
  .layout {
    grid-template-columns: 1fr;
  }
}
</style>
