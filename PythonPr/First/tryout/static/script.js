// POP-UP Start //
var modal = document.getElementById("all-pop-box");
var btn = document.getElementById("AddCustomEntry");
var span = document.getElementsByClassName("close")[0];

if (window.location.pathname == "/") {
btn.onclick = function() {  
  var fval = document.getElementById("le_input");
  var pval = document.getElementById("pop-number").value = fval.value;
  var pval = document.getElementById("pop-fact").value = "";
  modal.style.display = "block";
  }

  span.onclick = invis();
}


window.onclick = function(event) {
  if (event.target == modal) {
    span.onclick = invis();
  }
}
function invis() {
  modal.style.display = "none";
}
// POP-OP End //


//On Enter Click Button

var input = document.getElementById("search_input");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    searchFromNavBar();
  }
});


if (window.location.pathname == "/search/") {
  var input = document.getElementById("search_field");
  input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      document.getElementById("search_in_search").click();
    }
  });
}



function FocusInput() {
  if (window.location.pathname == "/") {
       document.getElementById("le_input").focus();
      } //focus uz inputbox atverot index lapu
  }


function searchFromNavBar() {

  var searchKey = document.getElementById("search_input").value;
  searchKeywords(searchKey);
}
function searchFromSearch() {

  var searchKey = document.getElementById("search_field").value;
  searchKeywords(searchKey);
  }

function searchKeywords(searchKey) {

  if (searchKey === "") {

    alert("Cant search an empty field!");
  } else {
    var host = location.hostname;
    var port = location.port;
    var searchUri = "/search/";
    if (port != "") {
      var searchLink = "http://" + host + ":" + port + searchUri + "?keywords=" + searchKey;
    } else {
      var searchLink = "http://" + host + searchUri + "?keywords=" + searchKey;
    }
    
    window.open(searchLink, "_self");
  }
}

function DeleteFromMain(the_id) {

  var home = "http://" + location.host;
  var del = home + "/" + the_id + "/delete/";

  if (confirm("R U sure")) {
    $.ajax({
      type : "GET",
      url: del,
      data: {'location': 'main_page'},
      dataType: 'json',
      success: function (data) {

        document.getElementById(the_id).parentNode.parentNode.style.display='none';
         // hides deleted element
      }
    })
  }  
}


function DeleteFromEntry(the_id) {

  
  var del = "delete/";
  if (confirm("R U sure?")) {
    $.ajax({
      type: 'GET',
      url: del,
      data: {'location': 'entry_page'},
      dataType: 'json',
      success: function (data) {
        window.open(home, "_self");

      },
    })
  }  
}


function SaveFromEntry(the_id) {

  
  var save = "save/";
  var form = document.getElementById('entry-fact-input').value; 
  if (confirm("R U sure?")) {
    $.ajax({
      type: 'GET',
      url: save,
      data: {'form': form,},
      dataType: 'json',
      success: function (data) {
  
        window.alert(data.info);

      },
    })
  }  
}

function SaveFromPopUp() {

  var home = "http://" + location.host;
  var create = "/create/";
  var number = document.getElementById('pop-number').value;
  var fact = document.getElementById('pop-fact').value;
 

    $.ajax({
      type: 'GET',
      url: create,
      data: { 'number': number,
              'fact'  : fact,
            },
      dataType: 'json',
      success: function (data) {
      if (data.success == 'true') {
        window.alert(data.info);
        modal.style.display = "none";
        document.getElementById('hist_butt').click();
        }
      else {
         window.alert(data.info);
      }
      },
    })
    
}



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


// for apitask entry page. Adds links to pictures

var linkBox = document.getElementById("link_box");
var imgBox = document.getElementById("img_box");
for (var obj = 0; obj < 10; obj++ ) {
var obj_id = "link-" + obj;
var ahref = document.getElementById(obj_id).innerText;
var wrap_obj = "#img-" + obj;
var wrap_class = "<a href='" + ahref + "' target='blank' class='img-link'></a>";
console.log(wrap_class);
$(wrap_obj).wrapAll(wrap_class);

}



//////////////////////////////////////////////
//////////////////////////////////////////////

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

