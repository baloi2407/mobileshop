function updateCart(action, element) {
    var id = element.attr("pid").toString();
    var eml = element[0].parentNode.children[1];
    var url = action === "plus" ? "/pluscart" : "/minuscart";

    $.ajax({
        type: "GET",
        url: url,
        data: {
            prod_id: id
        },
        success: function(data) {
            console.log("data = ", data);
            eml.innerText = data.quantity;
            document.getElementById("totalamount").innerText = data.amount;
        }
    });
}

$('.plus-cart').click(function() {
    updateCart("plus", $(this));
});

$('.minus-cart').click(function() {
    updateCart("minus", $(this));
});
function removeFromCart(element) {
    var id = element.attr("pid").toString();
    var url = "/removecart";

    $.ajax({
        type: "GET",
        url: url,
        data: {
            prod_id: id
        },
        success: function(data) {
            console.log("Product removed from cart");
            element.closest(".product-container").remove(); // Xóa hàng chứa sản phẩm
            document.getElementById("totalamount").innerText = data.amount;
        }
    });
}

$('.remove-cart').click(function() {
    removeFromCart($(this));
});

$('.plus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();


    $.ajax({
        type: "GET",
        url: "/pluswishlist",
        data: {
            prod_id: id
        },
        success: function(data) {
            window.location.href = `http://localhost:8000/product-details/${id}`;
        }
    });
});
$('.minus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();

    console.log(1)
    $.ajax({
        type: "GET",
        url: "/minuswishlist",
        data: {
            prod_id: id
        },
        success: function(data) {
            window.location.href = `http://localhost:8000/product-details/${id}`;
        }
    });
});
