<script setup>
import {onMounted} from "vue"
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import {useBackCardStore} from "@/stores/bankCard.js"
let store = useBackCardStore()
onMounted(()=>{
    store.getBankCardList()
})
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
