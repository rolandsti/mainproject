function myFunction1() {
  var elem = document.getElementById("test");
  elem.innerHTML = "Hello! -JavaScript2019";
  elem.hidden = false;
}


function myFunction2() {
var elem = document.getElementById("test");
elem.hidden = true;

var elem = document.getElementById("root");
// elem.hidden = true; // just hide object
elem.innerHTML = ""; // clear object content

var elem = document.getElementById("cubes");
elem.innerHTML = ""; 

var elem = document.getElementById("numbers");
elem.innerHTML = ""; 
}

function MovieAPI() {

const app = document.getElementById('root')
app.hidden = false;

//const logo = document.createElement('img')
//logo.src = 'logo.png'

const container = document.createElement('div')
container.setAttribute('class', 'container')

//app.appendChild(logo) pievieno logo attel root objekt html faila
app.appendChild(container)

var request = new XMLHttpRequest()
request.open('GET', 'https://ghibliapi.herokuapp.com/films', true)
request.onload = function() {

  var data = JSON.parse(this.response)
var howmany = document.getElementById('inputtext').value		
  if (request.status >= 200 && request.status < 400) {
	var count = 1
	
    data.forEach((movie, index) => {
	console.log(index);
	console.log(movie);
	if (count <= howmany) {
      const card = document.createElement('div')
      card.setAttribute('class', 'card')

      const h1 = document.createElement('h1')
      h1.textContent = movie.title

      const p = document.createElement('p')
      movie.description = movie.description.substring(0, 300)
      p.textContent = movie.description + "..."

      container.appendChild(card)
      card.appendChild(h1)
	card.appendChild(p)
	count = count + 1
	}
    })
  } else {
    const errorMessage = document.createElement('marquee')
    errorMessage.textContent = "Does not work!"
    app.appendChild(errorMessage)
  }
}

request.send()
}









function CubesForDays() {

const nrapp = document.getElementById('cubes')
nrapp.hidden = false;

var howmany = document.getElementById('inputtext').value
for (var i = 1; i<= howmany; i++) {



const cube = document.createElement('div') 
cube.setAttribute ('class', 'cube')
nrapp.appendChild(cube)

}



}

