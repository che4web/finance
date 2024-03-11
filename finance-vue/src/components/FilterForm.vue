<script setup>
import {ref} from "vue"
const emits  = defineEmits(['search'])
const search =ref('')
function send(){
    emits("do",search.value)
}

</script>
<template>
    <input v-model="search"  class="form-control"> 
    <button class="btn btn-primary" @click="send"> поиск </button>
</template>
