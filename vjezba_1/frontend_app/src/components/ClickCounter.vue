<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <section class="counter">
    <h2>Click counter</h2>
    <p class="value">{{ count }}</p>
    <div class="buttons">
      <button @click="count--">-1</button>
      <button @click="count++">+1</button>
      <button @click="count = 0">Reset</button>
    </div>
  </section>
</template>

<style scoped>
.counter {
  text-align: center;
  padding: 16px;
  margin-bottom: 24px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
}

.value {
  font-size: 48px;
  font-weight: bold;
  margin: 8px 0;
}

.buttons {
  display: flex;
  justify-content: center;
  gap: 8px;
}
</style>
