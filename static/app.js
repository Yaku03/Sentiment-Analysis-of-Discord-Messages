let temp;
let count = 0;
let updateTime = 100;
let done = false;
function getValues(){
    url = 'https://mcst.onrender.com/get'


    axios.get(url)
    .then(function(response) {
        document.getElementById('Positive').setAttribute('data-target', response.data.positive);
        document.getElementById('Neutral').setAttribute('data-target', response.data.neutral);
        document.getElementById('Negative').setAttribute('data-target', response.data.negative);
    })
    .catch(function(error) {
        console.log(error);
    });
    if(count === 1){
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => {
            counter.innerHTML = '0'
            const updateCounter = () => {
                const target = parseInt(+counter.getAttribute('data-target'));
                const c = +counter.innerHTML;

                const increment = 1;
                if(c < target){
                    counter.innerHTML = `${Math.ceil(c + increment)}`;
                    setTimeout(updateCounter, 1);
                }
                else{
                    counter.innerHTML = target;
                }
            }
            updateCounter();
        });
        clearInterval(interval);
        updateTime = 5000;
        interval = setInterval(getValues, updateTime);
    }
    else{
        document.getElementById('Positive').innerHTML = document.getElementById('Positive').getAttribute('data-target');
        document.getElementById('Neutral').innerHTML = document.getElementById('Neutral').getAttribute('data-target');
        document.getElementById('Negative').innerHTML = document.getElementById('Negative').getAttribute('data-target');
    }
    temp = parseInt(document.getElementById('Positive').getAttribute('data-target'));
    if(count <= 1){
        count++;
    }
};
let interval = window.setInterval(getValues, updateTime);





