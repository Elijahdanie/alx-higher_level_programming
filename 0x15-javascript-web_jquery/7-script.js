$.get('https://swapi.co/api/people/5/?format=json', (resp)=> {
  $('#character').text(resp.name);
});
