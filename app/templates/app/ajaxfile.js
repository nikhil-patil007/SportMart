$(document).ready(function(){
    // Add To Cart
    $("#addtocart").on('click',function(){
        var_qty
    });
    // End Cart
});


// Seller Delete Products..
$('div.product-wrapper').on('click','.S-delete-pro',function(){
    console.log('delete button clicked');
    let id = $(this).attr('data-sid');
    console.log(id);
    mydata = {pid:id, 'csrfmiddlewaretoken': '{{ csrf_token }}'}
    mythis = this;
    console.log(mythis)
    $.ajax({
        url : "{% url 'deleteprod' %}",
        method : "POST",
        data : mydata,
        success : function(data){
            console.log(data);
            if (data.status==1){
                console.log("Booking Deleted Successfully")
                $(mythis).closest("div.product-wrapper").fadeOut();
            }
            if (data.status==0){
                console.log("Unable To Delete Booking")
            }
        },
    });
});
