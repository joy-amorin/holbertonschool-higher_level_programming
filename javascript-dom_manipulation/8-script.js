document.addEventListener('DOMContentLoaded', (event) => {
    const insertHello = document.querySelector('#hello');
  
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(res => res.json())
      .then(data => {
        insertHello.appendChild(document.createTextNode(data.hello));
      });
  });