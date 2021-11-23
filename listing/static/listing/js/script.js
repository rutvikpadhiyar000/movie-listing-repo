allMovies = document.getElementsByClassName("movie-box");
rightHalf = document.getElementById("id-right-half");
leftHalf = document.getElementById("id-left-half");

function addToFavorites(element, elementParent) {
  if (elementParent.parentElement.id == "id-left-half") {
    element.innerHTML = "&#127775;";
    rightHalf.appendChild(elementParent);
  } else {
    element.innerHTML = "&#9734;";
    leftHalf.appendChild(elementParent);
  }
}
