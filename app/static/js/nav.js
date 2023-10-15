const hamburger = document.getElementById('hamburger')
const menu = document.querySelector('#menu')
hamburger.addEventListener('click',()=>{
    Array.from(hamburger.children).forEach(child=>{
        child.classList.toggle('bar')
        menu.classList.toggle('hidden')
    })
})