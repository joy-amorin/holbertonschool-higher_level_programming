const name_id = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'

fetch(url)
  .then(res => res.json())
  .then(data => { name_id.textContent = data.name; });