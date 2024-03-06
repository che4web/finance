<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import OperationList from "./views/OperationList.vue"
</script>

<template>
  <header>
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/card">card</RouterLink>
        <RouterLink to="/operation">Операции</RouterLink>
      </div>
      </nav>
  </header>

    <div class="container">
  <RouterView />  
      </div>
</template>

<style scoped>
</style>
