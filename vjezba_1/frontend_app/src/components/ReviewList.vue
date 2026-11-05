<script setup>
import DataSection from './DataSection.vue'
import { api } from '../api.js'

const stars = (rating) => '★'.repeat(rating) + '☆'.repeat(5 - rating)
</script>

<template>
  <DataSection title="Recenzije" :load="api.getReviews" v-slot="{ items }">
    <ul class="reviews">
      <li v-for="review in items" :key="review.id">
        <div class="head">
          <strong>{{ review.customer }}</strong>
          <span class="stars" :aria-label="`Ocjena ${review.rating} od 5`">{{ stars(review.rating) }}</span>
        </div>
        <p>{{ review.comment }}</p>
      </li>
    </ul>
  </DataSection>
</template>

<style scoped>
.reviews {
  list-style: none;
  margin: 0;
  padding: 0;
}

.reviews li {
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}

.reviews li:last-child {
  border-bottom: none;
}

.reviews p {
  margin: 4px 0 0;
}

.head {
  display: flex;
  justify-content: space-between;
  gap: 8px;
}

.stars {
  color: #d99a00;
}
</style>
