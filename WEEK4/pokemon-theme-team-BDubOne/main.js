
let imgBox = document.getElementById("poke-img")
let pokeName = document.getElementById("poke-name")
let pokeElement = document.getElementById("poke-elt")
let button = document.getElementById('catch-em');

function fetchData() {

    pokeElement.innerHTML = '';

    button.classList.add('clicked');

    const randomPokemon = Math.floor(Math.random() * 150) + 1;
    const pokeApi = `https://pokeapi.co/api/v2/pokemon/${randomPokemon}`;
    
    axios.get(pokeApi)
        .then(function (response) {


        const data = response.data;
            
        imgBox.innerHTML = `<img src="${data.sprites.front_shiny}" alt="Pokemon!" class="animate__animated animate__fadeIn">`;
        
        pokeName.innerHTML = `<h2 class="animate__animated animate__slideInRight">${data.name}</h2>`;

        const attributeList = document.createElement('ul');
        attributeList.classList.add('animate__animated', 'animate__slideInUp');



        // pokeName.innerHTML = `<h2>${data.name}</h2>`;

      

        const typeItem = document.createElement('li')
            typeItem.textContent = `Type: ${data.types[0].type.name}`; //.
            attributeList.appendChild(typeItem);

            const heightItem = document.createElement('li')
            heightItem.textContent = `Height: ${data.height}`;
            attributeList.appendChild(heightItem);

            const weightItem = document.createElement('li')
            weightItem.textContent = `weight: ${data.weight}`;
            attributeList.appendChild(weightItem);

            attributeList.classList.add('slide-up');
            
            pokeElement.appendChild(attributeList);

        })
        .catch(function (error) {
            console.error(error);
        });
    }

   
    button.addEventListener('click', fetchData)

