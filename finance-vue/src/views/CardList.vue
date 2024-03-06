<script setup>
import { ref,onMounted} from "vue"
import axios from "axios"
import {BankCard,Operation} from "@/api.js"
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
    data.value   = await BankCard.objects.filter({name:search.value})
}
async function getOperation(card){
    let response = await Operation.objects.filter({bankcard:card.id})
    card.operation_list =response
}
onMounted(()=>getData())

function save(op){
    Operation.objects.save(op)
}
</script>

<template>
    <div>
    <h1>  Список Карт</h1>
    <input v-model="search" @input="getData" class="form-control"> 
    <div>
    <div class="card mb-2" v-for="item in data" @click=getOperation(item)>  
        <div class="card-body">
            <div >{{item.id }} {{item.name}} {{item.balance}} </div>
            <ul> 
                <li v-for="op in  item.operation_list"> 
                    <input v-model="op.name"> <button @click.stop="save(op)"> сохранить</button>
                </li>
            </ul>
        </div>
        </div>
    </div>
    </div>
</template>

<style scoped>
</style>
