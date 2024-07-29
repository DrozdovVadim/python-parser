
function cleanField()
{
    var input=document.getElementById('inputField');
    var count=document.getElementById('count');
    var resultElement1 = document.getElementById('result1');
    var resultElement2 = document.getElementById('result2');
    var fs=document.getElementById('firstStore');
    var ss=document.getElementById('secondStore');
    resultElement1.innerHTML='';
    resultElement2.innerHTML='';
    fs.innerHTML='';
    ss.innerHTML='';
}
var arr1=[]
var arr2=[]
function parseUrl(s, u) {
    
    var res1= document.getElementById('result1')
    var res2= document.getElementById('result2')
    var firstStore=document.getElementById('firstStore')
    var secondtStore=document.getElementById('secondStore')
    var input=document.getElementById('inputField').value;
    var count=document.getElementById('count').value;
    var data={
        'input': input,
        'count': count,
    };
    var input=document.getElementById('inputField');
    var count=document.getElementById('count');
    var resultElement1 = document.getElementById('result1');
    var resultElement2 = document.getElementById('result2');
    var fs=document.getElementById('firstStore');
    var ss=document.getElementById('secondStore');
    resultElement1.innerHTML='';
    resultElement2.innerHTML='';
    fs.innerHTML='';
    ss.innerHTML='';
    fetch(u,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    
        
})

    
    .then(response => {
        if (!response.ok) {
            var storeInf;
            var err = document.createElement('span');
            s == 1 ? storeInf = firstStore : storeInf = secondtStore;
            err.textContent="Произшла ошибка на сервере, попробуйте ввести другой товар, или выбрать другой магазин"
            storeInf.appendChild(err)
            throw new Error(`Ошибка HTTP: ${response.status}`);
            
        }
        return response.json(); // или response.text() в зависимости от типа ответа
    })
    .then(data => {
        console.log(data)
        var storeInf;
        var resultElement;
        var total = document.createElement('span');
        var sr = document.createElement('span');
        var min=document.createElement('span');
        var max=document.createElement('span');
    
        s == 1 ? resultElement = res1 : resultElement = res2;
        s == 1 ? storeInf = firstStore : storeInf = secondtStore;
        storeInf.innerHTML=''
        s==1? arr1=[]: arr2=[]
    
        total.textContent ="Товаров нашлось- " +data[0].t;
        sr.textContent = "Средняя цена- " +data[0].srp;
        min.textContent="Минимальная цена- " +data[0].min;
        max.textContent="Максимальная цена- " +data[0].max
    
        storeInf.appendChild(total);
        storeInf.appendChild(sr);
        storeInf.appendChild(min);
        storeInf.appendChild(max)
            
        
        if (resultElement) {
            resultElement.innerHTML = '';
            
            data.forEach(product => {
                var productCard = document.createElement('div');
                productCard.className = 'productCard';
        
                var productImage = document.createElement('img');
                productImage.className = 'productImg';
                productImage.src = product.i; 
        
                var productName = document.createElement('div');
                var productCost=document.createElement('div');

                productName.className = 'productInfo';
                productCost.className='productInfo';

                productName.innerHTML = `${product.n}`;
                productCost.innerHTML=`${product.c} руб` ;
                productCard.appendChild(productImage);
                productCard.appendChild(productName);
                productCard.appendChild(productCost);
        

                resultElement.appendChild(productCard);
                s==1? arr1.push(product.c):arr2.push(product.c);
            });
            for (let i=0; i<arr1.length; i++)
                {
                    console.log(Math.abs(arr1[i]-arr2[i]))
                }
        } else {
            console.error('Элемент с id "result" не найден');
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}

function selectCheck() {
    var input = document.getElementById('inputField').value;
    var count = document.getElementById('count').value;
    var sel1=document.getElementById('select1').value;
    var sel2=document.getElementById('select2').value;
    var arr=["http://127.0.0.1:5000/parse/vkysvill","http://127.0.0.1:5000/parse/globus","http://127.0.0.1:5000/parse/lenta","http://127.0.0.1:5000/parse/metro", "http://127.0.0.1:5000/parse/paterochka"]
    console.log(sel1, sel2)
    if (input && count && sel1!='default' && sel2!='default' && sel1!=sel2 ) {
        parseUrl(1, arr[sel1-1])
        parseUrl(2, arr[sel2-1])
    } else {
        alert("Проверь выбор магазинов или заполнение строк поиска, надо выбрать два разных магазина и заполнить все строки");
    }
}
