const ul = document.querySelector('ul#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(res => res.json())
  .then(data => {
    data.results.forEach(object => {
      const li = document.createElement('li');
      li.textContent = object.title;
      ul.appendChild(li);
    });
  });