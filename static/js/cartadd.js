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
var decreBtns=document.getElementsByClassName('cart_quantity_down')
for (i=0;i<decreBtns.length;i++){
  decreBtns[i].addEventListener('click',function(){
        var prodcutId=this.dataset.product
        
        
        minuscart(prodcutId)
    })
}
function minuscart(pid){
  
  $.ajax({
      url: 'delete_cart',
      type: "POST",
      dataType: "json",
      data: JSON.stringify({'pid': pid,}),
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
      },
      success: (data) => {
        
        if(data.qty>0){
        document.getElementById("qtyinput"+pid).value=data.qty
        document.getElementById("p"+pid).innerHTML="$"+data.tqty

        }else{
            document.getElementById("tr"+pid).hidden=true

        }

      },
      error: (error) => {
        console.log(error);
      }
    });


}