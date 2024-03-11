<script setup>
import { ref,onMounted} from "vue"
import axios from "axios"
import {Operation} from "@/api.js"
//import { RouterLink, RouterView } from 'vue-router'
//import HelloWorld from './components/HelloWorld.vue'
import OperationList from "../components/OperationList.vue"
import FilterForm from "../components/FilterForm.vue"
const search = ref("")

function foo(s){
    search.value=s
}

</script>

<template>
    <div>
    <h1>  Список операций</h1>
    <FilterForm @do="foo"/> 
    <OperationList :search="search"/>
    </div>
</template>

<style scoped>
</style>
