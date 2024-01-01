document.addEventListener("DOMContentLoaded", ()=>{
   var elements = document.getElementsByTagName("img");
   for (var i = 0; i < elements.length; i++) {
      element = elements.item(i);

      if (element.naturalWidth < 2 ||  element.naturalHeight < 2){
         element.src = "/static/img/no_book_image.png";
      }
   }
});

