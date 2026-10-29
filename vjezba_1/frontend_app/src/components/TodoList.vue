<script setup>
import { ref, computed } from 'vue'

const newTask = ref('')
const tasks = ref([
  { id: 1, text: 'Napraviti Vue aplikaciju', done: true },
])

const remaining = computed(() => tasks.value.filter((t) => !t.done).length)

function addTask() {
  const text = newTask.value.trim()
  if (!text) return
  tasks.value.push({ id: Date.now(), text, done: false })
  newTask.value = ''
}

function removeTask(id) {
  tasks.value = tasks.value.filter((t) => t.id !== id)
}
</script>

<template>
  <section>
    <form @submit.prevent="addTask">
      <input v-model="newTask" placeholder="Novi zadatak..." />
      <button type="submit">Dodaj</button>
    </form>

    <ul>
      <li v-for="task in tasks" :key="task.id" :class="{ done: task.done }">
        <label>
          <input type="checkbox" v-model="task.done" />
          {{ task.text }}
        </label>
        <button class="remove" @click="removeTask(task.id)">✕</button>
      </li>
    </ul>

    <p>Preostalo zadataka: {{ remaining }}</p>
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
</style>
