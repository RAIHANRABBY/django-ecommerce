var updateBtns = document.getElementsByClassName('update-cart')

for(i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productId= this.dataset.product
        var action = this.dataset.action
        console.log('Product:',productId,'action:',action,User)
        if (User=='AnonymousUser'){
            console.log('user is not authenticated')
        }
        else{
            updateUserOrder(productId,action)
        }
    
    })
}

function updateUserOrder(productId,action){
    console.log('user is authenticated.sending data........')
    var url='/update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFTOKEN': csrftoken,
        },
        body:JSON.stringify({'ProductId':productId,'action':action})
    })
    .then((response)=>{
        return response.json
    })

    .then((data)=>{
        console.log('Data:', data)
        location.reload()
    })
    

}