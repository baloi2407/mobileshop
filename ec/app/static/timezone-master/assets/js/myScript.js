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
            if (eml) {
                eml.innerText = data.quantity;
            }
             
            var totalAmountElement = document.getElementById("totalamount");
            if (totalAmountElement) {
                totalAmountElement.innerText = data.amount;
            }

            var messageElement = document.getElementById("message");
            if (messageElement) {
                messageElement.innerText = data.message;
            }

            var errorMessageElement = document.getElementById('error-message');
            if (errorMessageElement) {
                errorMessageElement.innerText = ''; // Đảm bảo rằng thông báo lỗi trống trước khi cập nhật
            }
        },
        error: function(xhr, errmsg, err) {
            // Xử lý khi có lỗi trong request
            if (xhr.status === 400) {
                const errorMessage = JSON.parse(xhr.responseText).error;
                const errorMessageElement = document.getElementById('error-message');
                if (errorMessageElement) {
                    errorMessageElement.innerText = errorMessage;
                }
            }
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
            window.location.href = `/product-details/${id}`;
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
            window.location.href = `/product-details/${id}`;
        }
    });
});

$('.search-btn').click(function() {
    var pro_name = $('#pro_name').val();
    var brand = $('#brand').val();
    var min_price = $('#min_price').val();
    var max_price = $('#max_price').val();

    var url = `/advanced_search/?pro_name=${pro_name}&brand=${brand}&min_price=${min_price}&max_price=${max_price}`;

    $.ajax({
        type: "GET",
        url: url,
        success: function(data) {
            // Xử lý dữ liệu được trả về từ server ở đây
            // updateProductList(data.products); // Ví dụ: In ra dữ liệu sản phẩm
        },
        error: function(xhr, errmsg, err) {
            console.error('Error:', err);
        }
    });
});
