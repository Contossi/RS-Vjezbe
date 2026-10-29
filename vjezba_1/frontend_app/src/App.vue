<script setup>
import ClickCounter from './components/ClickCounter.vue'
import TodoList from './components/TodoList.vue'
</script>

<template>
  <main class="container">
    <h1>Vue.js Frontend App</h1>
    <p class="subtitle">Jednostavna aplikacija posluzena kao staticni sadrzaj.</p>
    <ClickCounter />
    <TodoList />
  </main>
</template>

<style scoped>
.container {
  max-width: 480px;
  margin: 48px auto;
  padding: 0 16px;
}

.subtitle {
  color: #666;
}
</style>
