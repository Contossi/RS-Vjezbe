<script setup>
import { ref, computed, onMounted } from 'vue'
import { api } from '../api.js'

const newTask = ref('')
const tasks = ref([])
const loading = ref(true)
const error = ref('')

const remaining = computed(() => tasks.value.filter((t) => !t.done).length)

async function run(action) {
  error.value = ''
  try {
    await action()
  } catch (err) {
    error.value = err.message
  }
}

function loadTasks() {
  return run(async () => {
    loading.value = true
    try {
      tasks.value = await api.getTasks()
    } finally {
      loading.value = false
    }
  })
}

function addTask() {
  const text = newTask.value.trim()
  if (!text) return
  return run(async () => {
    tasks.value.push(await api.addTask(text))
    newTask.value = ''
  })
}

function toggleTask(task) {
  return run(async () => {
    const updated = await api.updateTask(task.id, { done: !task.done })
    task.done = updated.done
  })
}

function removeTask(id) {
  return run(async () => {
    await api.deleteTask(id)
    tasks.value = tasks.value.filter((t) => t.id !== id)
  })
}

onMounted(loadTasks)
</script>

<template>
  <section>
    <h2>Zadaci (s API-ja)</h2>

    <form @submit.prevent="addTask">
      <input v-model="newTask" placeholder="Novi zadatak..." />
      <button type="submit">Dodaj</button>
    </form>

    <p v-if="error" class="error">Greska: {{ error }}</p>
    <p v-if="loading">Ucitavam zadatke...</p>

    <ul v-else>
      <li v-for="task in tasks" :key="task.id" :class="{ done: task.done }">
        <label>
          <input type="checkbox" :checked="task.done" @change="toggleTask(task)" />
          {{ task.text }}
        </label>
        <button class="remove" @click="removeTask(task.id)">✕</button>
      </li>
    </ul>

    <p>Preostalo zadataka: {{ remaining }}</p>
    <button @click="loadTasks">Osvjezi</button>
  </section>
</template>

<style scoped>
form {
  display: flex;
  gap: 8px;
}

form input {
  flex: 1;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}

li.done label {
  text-decoration: line-through;
  color: #999;
}

.remove {
  background: none;
  border: none;
  color: #c00;
  cursor: pointer;
}

.error {
  color: #c00;
}
</style>
