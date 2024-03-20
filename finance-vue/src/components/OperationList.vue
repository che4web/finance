<script setup>
import { ref,onMounted,watch} from "vue"
import {Operation,BankCard} from "@/api.js"
import {useBackCardStore} from "@/stores/bankCard.js"
const data =ref([])
const props =defineProps(['search','bankcard'])
const ordering = ref('')
async function getData(){
    let filter ={ordering:ordering.value}
    if (props.search){
        filter.search=props.search
    }
    if (props.bankcard){
        filter.bankcard=props.bankcard
    }
    data.value   = await Operation.objects.filter(filter)
}
let store = useBackCardStore()
onMounted(()=>{
    getData()
})
watch(()=>props.search,()=>getData())
watch(()=>ordering.value,()=>getData())

function setOrdering(name){
    if (ordering.value == name){
        ordering.value="-"+name
    }else{
        ordering.value=name
    }

    
}

const newItem= ref({})
async function saveItem(){
    let reponseItem =  await Operation.objects.dsave(newItem.value)

    data.value.push(reponseItem) 
    newItem.value= {}
}

</script>
<template>
    <div>
    <table  class="table table-bordered  table-hover">
        <thead>
            <tr>
                <th @click="setOrdering('id')"> id</th>
                <th @click="setOrdering('bankcard')"> карта</th>
                <th @click="setOrdering('name')"> название</th>
                <th @click="setOrdering('value')"> значение</th>
            </tr>
        </thead>
        <tbody >
            <tr v-for="item in data">  
                <td >{{item.id }}</td>
                <td>{{item.bankcard.name}}</td>
                <td>{{item.name}}</td>
                <td>{{item.value}}</td>
            </tr>
            <tr >  
                <td > {{newItem.id}}</td>
                <td ><select v-model="newItem.bankcard">
                        <option :value="bankcard" v-for="bankcard in store.bankCardList"> {{bankcard.name}}</option>
        
                    </select></td>
                <td ><input v-model="newItem.name"</td>
                <td ><input v-model="newItem.value"</td>
                <td > 
                    <button class="btn btn-primary" @click="saveItem()"> сохранить</button>
                </td>
            </tr>

        </tbody>
        </table>
    </div>
</template>
