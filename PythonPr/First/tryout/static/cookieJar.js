

function switchStyle() {

  var selectStyle = document.getElementById('style_select').value;

  if (selectStyle == "Custom") {
    document.getElementById("color_input").style.display = "block";
    var content = document.getElementById('content');
    var colorForCookie = document.getElementById("color_input").value;
    content.style.background = colorForCookie;


  } else {
    document.getElementById("color_input").style.display = "none";
    styleAddInSeetings(selectStyle); 



  }
}

function styleAddInSeetings (selectedCookieColor) {
  var content = document.getElementById('content');
  content.style.background = '';
  var contClass = content.className;
  content.classList.remove(contClass);


    if (selectedCookieColor == "Green") {
      content.classList.add("content-green");

    } else if (selectedCookieColor == "Blue") {
      content.classList.add("content-blue");

    } else if (selectedCookieColor == "Red") {
      content.classList.add("content-red");

    } else {
      content.classList.add("content-default");

    }
}





function customColor(colorId) {

   var content = document.getElementById('content');
   content.style.background = colorId;

}

function addStyle(almostBakedCookie) {

  var content = document.getElementById('content');
  if (almostBakedCookie != null) {
  var bakedCookieArray = almostBakedCookie.split('&');
  } else {
  var  bakedCookieArray = ["&", "&", "&", "&"]
  }
  var bakedCookie = bakedCookieArray[0];

  if (bakedCookie.charAt(0) === "#") {
    var content = document.getElementById('content');
    content.style.background = bakedCookie;

  } else {

    content.style.background = '';
    var contClass = content.className;
    content.classList.remove(contClass);

    if (bakedCookie == "Green") {
      content.classList.add("content-green");

    } else if (bakedCookie == "Blue") {
      content.classList.add("content-blue");

    } else if (bakedCookie == "Red") {
      content.classList.add("content-red");

    } else {
      content.classList.add("content-default");

    }
  }

  var bakedCookie = bakedCookieArray[1];
  if (bakedCookie == "false") {
    navButOff("numbers");
  } else { navButOn("numbers");}

  var bakedCookie = bakedCookieArray[2];
  if (bakedCookie == "false") {
    navButOff("stuff");
  } else { navButOn("stuff");}

  var bakedCookie = bakedCookieArray[3];
  if (bakedCookie == "false") {
    navButOff("api");
  } else { navButOn("api");}


}
function navButOff(navID) {
    var navString = "nav_" + navID;
    var navBut = document.getElementById(navString);
    navBut.style.display = "none";
}

function navButOn(navID) {
    var navString = "nav_" + navID;
    var navBut = document.getElementById(navString);
    navBut.style.display = "block";
}


document.onload = addStyleCookie();

function getStyleCookie() {

  var cookieName = "style=";
  var decodedCookie = document.cookie;
  
  var cookieArray = decodedCookie.split(';');


  for(var cookieLoop = 0; cookieLoop < cookieArray.length; cookieLoop++) {
    var cookie = cookieArray[cookieLoop];
    if (cookie.charAt(0) == ' ') {
      cookie = cookie.substring(1); 
    }
    if (cookie.indexOf(cookieName) == 0) {
      var bakedCookie = cookie.substring(cookieName.length, cookie.length);
      return bakedCookie; 
    }
  }

}


function saveStyleCookie() {

  var cookieStyle = document.getElementById('style_select').value;
  var numbersStatus = document.getElementById("numbers").checked;
  var stuffStatus = document.getElementById("stuff").checked;
  var apiStatus = document.getElementById("api").checked;


  if (cookieStyle == "Custom") {
        cookieStyle = document.getElementById('color_input').value
    var styleString = "style=" + cookieStyle;
  } else {
    var styleString = "style=" + cookieStyle;
  }

  if (numbersStatus == true) {
    styleString += "&true"
  } else {
    styleString += "&false"
  }
    if (stuffStatus == true) {
    styleString += "&true"
  } else {
    styleString += "&false"
  }
    if (apiStatus == true) {
    styleString += "&true; "
  } else {
    styleString += "&false; "
  }

  var cookieDate = new Date();
  var cookieDays = 14;
  cookieDate.setTime(cookieDate.getTime() + (30*24*60*60*1000));
  cookieExpires = cookieDate.toUTCString();
  expireString = "expires=" + cookieExpires + "; ";
  cookieString =  styleString + expireString + "path=/;";
  document.cookie = cookieString; // saved style cookie


  window.alert("Changes have been made!");

}

function addStyleCookie() {

  var bakedCookie = getStyleCookie();
  addStyle(bakedCookie);
}


document.onload = generateSettingsOptions();
function generateSettingsOptions() {


  if (window.location.pathname === "/settings/") {
    var almostBakedCookie = getStyleCookie();
    var styleTag = document.getElementById("style_select");

    if (almostBakedCookie != null) {
    var bakedCookieArray = almostBakedCookie.split('&');
    } else {
    var  bakedCookieArray = ["&", "&", "&", "&"]
    }

    bakedCookie = bakedCookieArray[0];


    if (bakedCookie == "White (Default)") {
      styleTag.innerHTML = styleTag.innerHTML + "<option selected>White (Default)</option>";
    } else {
      styleTag.innerHTML = styleTag.innerHTML + "<option>White (Default)</option>";
    }

    if (bakedCookie == "Green") {
      styleTag.innerHTML = styleTag.innerHTML + "<option selected>Green</option>";
    } else {
      styleTag.innerHTML = styleTag.innerHTML + "<option>Green</option>";
    }

    if (bakedCookie == "Blue") {
      styleTag.innerHTML = styleTag.innerHTML + "<option selected>Blue</option>";
    } else {
      styleTag.innerHTML = styleTag.innerHTML + "<option>Blue</option>";
    }

    if (bakedCookie == "Red") {
      styleTag.innerHTML = styleTag.innerHTML + "<option selected>Red</option>";

    } else {
      styleTag.innerHTML = styleTag.innerHTML + "<option>Red</option>";
    }
   
    if (bakedCookie.charAt(0) === "#") {
      styleTag.innerHTML = styleTag.innerHTML + "<option selected>Custom</option>";
      document.getElementById("color_input").style.display = "block";
      document.getElementById("color_input").value = bakedCookie;
    } else {
      styleTag.innerHTML = styleTag.innerHTML + "<option>Custom</option>";
    }

    bakedCookie = bakedCookieArray[1];
    if (bakedCookie == "false") {
      document.getElementById("numbers").checked = false;
    } else {
      document.getElementById("numbers").checked = true;
    }
    bakedCookie = bakedCookieArray[2];
    if (bakedCookie == "false") {
      document.getElementById("stuff").checked = false;
    } else {
      document.getElementById("stuff").checked = true;
    }
    bakedCookie = bakedCookieArray[3];
    if (bakedCookie == "false") {
      document.getElementById("api").checked = false;
    } else {
      document.getElementById("api").checked = true;

    }
  }
}






function navButtonInvis(navID) {
  var onoffStatus = document.getElementById(navID).checked;
  var navString = "nav_" + navID;
  var navBut = document.getElementById(navString);

    if (onoffStatus == true) {
     
      navBut.style.display = "block";

    } else {
     
      navBut.style.display = "none";
    }
    
}