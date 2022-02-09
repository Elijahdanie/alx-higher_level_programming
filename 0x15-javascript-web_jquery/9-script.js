$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (resp)=> {
  $('#hello').text(resp.hello);
});
