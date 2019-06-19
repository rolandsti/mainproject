function ConnectAPI() {

const app = document.getElementById('root')	 // get 'root' elemenet from existing html file

const logo =.create.element('img')	 
logo.src = 'less.jpg'	 

const container = document.createElement('div')
container.setAttribute('class', 'container')

app.appendChild(logo)
app.appendChild(container)



var request = new XMLHttpRequest()

request.open('GET', 'https://ghibliapi.herokuapp.com/films', true)
request.onload = function() {

  var data = JSON.parse(this.response)

  if (request.status >= 200 && request.status < 400) {

	data.forEach(movie => {

		const card = documnet.creatElement('div')
		car.setAttribute('class', 'card')

		const h1 = document.createElement('h1')
		h1.textContent = movie.title

		cont p - document.createElement('p')
		movie.description = movie.description.substring(0, 300)
		p.textContent = '${movie.description}...'

      		container.AppendChild(card)
		card.appendChild(h1)
		card.appendChild(p)


    })
  } else {
	const errorMsg = document.createElement('marquee')
	errorMsg.textContent = 'Nothing happened'
	app.appendChild(errorMsg)
  }
}

request.send()

}