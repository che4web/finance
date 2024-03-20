import {ref} from "vue"
import { defineStore } from 'pinia'
import {BankCard } from "@/api.js"
    /* option api
export const useBackCardStore = defineStore('bankcard', {
  state: () => {
    return { bankCardList: [] }
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    async getBankCardList() {
        this.bankCardList =await BankCard.objects.filter()
    },
  },
})
*/
export const useBackCardStore = defineStore('bankcard', ()=>{
   let bankCardList =ref([])

   async function  getBankCardList() {
        bankCardList.value =await BankCard.objects.filter()
   }
    return {bankCardList,getBankCardList}
})
