<script setup>
import { ref,onMounted} from "vue"
import axios from "axios"
import {Operation} from "@/api.js"
//import { RouterLink, RouterView } from 'vue-router'
//import HelloWorld from './components/HelloWorld.vue'
const itemList = ref(['1','2','3','4'])

const search = ref("")

function addItem(){
    itemList.value.push(search.value)
    search.value =search.value+"!!"
}

const data =ref([])
async function getData(){
    data.value   = await Operation.objects.filter({name:search.value})
}

onMounted(()=>getData())
</script>

<template>
    <div>
    <h1>  Список операций</h1>
    <input v-model="search" @input="getData" class="form-control"> 
    <div v-for="item in data">  {{item.id }} {{item.name}} {{item.value}}</div>
    </div>
</template>

<style scoped>
</style>
