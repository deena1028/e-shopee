function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
var updateBtns=document.getElementsByClassName('update-cart')
for (i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var prodcutId=this.dataset.product
        
        updateusercart(prodcutId)
    })
}
function updateusercart(pid){
  
    $.ajax({
        url: 'update_cart_item',
        type: "POST",
        dataType: "json",
        data: JSON.stringify({'pid': pid,}),
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
        },
        success: (data) => {
          document.getElementById("cartqty").innerHTML=data.qty
          document.getElementById("qtyinput"+pid).value=data.qty
          document.getElementById("p"+pid).innerHTML="$"+data.tqty

        },
        error: (error) => {
          console.log(error);
        }
        
      });


}
