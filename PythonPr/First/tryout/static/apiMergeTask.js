

function cityLookupInput(cityID) {

	
	if (cityID.length == 3) {

		var whereToRender = document.getElementById('render_content');
		var home = "http://" + location.host;
		var link = home + "/listofcities/";
		whereToRender.innerHTML = "";

		var searching = document.createElement("div");
		searching.classList.add("apitask-entry-search");
		searching.setAttribute("id", "searching");

		var searching_text = document.createElement("div");
		
		searching_text.classList.add("history-entry-left");
		searching_text.style.textAlign = "center";
		searching_text.style.width = "100%";
		searching_text.innerHTML = "Searching...";
		searching_text.setAttribute("id", "searching_text");	

		searching.appendChild(searching_text);
		whereToRender.appendChild(searching);

		$.ajax({
			type : "GET",
			url: link,
			data: {'location': cityID},
			dataType: 'json',
			success: function (data) {
				

				var resultCount = "There are " + data.result_count + " matching results."
				document.getElementById("searching").style.display = "block";
				document.getElementById("searching_text").innerHTML = resultCount;



				
				for (i = 0; i <= data.final_data.length - 1; i++) {

					

					var entry = document.createElement("div");
					entry.classList.add("history-entry");
					var entry_id = data.final_data[i]['city_id'];
					entry.setAttribute("id", entry_id);
					entry.setAttribute("onclick", "toContinue(id)");

					var entry_child = document.createElement("div");
					entry_child.classList.add("entry-apitask");
					entry_child.style.textAlign = "center";
					entry.appendChild(entry_child);
					entry_child.style.width = "100%";
					entry_child.style.cursor = "pointer";

					var entryText = data.final_data[i]['city_name'] + " -" + data.final_data[i]['country'] + "-";
					entry_child.innerText = entryText;
					var whereToRender = document.getElementById('render_content');
					whereToRender.appendChild(entry);


				}

				filterEntries()

				
			}
		});
	} else if (cityID.length > 3) {

			filterEntries()
	}	
}

function toContinue(key) {
	

	var home = "http://" + location.host;
  	var link = home + "/apitask/" + key;
  	window.open(link, "_self");
  	//window.open(home, "_self");
}


function filterEntries() {
	var whereToRender = document.getElementById('render_content');
	var entry_apitask = whereToRender.getElementsByClassName("history-entry");
	var cityID = document.getElementById("apitask_field").value.toUpperCase();
	var resultCount = 0;
		for (var j = 0; j < entry_apitask.length; j++) {

			entry_content = entry_apitask[j].getElementsByClassName("entry-apitask")[0];
			entry_text = entry_content.textContent;
			entry_text = entry_text.replace(/-/g, "");

			if (entry_text.toUpperCase().indexOf(cityID) > -1) {
				entry_apitask[j].style.display = "block";
				resultCount += 1;
			} else {
				entry_apitask[j].style.display = "none";
			}


		}
	var resultCount = "There are " + resultCount + " matching results."
	document.getElementById("searching_text").innerHTML = resultCount;
}


function cityLookupButton() {

	var cityID = document.getElementById("apitask_field").value;
	var home = "http://" + location.host;
	var link = home + "/apitask/?location=" + cityID;
	window.open(link, "_self");
		
}

document.getElementById("apitask_field").focus();

var input = document.getElementById("apitask_field");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    cityLookupButton();
  }
});