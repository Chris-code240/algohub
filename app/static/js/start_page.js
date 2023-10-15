const generateBtn = document.querySelector('#generate')
const reportsWrapper = document.querySelector('#reports')
const btn = document.querySelector('button')
generateBtn.addEventListener('click',()=>{
    generateBtn.innerHTML = '<i class="fa fa-circle-notch fa-spin"></i>'
    fetch('/app/analyze/',{method:'POST'}).then((res)=>res.json()).then((jres)=>{
        if(jres.success){
            generateBtn.innerHTML = 'Generate'
            reportsWrapper.querySelector('p').remove()
            const div = document.createElement('div')
            div.setAttribute('class','flex w-full')
            div.innerHTML = jres.data.code

            reportsWrapper.appendChild(div)
        }else{
            generateBtn.innerHTML = 'Generate'
        }
    })
})